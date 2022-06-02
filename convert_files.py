#!/usr/bin/python3

''' To convert files using ffmpeg. '''

import os

GIVEN_PATH = str(input('Path: '))
ANSWER = ''
DESIRED_ANSWERS = ['y', 'n']
CONVERT_TO = str(input('Convert it to: '))
# CONVERT_TO = 'mp3'

def ask():
    global ANSWER
    if_multiple_folders = str(input('Are there multiple folders inside?: '))
    if if_multiple_folders in DESIRED_ANSWERS:
        ANSWER = if_multiple_folders
    else:
        ask()

ask()

for file in os.listdir(GIVEN_PATH):
    if ANSWER == 'n':
        os.chdir(f'{GIVEN_PATH}')
        filename = str(file[:file.find('.')])
        cur_file_ext = str(file[file.find('.'):])
        if cur_file_ext.find('mp4') == -1 and convert_to != 'mp4':
            if cur_file_ext != convert_to:
                os.system(f'ffmpeg -y -i {os.path.join(GIVEN_PATH, file)} {os.path.join(GIVEN_PATH, filename)}.{convert_to}')
            else:
                break
    else:
        os.chdir(f'{GIVEN_PATH}/{file}')
        for image in os.listdir():
            filename = str(image[:image.find('.')])
            cur_file_ext = str(image[image.find('.'):])
            path = str(GIVEN_PATH) + '/' + file + '/' + filename
            if cur_file_ext.find('mp4') == -1 and convert_to != 'mp4':
                if cur_file_ext != convert_to:
                    os.system(
                        'ffmpeg -y -i ' + str(path + cur_file_ext) + ' ' + str(path + '.' + convert_to))
                else:
                    break