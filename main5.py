# IMPORTS -----------------------------------

from tkinter import *

# GLOBAL VARIABLES --------------------------

root = Tk()
after_id = ""
minutes = 0
seconds = 0
miliseconds = 0

# FUNCTIONS ---------------------------------

def start_sw():
    btn1.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()

def tick():
    global after_id, miliseconds, seconds, minutes
    after_id = root.after(10, tick)
    if miliseconds == 100:
        miliseconds = 0
        seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 0:
        label1.configure(text="{0:2d}:{1:2d}".format(seconds, miliseconds))
    elif minutes < 60:
        label1.configure(text="{0:2d}:{1:2d}".format(minutes, seconds))
    elif minutes >= 60:
        label1.configure(text="Выключи меня! Я устал...")
    miliseconds += 1

def stop_sw():
    btn2.grid_forget()
    btn3.grid(row=1, column=0, sticky="ew")
    btn4.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)

def continue_sw():
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()

def reset_sw():
    global miliseconds, seconds, minutes
    miliseconds = 0
    seconds = 0
    minutes = 0
    label1.configure(text="00:00")
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky="ew")

# PROGRAMME ----------------------------------

root.title("Stopwath")

label1 = Label(root, width=5, font=("Ubuntu", 100), text="00:00")
label1.grid(row=0, columnspan=2)

btn1 = Button(root, text="Start", font=("Ubuntu", 30), command=start_sw)
btn2 = Button(root, text="Stop", font=("Ubuntu", 30), command=stop_sw)
btn3 = Button(root, text="Continue", font=("Ubuntu", 30), command=continue_sw)
btn4 = Button(root, text="Reset", font=("Ubuntu", 30), command=reset_sw)

btn1.grid(row=1, columnspan=2, sticky="ew")


root.mainloop()