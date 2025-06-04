import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

from PIL import Image, ImageTk, ImageSequence 


root = tk.Tk()
root.title('Bunte Buttons')
root.resizable(height=False, width=False)
main = tk.Frame(root)

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
buttons.append(tk.Button(main, text='Ratespiel', bg='light green', font='blot, 60', fg='red', command=rate_spiel))
#Play Gongsound
buttons.append(tk.Button(main, text='Gong', bg='dark blue', font='blot, 60', fg='grey', command=play_gongsound))
#Popcorn Gif
buttons.append(tk.Button(main, text='Popcorn', bg='yellow', font='blot, 60', fg='white', command=open_anim_window))
#Shuffle Buttons
buttons.append(tk.Button(main, text='Shuffle', bg='light blue', font='blot, 60', fg='black', command=shuffle_buttons))
#
buttons.append(tk.Button(main, text='test5', bg='white', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(main, text='test6', bg='white', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(main, text='test7', bg='white', font='blot, 60', fg='red'))
#
buttons.append(tk.Button(main, text='test8', bg='white', font='blot, 60', fg='red'))

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
                buttons[button_index].grid(column=x, row=y, padx=5, pady=5, sticky='nesw')
            else:
                buttons[button_index].grid(column=x, row=y, padx=5, pady=5, sticky='nesw', columnspan=column_count - x)
                return

main.grid(column=0, row=0, padx=20, pady=20, sticky='nesw')
place_buttons()

# Load the image
bg_image = Image.open("./premium_photo-1687173116184-2277b7a516ca.jpg")  # Replace with your image path
bg_image = bg_image.resize((1200, 1000))   # Resize to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)
 
# Set the image as background using a Label
background_label1 = tk.Label(root, image=bg_photo)
background_label2 = tk.Label(main, image=bg_photo)

background_label1.place(x=0, y=0, relwidth=1, relheight=1)
background_label1.lower()
 
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
background_label2.lower()

def resize_background(event):
    # Berechne die neue Größe
    new_width = event.width
    new_height = event.height

    # Skaliere das Bild auf die neue Fenstergröße
    resized_image = bg_image.resize((new_width, new_height))
    bg_photo = ImageTk.PhotoImage(resized_image)

    # Aktualisiere das Label mit dem neuen Bild
    background_label1.config(image=bg_photo)
#root.bind('<Configure>', resize_background)


root.mainloop()
pygame.mixer.quit()
