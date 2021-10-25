import os
import random
import shutil

source = '/Users/murilokakazu/Projects/turing/datasets/esp32_motor/training/motor'
dest = '/Users/murilokakazu/Projects/turing/datasets/esp32_motor/validation/motor'
files = os.listdir(source)
no_of_files = 108

for file_name in random.sample(files, no_of_files):
    shutil.move(os.path.join(source, file_name), dest)