#!python3
# This program saves an inage from clipboard to your desktop,
# if the last thing copied was an image
# if not, it returns "No image in clipboard."

from PIL import ImageGrab as ig
from datetime import datetime as dt
import os


img=ig.grabclipboard()

if img is not None:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    tm=dt.now()
    filename='paste'+str(tm.year)+str(tm.month)+str(tm.day)+str(tm.hour)+str(tm.minute)+str(tm.second)+'.png'
    os.chdir(desktop)
    img.save(filename,'PNG')
    print('Image Saved on your Desktop.')
else:
    print('No image in clipboard.')
    
