import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

import button_functions

root = tk.Tk()
root.resizable(height=False, width=False)
buttons = []


import random

zufallszahl = 0
versuche = 0
eingabe = 0

def guess():
    if eingabe < zufallszahl:
        eingabe = sd.askinteger(title='', prompt='Zu niedrig')
    if zufallszahl < eingabe:
        eingabe = sd.askinteger(title='', prompt='Zu hoch')
    if eingabe == zufallszahl:
        mb.showinfo('Gewonnen!!')
        return
    guess()

def rate_spiel(): 
    # Das Programm wählt eine zufällige Zahl zwischen 1 und 100
    zufallszahl = random.randint(1, 100)
    versuche = 0
    eingabe = sd.askinteger(title='', prompt='Rate die Zahl zwischen 1 und 100')
    guess()

#Ratespiel
buttons.append(tk.Button(root, text='Ratespiel', bg='light green', font='blot, 60', fg='red', command=rate_spiel))
#
buttons.append(tk.Button(root, text='test2', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test3', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test3', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test3', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test3', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test3', bg='light green', font='blot, 60', fg='red'))


column_count = 3

#while len(buttons) % column_count != 0:
#    buttons.append(tk.Frame())

for y in range(column_count):
    for x in range(len(buttons)//column_count):
        button_index = x + y * len(buttons) // column_count
        if button_index == len(buttons):
            buttons[button_index].grid(column=x, row=y, columnspan=3)
        else:
            buttons[button_index].grid(column=x, row=y, padx=10, pady=10)
    

root.mainloop()