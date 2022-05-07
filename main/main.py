from json_manager import *
import colorama
from colorama import Fore
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import run as runPY

jsn = Json_Manager('config.json', False)
colorama.init(autoreset=True)
print(f"{Fore.GREEN}Welcome to NotificationBuilder [v2.1]\nProject By Jaazim")

startingVariables = ['inf', 'wrn', 'err']
quitVariables = ['quit', 'exit', 'leave', 'e', 'stop']
badINP = f"{Fore.GREEN}Invalid Command!"
noOfMessages = 0

jsn.clear_data()
jsn.write_data("msgs", 0)
jsn.append_data("title", "none")

root = Tk()
root.title("NotificationBuilder[v2]")
root.geometry('400x500')
root.resizable(False, False)
root_icon = PhotoImage(file='ast/chat.png')
root_font = 'Segoe UI Light Italic'
code_font = 'Segoe UI'
root.iconphoto(False, root_icon)

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

queue_txt = Label(main_frame, text='Queue:', font=(root_font, 15), fg='black')
queue_txt.pack()

queue_listbox_frame = Frame(main_frame)
queue_listbox_frame.pack()

queue_listbox = Listbox(queue_listbox_frame, font=(root_font, 15), fg='black')
slb = Scrollbar(queue_listbox_frame, command=queue_listbox.yview)
queue_listbox.configure(yscrollcommand = slb.set)
slb.pack(side=RIGHT, fill=Y)
def checkQueue(*reload):
    no_of_messages = jsn.get_data("msgs")
    if not reload:
        queue_listbox.delete(0,END)
        console_msg['text'] = 'Reloaded Queue'
    if int(no_of_messages) > 0:
        if int(no_of_messages) == 1:
            onlyOneMessage = jsn.get_data("1")
            queue_listbox.insert(END, onlyOneMessage)
            queue_listbox.pack()
        else:
            for xyz in range(int(no_of_messages) + 1):
                if xyz != 0:
                    queue_listbox.insert(END, f'{xyz}-{jsn.get_data(str(xyz))}')
            queue_listbox.pack()
    else:
        queue_listbox.insert(END, 'No Data in Queue')
        queue_listbox.pack()
checkQueue(True)

console_frame = Frame(main_frame, width=400, bg='black', height=35)
console_frame.pack(side=BOTTOM)

console_msg = Label(console_frame, text='-', fg='white', font=('Arial', 10), bg='black', width=400)
console_msg.pack(side=LEFT)

options_labelframe = LabelFrame(main_frame, text="Options", width=400)
options_labelframe.pack(pady=5, padx=5)

def run_programm():
    no_of_messages = jsn.get_data("msgs")
    if int(no_of_messages) > 0:
        tle_win = Toplevel(main_frame)
        tle_win.title("Enter Program Title")
        tle_txt = Label(tle_win, text="Program Title", font=(root_font, 10))
        tle_ent = Entry(tle_win, font=(root_font, 10))
        def startPrc():
            userProgramTitle = tle_ent.get()
            if len(userProgramTitle) > 2:
                jsn.change_data("title", str(userProgramTitle))
                tle_win.destroy()
                runPY.CompileAndRun()
                now = datetime.now()
                current_time = now.strftime("%I:%M:%S")
                console_msg['text'] = f'Successfully Ran Queue! {current_time}'
            else:
                console_msg['text'] = 'Minimum Program Title Length is 2 Characters'
                tle_win.destroy()
        tle_btn = Button(tle_win, text="Start Process", font=(root_font, 10), command=startPrc)
        tle_txt.grid(row=0, column=0, pady=2, padx=2)
        tle_ent.grid(row=0, column=1, pady=2, padx=2)
        tle_btn.grid(row=1, column=0, pady=2, padx=2)
    else:
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S")
        console_msg['text'] = f'Add 1 or More Messages to Play {current_time}'

run_btn = Button(options_labelframe, text="Run", font=(root_font, 15), relief=GROOVE, bd=0, command=run_programm, fg='green')
run_btn.grid(row=1, column=1)
def on_enter1(e):
    run_btn['fg'] = '#33449f'
def on_leave1(e):
    run_btn['fg'] = 'green'
run_btn.bind('<Enter>', on_enter1)
run_btn.bind('<Leave>', on_leave1)

