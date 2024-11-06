# https://www.geeksforgeeks.org/convert-png-to-jpg-using-python/
# First install PIL (Python Imaging Library) package
# pip install Pillow 

#importing the required package 
from PIL import Image 

path1=r'C:\temp\image.png'
path2=r'C:\temp\modified_image.jpg'


#open image in png format 
#img_png = Image.open("C:\temp\img.png") 

#The image object is used to save the image in jpg format 
#img_png.save('C:\temp\modified_img.jpg')

#open image in png format 
#img_png = Image.open('C:/temp/img.png') 

#The image object is used to save the image in jpg format 
#img_png.save('C:/temp/modified_img.jpg')

#open image in png format 
#img_png = Image.open('C:\\temp\\img.png') 
#print img_png.format, img_png.size, img_png.mode

#The image object is used to save the image in jpg format 
#img_png.save('C:\temp\modified_img.jpg')


#open image in png format 
img_png = Image.open(path1) 
print(img_png.format, img_png.size, img_png.mode)
img_png.show()
img_png.save(path2)
