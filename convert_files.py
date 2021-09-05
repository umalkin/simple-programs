#!/usr/bin/python3

''' To convert files using ffmpeg. '''
import os

given_path = str(input('Path: '))
convert_to = str(input('Desired file extension : '))

dest_folder = '/home/ako/Downloads/converted'

os.chdir(f'{given_path}')

os.system(f'cd .. && mkdir converted')

for file in os.listdir(given_path):
    filename = file[:file.find('.')-1]
    os.system(f'ffmpeg -i {os.path.join(given_path, file)} {os.path.join(dest_folder, filename)}.{convert_to}')