from random import randint
from shutil import copyfile
import sys
import os
path= os.chdir(r"C:\\Users\\Varun\\PycharmProjects\\secretmessage\\scrtmsg")

filenames=os.listdir(path)
'''for name in filenames:
    if name.endswith('.jpg'):
        copyfile(src+name,dest)
'''
def decode():
    for name in filenames:
        os.rename(name,name.strip("0123456789"))
    print("message decoded successfully")

def encode():
    for name in filenames:
        os.rename(name,str(randint(222,999))+name)
    print("message encoded successfully")

x=input("enter ur option \n 1--encode \n 2--decode \n ")
if x == '1':
    encode()
elif x == '2':
    decode()
else:
    print("invalid choice")
    print(x)

