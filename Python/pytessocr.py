#!python3
# This program detects text from the image in your clipboard,
# and adds the text to your clipboard,
# if the last thing copied was an image
# if not, it returns "No image in clipboard."

from PIL import ImageGrab as ig
import os, clipboard
from pytesseract import pytesseract as pt

pt.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
img=ig.grabclipboard()

if img is not None:
    text=pt.image_to_string(img)
    clipboard.copy(text[:-2])
    print('Image is analysed and text in now available in your clipboard.')
else:
    print('No image in clipboard.')
    
