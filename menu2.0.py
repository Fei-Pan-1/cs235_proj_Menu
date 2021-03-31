import tkinter as tk
from tkinter import *
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import csv
import random
from random import randrange
from tkinter import filedialog

df = pd.DataFrame(
    columns=['trail_no', 'predict', 'onset(s)', 'sequence', 'start_time', 'end_time', 'reaction_time(s)', 'error'])

window = tk.Tk()
window.title("cs235 project")
window.geometry("1180x500+50+0")

## initial to time when click button 'trail#', then update everytime when correctly click item
PRE_CLICK_TIME = datetime.now()
TRAIL_NO = 1
error = 0
predict = True
delay = 0
N = 1  # N th in predict sequence
maxN = 15
current_item = 0  # 0 represents 0th item
current_sequence = ''

# create menu bar
menuBar = Menu(window)
window.config(menu=menuBar)

lst1 = ["Nachos", "Chicken Taquito", "Tostada Bites", "Eggrolls", "Fries", "Chicken Wings", "Mac&Cheese",
        "Avocado Toast", "Samosa", "Chaat", "Paneer Tikka", "Potato Patty", "Spring Rolls", "Pork pot Stickers",
        "Shrimp Toast", "Garlic Tofu"]
lst2 = ["Enchiladas", "Stack Tacos", "Chicken Stew", "Bean Rice", "CheeseBurger", "Pepperoni Pizza", "Salad",
        "Sandwich", "Biryani", "Curry and Naan", "Chole Bhature", "Momos", "Kung Pao Chicken", "Noodles",
        "Dim sums", "Tofu with Rice"]
lst3 = ["Horchata", "Margarita ", "Agua Frasca", "Tequila", "Beer", "Scotch", "Hawaiian Punch", "Coke", "Lassi",
        "Buttermilk", "Masala Soda/carbonated water ", "Tea", "Green Tea", "Matcha", "Bubble Tea", "Cassia wine"]

lst1_to_lst2 = [[0, 3, 6], [0, 1, 7], [2, 3, 11], [1, 2, 15], [4, 5, 12], [4, 6, 9], [0, 1, 7], [6, 13, 15], [0, 8, 10],
                [7, 8, 10], [1, 9, 11], [4, 8, 10], [2, 12, 13], [3, 13, 15], [5, 12, 14], [1, 11, 14]]
lst2_to_lst3 = [[0, 1, 4], [1, 3, 7], [0, 2, 6], [2, 3, 14], [4, 7, 10], [4, 5, 15], [2, 6, 12], [1, 5, 6], [7, 8, 9],
                [4, 8, 9], [8, 9, 11], [3, 12, 14], [2, 14, 15], [0, 10, 13], [10, 12, 13], [6, 13, 15]]


def generateSequence():
    global N, current_sequence, current_item
    if N > maxN:
        print('Trail end! Click next Trail!')
        L1.config(text='Trail ends! Click next Trail!')
        L2.config(text='')
        L3.config(text='')
        if TRAIL_NO == 1:
            B1['state'] = DISABLED
            B2['state'] = NORMAL
        elif TRAIL_NO == 2:
            B2['state'] = DISABLED
            B3['state'] = NORMAL
        elif TRAIL_NO == 3:
            B3['state'] = DISABLED
            B4['state'] = NORMAL
        elif TRAIL_NO == 4:
            B4['state'] = DISABLED
            B5['state'] = NORMAL
        elif TRAIL_NO == 5:
            B5['state'] = DISABLED
            B6['state'] = NORMAL
        else:
            df.to_csv('menu_data.csv', index=True, header=True)     # save to csv file
            B6['state'] = DISABLED
            L1.config(text='Congratulations! You Finished All Trail!')
            L3.config(text='menu_data.csv File Exported!')
        N = 1
        return
    if N % 3 == 1:  # from Menu1
        i = randrange(16)
        current_sequence = "Menu1 -> " + lst1[i]
        print(current_sequence)
        current_item = i
    elif N % 3 == 2:  # from Menu2
        x = lst1_to_lst2[current_item]
        print("lst1 to lst2 check:")
        print(x)
        i = random.choice(x)
        current_sequence = "Menu2 -> " + lst2[i]
        print(current_sequence)
        current_item = i
    else:
        x = lst2_to_lst3[current_item]
        print("lst2 to lst3 check:")
        print(x)
        # i = random.choice(x)
        i = 10
        current_sequence = "Menu3 -> " + lst3[i]
        print(current_sequence)
        current_item = i

    L2.config(text=current_sequence)
    return current_sequence


def swapThreeItem(i, j, k, lst):
    if not predict:
        return
    lst[0], lst[i] = lst[i], lst[0]
    lst[1], lst[j] = lst[j], lst[1]
    lst[2], lst[k] = lst[k], lst[2]


