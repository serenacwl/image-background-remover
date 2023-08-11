from rembg import remove
from PIL import Image
import os

path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')
    
    edit = remove(img) # alpha_matting=True

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.png')