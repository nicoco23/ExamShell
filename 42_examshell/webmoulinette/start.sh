#!/bin/bash
# Lance la moulinette web (tous les Exams Rank détectés sous .resources/).
cd "$(dirname "$0")/.." || exit 1
exec python3 webmoulinette/server.py