def add_program():
    add_win = Toplevel(main_frame)
    add_win.title("Add New Line to Queue")
    add_win.geometry("400x400")
    master_font_size = 13

    messageType_txt = Label(add_win, text="Message Type >", font=(root_font, master_font_size))
    messageLine_txt = Label(add_win, text="New Message >", font=(root_font, master_font_size))

    comboBox_val = ['Information', 'Warning', 'Error']
    comboBox = ttk.Combobox(add_win, value=comboBox_val, width=20)
    comboBox['state'] = 'readonly'
    comboBox.current(0)
    msgLine_ent = Entry(add_win, bd=1, font=(root_font, master_font_size))

    def add_new_line():
        global noOfMessages
        noOfMessages = jsn.get_data("msgs")
        noOfMessages = int(noOfMessages)
        lineMsg = msgLine_ent.get()
        msgTypes_dict = {
            "Information": "inf",
            "Warning": "wrn",
            "Error": "err"
        }
        if len(lineMsg) < 50 and len(lineMsg) > 2:
            userMsgType = comboBox.get()
            finalMsgType = msgTypes_dict.get(str(userMsgType))
            if finalMsgType == 'inf':
                noOfMessages = noOfMessages + 1
                jsn.append_data(noOfMessages, f"inf-{lineMsg}")
                jsn.change_data("msgs", noOfMessages)
            elif finalMsgType == 'wrn':
                noOfMessages = noOfMessages + 1
                jsn.append_data(noOfMessages, f"wrn-{lineMsg}")
                jsn.change_data("msgs", noOfMessages)
            elif finalMsgType == 'err':
                noOfMessages = noOfMessages + 1
                jsn.append_data(noOfMessages, f"err-{lineMsg}")
                jsn.change_data("msgs", noOfMessages)
            console_msg['text'] = f'Added New Line! Reload Now.'
        else:
            messagebox.showerror("Error", "Min Line Length -> 2, Max Line Length -> 50")
        add_win.destroy()

    add_btn = Button(add_win, text='Add New Line', font=(root_font, 10), command=add_new_line)

    messageType_txt.grid(row=0, column=0, padx=3, pady=3)
    messageLine_txt.grid(row=1, column=0, padx=3, pady=3)
    comboBox.grid(row=0, column=1, padx=3, pady=3)
    msgLine_ent.grid(row=1, column=1, padx=3, pady=3)
    add_btn.grid(row=2, column=0, padx=3, pady=3)

    checkQueue()

add_btn = Button(options_labelframe, text="Add", font=(root_font, 15), relief=GROOVE, bd=0, command=add_program)
add_btn.grid(row=0, column=0)
def on_enter5(e):
    add_btn['fg'] = '#33449f'
def on_leave5(e):
    add_btn['fg'] = 'black'
add_btn.bind('<Enter>', on_enter5)
add_btn.bind('<Leave>', on_leave5)

def info_program():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    info_window = Toplevel(main_frame)
    info_window.title(f"Info {current_time}")
    info_window.geometry("300x200")
    console_msg['text'] = f'Opened Info Window at {current_time}'

    programTitle_txt = Label(info_window, text=f'Program Title > {jsn.get_data("title")}', font=(root_font, 15))
    totalLines_txt = Label(info_window, text=f'Total Lines in Queue > {jsn.get_data("msgs")}', font=(root_font, 15))

    programTitle_txt.grid(row=0, column=0)
    totalLines_txt.grid(row=1, column=0)


info_btn = Button(options_labelframe, text="Info", font=(root_font, 15), relief=GROOVE, bd=0, command=info_program)
info_btn.grid(row=0, column=1)
def on_enter2(e):
    info_btn['fg'] = '#33449f'
def on_leave2(e):
    info_btn['fg'] = 'black'
info_btn.bind('<Enter>', on_enter2)
info_btn.bind('<Leave>', on_leave2)

def exit_program():
    askExit = messagebox.askyesno(title="Confirm Exit", message="Do You Want to Exit?")
    if askExit or askExit == 'yes':
        jsn.clear_data()
        root.destroy()
        print(f"{Fore.CYAN}Exited, Thank You For Using!")
        quit()
    else:
        console_msg['text'] = f'Failed Exit'

exit_btn = Button(options_labelframe, text="Exit", font=(root_font, 15), relief=GROOVE, bd=0, fg='red', command=exit_program)
exit_btn.grid(row=1, column=0)
def on_enter3(e):
    exit_btn['fg'] = '#33449f'
def on_leave3(e):
    exit_btn['fg'] = 'red'
exit_btn.bind('<Enter>', on_enter3)
exit_btn.bind('<Leave>', on_leave3)


def delete_queue():
    global noOfMessages
    noOfMessages = jsn.get_data("msgs")
    jsn.delete_data(str(noOfMessages))
    jsn.change_data("msgs", str(int(noOfMessages) - 1))
    checkQueue()
    console_msg['text'] = f'Deleted Last Item in Queue'
    noOfMessages = jsn.get_data("msgs")

delete_btn = Button(options_labelframe, text="Delete", font=(root_font, 15), relief=GROOVE, bd=0, command=delete_queue)
delete_btn.grid(row=0, column=2)
def on_enter4(e):
    delete_btn['fg'] = '#33449f'
def on_leave4(e):
    delete_btn['fg'] = 'black'
delete_btn.bind('<Enter>', on_enter4)
delete_btn.bind('<Leave>', on_leave4)

reload_btn = Button(options_labelframe, text="Reload", font=(root_font, 15), relief=GROOVE, bd=0, command=checkQueue)
reload_btn.grid(row=0, column=3)
def on_enter5(e):
    reload_btn['fg'] = '#33449f'
def on_leave5(e):
    reload_btn['fg'] = 'black'
reload_btn.bind('<Enter>', on_enter5)
reload_btn.bind('<Leave>', on_leave5)


root.mainloop()
quit()