# Accept two arguments 1, folder name; 2, new folder
from PIL import Image
from pathlib import Path
import os
import sys

folder = sys.argv[1]
new_folder = Path(sys.argv[2])
new_folder.mkdir(exist_ok=True)

path_list = list(Path(folder).glob(('**/*.jpg')))

num = 1
for file in path_list:
	img = Image.open(file)
	img.save(f'{new_folder}/{str(num)}.png')
	num += 1