
from os import listdir
def queue_img(path):
    files = listdir(path)
    #print(files)
    return sorted(files, key = lambda x : int(x[-9:-4]))  # list

print(queue_img("./output"))