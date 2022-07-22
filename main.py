import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader

import pyttsx3 as tts
import os

Tk().withdraw()

file_location = askopenfilename()

file_name = os.path.basename(file_location)
name = os.path.splitext(file_name)

try:
    pdf_file = open(file_location, "rb")
except OSError:
    print("That didn't work.")
    sys.exit()

with pdf_file:
    reader = PdfReader(pdf_file)
    all_text = ""

    for page in reader.pages:
        all_text += page.extract_text()

    engine = tts.init()

    engine.setProperty("rate", 150)
    engine.save_to_file(all_text, f"{name[0]}.mp3")
    engine.runAndWait()