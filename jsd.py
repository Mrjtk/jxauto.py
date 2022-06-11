import os

import time
from time import *
path=input("Enter path to user Directory :- ")
domain=input("Enter URL to start scanning :- ")
try:
    with open(path+".bashrc" , "a")as a:
                  b=a.write("sublist3r -d "+ domain)
                  a.close()
    sleep(1)
    os.system("gnome-terminal")
    sleep(1)
    with open(path+".bashrc" , "r")as a:
                  c=a.read()
                  c=c.replace("sublist3r -d ","dirsearch -u ")
    with open(path+".bashrc","w")as file:
                    file.write(c)
                    file.close()
    os.system("gnome-terminal")
    sleep(1)
    with open(path+".bashrc" , "r")as a:
                  c=a.read()
                  c=c.replace("dirsearch -u ","spiderfoot -s ")
    with open(path+".bashrc","w")as file:
                    file.write(c)
                    file.close()
    os.system(path+"gnome-terminal")
    sleep(1)
    with open(path+".bashrc" , "r")as a:
                  c=a.read()
                  c=c.replace("spiderfoot -s ","photon --keys --dns -u ")
    with open(path+".bashrc","w")as file:
                    file.write(c)
                    file.close()
    os.system("gnome-terminal")
    sleep(1)
    with open(path+".bashrc" , "r")as a:
                  c=a.read()
                  c=c.replace("photon --keys --dns -u ","arjun -u https://")
    with open(path+".bashrc","w")as file:
                    file.write(c)
                    file.close()
    os.system("gnome-terminal")
    sleep(1)
    with open(path+".bashrc" , "r")as a:
                  c=a.read()
                  c=c.replace("arjun -u "+"https://"+domain," ")
    with open(path+".bashrc","w")as file:
                    file.write(c)
                    file.close()
except:
    pass
