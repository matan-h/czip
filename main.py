import zipfile
import os
from os import path

itm = lambda x:(path.isfile(x)) and (not x.endswith(".zip")) #and x is not print(x)
listdir = list(filter(itm, os.listdir()))
listdir.remove(path.basename(__file__))
#listdir = list(filter(lambda x:not x.endswith(".zip"),listdir))
print(listdir)

#quit(88888)
with zipfile.ZipFile("arduino_send.zip", "w") as zip_ref:
    for file in listdir:
        zip_ref.write(file)
