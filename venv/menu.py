import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("cs235 project")
window.geometry("600x500+50+0")

# create menu bar
menuBar = Menu(window)
window.config(menu=menuBar)

N = 16
m1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
m2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
m3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

# Add menu1
menu1 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu1', menu=menu1)
for i in range(N):
    menu1.add_command(label=m1[i], command=None)
    if (i + 1) % 4 == 0:
        menu1.add_separator()

# Add menu2
menu2 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu2', menu=menu2)
for i in range(N):
    menu2.add_command(label=m2[i], command=None)
    if (i + 1) % 4 == 0:
        menu2.add_separator()

# Add menu3
menu3 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu3', menu=menu3)
for i in range(N):
    menu3.add_command(label=m3[i], command=None)
    if (i + 1) % 4 == 0:
        menu3.add_separator()

# display Menu
window.config(menu=menuBar)
mainloop()