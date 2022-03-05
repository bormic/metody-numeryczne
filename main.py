# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:31:33 2021

@author: Michał Borkowski
"""

import tkinter.messagebox as tk
from tkinter.font import Font
from easygui import *
from tkinter import *
from math import *
import matplotlib.pyplot as plt
import itertools
import pylab as py
import numpy as np
import numexpr as ne
import pandas as pd
import sqlite3
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

dpz0 = 0.0000000001  # dokładność porównania z zerem
dwsqrt = 0.0000000001  # dokładność wyznaczenia pierwiastka


def SprawdzInt(wejscie):
    try:
        int(wejscie)
        return True
    except ValueError:
        return False


def SprawdzFloat(wejscie):
    try:
        float(wejscie)
        return True
    except ValueError:
        return False


def SprawdźWielomian(function, x):
    return ne.evaluate(function, {"x": x, "cos": cos(x), "sin": sin(x), "tan": tan(x), "cot": 1/tan(x)})


def TryEvaluate(wejscie):
    try:
        if(SprawdzInt(wielomian(wejscie, 10)) or SprawdzFloat(wielomian(wejscie, 10)) == True):
            return True
    except Exception:
        return False    


def inputBlock(wyb):
    if wyb == 1:
        test = False
        while test == False:
            # wyświetlana wiadomość
            text1 = "Podaj parametr a = "
            # tytuł okna
            title1 = "Zakres poszukiwan pierwiastka - metoda siecznych!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text1 = "Wprowadź parametr a tu..."
            # kreator okna wprowadzania
            output1 = str(enterbox(text1, title1, d_text1))
            
            if(SprawdzInt(output1) == True):
                test = True
            
        # tytuł okna
        title1 = "Wprowadziłeś parametr a:"
        # tekst domyślny wewnątrz okna wprowadzania
        d1_text = "a = "
        # kreator komunikatu
        msgbox(d1_text + output1, title1)

        a = int(output1)

        test = False
        while test == False:
            # wyświetlana wiadomość
            text2 = "Podaj parametr b = "
            # tytuł okna
            title2 = "Zakres poszukiwan pierwiastka - metoda siecznych!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text2 = "Wprowadź parametr b tu..."
            # kreator okna wprowadzania
            output2 = str(enterbox(text2, title2, d_text2))
        
            if(SprawdzInt(output2) == True):
                test = True        
        
        # tytuł okna
        title2 = "Wprowadziłeś parametr b:"
        # tekst domyślny wewnątrz okna wprowadzania
        d2_text = "b = "
        # kreator komunikatu
        msgbox(d2_text + output2, title2)

        b = int(output2)

        inputMessagec0 = "Zakres poszukiwan pierwiastka"
        inputMessagec1 = "Zakres poszukiwan pierwiastka od: " + str(a) + " do: " + str(b)
        tk.showinfo(inputMessagec0, inputMessagec1)

        return a, b

    elif wyb == 2:
        test = False
        while test == False:
            # wyświetlana wiadomość
            text1 = "Podaj parametr a = "
            # tytuł okna
            title1 = "Zakres poszukiwan pierwiastka - metoda falszywej prostej!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text1 = "Wprowadź parametr a tu..."
            # kreator okna wprowadzania        
            output1 = str(enterbox(text1, title1, d_text1))
            if(SprawdzInt(output1) == True):
                test = True
        
        # tytuł okna
        title1 = "Wprowadziłeś parametr a:"
        # tekst domyślny wewnątrz okna wprowadzania
        d1_text = "a = "
        # kreator komunikatu
        msgbox(d1_text + output1, title1)

        a = int(output1)

        test = False
        while test == False:
            # wyświetlana wiadomość
            text2 = "Podaj parametr b = "
            # tytuł okna
            title2 = "Zakres poszukiwan pierwiastka - metoda falszywej prostej!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text2 = "Wprowadź parametr b tu..."
            # kreator okna wprowadzania
            output2 = str(enterbox(text2, title2, d_text2))
            if(SprawdzInt(output2) == True):
                test = True
        
        # tytuł okna
        title2 = "Wprowadziłeś parametr b:"
        # tekst domyślny wewnątrz okna wprowadzania
        d2_text = "b = "
        # kreator komunikatu
        msgbox(d2_text + output2, title2)

        b = int(output2)

        inputMessagec0 = "Zakres poszukiwan pierwiastka"
        inputMessagec1 = "Zakres poszukiwan pierwiastka od: " + str(a) + " do: " + str(b)
        tk.showinfo(inputMessagec0, inputMessagec1)

        return a, b

    elif wyb == 3:
        test = False
        while test == False:
            # wyświetlana wiadomość
            text1 = "Podaj parametr a = "
            # tytuł okna
            title1 = "Zakres poszukiwan pierwiastka - metoda bisekcji!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text1 = "Wprowadź parametr a tu..."
            # kreator okna wprowadzania
            output1 = str(enterbox(text1, title1, d_text1))
            if(SprawdzInt(output1) == True):
                test = True

        # tytuł okna
        title1 = "Wprowadziłeś parametr a:"
        # tekst domyślny wewnątrz okna wprowadzania
        d1_text = "a = "
        # kreator komunikatu
        msgbox(d1_text + output1, title1)

        a = int(output1)

        test = False
        while test == False:
            # wyświetlana wiadomość
            text2 = "Podaj parametr b = "
            # tytuł okna
            title2 = "Zakres poszukiwan pierwiastka - metoda bisekcji!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text2 = "Wprowadź parametr b tu..."
            # kreator okna wprowadzania
            output2 = str(enterbox(text2, title2, d_text2))
            if(SprawdzInt(output2) == True):
                test = True        
        
        # tytuł okna
        title2 = "Wprowadziłeś parametr b:"
        # tekst domyślny wewnątrz okna wprowadzania
        d2_text = "b = "
        # kreator komunikatu
        msgbox(d2_text + output2, title2)

        b = int(output2)

        inputMessagec0 = "Zakres poszukiwan pierwiastka"
        inputMessagec1 = "Zakres poszukiwan pierwiastka od: " + str(a) + " do: " + str(b)
        tk.showinfo(inputMessagec0, inputMessagec1)

        return a, b

    else:
        test = False
        while test == False:
            # wyświetlana wiadomość
            text1 = "Podaj punkt startowy x0 = "
            # tytuł okna
            title1 = "Punkt startowy poszukiwan pierwiastka - metoda Newtona!"
            # tekst domyślny wewnątrz okna wprowadzania
            d_text1 = "Wprowadź punkt startowy x0 tu..."
            # kreator okna wprowadzania
            output1 = str(enterbox(text1, title1, d_text1))
            if(SprawdzInt(output1) == True):
                test = True         
        
        # tytuł okna
        title1 = "Wprowadziłeś punkt startowy x0:"
        # tekst domyślny wewnątrz okna wprowadzania
        d1_text = "a = "
        # kreator komunikatu
        msgbox(d1_text + output1, title1)

        a = int(output1)

        inputMessagec0 = "Punkt startowy poszukiwan pierwiastka"
        inputMessagec1 = "Punkt startowy poszukiwan pierwiastka x0 = " + str(a)
        tk.showinfo(inputMessagec0, inputMessagec1)

        return a


def wprowadz_wielomian():
    test = False
    while test == False:
        # operatory()
        # wyświetlana wiadomość
        text = "Podaj funkcję f(x) = "
        # tytuł okna
        title = "Obliczanie pierwiastka funkcji"
        # tekst domyślny wewnątrz okna wprowadzania
        d_text = "Wprowadź funkcję tu..."
        # kreator okna wprowadzania
        output = str(enterbox(text, title, d_text))
        # tytuł okna
        title = "Wprowadziłeś funkcję: "
        # tekst domyślny wewnątrz okna wprowadzania
        dt_text = "f(x) = "
        # kreator komunikatu
        msg = msgbox(dt_text + output, title)
        
        ev = TryEvaluate(output)
        if (ev == True):
            test = True

    wielomian = output
    
    wykres_1(wielomian)

    return wielomian


def wprowadz_wielomian_sprawdz():
    test = False
    while test == False:
        # operatory()
        # wyświetlana wiadomość
        text = "Podaj funkcję f(x) = "
        # tytuł okna
        title = "Sprawdzanie funkcji"
        # tekst domyślny wewnątrz okna wprowadzania
        d_text = "Wprowadź funkcję tu..."
        # kreator okna wprowadzania
        output = str(enterbox(text, title, d_text))
        # tytuł okna
        title = "Wprowadziłeś funkcję: "
        # tekst domyślny wewnątrz okna wprowadzania
        dt_text = "f(x) = "
        # kreator komunikatu
        msg = msgbox(dt_text + output, title)
        
        ev = TryEvaluate(output)
        if (ev == True):
            test = True

    wielomian = output
    wykres_2(wielomian)

    return wielomian


def operatory():
    operatory = np.array([['+', 'Suma, symbol dodatni', 'x + y'],
                          ['–', 'Różnica, symbol ujemny', 'x – y'],
                          ['*', 'Iloczyn', 'x * y'],
                          ['/', 'Iloraz', 'x / y'],
                          ['%', 'Modulo – reszta z dzielenia', 'x % y'],
                          ['//', 'Dzielenie całkowite', 'x // y'],
                          ['**', 'Potęga', 'x ** y'],
                          ['acos', 'Zwraca arcus cosinus argumentu x', 'acos(x)'],
                          ['asin', 'Zwraca arcus sinus argumentu x', 'asin(x)'],
                          ['atan', 'Zwraca arcus tangens argumentu x', 'atan(x)'],
                          ['atan2', 'Zwraca wartość atan(y / x)', 'atan2(y, x)'],
                          ['ceil',
                           'Zwraca najmniejszą liczbę całkowitą nie mniejszą od argumentu x w postaci liczby zmiennoprzecinkowej',
                           'ceil(x)'],
                          ['cos', 'Zwraca cosinus argumentu x', 'cos(x)'],
                          ['tanh', 'Zwraca tangens hiperboliczny argumentu x', 'tanh(x)']])
    info = "Używaj operatory języka python:"
    df = pd.DataFrame(data=operatory, index=None, columns=["OPERATOR", "OPIS", "UŻYCIE"])
    tk.showinfo(info, df)


def wielomian(function, x):
    return eval(function, {"x": x})


def pochodna_wielomianu(function, x):
    dx = 0.1  # Rozmiar elementarnego przesunięcia
    f_x1 = eval(function)
    x += dx
    f_x2 = eval(function)
    poch = (f_x2 - f_x1) / dx
    return poch


def wykres_1(function):
    # okno menue Tkinter
    window = Toplevel()

    # tytuł okna menue Tkinter
    window.title('Wykres funkcji')

    # rozmiar okna menue Tkinter
    window.geometry("800x600")

    # WYKRES!!!
    x = {}  # słownik wartości
    x = py.arange(-50, 50.2, 0.2)  # lista argumentów x
    y = []  # lista wartości
    for i in x:
        y.append(wielomian(function, i))  # lista argumentów y
    fig = plt.figure()
    ax = fig.add_subplot(111)
    yticks = np.arange(-10, 11, 2)
    yrange = (yticks[0], yticks[-1])
    ax.set_yticks(yticks)
    ax.set_ylim(yrange)
    ax.grid(True)  # włącza wyświetlanie pomocniczej
    fontsizes = itertools.cycle([8, 16, 24, 32])
    ax.set_xlabel('Oś X', fontsize=next(fontsizes))
    ax.set_ylabel('Oś Y', fontsize=next(fontsizes))
    ax.set_title('Wykres f(x) = ' + str(function) + '\n', fontsize=next(fontsizes))
    ax.plot(x, y, color='red', linewidth=2, alpha=0.2)
    # tworzenie Tkinter canvas
    # osadzanie figury Matplotlib
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()
    # umieszczenie canvas na oknie Tkinter
    canvas.get_tk_widget().pack()
    # tworzenie paska narzędzi Matplotlib
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
    # umieszczenie paska narzędzi w oknie Tkinter
    canvas.get_tk_widget().pack()


def wykres_2(function):
    # okno menue Tkinter
    window = Toplevel()

    # tytuł okna menue Tkinter
    window.title('Wykres funkcji')

    # rozmiar okna menue Tkinter
    window.geometry("800x600")

    # WYKRES!!!
    x = {}  # słownik wartości
    x = py.arange(-50, 50.2, 0.2)  # lista argumentów x
    y = []  # lista wartości
    for i in x:
        y.append(wielomian(function, i))  # lista argumentów y
    fig = plt.figure()
    ax = fig.add_subplot(111)
    yticks = np.arange(-100, 110, 10)
    yrange = (yticks[0], yticks[-1])
    ax.set_yticks(yticks)
    ax.set_ylim(yrange)
    ax.grid(True)  # włącza wyświetlanie pomocniczej
    fontsizes = itertools.cycle([8, 16, 24, 32])
    ax.set_xlabel('Oś X', fontsize=next(fontsizes))
    ax.set_ylabel('Oś Y', fontsize=next(fontsizes))
    ax.set_title('Wykres f(x) = ' + str(function) + '\n', fontsize=next(fontsizes))
    ax.plot(x, y, color='red', linewidth=2, alpha=0.2)
    # tworzenie Tkinter canvas
    # osadzanie figury Matplotlib
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()
    # umieszczenie canvas na oknie Tkinter
    canvas.get_tk_widget().pack()
    # tworzenie paska narzędzi Matplotlib
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
    # umieszczenie paska narzędzi w oknie Tkinter
    canvas.get_tk_widget().pack()


def wykres_bisekcji(function, a0, b0, x0):
    # okno menue Tkinter
    window1 = Toplevel()
    # tytuł okna menue Tkinter
    window1.title('Wykres funkcji')

    # rozmiar okna menue Tkinter
    window1.geometry("800x600")
    # WYKRES!!!
    x = []  # lista wartości
    x = py.arange(-10, 10.2, 0.2)  # lista argumentów x
    # print(x)
    y = []  # lista wartości
    for i in x:
        y.append(wielomian(function, i))  # lista argumentów y

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.plot(x, y, '-', color='red', linewidth=2, alpha=0.2, label="Wykres wielomianu")

    x_a_b = []
    x_a_b = a0 + b0
    y_a_b = []  # lista wartości
    for i in x_a_b:
        y_a_b.append(wielomian(function, i))  # lista argumentów y

    line2 = ax.plot(x_a_b, y_a_b, 'ro', label="Wykres przedziału: a = " + str(a0[0]) + ", b = " + str(b0[0]) + "\n" + "Miejsce zerowe to: " + str(x0))

    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    yticks = np.arange(-10, 11, 2)
    yrange = (yticks[0], yticks[-1])
    ax.set_yticks(yticks)
    ax.set_ylim(yrange)
    ax.grid(True)  # włącza wyświetlanie pomocniczej
    fontsizes = itertools.cycle([8, 16, 24, 32])
    ax.set_xlabel('Oś X', fontsize=next(fontsizes))
    ax.set_ylabel('Oś Y', fontsize=next(fontsizes))
    ax.set_title('Wykres f(x) = ' + str(function) + '\n', fontsize=next(fontsizes))
    # tworzenie Tkinter canvas
    # osadzanie figury Matplotlib
    canvas = FigureCanvasTkAgg(fig,
                               master=window1)
    canvas.draw()
    # umieszczenie canvas na oknie Tkinter
    canvas.get_tk_widget().pack()
    # tworzenie paska narzędzi Matplotlib
    toolbar = NavigationToolbar2Tk(canvas,
                                   window1)
    toolbar.update()
    # umieszczenie paska narzędzi w oknie Tkinter
    canvas.get_tk_widget().pack()


def wykres_siecznych(function, a0, b0, x0):
    # okno menue Tkinter
    window1 = Toplevel()
    # tytuł okna menue Tkinter
    window1.title('Wykres funkcji')

    # rozmiar okna menue Tkinter
    window1.geometry("800x600")
    # WYKRES!!!
    x = []  # lista wartości
    x = py.arange(-10, 10.2, 0.2)  # lista argumentów x
    # print(x)
    y = []  # lista wartości
    for i in x:
        y.append(wielomian(function, i))  # lista argumentów y

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.plot(x, y, '-', color='red', linewidth=2, alpha=0.2, label="Wykres wielomianu")

    x_a_b = []
    x_a_b = a0 + b0
    y_a_b = []  # lista wartości
    for i in x_a_b:
        y_a_b.append(wielomian(function, i))  # lista argumentów y

    line2 = ax.plot(x_a_b, y_a_b, 'ro', label="Wykres przedziału: a = " + str(a0[0]) + ", b = " + str(b0[0]) + "\n" + "Miejsce zerowe to: " + str(x0))

    x_siecz = []
    y_siecz = []
    ite = len(a0) - 1
    
    while (ite >= 0):
        x_siecz.append(a0[ite])
        x_siecz.append(b0[ite])
        for k in x_siecz:
            y_siecz.append(wielomian(function, k))  # lista argumentów y
        ite-=1
        line3 = ax.plot(x_siecz, y_siecz, 'b-', label="Wykres siecznch")
        x_siecz = []
        y_siecz = []
    
    lns = line1 + line2 + line3
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    yticks = np.arange(-10, 11, 2)
    yrange = (yticks[0], yticks[-1])
    ax.set_yticks(yticks)
    ax.set_ylim(yrange)
    ax.grid(True)  # włącza wyświetlanie pomocniczej
    fontsizes = itertools.cycle([8, 16, 24, 32])
    ax.set_xlabel('Oś X', fontsize=next(fontsizes))
    ax.set_ylabel('Oś Y', fontsize=next(fontsizes))
    ax.set_title('Wykres f(x) = ' + str(function) + '\n', fontsize=next(fontsizes))
    # tworzenie Tkinter canvas
    # osadzanie figury Matplotlib
    canvas = FigureCanvasTkAgg(fig,
                               master=window1)
    canvas.draw()
    # umieszczenie canvas na oknie Tkinter
    canvas.get_tk_widget().pack()
    # tworzenie paska narzędzi Matplotlib
    toolbar = NavigationToolbar2Tk(canvas,
                                   window1)
    toolbar.update()
    # umieszczenie paska narzędzi w oknie Tkinter
    canvas.get_tk_widget().pack()


def wykres_Newtona(function, a0, b0, x0, x_siecz, y_siecz):
    # okno menue Tkinter
    window1 = Toplevel()
    # tytuł okna menue Tkinter
    window1.title('Wykres funkcji')

    # rozmiar okna menue Tkinter
    window1.geometry("800x600")
    # WYKRES!!!
    x = []  # lista wartości
    x = py.arange(-10, 10.2, 0.2)  # lista argumentów x
    # print(x)
    y = []  # lista wartości
    for i in x:
        y.append(wielomian(function, i))  # lista argumentów y

    x_a_b = []
    x_a_b = py.arange(a0, b0, 0.1)
    np.append(x_a_b, a0)
    np.append(x_a_b, b0)
    y_a_b = []  # lista wartości
    for i in x_a_b:
        y_a_b.append(wielomian(function, i))  # lista argumentów y

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.plot(x, y, '-', color='red', linewidth=2, alpha=0.2, label="Wykres wielomianu, gdzie: " + "punkt startowy = " + str(a0) + ", iteracje = " + str(b0) + "\n" + "Miejsce zerowe to: " + str(
                        x0))
 
    line2 = ax.plot(x_siecz, y_siecz, 'go', label="Wykres siecznch")
  
    lns = line1 + line2
    
    
    
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    yticks = np.arange(-10, 11, 2)
    yrange = (yticks[0], yticks[-1])
    ax.set_yticks(yticks)
    ax.set_ylim(yrange)
    ax.grid(True)  # włącza wyświetlanie pomocniczej
    fontsizes = itertools.cycle([8, 16, 24, 32])
    ax.set_xlabel('Oś X', fontsize=next(fontsizes))
    ax.set_ylabel('Oś Y', fontsize=next(fontsizes))
    ax.set_title('Wykres f(x) = ' + str(function) + '\n', fontsize=next(fontsizes))
    # tworzenie Tkinter canvas
    # osadzanie figury Matplotlib
    canvas = FigureCanvasTkAgg(fig,
                               master=window1)
    canvas.draw()
    # umieszczenie canvas na oknie Tkinter
    canvas.get_tk_widget().pack()
    # tworzenie paska narzędzi Matplotlib
    toolbar = NavigationToolbar2Tk(canvas,
                                   window1)
    toolbar.update()
    # umieszczenie paska narzędzi w oknie Tkinter
    canvas.get_tk_widget().pack()


def check_user(username, password):
    query = 'SELECT * FROM login WHERE username = ? AND password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    return result


def Login(timeout_ms: int = 5000):  
    message = "Wprowadź nazwę użytkownika i hasło"
    title = "Login"
    fieldnames = ["Nazwa użytkownika", "Hasło"]
    field = []
    field = multpasswordbox(message, title, fieldnames)
    if field[0] == 's154509' and field[1] == 's154509':
        tk.showinfo("Logowanie do programu", "Zalogowałeś się pomyślnie")
        metodmainwindow()
    elif check_user(field[0], field[1]):
        tk.showinfo("Logowanie do programu", "Zalogowałeś się pomyślnie")
        metodmainwindow()        
    else:
        tk.showerror("Informacja o błędzie", "Nieprawidłowa nazwa użytkownika lub hasło")


def metoda_siecznych():
    # Obliczanie pierwiastka funkcji - metoda siecznych
    function = wprowadz_wielomian()
    a, b = inputBlock(1)

    x_a = []
    x_b = []
    x_0 = []
    x_a.append(a)
    x_b.append(b)
    
    f1 = wielomian(function, a)
    f2 = wielomian(function, b)
    i = 64
    while (i and (fabs(a - b) > dwsqrt)):
        if (fabs(a - b) < dpz0):
            tk.showerror("Informacja o błędzie", "Złe punkty startowe.")
            i = 0
            break
        x0 = a - f1 * (a - b) / (f1 - f2)
        x_0.append(x0)
        f0 = wielomian(function, x0)
        if (fabs(f0) < dpz0): break
        b = a
        x_b.append(b)
        f2 = f1
        a = x0
        x_a.append(a)
        f1 = f0
        i = i - 1
        if (i == 0): tk.showerror("Informacja o błędzie",
                                  "Przekroczony limit obiegow")  # print("Przekroczony limit obiegow\n")
    if (i):
        x0 = round(x0, 9)

        df = pd.DataFrame(columns=['Przedział a', 'Przedział b', 'Przybliżenie'])
        df['Przedział a'] = pd.Series(x_a)
        df['Przedział b'] = pd.Series(x_b)
        df['Przybliżenie'] = pd.Series(x_0)

        tk.showinfo("Miejsce zerowe", "Miejsce zerowe funkcji to: " + str(x0) + "\n i" + str(df))

        wykres_siecznych(function, x_a, x_b, x0)


def metoda_falszywej_prostej():
    # Obliczanie pierwiastka funkcji - metoda regula falsi
    function = wprowadz_wielomian()
    a, b = inputBlock(2)

    a0 = a
    b0 = b
    f_a = wielomian(function, a)
    f_b = wielomian(function, b)
    x1 = a
    x0 = b
    
    x_a = []
    x_b = []
    x_0 = []
    x_a.append(a)
    x_b.append(b)
    
    if (f_a * f_b > 0):
        tk.showerror("Informacja o błędzie", "Funkcja nie spelnia zalozen.")
    else:
        while (fabs(x1 - x0) > dwsqrt):
            x1 = x0
            x0 = a - f_a * (b - a) / (f_b - f_a)
            x_0.append(x0)
            f0 = wielomian(function, x0)
            if (fabs(f0) < dpz0): break
            if (f_a * f0 < 0):
                b = x0
                x_a.append(a)
                x_b.append(b)
                f_b = f0
            else:
                a = x0
                x_a.append(a)
                x_b.append(b)
                f_a = f0
        x0 = round(x0, 9)
        
        df = pd.DataFrame(columns=['Przedział a', 'Przedział b', 'Przybliżenie'])
        df['Przedział a'] = pd.Series(x_a)
        df['Przedział b'] = pd.Series(x_b)
        df['Przybliżenie'] = pd.Series(x_0)

        tk.showinfo("Miejsce zerowe", "Miejsce zerowe funkcji to: " + str(x0) + "\n i" + str(df))

        wykres_siecznych(function, x_a, x_b, x0) # wykres wspólny dla metody fałszywej prostej i metody siecznych


def metoda_Newtona():
    # Obliczanie pierwiastka funkcji - metoda Newtona
    function = wprowadz_wielomian()
    a = inputBlock(4)
    
    x_0 = []
    x_1 = []
    f_0 = []
    f_1 = []
    
    x0 = a
    x_1.append(x0)
    
    x1 = x0 - 1
    f0 = wielomian(function, x0)
    f_0.append(f0)
    i = 64
    while (i and (fabs(x1 - x0) > dwsqrt) and (fabs(f0) > dpz0)):
        f1 = pochodna_wielomianu(function, x0)
        f_1.append(f1)
        if (fabs(f1) < dpz0):
            tk.showerror("Informacja o błędzie", "Zly punkt startowy")
            i = 0
            break
        x1 = x0
        x0 = x0 - f0 / f1
        x_0.append(x0)
        x_1.append(x0)
        f0 = wielomian(function, x0)
        f_0.append(f0)

        i = i - 1
        if (i == 0): tk.showerror("Informacja o błędzie", "Przekroczony limit obiegow")
    if (i):
        x0 = round(x0, 9)

        df = pd.DataFrame(columns=['pkt_start', 'wart_fun', 'wart_poch', 'przybliżenie'])
        df['pkt_start'] = pd.Series(x_1)
        df['wart_fun'] = pd.Series(f_0)
        df['wart_poch'] = pd.Series(f_1)
        df['przybliżenie'] = pd.Series(x_0)
        pd.set_option('display.colheader_justify', 'center')
        txt = df.to_string(justify='center')
        txt.center(22, " ")
        tk.showinfo("Miejsce zerowe", "Miejsce zerowe funkcji to: " + str(x0) + "\n i  " + txt)        

        iteracje = 64 - i
        wykres_Newtona(function, a, iteracje, x0, x_1, f_0)


def metoda_bisekcji():
    # Obliczanie pierwiastka funkcji - metoda bisekcji!
    function = wprowadz_wielomian()
    a, b = inputBlock(3)

    x_a = []
    x_b = []
    x_0 = []
    x_a.append(a)
    x_b.append(b)
    
    
    f_a = wielomian(function, a)
    f_b = wielomian(function, b)
    if (f_a * f_b >= 0):
        tk.showerror("Informacja o błędzie", "Funkcja nie spełnia założeń.")
    else:
        while (fabs(a - b) > dwsqrt):
            x0 = (a + b) / 2
            x_0.append(x0)
            f0 = wielomian(function, x0)
            if (fabs(f0) < dpz0): break
            if (f_a * f0 < 0):
                b = x0
                x_b.append(b)
                x_a.append(a)
            else:
                a = x0
                x_a.append(a)
                x_b.append(b)
                f_a = f0
        x0 = round(x0, 9)

        df = pd.DataFrame(columns=['Przedział a', 'Przedział b', 'Przybliżenie'])
        df['Przedział a'] = pd.Series(x_a)
        df['Przedział b'] = pd.Series(x_b)
        df['Przybliżenie'] = pd.Series(x_0)

        tk.showinfo("Miejsce zerowe", "Miejsce zerowe funkcji to: " + str(x0) + "\n i" + str(df))

        wykres_bisekcji(function, x_a, x_b, x0)


def sprawdz_funkcje():
    function = wprowadz_wielomian_sprawdz()


def metodmainwindow():
    metodymainwindow = Toplevel()
    root.withdraw()
    metodymainwindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(metodymainwindow, image=filename)

    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)

    LoginLabel = Label(metodymainwindow, text="Wybierz metodę numerycznego przybliżania miejsc zerowych funkcji:",
                       bd=12, relief=GROOVE, fg="White", bg="blue",
                       font=("Calibri", 22, "bold"), pady=3)
    LoginLabel.pack(fill=X)

    MetodaFalszywejProstej = Button(metodymainwindow, text='Metoda falszywej prostej', command=metoda_falszywej_prostej,
                                    bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                                    font=("Calibri", 36, "bold"), pady=3)
    MetodaFalszywejProstej['font'] = BtnFont
    MetodaFalszywejProstej.pack(fill=X)

    MetodaSiecznych = Button(metodymainwindow, text='Metoda siecznych', command=metoda_siecznych, bd=12, relief=GROOVE,
                             fg="blue", bg="#ffffb3",
                             font=("Calibri", 36, "bold"), pady=3)
    MetodaSiecznych['font'] = BtnFont
    MetodaSiecznych.pack(fill=X)

    MetodaBisekcji = Button(metodymainwindow, text='Metoda bisekcji', command=metoda_bisekcji, bd=12, relief=GROOVE,
                            fg="blue", bg="#ffffb3",
                            font=("Calibri", 36, "bold"), pady=3)
    MetodaBisekcji['font'] = BtnFont
    MetodaBisekcji.pack(fill=X)

    MetodaNewtona = Button(metodymainwindow, text='Metoda Newtona', command=metoda_Newtona, bd=12, relief=GROOVE,
                           fg="blue", bg="#ffffb3",
                           font=("Calibri", 36, "bold"), pady=3)
    MetodaNewtona['font'] = BtnFont
    MetodaNewtona.pack(fill=X)

    SprawdzFunkcje = Button(metodymainwindow, text='Sprawdź funkcję', command=sprawdz_funkcje, bd=12, relief=GROOVE,
                            fg="blue", bg="#ffffb3",
                            font=("Calibri", 36, "bold"), pady=3)
    SprawdzFunkcje['font'] = BtnFont
    SprawdzFunkcje.pack(fill=X)


    LogoutBtn = Button(metodymainwindow, text='Zamknij', command=metodymainwindow.destroy, bd=12, relief=GROOVE,
                       fg="red",
                       bg="#ffffb3",
                       font=("Calibri", 36, "bold"), pady=3)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    MetodaFalszywejProstej.pack()
    MetodaSiecznych.pack()
    MetodaBisekcji.pack()
    MetodaNewtona.pack()
    ExitBtn.pack()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

root = Tk()
root.wm_attributes('-fullscreen', '1')
root.title("Wybrane metody numeryczne przybliżania miejsc zerowych funkcji !!!")
root.iconbitmap(default='logo.ico')
filename = PhotoImage(file="background.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
BtnFont = Font(family='Calibri(Body)', size=20)
MainLabel = Label(root, text="Wybrane metody numeryczne przybliżania miejsc zerowych funkcji!", bd=12, relief=GROOVE,
                  fg="White", bg="blue",
                  font=("Calibri", 22, "bold"), pady=3)
MainLabel.pack(fill=X)
im = PhotoImage(file='login.gif')

LgnBtn = Button(root, text='Wejdź', bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                font=("Calibri", 36, "bold"), pady=3, command=Login)
LgnBtn['font'] = BtnFont
LgnBtn.pack(fill=X)

ExitBtn = Button(root, text='Zamknij', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                 font=("Calibri", 36, "bold"), pady=3)
ExitBtn['font'] = BtnFont
ExitBtn.pack(fill=X)

MainLabel.pack()
LgnBtn.pack()
ExitBtn.pack()

root.mainloop()