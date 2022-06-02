#!/usr/bin/python3

''' Edit the name of the files. '''

import os
import string
import re

GIVEN_PATH = ''
POSSIBLE_ANSWERS_TASK = ['1', '2', '3', '4', '5']
POSSIBLE_ANSWERS_MULTIPLE_FOLDERS = ['y', 'n']
ANSWER_TASK = ''
ANSWER_MULTIPLE_FOLDERS = ''
CHARS_REMOVE = ''
CHARS_REPLACE = ''

def get_path():
    global GIVEN_PATH
    given_path = str(input('Path: '))

    if os.path.exists(given_path):
        GIVEN_PATH = given_path
    else:
        print('This folder doesn\'t exist. Try again.')
        get_path()

def ask_if_mulitple_folders():
    global ANSWER_MULTIPLE_FOLDERS
    get_path()
    if_multiple = str(input('Are there multiple folders inside?: '))
    if if_multiple in POSSIBLE_ANSWERS_MULTIPLE_FOLDERS:
        ANSWER_MULTIPLE_FOLDERS = if_multiple
        print(ANSWER_MULTIPLE_FOLDERS)
    else:
        ask_if_mulitple_folders()

def multiple_folders():
    for child_folder in os.listdir(GIVEN_PATH):
        path = f'{GIVEN_PATH}/{child_folder}'
        if ANSWER == '5':
            remove_spaces(path)
        elif ANSWER == '4':
            remove_unnecessary_chars_ending(path)
        elif ANSWER == '3':
            remove_unnecessary_chars_beginning(path)
        elif ANSWER == '2':
            change_chars(path)
        elif ANSWER == '1':
            remove_chars(path)

def remove_spaces(path):
    for file in os.listdir(path):
        old_name = str(file)
        new_name = ''

        if file.find('.py') != -1:
            pass
        else:
            for char in old_name:
                if char != ' ':
                    new_name += char

        print(f'Will change the name from {old_name} to {new_name}.')

        os.rename(f'{path}/{old_name}', f'{path}/{new_name}')

def remove_chars(path):
    strr = str(string.ascii_letters) + '.'

    for file in os.listdir(path):
        old_name = str(file)
        new_name = ''

        if file.find('.py') != -1:
            pass
        else:
            for char in old_name:
                if char in strr:
                    new_name += char

        print(f'Will change the name from {old_name} to {new_name}.')

        os.rename(f'{path}/{old_name}', f'{path}/{new_name}')

def change_chars(path):
    chars_to_remove = input(str('Character/s want to remove: '))
    chars_to_replace = input(str('Character/s want to replace: '))

    for file in os.listdir(path):
        old_name = str(file)
        new_name = str(file)

        if file.find('.py') != -1:
            pass
        else:
            if new_name.find(chars_to_remove) != -1:
                new_name = new_name.replace(chars_to_remove, chars_to_replace)
                print(f'Will change the name from {old_name} to {new_name}.')

            os.rename(f'{path}/{old_name}', f'{path}/{new_name}')
            print(new_name)

def ask_question():   
    global ANSWER
    answer = input(str('''What do you want to do?
    1 - Remove the characters, excluding English letters and dot
    2 - Change the character/s
    3 - Remove the unnecessary character/s BEFORE the no. order
    4 - Remove the unnecessary character/s AFTER the no. order, excluding order number and file ext.
    5 - Remove spaces :\n'''))

    if answer not in POSSIBLE_ANSWERS_TASK:
        print('Your answer is not included in the choices. Try again.\n')
        ask_question()
    else:
        ANSWER = answer
        
def run():
    ask_if_mulitple_folders()
    ask_question()
    if ANSWER_MULTIPLE_FOLDERS == 'n':
        if ANSWER == '5':
            remove_spaces(GIVEN_PATH)
        elif ANSWER == '4':
            remove_unnecessary_chars_ending(GIVEN_PATH)
        elif ANSWER == '3':
            remove_unnecessary_chars_beginning(GIVEN_PATH)
        elif ANSWER == '2':
            change_chars(GIVEN_PATH)
        elif ANSWER == '1':
            remove_chars(GIVEN_PATH)
    else:
        multiple_folders()

run()
