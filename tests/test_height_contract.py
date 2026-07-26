from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HeightContractTests(unittest.TestCase):
    def test_output_specifier_exposes_optional_height(self) -> None:
        source = (ROOT / "ImageMultiplier/OutputSpecifier.cs").read_text()
        self.assertIn("public int height { get; set; }", source)

    def test_missing_height_falls_back_to_width(self) -> None:
        source = (ROOT / "ImageMultiplier/ImageProcessor.cs").read_text()
        self.assertIn(
            "int height = outputter.height > 0 ? outputter.height : outputter.width;",
            source,
        )

    def test_height_controls_svg_and_bitmap_dimensions(self) -> None:
        source = (ROOT / "ImageMultiplier/ImageProcessor.cs").read_text()
        self.assertIn(
            "svgDocument.Height = new SvgUnit(SvgUnitType.Pixel, height);",
            source,
        )
        self.assertIn("new System.Drawing.Bitmap(width, height)", source)

    def test_syntax_definition_recognizes_height(self) -> None:
        syntax = (ROOT / "ImageMultiplier/ImageMultiplierSyntax.xml").read_text()
        self.assertIn("<Word>height</Word>", syntax)


if __name__ == "__main__":
    unittest.main()
