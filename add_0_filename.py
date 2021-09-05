#!/usr/bin/python3

''' Add 0 at the beginning of the filename/s if the filename/s starts with 1-9. '''

import os

given_path = str(input('Path: '))

for file in os.listdir(given_path):
    temp = file
    if len(file[:file.find('.')]) == 1:
        temp = f'0{file}'

        os.system(f'mv {os.path.join(given_path, file)} {os.path.join(given_path, temp)}')
