import time
import os
import subprocess
import json





a = '''\033[1;34;40m 
----------------------------------------- \033[1;34;40m
|\033[1;31;40m                               __\033[1;34;40m
|\033[1;31;40m                            .d$$b\033[1;34;40m
|\033[1;31;40m                           .' TO$;\\\033[1;34;40m
|\033[1;31;40m                          /  : TP._;\033[1;34;40m
|\033[1;31;40m                         / _.;  :Tb|\033[1;34;40m
|\033[1;31;40m                        /   /   ;j$j\033[1;34;40m
|\033[1;31;40m                    _.-"       d$$$$\033[1;34;40m
|\033[1;31;40m                  .' ..       d$$$$;\033[1;34;40m
|\033[1;31;40m                 /  /P'      d$$$$P. |\\\033[1;34;40m
|\033[1;31;40m                /   "      .d$$$P' |\^"l\033[1;34;40m
|\033[1;31;40m              .'           `T$P^"""""  :\033[1;34;40m
|\033[1;31;40m          ._.'      _.'                ;\033[1;34;40m
|\033[1;31;40m       `-.-".-'-' ._.       _.-"    .-"\033[1;34;40m
|\033[1;31;40m     `.-" _____  ._              .-"\033[1;34;40m
|\033[1;31;40m    -(.g$$$$$$$b.              .'\033[1;34;40m
|\033[1;31;40m      ""^^T$$$P^)            .(:\033[1;34;40m
|\033[1;31;40m        _/  -"  /.'         /:/;\033[1;34;40m
|\033[1;31;40m     ._.'-'`-'  ")/         /;/;\033[1;34;40m
|\033[1;31;40m  `-.-"..--""   " /         /  ;\033[1;34;40m
|\033[1;31;40m .-" ..--""        -'          :\033[1;34;40m
|\033[1;31;40m ..--""--.-"         (\      .-(\\\033[1;34;40m
|\033[1;31;40m   ..--""              `-\(\/;`\033[1;34;40m
|\033[1;31;40m     _.                      :\033[1;34;40m
|\033[1;31;40m                             ;`-\033[1;34;40m
|\033[1;31;40m                            :\\\033[1;34;40m
|\033[1;34;40m																	
--------------------------------------------
    WELCOME IN WORLD CALLED HACKER HELL'''
print(a)
print("\033[1;32;40m")
ipcollect =input("|==========|ENTER YOUR IP|==========| :")
print("|==========|CHECKING UR IP|==========|  ")
time.sleep(1)
print("-----------------\\---------------------")
time.sleep(1)
print("-----------------|----------------------")
time.sleep(1)
print("-----------------/----------------------")
time.sleep(1)
print("-----------------\\---------------------")
time.sleep(0.5)
os.system("clear")
time.sleep(0.3)
print(a)
print("\033[1;31;40m")
print("________________________________________________________")
print("|==========|      SELECT 1 TO DO A PING     |==========|")
print("|==========|  SELECT 2 TO DO A INFO GATHER  |==========|")
print("|==========| SELECT 3 TO DO A SERVICE SCAN  |==========|")
print("|==========|  SELECT 4 TO DO A DOS ATTACK   |==========|")
print(" |========||==========||==========||==========||======|")
print("|==========|      SELECT 00 TO GO BACK      |==========|")
print("--------------------------------------------------------")
print("\033[1;32;40m")
select2 =input(">>>>>----------------------->")

if select2 == "1":
        print(" ..................STARTING UR PING SACN..............")
        os.system("ping " + ipcollect)
    
elif select2 == "2":
        print(".....................GATHERING INFO...................")
        os.system("python3 locate.py -t  " + ipcollect)
    
elif select2 == "3":
        print("////////////////PERFORMING A SCAN ON YOUR IP///////////")
        os.system("nmap -sV -Pn " + ipcollect)
elif select2 == "4":
	DOS = input("////////////////ARE U DOING THIS IN AN ETHICAL WAY///////||Y/N||///")
	if DOS  == "y":
		print("////////////////PERFORMING A DOS ATTACK ON YOUR GIVER IP///////////")
		os.system("sudo hping3 " + ipcollect)
	elif DOS == "n":
		print("ACCESS DENIED!")
		exit()
elif select2 =='00':
	os.system("python3 lobby.py")
else:
	print("INVALID!!")

