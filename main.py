__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from functools import cache
from gettext import find
from importlib.metadata import files
from operator import itemgetter
import os
import shutil
from zipfile import ZipFile
import sys


# opdracht 1
def clean_cache():
    os.getcwd()
    if os.path.exists('cache'):
        shutil.rmtree('cache')
    os.mkdir('cache')

clean_cache()


# opdracht 2

def cache_zip(zip_file_path, cache_file_path):
    os.getcwd()
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall( cache_file_path)

cache_zip('data.zip', 'cache')


# opdracht 3


def cached_files():
    list_txt_doc = []
    path = os.path.join(os.getcwd(), 'cache')
    items_in_cache_folder = os.listdir('cache')
    for item in items_in_cache_folder:
        list_txt_doc.append(os.path.join(path,item))
    #print(list_txt_doc)
    return list_txt_doc

cached_files ()


#opdracht 4 - find_password
# find_password: takes the list of file paths from 
# cached_files as an argument. This function should read the 
# text in each one to see if the password is in there. Surely there 
# should be a word in there to incidicate the presence of the password? Once found, find_password should return this password string.

def find_password(list):
    password_str = 'password'
    for item in list:
        with open(item) as f:
            for line in f:
                if password_str in line:
                    print(line)
                    password = line[line.find(' '):-1].strip(' ')
                    print('wachtwoord is ' + password)
    return (password)

find_password(cached_files())
