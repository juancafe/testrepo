# https://www.geeksforgeeks.org/convert-png-to-jpg-using-python/
# First install PIL (Python Imaging Library) package
# pip install Pillow 

#importing the required package 
from PIL import Image 

#open image in png format 
img_png = Image.open('C:\temp\img.png') 

#The image object is used to save the image in jpg format 
img_png.save('C:\temp\modified_img.jpg')
