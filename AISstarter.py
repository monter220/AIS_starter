import tkinter
import shutil
import os
import webbrowser
from tkinter import messagebox as mb


def esc(event=None):
    AIS_start_window.destroy()
    quit()


def start_AIS(server):
    os.system('taskkill /im iexplore.exe')
    src = '//%s/Main/PACKS/ЕГЭ' % server
    dst = 'C:\Program Files\Croc\АИС Экзамен\Main\PACKS\ЕГЭ'
    if os.path.isdir(src):
        if os.path.exists(dst):
            shutil.rmtree(dst, ignore_errors=True)
            shutil.copytree(src, dst)
        else:
            shutil.copytree(src, dst)
        webbrowser.open_new_tab(server + '\exam')
        esc()
    else:
        mb.showerror('error', 'Server ' + server + ' is not found')


AIS_start_window = tkinter.Tk()
AIS_start_window.title('Start_AIS')
AIS_start_window.geometry('710x230')

d1 = tkinter.Label(height="3", width="5")
d1.grid(row=0, column=0)
d2 = tkinter.Label(height="3", width="5")
d2.grid(row=1, column=0)
d3 = tkinter.Label(height="3", width="5")
d3.grid(row=2, column=0)

battle_label = tkinter.Label(text='Боевые экзамены', font=("Arial", 16, "bold"))
battle_label.grid(row=0, column=1)

aisbattle_button = tkinter.Button(AIS_start_window, height="3", width="20", background="#069",
                                  foreground="#ccc", activebackground='#066', padx="20", pady="8", font="16",
                                  text='ОГЭ кроме химии', command=lambda: start_AIS('aisbattle2'))
aisbattle_button.grid(row=1, column=1)

aisbattlehim_button = tkinter.Button(AIS_start_window, height="3", width="20", background="#069",
                                     foreground="#ccc", activebackground='#066', padx="20", pady="8", font="16",
                                     text='ОГЭ по химии', command=lambda: start_AIS('aisbattle2him'))
aisbattlehim_button.grid(row=2, column=1)

d4 = tkinter.Label(height="3", width="20")
d4.grid(row=0, column=2)
d5 = tkinter.Label(height="3", width="20")
d5.grid(row=1, column=2)
d6 = tkinter.Label(height="3", width="20")
d6.grid(row=2, column=2)

rep_label = tkinter.Label(text='Репетиционные экзамены', font=("Arial", 16, "bold"))
rep_label.grid(row=0, column=3)

aisrep_button = tkinter.Button(AIS_start_window, height="3", width="20", background="#060",
                               foreground="#ccc", padx="20", activebackground='#063', pady="8", font="16",
                               text='ОГЭ кроме химии', command=lambda: start_AIS('aisrep'))
aisrep_button.grid(row=1, column=3)

aisrephim_button = tkinter.Button(AIS_start_window, height="3", width="20", background="#060",
                                  foreground="#ccc", padx="20", activebackground='#063', pady="8", font="16",
                                  text='ОГЭ по химии', command=lambda: start_AIS('aisrephim'))
aisrephim_button.grid(row=2, column=3)

AIS_start_window.protocol('WM_DELETE_WINDOW', esc)

# AIS_start_window.iconbitmap(r'icon.ico')
AIS_start_window.mainloop()