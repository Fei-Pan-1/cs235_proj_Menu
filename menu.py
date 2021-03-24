import tkinter as tk
from tkinter import *
import time
# import pandas as pd
import csv

# df = pd.DataFrame(colums=['delay', 'sequence', 'error', 'start_time', 'end_time', 'reaction_time'])
# print(df)

window = tk.Tk()
window.title("cs235 project")
window.geometry("600x500+50+0")


def callback(menu):
    x = menu.entrycget(0, "label")
    print(x)
    print(time.strftime('%H:%M:%S'))


# create menu bar
menuBar = Menu(window)
window.config(menu=menuBar)

lst1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
lst2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
lst3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]


def left_click(n, menu):
    # x = menu.entrycget(n, "label")
    # print(x)
    if menu == menu1:
        print("Menu1->" + lst1[n])
    if menu == menu2:
        print("Menu2->" + lst2[n])
    if menu == menu3:
        print("Menu3->" + lst3[n])
    print(time.strftime('%H:%M:%S'))


# Add menu1
menu1 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu1', menu=menu1)
for i in range(len(lst1)):
    menu1.add_command(label=lst1[i], command=lambda idx=i: left_click(idx, menu1))
    if (i + 1) % 4 == 0:
        menu1.add_separator()

# Add menu2
menu2 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu2', menu=menu2)
for i in range(len(lst2)):
    menu2.add_command(label=lst2[i], command=lambda idx=i: left_click(idx, menu2))
    if (i + 1) % 4 == 0:
        menu2.add_separator()

# Add menu3
menu3 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu3', menu=menu3)
for i in range(len(lst3)):
    menu3.add_command(label=lst3[i], command=lambda idx=i: left_click(idx, menu3))
    if (i + 1) % 4 == 0:
        menu3.add_separator()


# menu1.bind("<Button-1>", left_click)


# display Menu
window.config(menu=menuBar)
mainloop()