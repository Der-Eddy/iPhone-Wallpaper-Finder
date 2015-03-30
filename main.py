from PIL import Image
from os import listdir
import os.path
from shutil import copy2 as copy
from console import *

path = defaultInput("Bilder Source Ordner", "/Users/Eddy/Desktop/Cats/")
folder = defaultInput("iPhone Wallpaper Ordner", "/Users/Eddy/Desktop/Output/")

pathlist = listdir(path)

for File in pathlist:
    if File.startswith(".") or File.endswith("db"):
        continue
    filename = os.path.join(filepath)
    img = Image.open(filename)
    filepath = path + File
    print (filepath)
    if img.size[0] < img.size[1]:
        success(img.size)
        copy(filepath, folder)
    else:
        warning(img.size)