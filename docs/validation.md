# Validation

## Command

Run the root validation wrapper:

```bash
bash scripts/validate.sh
```

The wrapper performs a Linux-friendly smoke check. It verifies the expected
solution, C# project, add-in manifests, package metadata, and documentation
files, then parses the XML metadata files for well-formedness.

## Full Build Boundary

ImageMultiplier targets Xamarin Studio/MonoDevelop-era .NET Framework 4.5 add-in
tooling. Full build and packaging need a legacy workstation with:

- Xamarin Studio or compatible MonoDevelop add-in tooling.
- MSBuild/xbuild support for the project format.
- Restored packages from `ImageMultiplier/packages.config`.
- `mdtool` for package creation.

The historical package command documented in the README is:

```bash
"/Applications/Xamarin Studio.app/Contents/MacOS/mdtool" setup pack ImageMultiplier/bin/debug/ImageMultiplier.dll
```

In the current Linux environment, `msbuild`, `xbuild`, `nuget`, `mono`, and
`mdtool` are not installed, so CI uses the structural validation wrapper instead
of claiming a full add-in package build.

## Tests

No automated test project is currently present. The repeatable health check
available in this environment is `scripts/validate.sh`.
