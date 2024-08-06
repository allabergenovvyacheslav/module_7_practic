import tkinter
import os
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = tkinter.Tk()
window.title('Проводник')
window.geometry('353x220+300+300')
window.configure(bg='gray25')
window.resizable(False, False)


def file_select():
    filename = fd.askopenfilename(initialdir='/',
                                  title='Выбрать файл',
                                  filetypes=(('Файл', '.txt'),)
                                  )
    text['text'] += "  " + filename
    os.startfile(filename)


def close_wind():
    window.destroy()


def info_wind():
    showinfo(title='info', message='Инструкции работы окна Проводник:''\n'
                                   '1. нажмите на кнопку Выбор фала''\n'
                                   '2. откроется диск для выбора файлов''\n'
                                   '3. выберите файл')


def admin_wind():
    showinfo(title='admin', message='Вячеслав Аллабергенов''\n'
                                    "Курс Python - разработчик"'\n'
                                    'Университет Urban')


text = tkinter.Label(text='Файл',
                     height=4,
                     width=49,
                     background='white',
                     fg='blue',
                     bd=4,
                     relief=tkinter.RIDGE
                     )
text.place(x=0, y=55)

button_select = tkinter.Button(text='Выбрать файл',
                               height=3,
                               width=20,
                               bg='silver',
                               fg='blue',
                               cursor="hand2",
                               bd=4,
                               activebackground='gold',
                               relief=tkinter.RAISED,
                               command=file_select
                               )
button_select.place(x=0, y=150)

button_select_1 = tkinter.Button(text='Закрыть окно',
                                 height=3,
                                 width=20,
                                 bg='silver',
                                 fg='blue',
                                 cursor="hand2",
                                 bd=4,
                                 activebackground='gold',
                                 relief=tkinter.RAISED,
                                 command=close_wind
                                 )
button_select_1.place(x=199, y=150)

button_select_2 = tkinter.Button(text='info',
                                 height=1,
                                 width=10,
                                 pady=5,
                                 background='silver',
                                 fg='blue',
                                 bd=4,
                                 cursor="hand2",
                                 relief=tkinter.RAISED,
                                 command=info_wind
                                 )
button_select_2.place(x=0, y=1)

# button_select_3 = tkinter.Button(text='version',
#                                  height=1,
#                                  width=10,
#                                  pady=5,
#                                  background='silver',
#                                  fg='blue',
#                                  bd=4,
#                                  cursor="hand2",
#                                  relief=tkinter.RAISED
#                                  )
# button_select_3.place(x=135, y=1)

button_select_4 = tkinter.Button(text='admin',
                                 height=1,
                                 width=10,
                                 pady=5,
                                 background='silver',
                                 fg='blue',
                                 bd=4,
                                 cursor="hand2",
                                 relief=tkinter.RAISED,
                                 command=admin_wind
                                 )
button_select_4.place(x=270, y=1)
window.mainloop()
