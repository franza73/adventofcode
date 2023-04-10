#!/usr/local/bin/bash

for d in {1..25}; do
    f="day$d.py"
    [ -f "$f" ] || break
    echo "== $f =="
    flake8 $f
    python3 $f
done
