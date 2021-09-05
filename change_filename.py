#!/usr/bin/python3

''' Edit the name of the files. '''

import os

for file in os.listdir():

    old_name = file
    new_name = file

    if file.find('.py') != -1:
        pass
    else:
        if new_name.find('_') != -1:
            new_name = new_name.replace('_', ' ')


    os.rename(old_name, new_name)

    print(new_name)
