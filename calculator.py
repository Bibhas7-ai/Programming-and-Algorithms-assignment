from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('c:/users/calc.ico')
root.geometry("340x370")
root.configure(background="black")
e = Entry(root, width=50, borderwidth=5 )
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

conn = sqlite3.connect('calculator.db')

c = conn.cursor()


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_number =e.get()
    global f_num
    global math
    math = "addition"
    f_num = int (first_number)
    e.delete(0, END)
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)
def button_mode():
    first_number = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "power":
        e.insert(0, f_num ** int(second_number))
    if math == "modulus":
        e.insert(0, f_num % int(second_number))

button_1 = Button(root, text="1",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0",fg="blue",bg="grey", padx=30, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+",fg="blue",bg="orange", padx=30, pady=20, command= button_add)
button_mode = Button(root, text="%",fg="blue",bg="orange", padx=30, pady=20, command= button_mode)
button_subtract = Button(root, text="-",fg="blue",bg="orange", padx=30, pady=20, command= button_subtract)
button_multiply = Button(root, text="*", fg="blue",bg="orange",padx=30, pady=20, command= button_multiply)
button_divide = Button(root, text="/",fg="blue",bg="orange", padx=30, pady=20, command= button_divide)
button_power = Button(root, text="^",fg="blue",bg="orange", padx=30, pady=20, command= button_power)
button_equal = Button(root, text="=",fg="blue",bg="silver", padx=67, pady=20, command= button_equal)
button_clear = Button(root, text="clear",fg="blue",bg="dark grey", padx=57, pady=20, command= button_clear)

conn.commit()
ans = Entry(button_equal,width=30)


conn.close()

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_mode.grid(row=1, column=2)
button_power.grid(row=1, column=3, columnspan=2 )
button_add.grid(row=5, column=1)
button_clear.grid(row=1, column=0, columnspan=2  )
button_equal.grid(row=5, column=2, columnspan=2 )


root.mainloop()