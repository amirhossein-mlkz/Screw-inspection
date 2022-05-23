import os
import shutil

PATH = 'database/screws'
def get_screw_path(name):
    return os.path.join(PATH, name)



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




if __name__ == '__main__':
    print(get_screws_list())