from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class SvgRuntimeDependencyTests(unittest.TestCase):
    def test_fizzler_is_declared_for_svg_css_selectors(self) -> None:
        # Svg 3.0.84 declares Fizzler >= 1.1.0 for net35; packages.config must list it
        # explicitly because this legacy project does not resolve transitive dependencies.
        packages = ET.parse(ROOT / "ImageMultiplier/packages.config").getroot()
        fizzler = [p for p in packages.findall("package") if p.get("id") == "Fizzler"]
        self.assertEqual(1, len(fizzler))
        self.assertEqual("1.1.0", fizzler[0].get("version"))

    def test_fizzler_assembly_is_referenced_by_project(self) -> None:
        ns = {"m": "http://schemas.microsoft.com/developer/msbuild/2003"}
        project = ET.parse(ROOT / "ImageMultiplier/ImageMultiplier.csproj").getroot()
        hints = [
            ref.findtext("m:HintPath", namespaces=ns)
            for ref in project.iterfind(".//m:Reference", ns)
            if ref.get("Include") == "Fizzler"
        ]
        self.assertEqual([r"..\packages\Fizzler.1.1.0\lib\net35\Fizzler.dll"], hints)


if __name__ == "__main__":
    unittest.main()
