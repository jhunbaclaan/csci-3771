#@jhunbaclaan
# d.o.c (date of creation): 02/08/2026
# objective -- create a program that has a tkinter gui that includes the following:
# a .icon that replaces the original python feather icon
# title of the window as "Welcome to Python"
# four buttons with labels --
# button 1: HW#1; black background, white foreground
# button 2: HW#2; red background, white foreground
# button 3: HW#3; gray background, blue foreground
# button 4: EXIT; quits the program
# window must be 500x500 px

## NOTE: tkinter button colors do NOT work on macos
# to workaround this i'm importing tkmacosx since that's the easiest solution
import tkinter as tk
from tkmacosx import Button # comment this out if on windows or linux

# create the window
window = tk.Tk()
window.title("Welcome to Python")
window.geometry("500x500")
# changing image; again, issues with macos so i have to use some workarounds
image = tk.Image("photo", file="junepanda.gif") # various image formats included in the .zip, if on windows then i believe junepanda.ico OR junepanda.jpg works just fine
window.tk.call('wm', 'iconphoto', window._w, image)

# create buttons
button1 = Button(window, text="HW#1", bg="black", fg="white")
button2 = Button(window, text="HW#2", bg="red", fg="white")
button3 = Button(window, text="HW#3", bg="gray", fg="blue")
button4 = Button(window, text="EXIT", command=window.destroy)

# pack buttons
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

# construct window on run
window.mainloop()