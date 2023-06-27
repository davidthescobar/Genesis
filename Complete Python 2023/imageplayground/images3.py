from PIL import Image, ImageFilter

# Create an object from the Image class in the Image module
img = Image.open('./Pokedex/astro.jpg')

# Retains aspect rastio
img.thumbnail((400,400))

img.save('thumbnail.jpg')