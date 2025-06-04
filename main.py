import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd


root = tk.Tk()
root.resizable(height=False, width=False)
buttons = []


import random

def rate_spiel(): 
    # Die Funktion wählt eine zufällige Zahl zwischen 1 und 100
    minimum = 1
    maximum = 100
    zufallszahl = random.randint(minimum, maximum) 
    versuche = 0
    eingabe = minimum - 1
    title = 'Ratespiel'
    try:
        prompt = f'Rate die Zahl zwischen {minimum} und {maximum}.'
        while eingabe != zufallszahl:
            versuche +=1
            root.withdraw()
            eingabe = sd.askinteger(title=title, prompt=prompt, minvalue=minimum, maxvalue=maximum, parent=root)
            title = 'Falsch'
            if eingabe < zufallszahl:
                prompt = f'{eingabe} war zu niedrig.'
            if zufallszahl < eingabe:
                prompt = f'{eingabe} war zu hoch.'
  
        mb.showinfo('Gewonnen!', f'{zufallszahl} war richtig!\nDu hast {versuche} Versuche gebraucht.', parent=root)
    except:
        pass
    root.deiconify()


import pygame
pygame.mixer.init()

def play_gongsound():
    pygame.mixer.music.load('gong-sound-effect-308757.mp3')
    pygame.mixer.music.play()


from PIL import Image, ImageTk, ImageSequence 

def open_anim_window(): 
    anim_window = tk.Toplevel(root)
    anim_window.title("Animation")
 
    label = tk.Label(anim_window)
    label.pack()
 
    gif = Image.open("./giphy.gif")
    frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif)]
 
    def update_frame(index):
        frame = frames[index]
        label.configure(image=frame)
        anim_window.after(100, update_frame, (index + 1) % len(frames))
 
    update_frame(0)

def shuffle_buttons():
    for button in buttons:
        button.grid_forget()
    random.shuffle(buttons)
    place_buttons()

#Ratespiel
buttons.append(tk.Button(root, text='Ratespiel', bg='light green', font='blot, 60', fg='red', command=rate_spiel))
#Play Gongsound
buttons.append(tk.Button(root, text='Gong', bg='dark blue', font='blot, 60', fg='grey', command=play_gongsound))
#Popcorn Gif
buttons.append(tk.Button(root, text='Popcorn', bg='yellow', font='blot, 60', fg='white', command=open_anim_window))
#Shuffle Buttons
buttons.append(tk.Button(root, text='Shuffle', bg='light green', font='blot, 60', fg='red', command=shuffle_buttons))
#
buttons.append(tk.Button(root, text='test5', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test6', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test7', bg='light green', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(root, text='test8', bg='light green', font='blot, 60', fg='red'))


#Place the Buttons
def place_buttons():
    column_count = 3
    row_count = len(buttons)/column_count
    if row_count > int(row_count):
        row_count +=1
    row_count = int(row_count)
    for y in range(row_count):
        root.rowconfigure(y, weight=1)
        for x in range(column_count):
            root.columnconfigure(x, weight=1)
            button_index = x + y * column_count
            if button_index < len(buttons) -1:
                buttons[button_index].grid(column=x, row=y, padx=10, pady=10)
            else:
                buttons[button_index].grid(column=x, row=y, padx=10, pady=10, columnspan=column_count - x)
                return
            
place_buttons()

root.mainloop()
pygame.mixer.quit()