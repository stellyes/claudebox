"""
Creates an animated GIF: Earth photo visible through a spinning Claude star logo mask.
Uses actual globe.jpg and claude.svg from Downloads.
"""

import glob
import io
import math
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# --- Configuration ---
SIZE = 500          # Canvas size (square)
FRAMES = 288       # Frames for one full rotation (4x more for smooth animation)
DURATION = 40       # ms per frame (~25fps, same total rotation time)
OUTPUT = "claude_earth_spin.gif"

EARTH_PATH = "/Users/slimreaper/Downloads/globe.jpg"
SVG_PATH = "/Users/slimreaper/Downloads/claude.svg"


def load_earth(size):
    """Load and crop the Earth image to a centered square, resized to `size`."""
    img = Image.open(EARTH_PATH).convert("RGBA")
    w, h = img.size
    s = min(w, h)
    left = (w - s) // 2
    top = (h - s) // 2
    img = img.crop((left, top, left + s, top + s))
    img = img.resize((size, size), Image.LANCZOS)
    return img


def svg_to_mask(size):
    """
    Render the Claude SVG and extract the star shape as a grayscale mask.
    The SVG has an orange star (#d97757) on transparent, but qlmanage
    renders it on white -- so we threshold by detecting non-white pixels.
    """
    rendered = None

    # Try rsvg-convert first (preserves transparency)
    try:
        result = subprocess.run(
            ["rsvg-convert", "-w", str(size * 2), "-h", str(size * 2), SVG_PATH],
            capture_output=True, timeout=10
        )
        if result.returncode == 0:
            rendered = Image.open(io.BytesIO(result.stdout)).convert("RGBA")
            # rsvg preserves alpha, so use it directly
            _, _, _, a = rendered.split()
            mask = a.resize((size, size), Image.LANCZOS)
            mask = mask.point(lambda p: 255 if p > 50 else 0)
            return mask
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: qlmanage (macOS) - renders on white background
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            subprocess.run(
                ["qlmanage", "-t", "-s", str(size * 2), "-o", tmpdir, SVG_PATH],
                capture_output=True, timeout=10
            )
            pngs = glob.glob(f"{tmpdir}/*.png")
            if pngs:
                rendered = Image.open(pngs[0]).convert("RGB")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    if rendered is None:
        raise RuntimeError("Cannot render SVG. Install librsvg: brew install librsvg")

    # Extract mask from white-background render:
    # The star is orange (#d97757 ≈ R217 G119 B87), background is white (255,255,255)
    # Threshold: if pixel is NOT close to white, it's part of the star
    arr = np.array(rendered).astype(np.float32)
    # Distance from white
    white = np.array([255.0, 255.0, 255.0])
    dist = np.sqrt(np.sum((arr - white) ** 2, axis=2))
    # Anything more than ~30 away from pure white is star
    mask_arr = (dist > 30).astype(np.uint8) * 255

    mask = Image.fromarray(mask_arr, mode="L")
    mask = mask.resize((size, size), Image.LANCZOS)
    # Clean up edges
    mask = mask.point(lambda p: 255 if p > 128 else 0)
    return mask


def rotate_mask(mask, angle):
    """Rotate mask around its center by `angle` degrees."""
    return mask.rotate(angle, resample=Image.BICUBIC, expand=False)


def create_gif():
    print("Loading Earth image...")
    earth = load_earth(SIZE)

    print("Rendering Claude star mask from SVG...")
    base_mask = svg_to_mask(SIZE)

    # Crop to bounding box and re-center to fill the frame
    bbox = base_mask.getbbox()
    if bbox:
        cropped = base_mask.crop(bbox)
        cw, ch = cropped.size
        # Scale to fill ~90% of the frame
        target = int(SIZE * 0.90)
        scale = target / max(cw, ch)
        new_w, new_h = int(cw * scale), int(ch * scale)
        cropped = cropped.resize((new_w, new_h), Image.LANCZOS)
        # Re-threshold after resize
        cropped = cropped.point(lambda p: 255 if p > 128 else 0)
        base_mask = Image.new("L", (SIZE, SIZE), 0)
        ox = (SIZE - new_w) // 2
        oy = (SIZE - new_h) // 2
        base_mask.paste(cropped, (ox, oy))

    # Save mask for debugging
    base_mask.save("/tmp/claude_star_mask.png")
    print("  Mask saved to /tmp/claude_star_mask.png for inspection")

    print(f"Generating {FRAMES} frames...")
    frames = []
    bg_color = (0, 0, 0)

    for i in range(FRAMES):
        angle = (360 / FRAMES) * i

        rotated_mask = rotate_mask(base_mask, angle)

        # Black background, Earth visible through the star mask
        frame = Image.new("RGBA", (SIZE, SIZE), (*bg_color, 255))
        earth_masked = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        earth_masked.paste(earth, (0, 0), rotated_mask)
        frame = Image.alpha_composite(frame, earth_masked)

        frames.append(frame.convert("RGB"))

        if (i + 1) % 12 == 0:
            print(f"  Frame {i + 1}/{FRAMES}")

    print(f"Saving GIF to {OUTPUT}...")
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=DURATION,
        loop=0,
        optimize=True,
    )

    import os
    fsize = os.path.getsize(OUTPUT) / (1024 * 1024)
    print(f"Done! Created {OUTPUT} ({fsize:.1f} MB)")


if __name__ == "__main__":
    create_gif()
