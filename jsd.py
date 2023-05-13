
import os
import time
from click import style
import colorama
from colorama import Fore,Style
from time import *
user=os.getlogin()
os.system("clear")
colorama.init(autoreset=True)
try:
    logo=Fore.GREEN+Style.BRIGHT+'''           dP  .d888888             dP                              dP       
           88 d8'    88             88                              88       
           88 88aaaaa88a dP    dP d8888P .d8888b. .d8888b. dP    dP 88d888b. 
           88 88     88  88    88   88   88'  `88 Y8ooooo. 88    88 88'  `88 
    88.  .d8P 88     88  88.  .88   88   88.  .88       88 88.  .88 88.  .88 
     `Y8888'  88     88  `88888P'   dP   `88888P' `88888P' `88888P' 88Y8888' 
                                                                             
                                                                             '''
    
    print(logo)
    domain=input("Enter URL to start scanning :- ")
    try:
        with open("/home/"+user+"/"+".zshrc" , "a")as a:
                      b=a.write("sublist3r -d "+ domain)
                      a.close()
        sleep(1)
        os.system("gnome-terminal")
        sleep(1)
        with open("/home/"+user+"/.zshrc" , "r")as a:
                      c=a.read()
                      c=c.replace("sublist3r -d ","dirsearch -u ")
        with open("/home/"+user+"/.zshrc","w")as file:
                        file.write(c)
                        file.close()
        os.system("gnome-terminal")
        sleep(1)
        with open("/home/"+user+"/.zshrc" , "r")as a:
                      c=a.read()
                      c=c.replace("dirsearch -u ","spiderfoot -s ")
        with open("/home/"+user+"/.zshrc","w")as file:
                        file.write(c)
                        file.close()
        os.system("gnome-terminal")
        sleep(1)
        with open("/home/"+user+"/"+".zshrc" , "r")as a:
                      c=a.read()
                      c=c.replace("spiderfoot -s ","photon --keys --dns -u ")
        with open("/home/"+user+"/.zshrc","w")as file:
                        file.write(c)
                        file.close()
        os.system("gnome-terminal")
        sleep(1)
        with open("/home/"+user+"/.zshrc" , "r")as a:
                      c=a.read()
                      c=c.replace("photon --keys --dns -u ","arjun -u https://")
        with open("/home/"+user+"/.zshrc","w")as file:
                        file.write(c)
                        file.close()
        os.system("gnome-terminal")
        sleep(1)
        with open("/home/"+user+"/.zshrc" , "r")as a:
                      c=a.read()
                      c=c.replace("arjun -u "+"https://"+domain," ")
        with open("/home/"+user+"/.zshrc","w")as file:
                        file.write(c)
                        file.close()
    except:
        pass
except:
    print(Fore.RED+Style.BRIGHT+"Abort !")
