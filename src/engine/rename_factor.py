import os
import re
import shutil
import random

def list_video(path = "./../ex", types_accepted = ["mp4"]):
    files = os.listdir(path)
    liste_v = []
    for f in files :
        # TODO : bricoler les types
        if f[-3:] in types_accepted and not os.path.isdir(path+'/'+f):
            liste_v += [f]
    return liste_v

def create_folder_out(path = "./../ex"):
    if not os.path.exists(path+"/file_out") :
        os.mkdir(path+"/file_out")

def make_new_name(theme, tags, number, type = "mp4"):
    name = theme
    for t in tags :
        name += "_" + t
    if len(number) == 0 :
        number += "00"
    name += "_" + str(number) + "." + type
    return name

def get_number_name(name_video):
    try :
        num = re.search('\d+.\w+$', name_video)
        return num.group()[:-4]
    except Exception as e :
        # print(e)
        return ""

def copy_file_out(file,  newname, path = "./../ex"):
    while os.path.exists(path + '/file_out/' + newname) :
        newname = newname[:-4] + str(random.randrange(0, 9999)) + newname[-4:]
    shutil.copy( path + '/' + file, path + '/file_out/' + newname )

def del_file(file, path = "./../ex"):
    os.remove(path + '/' + file)

if __name__ == '__main__' : 
    create_folder_out()
    lv = list_video()
    for i in lv :
        print(i)
        new_name = make_new_name(
            "video", 
            ["test", "test2"], 
            get_number_name(i)
        )
        copy_file_out(i, new_name)
        # del_file(i)