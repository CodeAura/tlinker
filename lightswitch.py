import tkinter as tk
from typing import Text
window = tk.Tk()

button = tk.Button(text='Lamp aan', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
window['bg'] = 'black'

def clickButton(event):
    button.config(text=' Lamp uit')
    print ("Lamp is aan")
    window['bg'] = 'yellow'

button.bind("<Button-1>", clickButton) #Rechter button (Rightclick)

def clickButton1(event):
    button.config(text=' Lamp aan')
    print ("Lamp is uit")
    window['bg'] = 'Black'
button.bind("<Button-3>", clickButton1) #Linker button (Leftclick)
# schijf hier tussen je code

window.mainloop()
