import shutil
import subprocess
import turtle

from PIL import Image, ImageChops

def save_image(resolution=1, padding=10, filename="drawing.png"):
    if resolution <= 0:
        raise ValueError("resolution must be greater than 8")

    screen = turtle.Screen()
    screen.update()

    # Export the drawing
    eps_file = "drawing.eps"
    screen.getcanvas().postscript(file=eps_file)

    # Find Ghostscript
    gs = shutil.which("gs") or shutil.which("gswin64c") or shutil.which("gswin32c")
    if not gs:
        raise RuntimeError("Ghostscript is required. Install it to export EPS to PNG.")

    # Render at the requested resolution
    temp_file = "_drawing_temp.png"
    dpi = int(72 * resolution)

    subprocess.run(
        [
            gs,
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-dEPSCrop",
            "-sDEVICE=png16m",
            f"-r{dpi}",
            f"-sOutputFile={temp_file}",
            eps_file,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
    )

    # Open the rendered image
    img = Image.open(temp_file).convert("RGB")

    # Detect non-white pixels to remove blank space
    white = Image.new("RGB", img.size, "white")
    diff = ImageChops.difference(img, white).convert("L")
    diff = diff.point(lambda p: 255 if p > 10 else 0)
    bbox = diff.getbbox()

    if bbox:
        # Scale padding with resolution
        pad = round(padding * resolution)
        left, top, right, bottom = bbox

        # Crop while keeping padding around the drawing
        bbox = (
            max(0, left - pad),
            max(0, top - pad),
            min(img.width, right + pad),
            min(img.height, bottom + pad),
        )
        img = img.crop(bbox)

    img.save(filename, "PNG")

def draw_grid(
    interval=50,
    color="lightgray",
    axis_color="black",
    labeled_line_color="gray",
    labels=True,
    label_every=5,
    line_width=1,
    font_size=8,
):
    if interval <= 0:
        raise ValueError("interval must be greater than zero")
    if label_every < 1:
        raise ValueError("label_every must be at least 1")

    screen = turtle.Screen()
    screen.update()

    width = screen.window_width()
    height = screen.window_height()

    left, right = -width / 2, width / 2
    bottom, top = -height / 2, height / 2

    grid = turtle.Turtle(visible=False)
    grid.speed(0)
    grid.penup()
    grid.width(line_width)
    grid.color(color)

    # Vertical grid lines
    for x in range(
        int(left // interval) * interval,
        int(right // interval + 1) * interval + 1,
        interval,
    ):
        if x != 0:
            is_labeled = (x // interval) % label_every == 0

            grid.color(labeled_line_color if labels and is_labeled else color)

            grid.goto(x, bottom)
            grid.pendown()
            grid.goto(x, top)
            grid.penup()

    # Horizontal grid lines
    for y in range(
        int(bottom // interval) * interval,
        int(top // interval + 1) * interval + 1,
        interval,
    ):
        if y != 0:
            is_labeled = (y // interval) % label_every == 0

            grid.color(labeled_line_color if labels and is_labeled else color)

            grid.goto(left, y)
            grid.pendown()
            grid.goto(right, y)
            grid.penup()
        # Vertical grid lines

    # Coordinate axes
    grid.color(axis_color)
    grid.width(max(1, line_width + 1))

    grid.goto(left, 0)
    grid.pendown()
    grid.goto(right, 0)
    grid.penup()

    grid.goto(0, bottom)
    grid.pendown()
    grid.goto(0, top)
    grid.penup()

    # Coordinate labels: label every nth grid line
    if labels:
        grid.color(axis_color)
        grid.width(1)

        for x in range(
            int(left // interval) * interval,
            int(right // interval + 1) * interval + 1,
            interval,
        ):
            if x != 0 and (x // interval) % label_every == 0:
                grid.goto(x, 4)
                grid.write(str(x), align="center", font=("Arial", font_size, "normal"))

        for y in range(
            int(bottom // interval) * interval,
            int(top // interval + 1) * interval + 1,
            interval,
        ):
            if y != 0 and (y // interval) % label_every == 0:
                grid.goto(4, y)
                grid.write(str(y), align="left", font=("Arial", font_size, "normal"))

    screen.update()
    return grid
