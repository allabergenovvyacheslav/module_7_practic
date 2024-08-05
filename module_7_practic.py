import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Select a file',
                                          filetypes=(('File', '.txt'),)
                                          )
    text['text'] += "  " + filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('395x175')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window,
                     text='File',
                     height=5,
                     width=56,
                     bg='silver',
                     fg='red'
                     )
text.grid(column=1, row=1)
button = tkinter.Button(window,
                        height=5,
                        width=15,
                        bg='silver',
                        fg='blue',
                        text='Select a file',
                        command=file_select
                        )
button.grid(column=1, row=2, pady=5)

window.mainloop()
