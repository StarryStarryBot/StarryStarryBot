from pathlib import Path

from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x393")
window.configure(bg = "#03071E")


canvas = Canvas(
    window,
    bg = "#03071E",
    height = 393,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    20.0,
    20.0,
    302.0,
    291.0,
    fill="#6A040F",
    outline="")

canvas.create_rectangle(
    322.0,
    20.0,
    480.0,
    82.0,
    fill="#9D0208",
    outline="")

canvas.create_rectangle(
    20.0,
    311.0,
    480.0,
    373.0,
    fill="#E85D04",
    outline="")

canvas.create_rectangle(
    322.0,
    102.0,
    480.0,
    164.0,
    fill="#9D0208",
    outline="")

canvas.create_rectangle(
    322.0,
    184.0,
    480.0,
    291.0,
    fill="#D00000",
    outline="")

canvas.create_text(
    21.0,
    311.0,
    anchor="nw",
    text="Starry Starry Bot GUI",
    fill="#FFFFFF",
    font=("Inter", 35 * -1),
    justify="center"
)

canvas.create_text(
    322.0,
    184.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Inter", 35 * -1)
)

canvas.create_text(
    322.0,
    102.0,
    anchor="nw",
    text="GPS",
    fill="#FFFFFF",
    font=("Inter", 35 * -1),
    justify="center"
)


canvas.create_text(
    322.0,
    20.0,
    anchor="nw",
    text="Time",
    fill="#FFFFFF",
    font=("Inter", 35 * -1),
    justify="center"
)

window.resizable(False, False)
window.mainloop()
