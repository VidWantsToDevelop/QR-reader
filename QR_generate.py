from tkinter import *
from PIL import Image, ImageTk
import os
from QR_functions import *

window = Tk()
window.title = "Let me do my job!"
window.geometry("550x350")
window.configure(background='#222222')
window.maxsize(550, 350)
window.iconphoto(False, PhotoImage(file='icon.png'))

initial_settings(window)

window.mainloop()