# -*- coding: UTF-8 -*-
import tkinter as tk
import datetime
import pandas as pd
from PIL import Image, ImageTk
import pygame
from hijri_converter import convert
from time import strftime

class Clock:
    def __init__(self,root):
        self.Adan_time = []
        self.upper_frame = tk.Frame(root, background="black")
        self.lower_frame = tk.Frame(root, background="orange")
        self.bottom_frame = tk.Frame(root, background="dark red")

        self.current_time = tk.Label(
            self.upper_frame, font=('calibri', 40, 'bold'),
            background="black",
            relief="solid",
            foreground='white',
            borderwidth=5)

        self.current_date = tk.Label(
            self.upper_frame, font=('calibri', 20, 'bold'),
            background="black",
            foreground='white', )

        self.hijri_date = tk.Label(
            self.upper_frame, font=('calibri', 20, 'bold'),
            background="black",
            foreground='white', )

        self.prayer = tk.Label(
            self.lower_frame, text="Prayer", font=('calibri', 35, 'bold'),
            background="orange",
            foreground='white', )

        self.begining = tk.Label(
            self.lower_frame, text="Begining", font=('calibri', 35, 'bold'),
            background="orange",
            foreground='white', )

        self.jamat = tk.Label(
            self.lower_frame, text="Jamat", font=('calibri', 35, 'bold'),
            background="orange",
            foreground='white', )

        self.fajr = tk.Label(
            self.lower_frame, text="الفجر", font=('times', 25, 'bold'),
            background="orange",
            foreground='white')
        self.fajr_begining_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.fajr_jamat_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.dhur = tk.Label(
            self.lower_frame, text="الظُهر", font=('times', 25, 'bold'),
            background="orange",
            foreground='white')
        self.dhur_begining_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.dhur_jamat_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.asar = tk.Label(
            self.lower_frame, text="العصر", font=('times', 25, 'bold'),
            background="orange",
            foreground='white')
        self.asar_begining_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.asar_jamat_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.maghrib = tk.Label(
            self.lower_frame, text="المغرب", font=('times', 25, 'bold'),
            background="orange",
            foreground='white')
        self.maghrib_begining_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.maghrib_jamat_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.isha = tk.Label(
            self.lower_frame, text="العِشاء", font=('times', 25, 'bold'),
            background="orange",
            foreground='white')
        self.isha_begining_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.isha_jamat_time = tk.Label(
            self.lower_frame, font=('calibri', 25, 'bold'),
            background="orange",
            foreground='white', )
        self.shuruq = tk.Label(
            self.bottom_frame, text="الشروق", font=('times', 25, 'bold'),
            background="dark red",
            foreground='white')
        self.shuruq_label_time = tk.Label(
            self.bottom_frame, font=('calibri', 25, 'bold'),
            background="dark red",
            foreground='white', )
        self.dhuha = tk.Label(
            self.bottom_frame, text="الضحى", font=('times', 25, 'bold'),
            background="dark red",
            foreground='white')
        self.dhuha_label_time = tk.Label(
            self.bottom_frame, font=('calibri', 25, 'bold'),
            background="dark red",
            foreground='white', )
        # Placing clock at the centre
        # # of the tkinter window

        self.upper_frame.place(relx=0.0, rely=0.01, relwidth=1, relheight=0.12)
        self.lower_frame.place(relx=0.0, rely=0.13, relwidth=1, relheight=0.7)
        self.bottom_frame.place(relx=0.0, rely=0.82, relwidth=1, relheight=0.22)

        self.current_time.place(relx=0.48, rely=0.5, anchor=tk.CENTER)
        self.current_date.place(relx=0.01, rely=0.5, anchor=tk.W)
        self.hijri_date.place(relx=0.98, rely=0.5, anchor=tk.E)
        self.prayer.place(relx=0.09, rely=0.05, anchor=tk.CENTER)
        self.begining.place(relx=0.39, rely=0.05, anchor=tk.W)
        self.jamat.place(relx=0.93, rely=0.05, anchor=tk.E)
        self.fajr.place(relx=0.05, rely=0.20, anchor=tk.W)
        self.fajr_begining_time.place(relx=0.45, rely=0.20, anchor=tk.CENTER)
        self.fajr_jamat_time.place(relx=0.90, rely=0.20, anchor=tk.E)
        self.dhur.place(relx=0.05, rely=0.35, anchor=tk.W)
        self.dhur_begining_time.place(relx=0.45, rely=0.35, anchor=tk.CENTER)
        self.dhur_jamat_time.place(relx=0.90, rely=0.35, anchor=tk.E)
        self.asar.place(relx=0.05, rely=0.50, anchor=tk.W)
        self.asar_begining_time.place(relx=0.45, rely=0.50, anchor=tk.CENTER)
        self.asar_jamat_time.place(relx=0.90, rely=0.50, anchor=tk.E)
        self.maghrib.place(relx=0.05, rely=0.65, anchor=tk.W)
        self.maghrib_begining_time.place(relx=0.45, rely=0.65, anchor=tk.CENTER)
        self.maghrib_jamat_time.place(relx=0.90, rely=0.65, anchor=tk.E)
        self.isha.place(relx=0.05, rely=0.80, anchor=tk.W)
        self.isha_begining_time.place(relx=0.45, rely=0.80, anchor=tk.CENTER)
        self.isha_jamat_time.place(relx=0.90, rely=0.80, anchor=tk.E)
        self.dhuha.place(relx=0.90, rely=0.25, anchor=tk.E)
        self.dhuha_label_time.place(relx=0.90, rely=0.65, anchor=tk.E)
        self.shuruq.place(relx=0.05, rely=0.25, anchor=tk.W)
        self.shuruq_label_time.place(relx=0.05, rely=0.65, anchor=tk.W)

        self.update_window()
        self.time(root)

    def adan_window(self,root):
        splash_screen = tk.Frame(root, background='#800000')
        splash_screen.place(relwidth=1.0, relheight=1.0)
        load = Image.open("Silent_Mode.jpg")
        new_load = load.resize((500, 500))
        bg = ImageTk.PhotoImage(new_load)
        # Create Canvas
        canvas1 = tk.Canvas(splash_screen, width=500, height=500)
        canvas1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # Display image
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        pygame.mixer.init()
        pygame.mixer.music.load("Adan Makkah.mp3")
        pygame.mixer.music.play(loops=0)
        while pygame.mixer.music.get_busy():
            splash_screen.update()
        else:
            splash_screen.destroy()

    def update_window(self):
        df = pd.read_csv(
            'prayerDataSet.csv')
        # df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')#()
        day_str = strftime('%d')
        month_str = strftime('%m')
        day_int = int(day_str)
        month_int = int(month_str)
        match_date1 = ''
        match_date3 = ''
        match_date4 = ''
        if day_int < 10 and month_int < 10:
            match_date1 = strftime('%d/%m/')
            match_date1 = match_date1.replace('0', '')
            match_date1 += strftime('%Y')
        match_date2 = strftime('%d/%m/%Y')
        if day_int < 10:
            match_date3 = strftime('%d/')
            match_date3 = match_date3.replace('0', '')
            match_date3 += strftime('%m/%Y')
        if month_int < 10:
            match_date4 = strftime('%m')
            match_date4 = strftime('%d/') + match_date4.replace('0', '')
            match_date4 += strftime('/%Y')
        filtered_df = df.loc[
            (df['Date'] == match_date1) |
            (df['Date'] == match_date2) |
            (df['Date'] == match_date3) |
            (df['Date'] == match_date4)]
        filtered_df = filtered_df[["Fajr", "Shuruq", "Dhuha", "Dhuhr", "Asr", "Maghrib", "Isha"]]
        remove_square_bracket = filtered_df.values.tolist()
        self.Adan_time = list(
            [str(remove_square_bracket[0][0]),
             str(remove_square_bracket[0][3]),
             str(remove_square_bracket[0][4]),
             str(remove_square_bracket[0][5]),
             str(remove_square_bracket[0][6])])
        shuruq_time = str(remove_square_bracket[0][1])
        dhuha_time = str(remove_square_bracket[0][2])

        self.dhuha_label_time.config(text=dhuha_time)
        self.shuruq_label_time.config(text=shuruq_time)

        int_num = 0
        str_num = '0'

        self.fajr_begining_time.config(text=self.Adan_time[0])
        if self.Adan_time[0][2:] > '44':
            int_num = int(self.Adan_time[0][:1]) + 1
            str_num = str(int_num)
            int_num = int(self.Adan_time[0][2:]) + 15 - 60
            if int_num < 10:
                str_num = str_num + ":0" + str(int_num)
            else:
                str_num = str_num + ":" + str(int_num)
        else:
            int_num = int(self.Adan_time[0][:1])
            str_num = str(int_num)
            int_num = int(self.Adan_time[0][2:]) + 15
            str_num = str_num + ":" + str(int_num)

        self.fajr_jamat_time.config(text=str_num)

        self.dhur_begining_time.config(text=self.Adan_time[1])
        if self.Adan_time[1][3:] > '44':
            int_num = int(self.Adan_time[1][:2]) + 1
            str_num = str(int_num)
            int_num = int(self.Adan_time[1][3:]) + 15 - 60
            if int_num < 10:
                str_num = str_num + ":0" + str(int_num)
            else:
                str_num = str_num + ":" + str(int_num)
        else:
            int_num = int(self.Adan_time[1][:2])
            str_num = str(int_num)
            int_num = int(self.Adan_time[1][3:]) + 15
            str_num = str_num + ":" + str(int_num)

        self.dhur_jamat_time.config(text=str_num)

        if self.Adan_time[2][:2] > '12':
            int_num = int(self.Adan_time[2][:2]) - 12
            str_num = str(int_num) + self.Adan_time[2][2:]

        self.asar_begining_time.config(text=str_num)

        if self.Adan_time[2][3:] > '44':
            int_num = int(str_num[0]) + 1
            str_num = str(int_num)
            int_num = int(self.Adan_time[2][3:]) + 15 - 60
            if int_num < 10:
                str_num = str_num + ":0" + str(int_num)
            else:
                str_num = str_num + ":" + str(int_num)
        else:
            int_num = int(str_num[0])
            str_num = str(int_num)
            int_num = int(self.Adan_time[2][3:]) + 15
            str_num = str_num + ":" + str(int_num)

        self.asar_jamat_time.config(text=str_num)

        if self.Adan_time[3][:2] > '12':
            int_num = int(self.Adan_time[3][:2]) - 12
            str_num = str(int_num) + self.Adan_time[3][2:]

        self.maghrib_begining_time.config(text=str_num)

        if self.Adan_time[3][3:] > '44':
            int_num = int(str_num[0]) + 1
            str_num = str(int_num)
            int_num = int(self.Adan_time[3][3:]) + 15 - 60
            if int_num < 10:
                str_num = str_num + ":0" + str(int_num)
            else:
                str_num = str_num + ":" + str(int_num)
        else:
            int_num = int(str_num[0])
            str_num = str(int_num)
            int_num = int(self.Adan_time[3][3:]) + 15
            str_num = str_num + ":" + str(int_num)

        self.maghrib_jamat_time.config(text=str_num)

        if self.Adan_time[4][:2] > '12':
            int_num = int(self.Adan_time[4][:2]) - 12
            str_num = str(int_num) + self.Adan_time[4][2:]

        self.isha_begining_time.config(text=str_num)

        if self.Adan_time[4][3:] > '44':
            int_num = int(str_num[0]) + 1
            str_num = str(int_num)
            int_num = int(self.Adan_time[4][3:]) + 15 - 60
            if int_num < 10:
                str_num = str_num + ":0" + str(int_num)
            else:
                str_num = str_num + ":" + str(int_num)
        else:
            int_num = int(str_num[0])
            str_num = str(int_num)
            int_num = int(self.Adan_time[4][3:]) + 15
            str_num = str_num + ":" + str(int_num)

        self.isha_jamat_time.config(text=str_num)

        date_str = strftime('%a %d %b,\n     %Y')
        d = datetime.datetime.now()
        h = convert.Gregorian(d.year, d.month, d.day).to_hijri()
        lst = list(h.datetuple())
        hijri_date_str = str(lst[2]) + str(" ") + str(h.month_name()) + str("\n") + str("     ") + str(lst[0])
        self.current_date.config(text=date_str)
        self.hijri_date.config(text=hijri_date_str)

    def time(self,root):
        time_str = strftime('%I:%M:%S %p')
        longtime_str = strftime('%H:%M:%S %p')

        if time_str[0:5] == "12:00":
            self.update_window()

        self.current_time.config(text=time_str)

        if longtime_str[0:5] in self.Adan_time:
            self.adan_window(root)
            self.update_window()

        self.current_time.after(1000, self.time,root)
    


# creating tkinter window
root = tk.Tk()
# set window size
root.geometry("700x650")
root.minsize(700, 650)
root.title('Clock')    


my_clock = Clock(root)
root.mainloop()
