# https://jacobnarayan.com/blogs/how-to-convert-pngs-to-jpgs-in-7-lines-of-python
# First install PIL (Python Imaging Library) package
# pip install Pillow 

from PIL import Image 
import os 

files = os.listdir('path/to/directory') # list of files in directory

for file in files:  

    if file.endswith('.png'): # check if file is png

        im = Image.open(file).convert("RGB") # open file as an image object

        im.save('path/to/directory' + file[:-4] + '.jpg', quality=95, optimize=True) # save image as jpg with options