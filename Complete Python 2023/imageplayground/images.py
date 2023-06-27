# pip3 install pillow
from PIL import Image, ImageFilter

# Create an object from the Image class in the Image module
img = Image.open('./pikachu.png')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')