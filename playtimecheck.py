import datetime
import time
import os
import json
import psutil


def process_exists(process_name):
    return process_name in (p.name().lower() for p in psutil.process_iter())


def clear_screen():
    os.system('cls')


def save_data_to_file():
    dict_file = 'd:\\users\\sebas\\onedrive\\repositories\\playtimecheck\data.json'
    with open(dict_file, 'w') as file:
        json.dump(data_dict, file, indent=4)


clear_screen()

chrome_activity = []
notepad_activity = []
ToDo_activity = []


while True:

    now = datetime.datetime.now() # get actual data & time

    if process_exists('chrome.exe') == True: 
        chrome_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Chrome działa')

    if process_exists('chrome.exe') == False: 
        chrome_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Chrome nie działa')

    if process_exists('notepad.exe') == True:
        notepad_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Notepad działa')

    if process_exists('notepad.exe') == False:
        notepad_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Notepad nie działa')
    
    if process_exists('todo.exe') == True:
        ToDo_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', True])
        print(f'{now:%Y-%m-%d %H:%M:%S}: ToDo działa')

    if process_exists('todo.exe') == False:
        ToDo_activity.append([f'{now:%Y-%m-%d %H:%M:%S}', False])
        print(f'{now:%Y-%m-%d %H:%M:%S}: Todo nie działa')
    
    data_dict = {'Chrome': chrome_activity, 'Notepad': notepad_activity, 'ToDo': ToDo_activity}

    save_data_to_file() 
    time.sleep(3) 
