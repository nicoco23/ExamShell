# Moulinette web — Exam Rank 02

Un éditeur de code dans le navigateur qui lance la **vraie moulinette** du repo
(`.resources/rank02/*/*/tester.sh`) sur ton code, avec correction quasi temps réel.

## Lancer

```bash
bash webmoulinette/start.sh
```

Puis ouvre **http://127.0.0.1:4242** dans ton navigateur.

`Ctrl+C` dans le terminal pour arrêter.

> Si le port 4242 est déjà pris (« Address already in use »), un ancien
> serveur tourne encore : `pkill -f webmoulinette/server.py` puis relance.

## Une seule app, trois onglets

En haut de la page :

- **📖 Cours** — le cours complet (les 8 familles, checkpoints, auto-évaluation,
  quiz) directement intégré, sans quitter l'app.
- **⌨️ Entraînement** — l'éditeur + la moulinette (voir ci-dessous).
- **⏱ Examen** — le mode chronométré avec tirage aléatoire.

Tu lis le cours et tu codes au même endroit : bascule d'un onglet à l'autre
quand tu veux.

### Coder directement dans le cours

L'onglet **📖 Cours** contient des **éditeurs intégrés**. Après chaque famille
(et dans la boîte à outils) : un exercice mis en avant + un **« Banc
d'exercices »** dépliable qui regroupe **tous les autres exercices de cette
notion**. Au total, **les 55 exercices de l'exam sont codables directement dans
le cours**, chacun rangé dans sa famille, compilés/testés par la vraie
moulinette (*Tester* ou `Ctrl+Entrée`). Le code est partagé avec l'onglet
Entraînement (même stockage local).

Le cours est organisé en titres **« Notion : … »** (transformer argv[1],
découper en mots, ensembles, maths, bits, allocation, listes, tri/récursion,
reproductions libc &amp; divers) et se termine par un index
« 06 — Les 55 exercices, notion par notion ».

Les **sujets sont affichés en français** : les traductions vivent dans
`webmoulinette/sujets_fr.py` et sont servies à la place de l'anglais. Les
fichiers d'origine (`.resources/**/sub.txt`) ne sont pas modifiés, et la
correction reste 100 % identique (métadonnées lues sur le sujet d'origine).

## Utilisation

1. Choisis un exercice dans la colonne de gauche (les 55 exos des niveaux 0 à 3).
2. Le sujet s'affiche en haut, un squelette de départ est pré-rempli.
3. Écris ton code. Avec **« correction auto »** activée, la moulinette se
   relance ~1 s après que tu arrêtes de taper. Sinon, clique **▶ Tester**
   (ou `Ctrl+Entrée`).
4. Le verdict s'affiche : `PASSED`, `FAIL` (avec sortie attendue vs la tienne),
   `NE COMPILE PAS` (erreurs gcc) ou `TIMEOUT`.

- Ton code est sauvegardé par exercice dans le navigateur (localStorage).
- `reset` remet le squelette de départ.
- Une pastille ✓ / ✗ apparaît à côté de chaque exercice réussi / raté.

## Mode examen (chrono + tirage aléatoire)

Bascule sur **Examen** en haut à gauche, choisis une durée (1 h / 2 h / 3 h)
et lance :

- Un sujet est **tiré au hasard** dans le niveau courant (0 → 3).
- Réussir le sujet **fait passer au niveau suivant** ; les 4 niveaux validés = examen réussi.
- **↻ Passer** tire un autre sujet du même niveau (sans avancer).
- Un **chronomètre global** décompte (orange à 5 min, rouge clignotant à 1 min).
  À zéro, l'examen s'arrête et un récapitulatif s'affiche.
- La liste de gauche est verrouillée pendant l'examen (pas de triche).
- L'examen **survit à un rechargement** de page tant qu'il reste du temps.

## Comment ça marche

Le serveur écrit ton code dans `rendu/<exo>/<exo>.c` (exactement comme le shell
d'exam), se place dans le dossier de l'exercice et exécute `tester.sh`, qui
compile ta solution **et** la solution de référence puis compare les sorties.
C'est donc la moulinette d'origine, pas une réimplémentation.

## Prérequis

- `python3` (serveur, stdlib uniquement — aucune dépendance)
- `gcc` ou `cc` (compilation C)

## Sécurité

Le serveur **compile et exécute du code C local**. Il n'écoute que sur
`127.0.0.1` (localhost). À n'utiliser que sur ta propre machine, comme le
shell d'exam d'origine.
