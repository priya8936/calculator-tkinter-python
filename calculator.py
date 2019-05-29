###SIMPLE CALCULATOR
import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()
mainWindow.title("calculator")
heading_label=tk.Label(mainWindow,text="enter first number",pady=(10),padx=(20))
heading_label.pack()
name_field=tk.Entry(mainWindow)
name_field.pack()
heading_label2=tk.Label(mainWindow,text="enter second number",pady=(10),padx=(20))
heading_label2.pack()
name_field2=tk.Entry(mainWindow)
name_field2.pack()

heading_label=tk.Label(mainWindow,text="OPERATIONS",pady=(10),padx=(20))
heading_label.pack()

button=tk.Button(mainWindow,text="+",command=lambda:add(),pady=(10),padx=(20))

button.pack()

button=tk.Button(mainWindow,text="-",command=lambda:minus(),pady=(10),padx=(20))

button.pack()

button=tk.Button(mainWindow,text="*",command=lambda:mul(),pady=(10),padx=(20))

button.pack()

button=tk.Button(mainWindow,text="/",command=lambda:div(),pady=(10),padx=(20))

button.pack()

result_label=tk.Label(mainWindow,text="operation result is:-",pady=(10),padx=(20))
result_label.pack()



def add():
    try:
        first_num = int(name_field.get())
        second_num = int(name_field2.get())
        result=first_num+second_num
        #print(first_num+second_num)
        result_label.config(text="result:"+str(result))
    except ValueError:
        messagebox.showerror("error","divide by zero")

def minus():
    try:
        first_num = int(name_field.get())
        second_num = int(name_field2.get())
        result = first_num - second_num
        #print(first_num-second_num)
        result_label.config(text="result:" + str(result))
    except ValueError:
        messagebox.showerror("error","divide by zero")

def mul():
    try:
        first_num = int(name_field.get())
        second_num = int(name_field2.get())
        result = first_num * second_num
        #print(first_num*second_num)
        result_label.config(text="result:" + str(result))
    except ValueError:
        messagebox.showerror("error","divide by zero")
def div():
    try:
        first_num = int(name_field.get())
        second_num = int(name_field2.get())
        result = first_num / second_num
        #print(first_num/second_num)
        result_label.config(text="result:" + str(result))
    except ValueError:
        messagebox.showerror("error","value must be of integer type")
    except ZeroDivisionError:

        messagebox.showerror("error", "divide by zero")

mainWindow.mainloop()

