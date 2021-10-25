import os
import random
import shutil

for clazz in ['esp32', 'motor']:
    source = f'/Users/murilokakazu/Projects/turing/datasets/esp32_motor/training/{clazz}'
    dest = f'/Users/murilokakazu/Projects/turing/datasets/esp32_motor/test/{clazz}'
    files = os.listdir(source)
    no_of_files = len(files) * 0.05

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(source, file_name), dest)

for clazz in ['esp32', 'motor']:
    source = f'/Users/murilokakazu/Projects/turing/datasets/esp32_motor/training/{clazz}'
    dest = f'/Users/murilokakazu/Projects/turing/datasets/esp32_motor/validation/{clazz}'
    files = os.listdir(source)
    no_of_files = len(files) * 0.2

    for file_name in random.sample(files, no_of_files):
        shutil.move(os.path.join(source, file_name), dest)