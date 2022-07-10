import os
import shutil
import cv2
import time
from datetime import datetime

PATH = 'database/screws'
def get_screw_path(name):
    return os.path.join(PATH, name)


def save_image(img, main_path, screw_name, direction):
    path = os.path.join(main_path, screw_name)
    if not os.path.isdir(path):
        os.mkdir(path)
    
    path = os.path.join( path, direction )
    if not os.path.isdir(path):
        os.mkdir(path)
    
    idx = len(os.listdir(path))
    now = datetime.now()
    
    name = '{idx}_{year}-{month}-{day}__{hour}-{minute}.bmp'.format( idx = idx,
                                                                   year = now.year,
                                                                   month = now.month,
                                                                   day = now.day, 
                                                                   hour = now.hour,
                                                                   minute = now.minute,   )

    path = os.path.join(path, name )
    cv2.imwrite(path, img)
    
    return path


def get_screws_list():
    return os.listdir(PATH)


def add_screw(name):
    path = get_screw_path(name)
    if not os.path.isdir(path):
        os.mkdir(path)
        return True
    return False

    
def remove_screw(name):
    path = get_screw_path(name)
    if os.path.isdir(path) and len(os.listdir(PATH))>0:
        shutil.rmtree(path)
        return True
    return False


def clear_empty_screw():
    for screw in os.listdir( PATH ):
        path = os.path.join(PATH, screw)
        if os.listdir(path) == 0:
            shutil.rmtree(path)


def save_screw_image(screw_name,imgs):

    path=os.path.join(PATH,screw_name)
    date_time=date_funcs.get_datetime()
    print('path',path,'date',date_time)
    path=os.path.join(path,date_time)
    try:
        cv2.imwrite(path+'top.jpg',imgs[0])
        cv2.imwrite(path+'side.jpg',imgs[1])
    except:
        print('cant write image')



def creat_screw_db():
    if not os.path.isdir(PATH):
        os.mkdir(PATH)
        
        
def check_dir(path):
    return os.path.isdir(path)
        
creat_screw_db()
        





if __name__ == '__main__':
    print(get_screws_list())