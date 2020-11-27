import os
import glob
import shutil
from os import path

class_names = []

parent_dir = "/Users/yarusx/Downloads/images/"
try:
    os.mkdir('/Users/yarusx/Downloads/images/Dog')
except:
    pass

try:
    os.mkdir('/Users/yarusx/Downloads/images/Cat')
except:
    pass

sub_dir_dog = '/Users/yarusx/Downloads/images/Dog'
sub_dir_cat = '/Users/yarusx/Downloads/images/Cat'

temp_dirname = ''
current_dir = ''

filename = glob.glob(parent_dir+"*.jpg")

for file in filename:

    temp_dirname = str(os.path.splitext(file)[0])[31:].lower()
    ind = int(len(temp_dirname.split("_")))
    temp_dirname = temp_dirname.split("_")[:ind-1]
    temp_dirname = '_'.join(temp_dirname)

    if not str(temp_dirname) in class_names: class_names.append(str(temp_dirname))

    if str(os.path.splitext(file)[0])[31].isupper() is True:
        current_dir = os.path.join(sub_dir_cat, temp_dirname)
        #print(current_dir)
        try:
            os.mkdir(sub_dir_cat+"/"+temp_dirname)
        except:
            pass

        shutil.move(file,current_dir)

    if str(os.path.splitext(file)[0])[31].isupper() is False:
        current_dir = os.path.join(sub_dir_dog, temp_dirname)
        #print(current_dir)
        try:
            os.mkdir(sub_dir_dog+"/"+temp_dirname)
        except:
            pass

        shutil.move(file,current_dir)

file = open(parent_dir+"/class_names.txt", "w")
file.write(str(class_names))
file.close()
