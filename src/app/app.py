'''
Created on Nov 23, 2020

@author: manso
'''

import tkinter as tk                    # Import for gui.
from tkinter import filedialog, Text    # Import for file browsing and displaying text.
import os

root = tk.Tk()
apps = []

if os.path.isfile('Saved Apps.txt'):
    with open('Saved Apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()


    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    # print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

openFile = tk.Button(root, text="Open File",
                     padx=10, pady=5,
                     fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps",
                     padx=10, pady=5,
                     fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('Saved Apps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')



