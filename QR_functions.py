from tkinter import *
import os
from tkinter import filedialog
from typing import Any
import qrcode
import cv2
from PIL import Image, ImageTk

open_file = ""

def generate(e, text):
    data = e
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    try:
        img.save('./QRs/qrcode001.png')
        text.delete("1.0", 'end')
        text.insert("1.0", e)
    except:
        os.mkdir("QRs")
        img.save('./QRs/qrcide001.png')

def ask_for_qr(dictionary):
    fd = filedialog.askopenfilename(
        title='Choose the image',
        initialdir='./',
    )
    global open_file
    open_file = fd
    dictionary['file_name'].delete("1.0", 'end')
    dictionary['file_name'].insert(END, os.path.split(open_file)[1])

def switch(dictionary, open_file):

    if dictionary["switch_btn"]['text'] == "QR-generator":
        dictionary["switch_btn"]['text']= 'QR-reader'
        dictionary["label"]['text'] = "Open your QR-code image"
        dictionary["text"].delete("1.0", 'end')
        dictionary["url_input"].grid_forget()
        dictionary['dialogue_btn'] = Button(dictionary["frame_wrapper"], text='Choose', command=lambda: ask_for_qr(dictionary))
        dictionary['dialogue_btn'].grid(column=0, row=2,sticky=W, pady=5, padx=15)
        dictionary['generate_button']['text'] = "Read"
        dictionary['generate_button'].config(padx = 5, pady=0, command = lambda: read(dictionary))
        dictionary['generate_button'].grid(column=0, row=2, sticky=E)

    else:
        dictionary["switch_btn"]['text'] = "QR-generator"
        dictionary['label']['text'] = "Put your text in the input field"
        dictionary["text"].delete("1.0", "end")
        dictionary['dialogue_btn'].grid_forget()
        dictionary["url_input"].grid(column=0, row=2, pady=5,padx=5, ipadx=15, ipady=15)
        dictionary['generate_button']["command"] = lambda: generate(dictionary["url_input"].get(), dictionary["text"])
        dictionary['generate_button'].grid(column=0, row=3, sticky=N)
        dictionary['generate_button'].config(padx=15, pady=15, text="Generate")


#Read the qr_code
def read(dictionary):
    print(os.path.split(open_file)[1])
    image = cv2.imread(open_file)
    detect = cv2.QRCodeDetector()
    data, ver_ar, bin_qr = detect.detectAndDecode(image)
    if ver_ar is not None:
        print("QRCode data:")
        print(data)
        dictionary['text'].delete("1.0", "end")
        dictionary['text'].insert(END, data)
    else:
        dictionary['text'].delete("1.0", "end")
        dictionary['text'].insert(END, "Error occured")
    
    
#Title settings
def initial_settings(root):
    open_file = ""
    dict_of_elements = {}

    frame_wrapper = Frame(root, bg='#222222')
    frame_wrapper.pack(side=LEFT)
    dict_of_elements["frame_wrapper"] = frame_wrapper

    label = Label(frame_wrapper, text='Put your text in the input field', bg='#222222', fg='white', pady=5, padx=5)
    label.grid(column = 0, row=1, pady=5, padx=5)
    dict_of_elements["label"] = label

    url_input = Entry(frame_wrapper)
    url_input.grid(column=0, row=2, pady=5, padx=5, ipadx=15, ipady=15)
    dict_of_elements["url_input"] = url_input

    text_label = Label(root, height=159,width=75)
    text_label.config(bg='#222222')
    text_label.pack(pady=15, padx=25,  side=RIGHT)
    file_name = Text(text_label)
    file_name.config(font=("Helvetica", 8), fg='black', height=1, width=15)
    file_name.pack()
    dict_of_elements["file_name"] = file_name
    text = Text(text_label, height=10, width=50)
    text.insert(END,"Right now it is empty, please write down your text in the input field and press \"GENERATE\" button")
    text.config(font=('Helvetica', 8), bg='white', fg='black')
    text.pack()
    dict_of_elements["text"] = text

    btn = Button(frame_wrapper,padx=15, pady=15, text='Generate', command= lambda: generate(url_input.get(), text))
    btn.grid(column=0, row=3, pady=5, padx=5)
    dict_of_elements["generate_button"] = btn

    switch_btn = Button(frame_wrapper, padx=5,pady=5, text='QR-generator', command = lambda: switch(dict_of_elements, open_file))
    switch_btn.grid(column=0, row=0, pady=15)
    dict_of_elements["switch_btn"] = switch_btn