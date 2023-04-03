import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculator')
root.geometry("200x350")

can = 0 # location change variable.
pan = 0 # location change variable.
nam = 0 # location change variable.
x = [] # variable_that_collects_numbers_as_well_as_signs.

class main: # a class for collecting output and solving.
    
    def sub_7():
        global can, pan, nam, x
        if can>=200: # to change location.
            pan+=20
            can=0
            nam+=1
        if nam < 5: # output of numbers
            x.append('7')
            label = ttk.Label(text="7", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10
        

    def sub_8():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('8')
            label = ttk.Label(text="8", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_9():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('9')
            label = ttk.Label(text="9", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_clean_up(): # for cleansing
        global can, pan, x
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=0)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=20)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=40)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=60)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=80)
        can = 0
        pan = 0
        x = []

    def sub_4():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('4')
            label = ttk.Label(text="4", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_5():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('5')
            label = ttk.Label(text="5", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_6():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('6')
            label = ttk.Label(text="6", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_plas():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('+')
            label = ttk.Label(text="+", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_1():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('1')
            label = ttk.Label(text="1", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_2():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('2')
            label = ttk.Label(text="2", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_3():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('3')
            label = ttk.Label(text="3", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_mainus():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('-')
            label = ttk.Label(text="-", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_brek_l():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('(')
            label = ttk.Label(text="(", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_brek_r():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append(')')
            label = ttk.Label(text=")", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_divaid():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('/')
            label = ttk.Label(text="÷", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_times():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('*')
            label = ttk.Label(text="*", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_procent():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('**')
            label = ttk.Label(text="^", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=14

    def sub_tiyp_float():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('0')
            label = ttk.Label(text="0", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_corn():
        global can, pan, nam, x
        if can>=200:
            pan+=20
            can=0
            nam+=1
        if nam < 5:
            x.append('**0.5')
            label = ttk.Label(text="√", font='Arial, 10')
            label.place(x=can, y=pan)
            can+=10

    def sub_solv(): # for deriving solutions
        global can, pan, x
        x=''.join(x)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=0)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=20)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=40)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=60)
        label = ttk.Label(text="                                                                                                   ", font='Arial, 10')
        label.place(x=0, y=80)
        if len(x)>0: # to filter out errors
            label = ttk.Label(text=(eval(x)), font='Arial, 10')
            label.place(x=0, y=0)
        can = 0
        pan = 0
        x = []

def Batton(): # to display buttons on the screen

    btn_7 = tk.Button(text="7", height=2, width=5, bg='#848482', command=main.sub_7)
    btn_7.place(x=0.5, y=100)

    btn_8 = tk.Button(text="8", height=2, width=5, bg='#848482', command=main.sub_8)
    btn_8.place(x=50.5, y=100)

    btn_9 = tk.Button(text="9", height=2, width=5, bg='#848482', command=main.sub_9)
    btn_9.place(x=100.5, y=100)

    btn_clean_up = tk.Button(text="AC", height=2, width=5, bg='#848482', command=main.sub_clean_up)
    btn_clean_up.place(x=150.5, y=100)

    btn_4 = tk.Button(text="4", height=2, width=5, bg='#848482', command=main.sub_4)
    btn_4.place(x=0.5, y=150)

    btn_5 = tk.Button(text="5", height=2, width=5, bg='#848482', command=main.sub_5)
    btn_5.place(x=50.5, y=150)

    btn_6 = tk.Button(text="6", height=2, width=5, bg='#848482', command=main.sub_6)
    btn_6.place(x=100.5, y=150)

    btn_plas = tk.Button(text="+", height=2, width=5, bg='#848482', command=main.sub_plas)
    btn_plas.place(x=150.5, y=150)

    btn_1 = tk.Button(text="1", height=2, width=5, bg='#848482', command=main.sub_1)
    btn_1.place(x=0.5, y=200)

    btn_2 = tk.Button(text="2", height=2, width=5, bg='#848482', command=main.sub_2)
    btn_2.place(x=50.5, y=200)

    btn_3 = tk.Button(text="3", height=2, width=5, bg='#848482', command=main.sub_3)
    btn_3.place(x=100.5, y=200)

    btn_mainus = tk.Button(text="-", height=2, width=5, bg='#848482', command=main.sub_mainus)
    btn_mainus.place(x=150.5, y=200)

    btn_brek_l = tk.Button(text="(", height=2, width=5, bg='#848482', command=main.sub_brek_l)
    btn_brek_l.place(x=0.5, y=250)

    btn_brek_r = tk.Button(text=")", height=2, width=5, bg='#848482', command=main.sub_brek_r)
    btn_brek_r.place(x=50.5, y=250)

    btn_divaid = tk.Button(text="÷", height=2, width=5, bg='#848482', command=main.sub_divaid)
    btn_divaid.place(x=100.5, y=250)

    btn_times = tk.Button(text="*", height=2, width=5, bg='#848482', command=main.sub_times)
    btn_times.place(x=150.5, y=250)

    btn_procent = tk.Button(text="^", height=2, width=5, bg='#848482', command=main.sub_procent)
    btn_procent.place(x=0.5, y=300)

    btn_tiyp_float = tk.Button(text="0", height=2, width=5, bg='#848482', command=main.sub_tiyp_float)
    btn_tiyp_float.place(x=50.5, y=300)

    btn_corn = tk.Button(text="√", height=2, width=5, bg='#848482', command=main.sub_corn)
    btn_corn.place(x=100.5, y=300)

    btn_solv = tk.Button(text="=", height=2, width=5, bg='#87CEFA', command=main.sub_solv)
    btn_solv.place(x=150.5, y=300)

Batton() # to call a function with buttons

root.mainloop() 
