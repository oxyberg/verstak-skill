#!/usr/bin/env python3
"""Create diagnostic overlay/diff artifacts without resizing source images."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        from PIL import Image, ImageChops, ImageStat
    except ImportError:
        parser.exit(2, "Pillow unavailable: use an existing image tool or visual inspection.\n")

    def opaque(path):
        with Image.open(path) as source:
            rgba = source.convert("RGBA")
            background = Image.new("RGBA", rgba.size, "white")
            return Image.alpha_composite(background, rgba).convert("RGB")

    try:
        reference, actual = opaque(args.reference), opaque(args.actual)
        if reference.size != actual.size:
            parser.error(f"Image dimensions differ: {reference.size} vs {actual.size}; align captures, do not resize.")
        outputs = {name: args.output_dir / name for name in ("overlay.png", "diff.png", "summary.json")}
        sources = {args.reference.resolve(), args.actual.resolve()}
        if any(path.resolve() in sources for path in outputs.values()):
            parser.error("Output would overwrite a source image; choose another output directory.")
        diff = ImageChops.difference(reference, actual)
        red, green, blue = diff.split()
        maximum = ImageChops.lighter(ImageChops.lighter(red, green), blue)
        histogram = maximum.histogram()
        pixels = reference.width * reference.height
        summary = {
            "size_px": list(reference.size),
            "changed_pixel_fraction": (pixels - histogram[0]) / pixels,
            "mean_absolute_channel_difference_0_255": sum(ImageStat.Stat(diff).mean) / 3,
            "difference_bbox": maximum.getbbox(),
            "artifacts": {name: str(path.resolve()) for name, path in outputs.items()},
            "note": "Diagnostic only; visual inspection determines fidelity.",
        }
        args.output_dir.mkdir(parents=True, exist_ok=True)
        Image.blend(reference, actual, 0.5).save(outputs["overlay.png"])
        diff.save(outputs["diff.png"])
        outputs["summary.json"].write_text(json.dumps(summary, indent=2) + "\n")
        print(json.dumps(summary))
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        parser.exit(2, f"Comparison failed: {error}\n")


if __name__ == "__main__":
    main()