def swapTwoItem(i, j, k, lst):
    if not predict:
        return
    numset = [0, 1, 2]
    indexset = [i, j, k]
    if i in numset:
        numset.remove(i)
        indexset.remove(i)
    if j in numset:
        numset.remove(j)
        indexset.remove(j)
    if k in numset:
        numset.remove(k)
        indexset.remove(k)
    lst[numset[0]], lst[indexset[0]] = lst[indexset[0]], lst[numset[0]]
    if len(numset) > 1:
        lst[numset[1]], lst[indexset[1]] = lst[indexset[1]], lst[numset[1]]


def swapOneItem(i, j, k, lst):
    if not predict:
        return
    numset = [0, 1, 2]
    indexset = [i, j, k]
    if i in numset:
        numset.remove(i)
        indexset.remove(i)
    if j in numset:
        numset.remove(j)
        indexset.remove(j)
    if k in numset:
        numset.remove(k)
        indexset.remove(k)
    lst[numset[0]], lst[indexset[0]] = lst[indexset[0]], lst[numset[0]]


def left_click1(n):
    global PRE_CLICK_TIME, df, error, N
    item = "Menu1 -> " + lst1[n]
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != current_sequence:
        error += 1
        print('Choose Again. Wrong item clicked!')
        L3.config(text='X', fg='red')
        return

    L3.config(text='✓', fg="green")
    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000 - delay

    # add data to df
    df = df.append(
        pd.Series([TRAIL_NO, predict, delay, current_sequence, PRE_CLICK_TIME, click_time, reaction_time, error],
                  index=df.columns),
        ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0
    N += 1
    generateSequence()

    clearmenu(menu2)
    lst = lst2.copy()
    if n == 0:
        swapTwoItem(0, 3, 6, lst)
    elif n == 1:
        swapOneItem(0, 1, 7, lst)
    elif n == 2:
        swapTwoItem(2, 3, 11, lst)
    elif n == 3:
        swapTwoItem(1, 2, 15, lst)
    elif n == 4:
        swapThreeItem(4, 5, 12, lst)
    elif n == 5:
        swapThreeItem(4, 6, 9, lst)
    elif n == 6:
        swapOneItem(0, 1, 7, lst)
    elif n == 7:
        swapThreeItem(6, 13, 15, lst)
    elif n == 8:
        swapTwoItem(0, 8, 10, lst)
    elif n == 9:
        swapThreeItem(7, 8, 10, lst)
    elif n == 10:
        swapTwoItem(1, 9, 11, lst)
    elif n == 11:
        swapThreeItem(4, 8, 10, lst)
    elif n == 12:
        swapTwoItem(2, 12, 13, lst)
    elif n == 13:
        swapThreeItem(3, 13, 15, lst)
    elif n == 14:
        swapThreeItem(5, 12, 14, lst)
    elif n == 15:
        swapTwoItem(1, 11, 14, lst)
    addMenu2(lst)


def left_click2(menu_item_name):
    global PRE_CLICK_TIME, df, error, N
    item = "Menu2 -> " + menu_item_name
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != current_sequence:
        error += 1
        print('Choose Again. Wrong item clicked! ')
        L3.config(text='X', fg='red')
        return

    L3.config(text='✓', fg="green")
    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000 - delay

    # add data to df
    df = df.append(
        pd.Series([TRAIL_NO, predict, delay, current_sequence, PRE_CLICK_TIME, click_time, reaction_time, error],
                  index=df.columns),
        ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0
    N += 1
    generateSequence()

    clearmenu(menu3)
    lst = lst3.copy()
    if menu_item_name == "Enchiladas":
        swapOneItem(0, 1, 4, lst)
    elif menu_item_name == "Stack Tacos":
        swapTwoItem(1, 3, 7, lst)
    elif menu_item_name == "Chicken Stew":
        swapOneItem(0, 2, 6, lst)
    elif menu_item_name == "Bean Rice":
        swapTwoItem(2, 3, 14, lst)
    elif menu_item_name == "CheeseBurger":
        swapThreeItem(4, 7, 10, lst)
    elif menu_item_name == "Pepperoni Pizza":
        swapThreeItem(4, 5, 15, lst)
    elif menu_item_name == "Salad":
        swapTwoItem(2, 6, 12, lst)
    elif menu_item_name == "Sandwich":
        swapTwoItem(1, 5, 6, lst)
    elif menu_item_name == "Biryani":
        swapThreeItem(7, 8, 9, lst)
    elif menu_item_name == "Curry and Naan":
        swapThreeItem(4, 8, 9, lst)
    elif menu_item_name == "Chole Bhature":
        swapThreeItem(8, 9, 11, lst)
    elif menu_item_name == "Momos":
        swapThreeItem(3, 12, 14, lst)
    elif menu_item_name == "Kung Pao Chicken":
        swapTwoItem(2, 14, 15, lst)
    elif menu_item_name == "Noodles":
        swapTwoItem(0, 10, 13, lst)
    elif menu_item_name == "Dim sums":
        swapThreeItem(10, 12, 13, lst)
    elif menu_item_name == "Tofu with Rice":
        swapThreeItem(6, 13, 15, lst)
    addMenu3(lst)


def left_click3(menu_item_name):
    global PRE_CLICK_TIME, df, error, N
    lst = []
    item = "Menu3 -> " + menu_item_name
    click_time = datetime.now()
    print(item)
    print(click_time)
    print(PRE_CLICK_TIME)
    if item != current_sequence:
        error += 1
        print('Choose Again. Wrong item clicked!')
        L3.config(text='X', fg='red')
        return

    L3.config(text='✓', fg="green")
    diff = click_time - PRE_CLICK_TIME
    print('Reaction time: ')
    print(diff)
    reaction_time = diff.seconds + diff.microseconds / 1000000 - delay

    # add data to df
    df = df.append(
        pd.Series([TRAIL_NO, predict, delay, current_sequence, PRE_CLICK_TIME, click_time, reaction_time, error],
                  index=df.columns),
        ignore_index=True)
    pd.set_option('max_columns', None)
    print(df)
    PRE_CLICK_TIME = click_time
    error = 0
    N += 1
    generateSequence()

    clearmenu(menu1)
    addMenu1(lst1)


def addMenu1(lst1):
    time.sleep(delay)
    for i in range(len(lst1)):
        menu1.add_command(label=lst1[i], command=lambda idx=i: left_click1(idx))
        if (i + 1) % 4 == 0:
            menu1.add_separator()


def addMenu2(lst):
    time.sleep(delay)
    for i in range(len(lst)):
        menu2.add_command(label=lst[i], command=lambda menu_item_name=lst[i]: left_click2(menu_item_name))
        if (i + 1) % 4 == 0:
            menu2.add_separator()
    print("current menu2 is:\n")
    print(lst)


def addMenu3(lst):
    time.sleep(delay)
    for i in range(len(lst)):
        menu3.add_command(label=lst[i], command=lambda menu_item_name=lst[i]: left_click3(menu_item_name))
        if (i + 1) % 4 == 0:
            menu3.add_separator()
    print("current menu3 is:\n")
    print(lst)


def clearmenu(menu):
    menu.delete(0, 256)


# Add menus
menu1 = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Menu1', menu=menu1)
addMenu1(lst1)

menu2 = Menu(menuBar, tearoff=0)
clearmenu(menu2)
menuBar.add_cascade(label='Menu2', menu=menu2)

menu3 = Menu(menuBar, tearoff=0)
clearmenu(menu3)
menuBar.add_cascade(label='Menu3', menu=menu3)


def openTrail(n):
    global PRE_CLICK_TIME, TRAIL_NO, predict, delay
    generateSequence()
    L1.config(text='Please Click Menu Item:')
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
    print(n)
    print(PRE_CLICK_TIME)
    return


# display Menu
window.config(menu=menuBar)

L1 = Label(window, text="Please Choose A Trail: ",
           fg="red",
           font="Times 14")
L1.place(x=40, y=400)
L2 = Label(window,
           text=current_sequence,
           fg="light green",
           bg="dark green",
           font="Helvetica 16 bold")
L2.place(x=40, y=420)
L3 = Label(window, text="",
           fg="red",
           font="Helvetica 14 bold")
L3.place(x=40, y=400)
L1.pack()
L2.pack()
L3.pack()

# Add buttons
B1 = tk.Button(window, text="Trail 1", padx=10, pady=5, command=lambda: openTrail(1))
B1.pack()
B2 = tk.Button(window, text="Trail 2", padx=10, pady=5, command=lambda: openTrail(2))
B2['state'] = DISABLED
B2.pack()
B3 = tk.Button(window, text="Trail 3", padx=10, pady=5, command=lambda: openTrail(3))
B3['state'] = DISABLED
B3.pack()
B4 = tk.Button(window, text="Trail 4", padx=10, pady=5, command=lambda: openTrail(4))
B4['state'] = DISABLED
B4.pack()
B5 = tk.Button(window, text="Trail 5", padx=10, pady=5, command=lambda: openTrail(5))
B5['state'] = DISABLED
B5.pack()
B6 = tk.Button(window, text="Trail 6", padx=10, pady=5, command=lambda: openTrail(6))
B6['state'] = DISABLED
B6.pack()

canvas1 = tk.Canvas(window, width=300, height=300, bg='white', relief='raised')
canvas1.pack()

# def exportCSV():
#     global df
#     export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
#     df.to_csv(export_file_path, index=True, header=True)
#
# saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='grey', fg='blue',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 150, window=saveAsButton_CSV)

window.mainloop()