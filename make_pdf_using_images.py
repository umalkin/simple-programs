#!/usr/bin/python3

''' Make a PDF from images. '''

import os
from fpdf import FPDF

images_loc = str(input('Path of the target folder: '))
rename = ''
convert = ''
multiple_folders = ''
desired_name_pdf = str(input('Desired name of the PDF file: '))

# target_folder = str(input('Name of the target folder: '))

list_subfolders = []
list_images = []

desired_answers = ['y', 'n']

def chdir():
    os.chdir(images_loc)

# Change directory.
chdir()

def need_to_rename():
    global rename
    prompt = str(input('Do you need to rename the images? (y/n): '))
    if prompt not in desired_answers:
        print('Please only type y or n.\n')
        need_to_rename()
    else:
        rename = prompt
        print(rename)
        # rename_images()

def need_to_convert():
    global convert
    prompt = str(input('Do you need to convert the images? (y/n): '))
    if prompt not in desired_answers:
        print('Please only type y or n.\n')
        need_to_convert()
    else:
        convert = prompt
        print(convert)
        convert_images()

def if_multiple_folders():
    global multiple_folders
    prompt = str(input('Are there multiple folders inside the given path? (y/n): '))
    if prompt not in desired_answers:
        print('Please only type y or n.\n')
        if_multiple_folders()
    else:
        multiple_folders = prompt
        print(multiple_folders)

# Rename each file by adding the folder name before the file extension.
# Make sure that the images_loc only contains folder/s with image/s you want to include in a PDF file. 

def rename_images():
    for folder in os.listdir(): # target_folder is the argument for the listdir method
        # path_joined = os.path.join(target_folder, folder)
        # if os.path.isdir(path_joined):
        #     print(path_joined)
        if multiple_folders == 'y':
            os.chdir(f'{images_loc}/{folder}')
            for image in os.listdir():
                curr_folder = f'_{os.getcwd()[-1]}'
                print(f'Renaming {image}')
                new_name = f'{image[:-5]}{curr_folder.upper()}{image[-5:]}'
                os.rename(image, new_name)
        else:
            # for image in os.listdir():
            curr_folder = f'_{os.getcwd()[-1]}'
            print(f'Renaming {folder}')
            new_name = f'{folder[:-5]}{curr_folder.upper()}{folder[-5:]}'
            os.rename(folder, new_name)   
        chdir()

# Convert webp to jpg

def convert_images():
    for folder in os.listdir():
        if multiple_folders != 'n':
            os.chdir(f'{images_loc}/{folder}')
            for image in os.listdir():
                print(f'Converting {image}')
                os.system(f'ffmpeg -i {image} {image[:-4]}jpg >/dev/null 2>&1') # >/dev/null 2>&1 is to hide shell.
        else:
            print(f'Converting {folder}')
            os.system(f'ffmpeg -i {folder} {folder[:-4]}jpg >/dev/null 2>&1',)
        
    chdir()

# Append the path of each jpg to the list

def append_path():
    for folder in os.listdir():
        global list_images
        if multiple_folders == 'y':
            os.chdir(f'{images_loc}/{folder}')
            for image in os.listdir():
                if image.find('jpg') != -1:
                    list_images.append(f'{os.getcwd()}/{image}')
        else:
            if folder.find('jpg') != -1:
                list_images.append(f'{os.getcwd()}/{folder}')

    chdir()

    list_images = sorted(list_images)

# Generate a PDF file

def make_pdf():
    pdf = FPDF()

    for image in list_images:
        page = pdf.add_page()
        pdf.image(image, 0,0,210,297) # A4 size page
        
    pdf.output(f'{images_loc}/{desired_name_pdf}.pdf', 'F')
    
    print('The PDF file has been generated successfully.')


def ask_questions():
    if_multiple_folders()
    need_to_rename()
    need_to_convert()

def final():
    ask_questions()
    append_path()
    make_pdf()


final()
