#!/usr/bin/env python3
"""
Moulinette web locale pour les Exams Rank 42.

Sert un editeur de code dans le navigateur et lance la VRAIE moulinette
du repo (.resources/rankXX/levelY/<exo>/tester.sh) sur le code saisi.
Les ranks disponibles (rank02, rank03, ...) sont decouverts automatiquement
sous .resources/.

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
from urllib.parse import urlparse, parse_qs

try:
    from sujets_fr import SUJETS as SUJETS_FR_RANK02
except ImportError:
    SUJETS_FR_RANK02 = {}

try:
    from sujets_fr_rank03 import SUJETS as SUJETS_FR_RANK03
except ImportError:
    SUJETS_FR_RANK03 = {}

# Traductions francaises des sujets, par rank (les noms d'exercices ne sont
# pas garantis uniques d'un rank a l'autre : la table est donc scopee).
SUJETS_FR = {
    "rank02": SUJETS_FR_RANK02,
    "rank03": SUJETS_FR_RANK03,
}

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
RESOURCES_DIR = os.path.join(REPO_ROOT, ".resources")
RENDU_DIR = os.path.join(REPO_ROOT, "rendu")

DEFAULT_RANK = "rank02"
RANK_TITLES = {
    "rank02": "Exam Rank 02",
    "rank03": "Exam Rank 03",
    "rank04": "Exam Rank 04",
    "rank05": "Exam Rank 05",
    "rank06": "Exam Rank 06",
}

# Pages de cours disponibles, par rank. Les autres ranks n'ont pas (encore)
# de cours : l'onglet est desactive cote client.
COURSE_FILES = {
    "rank02": "cours.html",
    "rank03": "cours_rank03.html",
}

HOST = "127.0.0.1"
PORT = 4242
TIMEOUT_S = 12

ANSI = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\([AB0-2]|\x1b[=>]")
CLEANUP = ["out1", "out2", "out1.txt", "out2.txt", "a.out", "tester_output.log"]

# Sujets ou le squelette generique (derive du prototype dans sub.txt) ne
# convient pas tel quel (parametres variadiques non nommes, header a inclure,
# etc). Cle : (rank, nom_exo).
STARTER_OVERRIDES = {
    ("rank03", "scanf"): (
        '/* ft_scanf — complete le squelette fourni par le sujet. */\n'
        '/* Fonctions autorisees : fgetc, ungetc, ferror, feof, isspace,\n'
        '   isdigit, stdin, va_start, va_arg, va_copy, va_end */\n'
        '\n'
        '#include <stdarg.h>\n'
        '#include <stdio.h>\n'
        '#include <ctype.h>\n'
        '\n'
        'int\tmatch_space(FILE *f)\n'
        '{\n'
        '\t// a completer\n'
        '\treturn (0);\n'
        '}\n'
        '\n'
        'int\tmatch_char(FILE *f, char c)\n'
        '{\n'
        '\t// a completer\n'
        '\treturn (0);\n'
        '}\n'
        '\n'
        'int\tscan_char(FILE *f, va_list ap)\n'
        '{\n'
        '\t// a completer\n'
        '\treturn (0);\n'
        '}\n'
        '\n'
        'int\tscan_int(FILE *f, va_list ap)\n'
        '{\n'
        '\t// a completer\n'
        '\treturn (0);\n'
        '}\n'
        '\n'
        'int\tscan_string(FILE *f, va_list ap)\n'
        '{\n'
        '\t// a completer\n'
        '\treturn (0);\n'
        '}\n'
        '\n'
        'int\tmatch_conv(FILE *f, const char **format, va_list ap)\n'
        '{\n'
        '\tswitch (**format)\n'
        '\t{\n'
        '\t\tcase \'c\':\n'
        '\t\t\treturn scan_char(f, ap);\n'
        '\t\tcase \'d\':\n'
        '\t\t\tmatch_space(f);\n'
        '\t\t\treturn scan_int(f, ap);\n'
        '\t\tcase \'s\':\n'
        '\t\t\tmatch_space(f);\n'
        '\t\t\treturn scan_string(f, ap);\n'
        '\t\tcase EOF:\n'
        '\t\t\treturn -1;\n'
        '\t\tdefault:\n'
        '\t\t\treturn -1;\n'
        '\t}\n'
        '}\n'
        '\n'
        'int\tft_vfscanf(FILE *f, const char *format, va_list ap)\n'
        '{\n'
        '\tint nconv = 0;\n'
        '\n'
        '\tint c = fgetc(f);\n'
        '\tif (c == EOF)\n'
        '\t\treturn EOF;\n'
        '\tungetc(c, f);\n'
        '\n'
        '\twhile (*format)\n'
        '\t{\n'
        '\t\tif (*format == \'%\')\n'
        '\t\t{\n'
        '\t\t\tformat++;\n'
        '\t\t\tif (match_conv(f, &format, ap) != 1)\n'
        '\t\t\t\tbreak;\n'
        '\t\t\telse\n'
        '\t\t\t\tnconv++;\n'
        '\t\t}\n'
        '\t\telse if (isspace(*format))\n'
        '\t\t{\n'
        '\t\t\tif (match_space(f) == -1)\n'
        '\t\t\t\tbreak;\n'
        '\t\t}\n'
        '\t\telse if (match_char(f, *format) != 1)\n'
        '\t\t\tbreak;\n'
        '\t\tformat++;\n'
        '\t}\n'
        '\n'
        '\tif (ferror(f))\n'
        '\t\treturn EOF;\n'
        '\treturn nconv;\n'
        '}\n'
        '\n'
        'int\tft_scanf(const char *format, ...)\n'
        '{\n'
        '\tva_list\tap;\n'
        '\tint\t\tret;\n'
        '\n'
        '\tva_start(ap, format);\n'
        '\tret = ft_vfscanf(stdin, format, ap);\n'
        '\tva_end(ap);\n'
        '\treturn (ret);\n'
        '}\n'
    ),
}

# Sujets dont le squelette de depart est un fichier fourni dans le dossier du
# sujet (code casse a reparer, boilerplate a completer). Valeur :
# (fichier_source, prefixe_ajoute, suffixe_ajoute). Cle : (rank, nom_exo).
STARTER_FROM_FILE = {
    # Le sujet fournit broken_gnl.c (le code casse) ; le fichier a rendre est
    # get_next_line.c. On part donc du code casse, a reparer sur place.
    ("rank03", "broken_gnl"): (
        "broken_gnl.c",
        "/* get_next_line.c — repare ce code (il vient de broken_gnl.c).\n"
        "   Fonctions autorisees : read, free, malloc\n"
        "   Compile avec -D BUFFER_SIZE=xx : ne redefinis pas BUFFER_SIZE. */\n\n",
        "",
    ),
    # tsp.c fournit le main et declare 3 fonctions a implementer : on ajoute
    # des stubs pour que le squelette compile et lie des le depart.
    ("rank03", "tsp"): (
        "tsp.c",
        "/* tsp.c — le main et les prototypes sont fournis par le sujet.\n"
        "   A toi d'ecrire distance(), total_distance() et solve(). */\n\n",
        "\n"
        "float\tdistance(t_city a, t_city b)\n"
        "{\n"
        "\t(void)a;\n"
        "\t(void)b;\n"
        "\treturn (0.0f);\n"
        "}\n"
        "\n"
        "float\ttotal_distance(t_city *cities, int *path, int n)\n"
        "{\n"
        "\t(void)cities;\n"
        "\t(void)path;\n"
        "\t(void)n;\n"
        "\treturn (0.0f);\n"
        "}\n"
        "\n"
        "void\tsolve(t_city *cities, int *path, int n, int pos, float *min)\n"
        "{\n"
        "\t(void)cities;\n"
        "\t(void)path;\n"
        "\t(void)n;\n"
        "\t(void)pos;\n"
        "\t(void)min;\n"
        "}\n",
    ),
}


def starter_from_file(edir, spec):
    """Lit le squelette fourni par le sujet, ou None si illisible."""
    src, prefix, suffix = spec
    try:
        with open(os.path.join(edir, src), "r", errors="replace") as f:
            body = f.read()
    except OSError:
        return None
    if body and not body.endswith("\n"):
        body += "\n"
    return prefix + body + suffix


# Fichiers annexes (deja "corrects" / boilerplate) a recopier depuis le sujet
# dans rendu/<exo>/ avant de lancer la moulinette, en plus du fichier que
# l'utilisateur edite. Cle : (rank, nom_exo).
EXTRA_FILES = {
    ("rank03", "broken_gnl"): ["get_next_line.h"],
}


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

    # Prototype : ligne de declaration C apres "declared/prototyped as
    # follows" ou "prototype should be"
    prototype = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low_line = line.lower()
        if "as follows" in low_line or "should be" in low_line:
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
    if "write" in low or "read" in low:
        inc += "#include <unistd.h>\n"
    if "printf" in low:
        inc += "#include <stdio.h>\n"
    if "malloc" in low or "free" in low or "atoi" in low or "exit" in low:
        inc += "#include <stdlib.h>\n"
    if inc:
        inc += "\n"
    return header + inc + proto + "\n{\n\t\n}\n"


def discover_ranks():
    """Scanne .resources/rankNN/levelY/ et ne garde que les ranks ayant au
    moins un exercice (sub.txt + tester.sh)."""
    ranks = {}
    if not os.path.isdir(RESOURCES_DIR):
        return ranks
    for rank in sorted(os.listdir(RESOURCES_DIR)):
        if not re.match(r"^rank\d+$", rank):
            continue
        rdir = os.path.join(RESOURCES_DIR, rank)
        if not os.path.isdir(rdir):
            continue
        levels = []
        for level in sorted(os.listdir(rdir)):
            ldir = os.path.join(rdir, level)
            if not os.path.isdir(ldir):
                continue
            has_exo = any(
                os.path.isfile(os.path.join(ldir, n, "sub.txt"))
                and os.path.isfile(os.path.join(ldir, n, "tester.sh"))
                for n in os.listdir(ldir)
                if os.path.isdir(os.path.join(ldir, n))
            )
            if has_exo:
                levels.append(level)
        if levels:
            ranks[rank] = levels
    return ranks


def discover(rank, levels):
    exos = {}
    for level in levels:
        ldir = os.path.join(RESOURCES_DIR, rank, level)
        if not os.path.isdir(ldir):
            continue
        for name in sorted(os.listdir(ldir)):
            edir = os.path.join(ldir, name)
            sub = os.path.join(edir, "sub.txt")
            tester = os.path.join(edir, "tester.sh")
            if not (os.path.isfile(sub) and os.path.isfile(tester)):
                continue
            text, expected, allowed, proto, is_prog = parse_subject(sub)
            key = (rank, name)
            starter = STARTER_OVERRIDES.get(key)
            if starter is None and key in STARTER_FROM_FILE:
                starter = starter_from_file(edir, STARTER_FROM_FILE[key])
            if starter is None:
                starter = make_starter(name, expected, allowed, proto, is_prog)
            exos[name] = {
                "name": name,
                "level": level,
                "dir": edir,
                "subject": SUJETS_FR.get(rank, {}).get(name, text),
                "expected_file": expected or (name + ".c"),
                "allowed": allowed,
                "is_program": is_prog,
                "starter": starter,
                "extra_files": EXTRA_FILES.get(key, []),
            }
    return exos


RANKS = discover_ranks()
EXOS = {rank: discover(rank, levels) for rank, levels in RANKS.items()}


def snapshot(edir):
    """Liste les fichiers presents dans le dossier du sujet avant un run."""
    try:
        return set(os.listdir(edir))
    except OSError:
        return set()


def cleanup(edir, before=None):
    """Supprime les artefacts laisses par tester.sh.

    Certains testers (n_queens, par ex.) ne nettoient pas derriere eux : on
    retire tout fichier apparu pendant le run, plus les noms connus.
    """
    for f in CLEANUP:
        try:
            os.remove(os.path.join(edir, f))
        except OSError:
            pass
    if before is None:
        return
    for f in snapshot(edir) - before:
        path = os.path.join(edir, f)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except OSError:
            pass


def run_test(rank, name, code):
    exo = EXOS.get(rank, {}).get(name)
    if not exo:
        return {"status": "error", "message": "Exercice inconnu."}

    rendu = os.path.join(RENDU_DIR, name)
    os.makedirs(rendu, exist_ok=True)
    with open(os.path.join(rendu, exo["expected_file"]), "w") as f:
        f.write(code)
    for extra in exo["extra_files"]:
        src = os.path.join(exo["dir"], extra)
        if os.path.isfile(src):
            shutil.copyfile(src, os.path.join(rendu, extra))

    edir = exo["dir"]
    before = snapshot(edir)
    cleanup(edir, before)
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
        cleanup(edir, before)

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
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        if path in ("/", "/index.html"):
            try:
                with open(os.path.join(HERE, "index.html"), "rb") as f:
                    self._send(200, f.read(), "text/html")
            except OSError:
                self._send(500, "index.html introuvable", "text/plain")
        elif path in ("/cours", "/cours.html"):
            rank = (query.get("rank") or [DEFAULT_RANK])[0]
            fname = COURSE_FILES.get(rank)
            if not fname:
                self._send(404, "Pas de cours pour ce rank.", "text/plain")
                return
            try:
                with open(os.path.join(HERE, fname), "rb") as f:
                    self._send(200, f.read(), "text/html")
            except OSError:
                self._send(500, fname + " introuvable", "text/plain")
        elif path == "/api/ranks":
            payload = [
                {
                    "rank": rank,
                    "title": RANK_TITLES.get(rank, rank),
                    "levels": levels,
                    "has_course": rank in COURSE_FILES
                    and os.path.isfile(os.path.join(HERE, COURSE_FILES[rank])),
                }
                for rank, levels in RANKS.items()
            ]
            self._send(200, json.dumps(payload))
        elif path == "/api/exercises":
            rank = (query.get("rank") or [DEFAULT_RANK])[0]
            levels = RANKS.get(rank, [])
            exos = EXOS.get(rank, {})
            payload = []
            for level in levels:
                items = [
                    {
                        "name": e["name"],
                        "subject": e["subject"],
                        "allowed": e["allowed"],
                        "is_program": e["is_program"],
                        "expected_file": e["expected_file"],
                        "starter": e["starter"],
                    }
                    for e in exos.values()
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
        rank = body.get("rank") or DEFAULT_RANK
        name = body.get("name", "")
        code = body.get("code", "")
        if name not in EXOS.get(rank, {}):
            self._send(400, json.dumps({"status": "error", "message": "Exercice inconnu"}))
            return
        result = run_test(rank, name, code)
        self._send(200, json.dumps(result))


def main():
    if not any(EXOS.values()):
        print("Aucun exercice trouve sous .resources/ — es-tu bien dans le repo ?")
        sys.exit(1)
    if not shutil.which("gcc") and not shutil.which("cc"):
        print("gcc/cc introuvable : la moulinette a besoin d'un compilateur C.")
        sys.exit(1)
    os.makedirs(RENDU_DIR, exist_ok=True)
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print("=" * 54)
    print("  Moulinette web — 42 Exams")
    for rank in RANKS:
        print("  %-8s %-16s %d exercices" % (rank, RANK_TITLES.get(rank, ""), len(EXOS[rank])))
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
