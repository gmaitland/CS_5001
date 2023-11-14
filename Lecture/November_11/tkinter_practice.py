"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - tkinter_practice.py
"""

import tkinter

window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Data to display '
         'Data to test')
# data.set('Show your work')
label = tkinter.Label(window, textvariable=data)
label.pack()

window.mainloop()

# Looks like we are using setter and getter functions again
