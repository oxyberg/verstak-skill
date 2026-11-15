import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image


SCRIPT = Path(__file__).resolve().parents[1] / "verstak/scripts/compare_images.py"


class CompareImagesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.reference = self.root / "reference.png"
        self.actual = self.root / "actual.png"
        Image.new("RGB", (4, 4), "white").save(self.reference)
        Image.new("RGB", (4, 4), "white").save(self.actual)

    def compare(self, output=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.reference), str(self.actual),
             "--output-dir", str(output or self.root / "output")],
            capture_output=True, text=True,
        )

    def test_identical_images(self):
        result = self.compare()
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["changed_pixel_fraction"], 0)
        self.assertIsNone(summary["difference_bbox"])
        with Image.open(self.root / "output/overlay.png") as overlay:
            self.assertEqual(overlay.getpixel((0, 0)), (255, 255, 255))

    def test_single_pixel_difference(self):
        actual = Image.new("RGB", (4, 4), "white")
        actual.putpixel((2, 1), (0, 255, 255))
        actual.save(self.actual)
        result = self.compare()
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = json.loads(result.stdout)
        self.assertEqual(summary["changed_pixel_fraction"], 1 / 16)
        self.assertEqual(summary["difference_bbox"], [2, 1, 3, 2])
        self.assertAlmostEqual(summary["mean_absolute_channel_difference_0_255"], 255 / 48)
        with Image.open(self.root / "output/diff.png") as diff:
            self.assertEqual(diff.getpixel((2, 1)), (255, 0, 0))

    def test_transparency_composited_on_white(self):
        Image.new("RGBA", (4, 4), (0, 0, 0, 0)).save(self.actual)
        result = self.compare()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["changed_pixel_fraction"], 0)

    def test_dimension_mismatch_does_not_generate_artifacts(self):
        Image.new("RGB", (5, 4)).save(self.actual)
        result = self.compare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dimensions differ", result.stderr)
        self.assertFalse((self.root / "output").exists())

    def test_source_cannot_be_overwritten(self):
        self.reference = self.root / "overlay.png"
        Image.new("RGB", (4, 4), "white").save(self.reference)
        original = self.reference.read_bytes()
        result = self.compare(self.root)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.reference.read_bytes(), original)

    def test_missing_input(self):
        self.actual.unlink()
        result = self.compare()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Comparison failed", result.stderr)


if __name__ == "__main__":
    unittest.main()
