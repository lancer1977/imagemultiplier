# ImageMultiplier Repo State

Last reviewed: 2026-07-03

## Purpose

`ImageMultiplier` is a Xamarin Studio add-in that reads `.multiplier`
specifications and generates resized PNG outputs from matching SVG source files.

## Current State

- Main solution: `ImageMultiplier.sln`.
- Add-in project: `ImageMultiplier/ImageMultiplier.csproj`.
- Add-in metadata: `Manifest.addin.xml`, `addin.info`, `addin-project.xml`, and
  `ImageMultiplier/Properties/ImageMultiplier.addin.xml`.
- Package metadata: `ImageMultiplier/packages.config`.
- Full packaging depends on Xamarin Studio/MonoDevelop-era tooling that is not
  installed in this Linux environment.

## Native Validation

```bash
bash scripts/validate.sh
```

The current validation path checks repository shape and XML metadata. Full build
and `.mpack` generation should be verified on a legacy Xamarin Studio-compatible
machine.
