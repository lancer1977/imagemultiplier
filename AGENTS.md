# AGENTS.md

## Purpose

This repository contains a legacy Xamarin Studio add-in for generating multiple
PNG sizes from SVG source files and `.multiplier` specifications.

## Workflow

- Read `README.md`, `repo-state.md`, and `docs/index.md` before changing files.
- Keep maintenance changes small and focused.
- Do not modernize the add-in or project format unless that is the named task.
- Treat full package builds as legacy Xamarin Studio/MonoDevelop environment
  work.

## Validation

Run the repo-native validation script:

```bash
bash scripts/validate.sh
```

The script performs a Linux-friendly repository shape and XML metadata smoke.
Full add-in packaging requires Xamarin Studio or a compatible MonoDevelop add-in
toolchain.
