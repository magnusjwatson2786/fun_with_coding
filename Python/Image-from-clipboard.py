#!python3
# This program saves an inage from clipboard to your desktop,
# if the last thing copied was an image
# if not, it returns "No image in clipboard."

from PIL import ImageGrab as ig
from datetime import datetime as dt
import os
from functools import reduce

img=ig.grabclipboard()


if img is not None:
    userprofile=os.path.join(os.environ['USERPROFILE'])
    desktopfolder = os.path.join(userprofile, 'Desktop','Screenshots')
    if os.path.exists(desktopfolder) is not True:
        os.mkdir(desktopfolder)
    tm=dt.now()
    filename='paste'+str(tm.year)+str(tm.month)+str(tm.day)+str(tm.hour)+str(tm.minute)+str(tm.second)+'.png'
    os.chdir(desktopfolder)
    img.save(filename,'PNG')
    print('Image Saved on your Desktop.')
else:
    print('No image in clipboard.')
    
