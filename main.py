from tkinter import Tk
from tkinter.filedialog import askopenfilename
from gtts import gTTS
from PyPDF2 import PdfReader

import pdfplumber as pdfplumber
import os

Tk().withdraw()

file_location = askopenfilename()

file_name = os.path.basename(file_location)
name = os.path.splitext(file_name)

try:
    pdf_file = open(file_location, "rb")
except:
    print("That didn't work.")

reader = PdfReader(pdf_file)
all_text = ""

for page in reader.pages:
    all_text += page.extract_text()

tts = gTTS(text=all_text, lang="en")
tts.save(f"{name[0]}.mp3")