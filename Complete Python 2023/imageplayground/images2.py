from PIL import Image, ImageFilter

# Create an object from the Image class in the Image module
img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
rotated = filtered_img.rotate(90)
resize = rotated.resize((300, 300))
box = (100, 100, 400, 400)
cropped = resize.crop(box)
cropped.save('blur.png', 'png')
cropped.show()