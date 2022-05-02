from json_manager import *
import colorama
from colorama import Fore
import os
import tkinter
from tkinter import messagebox
import run as runPY

jsn = Json_Manager('config.json', False)
colorama.init(autoreset=True)
print(f"{Fore.GREEN}Welcome to NotificationBuilder [v0]\nProject By Jaazim\n\n{Fore.CYAN}Start By Reading The Docs at The Github Page (https://github.com/Jaasim2008/notificationBuilder)\n")

startingVariables = ['inf', 'wrn', 'err']
quitVariables = ['quit', 'exit', 'leave', 'e', 'stop']
badINP = f"{Fore.GREEN}Invalid Command!"
noOfMessages = 0

jsn.clear_data()
jsn.write_data("msgs", 0)

userTitle = ""
def askTitle():
    global userTitle
    userTitle = input("Program Title > ")
    if len(userTitle) < 2:
        print(f"{Fore.RED}Minimum Title Length is 2 Charecters!")
        askTitle()
askTitle()

jsn.append_data("title", userTitle)

def startMain():
    global noOfMessages
    userINP = input("> ")
    userINP = userINP.lower()
    userMSG = userINP[4:]
    try:
        for y in quitVariables:
            if userINP == y:
                jsn.clear_data()
                print(f"{Fore.CYAN}Exited, Thank You For Using!")
                quit()
        if userINP == "play":
            if int(noOfMessages) > 0:
                runPY.CompileAndRun()
            else:
                print(f"{Fore.CYAN}Add 1 or More Messages to Play")
        elif userINP == "info":
            print(f"{Fore.CYAN}JSON Information:\nProgram Title : {Fore.GREEN}{jsn.get_data('title')}{Fore.CYAN}\nTotal No.Of Lines in Queue : {Fore.GREEN}{jsn.get_data('msgs')}")
        elif userINP == "title":
            userNewTitle = input("New Program Title > ")
            if userNewTitle != " " or userNewTitle != "" and len(str(userNewTitle)) > 2:
                jsn.change_data("title", userNewTitle)
                print(f"{Fore.CYAN}Successfully Changed Title!")
                startMain()
        elif userINP[3] == " ":
            for x in startingVariables:
                if userINP[:3] == x:
                    if x == "inf":
                        noOfMessages = noOfMessages + 1
                        jsn.append_data(noOfMessages, f"{x}-{userMSG}")
                        jsn.change_data("msgs", noOfMessages)
                        print(f"{Fore.CYAN}Added Line to Queue, Line -> {Fore.RED}{x}-{userMSG}{Fore.CYAN}, Total Lines -> {Fore.RED}{noOfMessages}{Fore.CYAN}")
                    elif x == "wrn":
                        noOfMessages = noOfMessages + 1
                        jsn.append_data(noOfMessages, f"{x}-{userMSG}")
                        jsn.change_data("msgs", noOfMessages)
                        print(f"{Fore.CYAN}Added Line to Queue, Line -> {Fore.RED}{x}-{userMSG}{Fore.CYAN}, Total Lines -> {Fore.RED}{noOfMessages}{Fore.CYAN}")
                    elif x == "err":
                        noOfMessages = noOfMessages + 1
                        jsn.append_data(noOfMessages, f"{x}-{userMSG}")
                        jsn.change_data("msgs", noOfMessages)
                        print(f"{Fore.CYAN}Added Line to Queue, Line -> {Fore.RED}{x}-{userMSG}{Fore.CYAN}, Total Lines in Queue -> {Fore.RED}{noOfMessages}{Fore.CYAN}")
        else:
            print(badINP)
            startMain()
        startMain()
    except Exception as e:
        print(badINP)
        print(f"{Fore.CYAN}Error -> {e}")
startMain()