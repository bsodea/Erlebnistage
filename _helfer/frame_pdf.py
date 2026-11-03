
import os
from PIL import Image, ImageDraw, ImageFilter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

# ---------------- CONFIGURATION ----------------

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "framed_images"
OUTPUT_PDF = "gold_framed_collection.pdf"

PAGE_SIZE = A4
DPI = 200

# Frame dimensions in pixels
FRAME_WIDTH = 65
OUTER_MARGIN = 25

# Gold color palette
GOLD_DARK = (105, 65, 15)
GOLD_MID = (190, 145, 55)
GOLD_LIGHT = (255, 230, 145)
GOLD_BRIGHT = (255, 248, 210)

# ------------------------------------------------


def create_gold_frame(image):
    """Add a realistic-looking metallic gold frame."""

    image = image.convert("RGB")

    w, h = image.size
    fw = FRAME_WIDTH

    # Create canvas with space for frame
    result = Image.new(
        "RGB",
        (w + 2 * fw, h + 2 * fw),
        GOLD_DARK
    )

    draw = ImageDraw.Draw(result)

    # Main gold frame, built from multiple metallic bands
    bands = [
        (0, 0, w + 2*fw - 1, h + 2*fw - 1, GOLD_DARK, 0),
        (7, 7, w + 2*fw - 8, h + 2*fw - 8, GOLD_MID, 5),
        (14, 14, w + 2*fw - 15, h + 2*fw - 15, GOLD_LIGHT, 4),
        (22, 22, w + 2*fw - 23, h + 2*fw - 23, GOLD_MID, 5),
        (30, 30, w + 2*fw - 31, h + 2*fw - 31, GOLD_BRIGHT, 3),
    ]

    for x1, y1, x2, y2, color, width in bands:
        draw.rectangle(
            [x1, y1, x2, y2],
            outline=color,
            width=width
        )

    # Add subtle decorative gold detailing
    for offset in range(38, fw - 8, 7):
        draw.rectangle(
            [
                offset,
                offset,
                w + 2*fw - offset - 1,
                h + 2*fw - offset - 1
            ],
            outline=GOLD_MID,
            width=1
        )

    # Add corner ornaments
    corner_size = 18
    corners = [
        (fw, fw),
        (w + fw, fw),
        (fw, h + fw),
        (w + fw, h + fw)
    ]

    for cx, cy in corners:
        draw.ellipse(
            [
                cx - corner_size // 2,
                cy - corner_size // 2,
                cx + corner_size // 2,
                cy + corner_size // 2
            ],
            fill=GOLD_LIGHT,
            outline=GOLD_DARK,
            width=3
        )

    # Insert original image inside frame
    result.paste(image, (fw, fw))

    return result


def process_images():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    images = [
        f for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff")
        )
    ]

    images.sort()

    if not images:
        print("No images found!")
        return

    page_width, page_height = PAGE_SIZE

    pdf = canvas.Canvas(
        OUTPUT_PDF,
        pagesize=PAGE_SIZE
    )

    for index, filename in enumerate(images):

        print(f"Processing {filename}...")

        path = os.path.join(INPUT_FOLDER, filename)

        with Image.open(path) as original:
            original = original.convert("RGB")

            # Resize huge source images for manageable processing
            original.thumbnail((2400, 2400), Image.Resampling.LANCZOS)

            # Add gold frame
            framed = create_gold_frame(original)

            # Save framed image
            output_path = os.path.join(
                OUTPUT_FOLDER,
                f"framed_{index + 1:03d}.jpg"
            )

            framed.save(
                output_path,
                "JPEG",
                quality=95,
                dpi=(DPI, DPI)
            )

        # Calculate PDF image dimensions
        img_width, img_height = framed.size

        # Available page area (leave margins)
        margin = 35

        available_width = page_width - 2 * margin
        available_height = page_height - 2 * margin

        # Preserve aspect ratio
        scale = min(
            available_width / img_width,
            available_height / img_height
        )

        final_width = img_width * scale
        final_height = img_height * scale

        # Center on page
        x = (page_width - final_width) / 2
        y = (page_height - final_height) / 2

        # White PDF background
        pdf.setFillColorRGB(1, 1, 1)
        pdf.rect(0, 0, page_width, page_height, fill=1, stroke=0)

        # Place image
        pdf.drawImage(
            ImageReader(output_path),
            x,
            y,
            width=final_width,
            height=final_height,
            preserveAspectRatio=True
        )

        # One image per page
        pdf.showPage()

    pdf.save()

    print("\nDone!")
    print(f"PDF created: {OUTPUT_PDF}")
    print(f"Framed images saved in: {OUTPUT_FOLDER}")


if __name__ == "__main__":
    process_images()
