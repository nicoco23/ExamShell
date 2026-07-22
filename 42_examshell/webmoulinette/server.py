#!/usr/bin/env python3
"""
Moulinette web locale pour l'Exam Rank 02 (42).

Sert un editeur de code dans le navigateur et lance la VRAIE moulinette
du repo (.resources/rankXX/levelY/<exo>/tester.sh) sur le code saisi.

Usage :
    python3 webmoulinette/server.py
puis ouvrir http://127.0.0.1:4242

Ne bind que sur localhost. Compile et execute du code C local : a n'utiliser
que sur ta propre machine (exactement comme le shell d'exam d'origine).
"""

import json
import os
import re
import shutil
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

try:
    from sujets_fr import SUJETS as SUJETS_FR
except ImportError:
    SUJETS_FR = {}

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
RENDU_DIR = os.path.join(REPO_ROOT, "rendu")

RANK = "rank02"
LEVELS = ["level0", "level1", "level2", "level3"]

HOST = "127.0.0.1"
PORT = 4242
TIMEOUT_S = 12

ANSI = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\([AB0-2]|\x1b[=>]")
CLEANUP = ["out1", "out2", "out1.txt", "out2.txt", "a.out", "tester_output.log"]


def strip_ansi(text):
    return ANSI.sub("", text).replace("\x0f", "")


def parse_subject(path):
    """Lit sub.txt -> (texte, expected_file, allowed, prototype, is_program)."""
    try:
        with open(path, "r", errors="replace") as f:
            text = f.read()
    except OSError:
        return "", None, "", None, False

    expected = None
    allowed = ""
    for line in text.splitlines():
        low = line.lower()
        if low.startswith("expected files"):
            m = re.search(r"([A-Za-z0-9_]+\.c)", line)
            if m:
                expected = m.group(1)
        elif low.startswith("allowed functions"):
            allowed = line.split(":", 1)[1].strip() if ":" in line else ""

    is_program = "write a program" in text.lower()

    # Prototype : ligne de declaration C apres "declared/prototyped as follows"
    prototype = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "as follows" in line.lower():
            for j in range(i + 1, min(i + 6, len(lines))):
                cand = lines[j].strip()
                if cand and ("(" in cand and ")" in cand):
                    prototype = cand
                    break
            if prototype:
                break
    return text, expected, allowed, prototype, is_program


def make_starter(name, expected, allowed, prototype, is_program):
    header = "/* %s */\n" % name
    if allowed:
        header += "/* Fonctions autorisees : %s */\n" % allowed
    header += "\n"
    if is_program or not prototype:
        inc = ""
        low = allowed.lower()
        if "write" in low:
            inc += "#include <unistd.h>\n"
        if "printf" in low:
            inc += "#include <stdio.h>\n"
        if "malloc" in low or "free" in low or "atoi" in low or "exit" in low:
            inc += "#include <stdlib.h>\n"
        if inc:
            inc += "\n"
        return header + inc + (
            "int\tmain(int argc, char **argv)\n"
            "{\n"
            "\t(void)argc;\n"
            "\t(void)argv;\n"
            "\treturn (0);\n"
            "}\n"
        )
    # fonction : transforme le prototype en definition vide
    proto = prototype.rstrip(";").rstrip()
    inc = ""
    low = allowed.lower()
    if "write" in low:
        inc += "#include <unistd.h>\n"
    if "printf" in low:
        inc += "#include <stdio.h>\n"
    if "malloc" in low or "free" in low or "atoi" in low or "exit" in low:
        inc += "#include <stdlib.h>\n"
    if inc:
        inc += "\n"
    return header + inc + proto + "\n{\n\t\n}\n"


def discover():
    exos = {}
    for level in LEVELS:
        ldir = os.path.join(REPO_ROOT, ".resources", RANK, level)
        if not os.path.isdir(ldir):
            continue
        for name in sorted(os.listdir(ldir)):
            edir = os.path.join(ldir, name)
            sub = os.path.join(edir, "sub.txt")
            tester = os.path.join(edir, "tester.sh")
            if not (os.path.isfile(sub) and os.path.isfile(tester)):
                continue
            text, expected, allowed, proto, is_prog = parse_subject(sub)
            exos[name] = {
                "name": name,
                "level": level,
                "dir": edir,
                "subject": SUJETS_FR.get(name, text),
                "expected_file": expected or (name + ".c"),
                "allowed": allowed,
                "is_program": is_prog,
                "starter": make_starter(name, expected, allowed, proto, is_prog),
            }
    return exos


EXOS = discover()


def cleanup(edir):
    for f in CLEANUP:
        try:
            os.remove(os.path.join(edir, f))
        except OSError:
            pass


def run_test(name, code):
    exo = EXOS.get(name)
    if not exo:
        return {"status": "error", "message": "Exercice inconnu."}

    rendu = os.path.join(RENDU_DIR, name)
    os.makedirs(rendu, exist_ok=True)
    with open(os.path.join(rendu, exo["expected_file"]), "w") as f:
        f.write(code)

    edir = exo["dir"]
    cleanup(edir)
    try:
        proc = subprocess.run(
            ["bash", "tester.sh"],
            cwd=edir,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=TIMEOUT_S,
        )
        out = strip_ansi((proc.stdout or "") + (proc.stderr or ""))
        status = classify(out)
    except subprocess.TimeoutExpired as e:
        partial = ""
        if e.stdout:
            partial = e.stdout if isinstance(e.stdout, str) else e.stdout.decode(errors="replace")
        out = strip_ansi(partial) + "\nTIMEOUT (boucle infinie ?)"
        status = "timeout"
    finally:
        cleanup(edir)

    result = {"status": status, "raw": out.strip()}
    if status == "fail":
        exp = re.search(r"Expected Output:\s*(.*)", out)
        yours = re.search(r"Your Output:\s*(.*)", out)
        if exp:
            result["expected"] = exp.group(1).strip()
        if yours:
            result["your"] = yours.group(1).strip()
    return result


def classify(out):
    if "PASSED" in out:
        return "passed"
    if "TIMEOUT" in out:
        return "timeout"
    if re.search(r"^[^\n]*error:", out, re.MULTILINE) or "Werror" in out:
        return "compile_error"
    if "FAIL" in out:
        return "fail"
    return "unknown"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            try:
                with open(os.path.join(HERE, "index.html"), "rb") as f:
                    self._send(200, f.read(), "text/html")
            except OSError:
                self._send(500, "index.html introuvable", "text/plain")
        elif self.path in ("/cours", "/cours.html"):
            try:
                with open(os.path.join(HERE, "cours.html"), "rb") as f:
                    self._send(200, f.read(), "text/html")
            except OSError:
                self._send(500, "cours.html introuvable", "text/plain")
        elif self.path == "/api/exercises":
            payload = []
            for level in LEVELS:
                items = [
                    {
                        "name": e["name"],
                        "subject": e["subject"],
                        "allowed": e["allowed"],
                        "is_program": e["is_program"],
                        "expected_file": e["expected_file"],
                        "starter": e["starter"],
                    }
                    for e in EXOS.values()
                    if e["level"] == level
                ]
                items.sort(key=lambda x: x["name"])
                payload.append({"level": level, "exercises": items})
            self._send(200, json.dumps(payload))
        else:
            self._send(404, json.dumps({"error": "not found"}))

    def do_POST(self):
        if self.path != "/api/test":
            self._send(404, json.dumps({"error": "not found"}))
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")
        except (ValueError, TypeError):
            self._send(400, json.dumps({"status": "error", "message": "JSON invalide"}))
            return
        name = body.get("name", "")
        code = body.get("code", "")
        if name not in EXOS:
            self._send(400, json.dumps({"status": "error", "message": "Exercice inconnu"}))
            return
        result = run_test(name, code)
        self._send(200, json.dumps(result))


def main():
    if not EXOS:
        print("Aucun exercice trouve sous .resources/%s/ — es-tu bien dans le repo ?" % RANK)
        sys.exit(1)
    if not shutil.which("gcc") and not shutil.which("cc"):
        print("gcc/cc introuvable : la moulinette a besoin d'un compilateur C.")
        sys.exit(1)
    os.makedirs(RENDU_DIR, exist_ok=True)
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print("=" * 54)
    print("  Moulinette web — Exam Rank 02")
    print("  %d exercices charges" % len(EXOS))
    print("  Ouvre :  http://%s:%d" % (HOST, PORT))
    print("  Ctrl+C pour arreter")
    print("=" * 54)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nArret.")
        srv.shutdown()


if __name__ == "__main__":
    main()
