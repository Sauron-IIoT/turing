import os
from os import listdir
from PIL import Image

counter = 0

for filename in listdir('./datasets/esp32_motor/training/esp32'):
    if filename.endswith('.jpg'):
        try:
            img = Image.open('./datasets/esp32_motor/training/esp32/'+filename)  # open the image file
            img.load()
        except (IOError, SyntaxError) as e:
            print(f'bad image: {filename}')
            counter+=1
            os.remove('./datasets/esp32_motor/training/esp32/'+filename)

for filename in listdir('./datasets/esp32_motor/training/motor'):
    if filename.endswith('.jpg'):
        try:
            img = Image.open('./datasets/esp32_motor/training/motor/'+filename)  # open the image file
            img.load()
        except (IOError, SyntaxError) as e:
            print(f'bad image: {filename}')
            counter+=1
            os.remove('./datasets/esp32_motor/training/motor/'+filename)

print(f'removed {counter} bad images')