#!/usr/bin/env bash
set -euo pipefail

find . -maxdepth 3 -type f \( -name '*.xml' -o -name '*.csproj' -o -name '*.config' -o -name '*.resx' \) -print0 \
  | xargs -0 xmllint --noout
python3 -m unittest -v tests/test_height_contract.py
