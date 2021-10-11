#!/usr/bin/python3

import os
from PIL import Image

target_folder_name = str(input('Target folder name : '))
ask_if_with_taksbar = str(input('Does the images have taskabr? (y/n, default - y): '))
# dest_folder_name = str(input('Destined folder name : '))

with_taksbar = 'y'

images = os.listdir(target_folder_name)

if 'cropped' not in os.listdir(target_folder_name):
    os.mkdir(f'/home/ako/{target_folder_name}/cropped')
    
if ask_if_with_taksbar == 'y' or ask_if_with_taksbar == '':
    with_taksbar = 'y'
else:
    with_taksbar = 'n'
    
counter = 0


for image in images:
    if image[-3:] == 'png':
        target_image = f'/home/ako/{target_folder_name}/{image}'
        img = Image.open(target_image)
    
        name = f'cropped-{image}'
        height, width = img.size
        
        # For Images with Taskbar.
        
        # left = 70
        # top = 160
        # right = width*1.2
        # bottom = height-260
        cropped = ''
        
        print(f'Cropping {target_image}.')
        
        if with_taksbar == 'y':
            cropped = img.crop((70, 105, width*1.3, height-255))
            # cropped = img.crop((70, 160, width*1.2, height-260)) # For Coursera
            cropped.save(f'/home/ako/{target_folder_name}/cropped/{name}')
            
        else:
            cropped = img.crop((0, 80, width*1.2, height-255))
            cropped.save(f'/home/ako/{target_folder_name}/cropped/{name}')
        
        #cropped = img.crop((70, 160, width*1.2, height-260)) # For Images with Taskbar.
        # cropped = img.crop((0, 80, width*1.2, height-255))
        cropped.save(f'/home/ako/{target_folder_name}/cropped/{name}')
        
        counter += 1
        
print(f'Cropped {counter} images.')
