from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog


root = Tk()
root.title('Проводник')
root.geometry('350x300+300+300')


def file_wind():
    file_name = filedialog.askopenfilename(initialdir='/')
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        text_wind.delete('1.0', END)
        text_wind.insert('1.0', text)


def info_wind():
    showinfo(title='Info', message='Инструкции работы окна Проводник:''\n'
                                   '1. нажмите на кнопку Выбор фаЙла''\n'
                                   '2. откроется диск для выбора файлов''\n'
                                   '3. выберите файл')


def admin_wind():
    showinfo(title='Admin', message='Вячеслав Аллабергенов''\n'
                                    "Курс Python - разработчик"'\n'
                                    'Университет Urban')


text_wind = Text(root)
text_wind.grid(column=0, columnspan=2, row=0)

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Выберите файл', command=file_wind)

info_menu = Menu(main_menu, tearoff=0)
info_menu.add_command(label='О программе', command=info_wind)

admin_menu = Menu(main_menu, tearoff=0)
admin_menu.add_command(label='Информация о разработчике', command=admin_wind)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Info', menu=info_menu)
main_menu.add_cascade(label='Admin', menu=admin_menu)

root.mainloop()
