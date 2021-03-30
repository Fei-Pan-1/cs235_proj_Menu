import tkinter as tk
from tkinter import *
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import csv

df = pd.DataFrame(columns=['trail_no', 'predict', 'onset', 'sequence', 'start_time', 'end_time', 'reaction_time(s)', 'error'])

window = tk.Tk()
window.title("cs235 project")
window.geometry("600x500+50+0")

## TODO: initial to time when click button 'trail#', then update everytime when correctly click item
PRE_CLICK_TIME = datetime.now()
## TODO: update trail number when click button 'trail#'
TRAIL_NO = 1
error = 0
predict = True
# onset (0, 0.25. 0.5)
delay = 0


# create menu bar
menuBar = Menu(window)
window.config(menu=menuBar)

lst1 = ["Nachos", "Chicken Taquito", "Tostada Bites", "Eggrolls", "Fries", "Chicken Wings", "Mac&Cheese",
        "Avocado Toast", "Samosa", "Chaat", "Paneer Tikka", "Potato Patty", "Spring Rolls", "Pork pot Stickers",
        "Shrimp Toast", "Garlic Tofu"]
lst2 = ["Enchiladas", "Stack Tacos", "Chicken Stew", "Bean Rice", "CheeseBurger", "Pepperoni Pizza", "Salad",
        "Sandwich", "Biryani", "Curry and Naan", " Chole Bhature ", " Momos", "Kung Pao Chicken ", "Noodles",
        "Dim sums", "Tofu with Rice"]
lst3 = ["Horchata", "Margarita ", "Agua Frasca", "Tequila", "Beer", "Scotch", "Hawaiian Punch", "Coke", "Lassi",
        "Buttermilk", "Masala Soda/carbonated water ", "Tea", "Green Tea", "Matcha", "Bubble Tea", "Cassia wine"]

lst1_to_lst2 = [[0,3,6]]
## TODO: need to be fixed
def generateSequence():
    str = ''
    for i in range(16):
        str = str + '\n' + 'Menu1 -> ' + lst1[i] \
              + '\n' + 'Menu2 -> ' + lst2[i] \
              + '\n' + 'Menu3 -> ' + lst3[i]

    str = str + 'end'
    print(str)
    return str


def getSequence():
    ## TODO: get text from Label
    text = ''
    return text

def swapThreeItem(i, j, k, n, lst):
    if not predict:
        return
    print(i, j, k)
    lst[0], lst[i] = lst[i], lst[0]
    lst[1], lst[j] = lst[j], lst[1]
    lst[2], lst[k] = lst[k], lst[2]
    print(lst)
    # lst[0], lst[k] = lst[k], lst[0]
    # lst[1], lst[j] = lst[j], lst[1]
    # lst[2], lst[i] = lst[i], lst[2]


def swapTwoItem(i, j, n, lst):
    if not predict:
        return
    lst[0], lst[i] = lst[j], lst[0]
    lst[1], lst[j] = lst[j], lst[1]


def swapFourItem(i, j, k, m, n, lst):
    if not predict:
        return
    lst[0], lst[k] = lst[k], lst[0]
    lst[1], lst[j] = lst[j], lst[1]
    lst[2], lst[i] = lst[i], lst[2]
    lst[3], lst[m] = lst[m], lst[3]


