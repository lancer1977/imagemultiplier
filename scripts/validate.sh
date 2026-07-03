#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

required_paths=(
  "AGENTS.md"
  "README.md"
  "repo-state.md"
  "docs/index.md"
  "docs/validation.md"
  ".devstudio/project.yaml"
  "ImageMultiplier.sln"
  "ImageMultiplier/ImageMultiplier.csproj"
  "ImageMultiplier/packages.config"
  "ImageMultiplier/Manifest.addin.xml"
  "ImageMultiplier/Properties/ImageMultiplier.addin.xml"
  "ImageMultiplier/addin.info"
  "ImageMultiplier/ImageMultiplierGenerator.cs"
  "ImageMultiplier/ImageProcessor.cs"
  "addin-project.xml"
)

for path in "${required_paths[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "Missing required path: $path" >&2
    exit 1
  fi
done

python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET

for raw_path in [
    "ImageMultiplier/ImageMultiplier.csproj",
    "ImageMultiplier/packages.config",
    "ImageMultiplier/Manifest.addin.xml",
    "ImageMultiplier/Properties/ImageMultiplier.addin.xml",
    "addin-project.xml",
]:
    path = Path(raw_path)
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        raise SystemExit(f"Invalid XML in {path}: {exc}") from exc
PY

echo "ImageMultiplier repository shape validation passed."
