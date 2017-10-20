import docx2txt
from PyDictionary import PyDictionary
import re

dictionary = PyDictionary()

file_name = input('enter file path')

action = input('enter l to lengthen file or s to shorten file')

file_name = str(file_name)

file = ''

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if ".docx" in file_name:
    f = docx2txt.process(file_name)
    for line in f:
        for char in line:
            try:
                file += char
            except char == ' ':
                file += ','
            except char not in alphabet:
                continue
    f.close()
elif ".txt" in file_name:
    f = open(file_name,'r')
    for line in f:
        for char in line:
            if char not in alphabet:
                file += ' '
            else:
                file += char

    f.close()
else:
    print("filetype not supported")

file = file.split()


if action == 'l':
    for i in file:
        if len(max(dictionary.synonym(i))) > len(i):
            f = open(file_name, 'r+')
            new_file = re.sub(i, max(dictionary.synonym(i)), f.read())
            f.truncate(0)
            f.write(new_file)
elif action == 's':
    for i in file:
        if len(min(dictionary.synonym(i))) < len(i):
            f = open(file_name, 'r+')
            new_file = re.sub(i, min(dictionary.synonym(i)), f.read())
            f.truncate(0)
            f.write(new_file)
else:
    print('you did not choose l or s')
