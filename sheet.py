
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\USER\OneDrive\Desktop\client_secret.json",scope)
client = gspread.authorize(creds)
sheet = client.open("soft_list").sheet1 
l1 = sheet.get_all_values() 
 
# Import the required libraries
import tkinter
from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Unauthorized Software Detection")
win.geometry("500x400")
win.configure(bg='honeydew3')

# Define a function to get the output for selected option
# Define a function to get the output for selected option
def selection():
   selected = "Unauthorized software List:"
   label.config(text=selected, font=("Cascadia Code SemiBold", 13))
   listbox.delete(0, "end") # clear listbox
   # populate listbox
   col = sheet.col_values(radio.get())
   for i in col:
        listbox.insert("end", i)
radio = IntVar()
Label(text="Unauthorized Software Detection", font=("Century Gothic", 15, "bold")).pack()
Label(text="The List of Computers:", font=('Aerial 12')).place(x = 40, y = 60)

# Define radiobutton for each options
rn = Radiobutton(win, text="Default softwares", variable=radio, value=1, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=90)
r1 = Radiobutton(win, text="computer1", variable=radio, value=2, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=110)
r2 = Radiobutton(win, text="Computer2", variable=radio, value=3, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=130)
r3 = Radiobutton(win, text="Computer3", variable=radio, value=4, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=150)
r4 = Radiobutton(win, text="Computer4", variable=radio, value=5, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=170)
r5 = Radiobutton(win, text="Computer5", variable=radio, value=6, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=190)
r6 = Radiobutton(win, text="Computer6", variable=radio, value=7, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=210)
r7 = Radiobutton(win, text="Computer7", variable=radio, value=8, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=230)
r8 = Radiobutton(win, text="Computer8", variable=radio, value=9, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=250)
r9 = Radiobutton(win, text="Computer9", variable=radio, value=10, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=270)
r10 = Radiobutton(win, text="Computer10", variable=radio, value=11, command=selection, font=("Consolas", 11)).place(anchor="nw", x=40, y=290)


# Define a label widget
label = Label(win)
label.pack(anchor=E)
listbox = tkinter.Listbox(win)
listbox.pack(side=RIGHT, fill=BOTH)
listbox.configure(background="skyblue4", foreground="white", font=('Candara 13'))
win.mainloop()