#!/bin/bash
# Lance la moulinette web pour l'Exam Rank 02.
cd "$(dirname "$0")/.." || exit 1
exec python3 webmoulinette/server.py
