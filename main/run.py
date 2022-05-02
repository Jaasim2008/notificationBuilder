#!/usr/bin/env python3

from json_manager import *
import colorama
from colorama import Fore
import os
import tkinter
from tkinter import messagebox

jsn = Json_Manager('config.json', False)
colorama.init(autoreset=True)

def CompileAndRun():
    programTitle = jsn.get_data("title")
    no_of_messages = jsn.get_data("msgs")
    if int(no_of_messages) == 1:
        onlyOneMessage = jsn.get_data("1")
        if onlyOneMessage[:3] == "inf":
            messagebox.showinfo(programTitle, onlyOneMessage[4:])
        elif onlyOneMessage[:3] == "wrn":
            messagebox.showwarning(programTitle, onlyOneMessage[4:])
        elif onlyOneMessage[:3] == "err":
            messagebox.showerror(programTitle, onlyOneMessage[4:])
    elif int(no_of_messages) > 1:
        array1 = []
        for r in range(int(no_of_messages) + 1):
            if r != 0:
                cacheData = jsn.get_data(str(r))
                array1.append(cacheData)
        for x in range(int(len(array1))):
            if array1[x][:3] == "inf":
                messagebox.showinfo(programTitle, array1[x][4:])
            elif array1[x][:3] == "wrn":
                messagebox.showwarning(programTitle, array1[x][4:])
            elif array1[x][:3] == "err":
                messagebox.showerror(programTitle, array1[x][4:])
    else:
        print(f"{Fore.RED}Error Occurred During Compling Process!")
        jsn.clear_data()
        quit()
    print(f"{Fore.CYAN}Process Finished!")