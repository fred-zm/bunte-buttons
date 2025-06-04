import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

root = tk.Tk()
root.resizable(height=False, width=False)
buttons = []


import random

def rate_spiel(): 
    # Das Programm wählt eine zufällige Zahl zwischen 1 und 100
    minimum = 1
    maximum = 100
    zufallszahl = random.randint(minimum, maximum) 
    versuche = 0
    eingabe = minimum - 1
    try:
        prompt = f'Rate die Zahl zwischen {minimum} und {maximum}.'
        while eingabe != zufallszahl:
            versuche +=1
            eingabe = sd.askinteger(title='Falsch', prompt=prompt, minvalue=minimum, maxvalue=maximum, parent=root)
            if eingabe < zufallszahl:
                prompt = f'{eingabe} war zu niedrig.'
            if zufallszahl < eingabe:
                prompt = f'{eingabe} war zu hoch.'
  
        mb.showinfo('Gewonnen!', f'{zufallszahl} war richtig!\nDu hast {versuche} Versuche gebraucht.', parent=root)
    except:
        pass



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