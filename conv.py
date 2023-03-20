import os
import sys
import struct
import tkinter
from tkinter import filedialog


def TNES(bf: bytearray):
    """TNES形式
    詳しくは→https://wiki.nesdev.com/w/index.php/TNES
    """
    bf[:4] = b"\x4E\x45\x53\x1A"
    return bf


def SAVE(data: bytearray, filename: str):
    while os.path.exists(filename):
        filename = f"_{filename}"
    with open(filename, "xb") as f:
        f.write(data)
        print(f"file saved successfully: {filename}")


def main():
    if getattr(sys, "frozen", False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    root = tkinter.Tk()
    root.withdraw()

    files = sys.argv[1:] or filedialog.askopenfilenames(
        initialdir=current_dir, title="ROMファイルを選択（複数可）", filetypes=[("all files", "*.*")])

    for file in files:
        os.chdir(os.path.dirname(file))
        filename = os.path.splitext(os.path.basename(file))[0]

        with open(file, "rb") as f:
            bf = bytearray(f.read())
            if bf[:4] == b"TNES":
                SAVE(TNES(bf), f"{filename}.nes")
    return


if __name__ == "__main__":
    main()