def left_click1(n):

    global PRE_CLICK_TIME, df, error
    lst = []
    item = "Menu1 -> " + lst1[n]
    ## TODU: text == a step of sequence!!!
    text = 'Menu1 -> Nachos'
    # click_time = time.time()
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != text:
        error += 1
        print('Choose Again. Wrong item clicked!')
        return

    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000

    # add data to df
    df = df.append(pd.Series([TRAIL_NO, predict, delay, text, PRE_CLICK_TIME, click_time, reaction_time, error], index=df.columns),
                   ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0

    clearmenu(menu2)
    if n == 0:
        lst = lst2
        swapThreeItem(0, 3, 6, n, lst)
    elif n == 1:
        lst = lst2
        swapThreeItem(0, 1, 7, n, lst)
    elif n == 2:
        lst = lst2
        swapThreeItem(2, 3, 11, n, lst)
    elif n == 3:
        lst = lst2
        swapTwoItem(1, 2, n, lst)
    elif n == 4:
        lst = lst2
        swapThreeItem(4, 5, 12, n, lst)
    elif n == 5:
        lst = lst2
        swapTwoItem(6, 9, n, lst)
    elif n == 6:
        lst = lst2
        swapThreeItem(0, 1, 7, n, lst)
    elif n == 7:
        lst = lst2
        swapThreeItem(6, 13, 15, n, lst)
    elif n == 8:
        lst = lst2
        swapThreeItem(0, 8, 10, n, lst)
    elif n == 9:
        lst = lst2
        swapThreeItem(7, 10, 8, n, lst)
    elif n == 10:
        lst = lst2
        swapThreeItem(1, 9, 11, n, lst)
    elif n == 11:
        lst = lst2
        swapThreeItem(4, 8, 10, n, lst)
    elif n == 12:
        lst = lst2
        swapThreeItem(2, 12, 13, n, lst)
    elif n == 13:
        lst = lst2
        swapThreeItem(13, 15, 7, n, lst)
    elif n == 14:
        lst = lst2
        swapThreeItem(14, 12, 5, n, lst)
    elif n == 15:
        lst = lst2
        swapThreeItem(1, 11, 14, n, lst)
    addMenu2(lst)


def left_click2(n, lst2):
    global PRE_CLICK_TIME, df, error
    lst = []
    item = "Menu2 -> " + lst2[n]
    ## TODU: text == a step of sequence!!!
    text = 'Menu2 -> Salad'
    # click_time = time.time()
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != text:
        error += 1
        print('Choose Again. Wrong item clicked!')
        return

    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000

    # add data to df
    df = df.append(pd.Series([TRAIL_NO, predict, delay, text, PRE_CLICK_TIME, click_time, reaction_time, error], index=df.columns),
                   ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0

    clearmenu(menu3)
    if n == 0:
        lst = lst3
        swapThreeItem(0, 1, 4, n, lst)
    elif n == 1:
        lst = lst3
        swapThreeItem(3, 1, 7, n, lst)
    elif n == 2:
        lst = lst3
        swapThreeItem(0, 2, 6, n, lst)
    elif n == 3:
        lst = lst3
        swapThreeItem(2, 3, 14, n, lst)
    elif n == 4:
        lst = lst3
        swapThreeItem(4, 7, 10, n, lst)
    elif n == 5:
        lst = lst3
        swapThreeItem(4, 5, 15, n, lst)
    elif n == 6:
        lst = lst3
        swapThreeItem(2, 6, 12, n, lst)
    elif n == 7:
        lst = lst3
        swapThreeItem(1, 5, 6, n, lst)
    elif n == 8:
        lst = lst3
        swapThreeItem(7, 8, 9, n, lst)
    elif n == 9:
        lst = lst3
        swapThreeItem(4, 8, 9, n, lst)
    elif n == 10:
        lst = lst3
        swapThreeItem(8, 9, 11, n, lst)
    elif n == 11:
        lst = lst3
        swapThreeItem(3, 12, 14, n, lst)
    elif n == 12:
        lst = lst3
        swapThreeItem(2, 15, 14, n, lst)
    elif n == 13:
        lst = lst3
        swapThreeItem(0, 10, 13, n, lst)
    elif n == 14:
        lst = lst3
        swapThreeItem(10, 12, 13, n, lst)
    elif n == 15:
        lst = lst
        swapThreeItem(6, 13, 15, n, lst)
    addMenu3(lst)


def left_click3(n, lst3):
    global PRE_CLICK_TIME, df, error
    lst = []
    item = "Menu3 -> " + lst3[n]
    ## TODO: text == a step of sequence!!!
    text = 'Menu3 -> Coke'
    # click_time = time.time()
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != text:
        error += 1
        print('Choose Again. Wrong item clicked!')
        return

    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000

    # add data to df
    df = df.append(pd.Series([TRAIL_NO, predict, delay, text, PRE_CLICK_TIME, click_time, reaction_time, error], index=df.columns),
                   ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0

    clearmenu(menu1)
    addMenu1(lst1)


def addMenu1(lst1):
    # Add menu1
    # time.sleep(delay)
    # for i in range(len(lst1)):
    #     menu1.add_command(label=lst1[i], command=lambda idx=i: left_click1(idx, lst1))
    #     if (i + 1) % 4 == 0:
    #         menu1.add_separator()
    # print("menu 1 opened")
    time.sleep(delay)
    for i in range(len(lst1)):
        menu1.add_command(label=lst1[i], command=lambda idx=i: left_click1(idx))
        if (i + 1) % 4 == 0:
            menu1.add_separator()



def addMenu2(lst2):
    # Add menu2
    time.sleep(delay)
    for i in range(len(lst2)):
        menu2.add_command(label=lst2[i], command=lambda idx=i: left_click2(idx, lst2))
        if (i + 1) % 4 == 0:
            menu2.add_separator()
    print("current menu2 is:\n")
    print(lst2)


def addMenu3(lst3):
    # Add menu3
    time.sleep(delay)
    for i in range(len(lst3)):
        menu3.add_command(label=lst3[i], command=lambda idx=i: left_click3(idx, lst3))
        if (i + 1) % 4 == 0:
            menu3.add_separator()
    print("current menu3 is:\n")
    print(lst3)


# def clearmenu1(menu):
#     menu.delete(0, 256)
#     for i in range(16):
#         menu.add_command(label=' ')
#         if (i + 1) % 4 == 0:
#             menu.add_separator()


def clearmenu(menu):
    menu.delete(0, 256)


# Add menu1

# menu1 = Menu(menuBar, tearoff=0)
# time.sleep(delay)
# menuBar.add_cascade(label='Menu1', menu=menu1)
# time.sleep(delay)
# for i in range(len(lst1)):
#     menu1.add_command(label=lst1[i], command=lambda idx=i: left_click1(idx))
#     if (i + 1) % 4 == 0:
#         menu1.add_separator()
menu1 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu1', menu=menu1)
addMenu1(lst1)

menu2 = Menu(menuBar, tearoff=0)
clearmenu(menu2)
menuBar.add_cascade(label='Menu2', menu=menu2)

menu3 = Menu(menuBar, tearoff=0)
clearmenu(menu3)
menuBar.add_cascade(label='Menu3', menu=menu3)
str = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' + generateSequence()


def openTrail(n):
    ## TODO: open predict static menu
    global PRE_CLICK_TIME, TRAIL_NO, predict, delay
    TRAIL_NO = n
    if n > 3:
        predict = False
    else:
        predict = True
    if n % 3 == 1:
        delay = 0
    elif n % 3 == 2:
        delay = 0.25
    else:
        delay = 0.5
    PRE_CLICK_TIME = datetime.now()
    # print("Start Trail " + str(n) + ":")
    print(n)
    print(PRE_CLICK_TIME)
    return


# Add buttons
B1 = tk.Button(window, text="Trail 1", padx=10, pady=5, command=lambda: openTrail(1))
B1.grid(row=0, column=0)
B1.pack()
B2 = tk.Button(window, text="Trail 2", padx=10, pady=5, command=lambda: openTrail(2))
# B2['state'] = DISABLED
B2.pack()
B3 = tk.Button(window, text="Trail 3", padx=10, pady=5, command=lambda: openTrail(3))
# B3['state'] = DISABLED
B3.pack()
B4 = tk.Button(window, text="Trail 4", padx=10, pady=5, command=lambda: openTrail(4))
# B4['state'] = DISABLED
B4.pack()
B5 = tk.Button(window, text="Trail 5", padx=10, pady=5, command=lambda: openTrail(5))
# B5['state'] = DISABLED
B5.pack()
B6 = tk.Button(window, text="Trail 6", padx=10, pady=5, command=lambda: openTrail(6))
# B6['state'] = DISABLED
B6.pack()

# display Menu
window.config(menu=menuBar)

T = tk.Text(window, height=400, width=120)
# T = Label(window, text=str)
# T.place(x=0,y=10)
T.pack()
T.insert(tk.END, str)
window.mainloop()

# mainloop()
