#This is a simple STEAM GiftCard generator Made by ANDRO
#Im new in coding, if u want to help me: andro#9999(my discord)
#Coded in 5/9/2020
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
from colorama import Fore, init, Style, Back
from datetime import date

os.system("title [STEAM] GiftCard Generator - andro#9999")
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Style.BRIGHT + Fore.YELLOW + Back.BLACK +'[*] Loading... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

os.system("cls")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome to "+Fore.BLUE+"Steam Key Generator")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [1] "+Fore.BLUE+"Format 1"+" XXXXX-XXXXX-XXXXX-XXXXX")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [2] "+Fore.BLUE+"Format 2"+" XXXXX-XXXXX-XXXXX")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [3] "+Fore.BLUE+"Credits")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [4] "+Fore.BLUE+"Exit")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

opcion = int(input("Choice: "))

if opcion==1:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                     SteamKey Generator"+Fore.WHITE+" Made by "+Fore.YELLOW+"andro#9999")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	cantidad = input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nHow many giftcards want to generate: ")
	while(int(count)<int(cantidad)):
	    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	    f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a") 
	    f.write(Generated+"\n")
	    print(Style.BRIGHT + Fore.YELLOW + Back.BLACK +"Generated code: "+Fore.BLUE + Generated)
	    count+=1
	input(Fore.GREEN+"\nCodes have been generated & saved!\nPress enter to exit.")
	pass

if opcion==2:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                     SteamKey Generator"+Fore.WHITE+" Made by "+Fore.YELLOW+"andro#9999")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	cantidad = input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nHow many giftcards want to generate: ")
	while(int(count)<int(cantidad)):
	    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	    f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a") 
	    f.write(Generated+"\n")
	    print(Style.BRIGHT + Fore.YELLOW + Back.BLACK +"Generated code: "+Fore.BLUE + Generated)
	    count+=1
	input(Fore.GREEN+"\nCodes have been generated & saved!\nPress enter to exit.")
	pass

if opcion==3:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         SteamKey Generator"+Fore.WHITE+" Made by "+Fore.YELLOW+"andro#9999")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Github] "+Fore.YELLOW+"androexe")   
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Discord] "+Fore.YELLOW+"andro#9999")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nEnter to exit")
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Closing!")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass

if opcion==4:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Closing!...")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass