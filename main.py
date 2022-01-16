from cgitb import text
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import os
import pyglet


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.LocalLang = "TH"
        self.SetConfigure()
        self.ShowImage("Main_Img")
        self.TextShow()
        self.ShowButton()
        self.ShowButtonThai()
        self.ShowButtonEng()
        self.wk18K = Label(
            self, text="Dev wk-18k created 2022 Thailand", font=("Sawasdee", 9)).place(x=60, y=400)

    def SetConfigure(self):
        # configure the root window
        self.title('โปรแกรมสุ่มอาหาร')
        self.geometry('300x430')
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.TitleAlert = "อาหารของคุณคือ"
        pyglet.font.add_file("font\Sawasdee.ttf")

    def ShowImage(self, Image_Path):
        self.imageSource = Image.open(f"Image/{Image_Path}.png")
        self.resize_image = self.imageSource.resize((250, 250))
        self.imageDisplay = ImageTk.PhotoImage(self.resize_image)
        self.DisplayImage = ttk.Label(image=self.imageDisplay)
        self.DisplayImage.image = self.imageDisplay
        self.DisplayImage.grid(row=0, column=0, padx=25, pady=10)

    def TextShow(self):
        # label
        self.labelNameFood = ttk.Label(
            self, text='ไม่รู้จะกินอะไรลองกดสุ่มอาหารดูสิ!', font=("Sawasdee", 13), wraplength=300, justify="center")
        self.labelNameFood.grid(row=1, column=0,)

    def ShowButton(self):
        # button
        self.button = Button(
            self, text='กดเพื่อสุ่มอาหาร', font=font.Font(family="Sawasdee", size=11))
        self.button['command'] = self.button_clicked
        self.button.grid(row=4, column=0,)

    def ShowButtonThai(self):
        # button
        photo = Image.open(r"Localization\thai.png")
        resize_image = photo.resize((50, 40))
        photo = ImageTk.PhotoImage(resize_image)
        self.buttonThai = Button(self, image=photo)
        self.buttonThai.image = photo
        self.buttonThai['command'] = self.ChangetoThai
        self.buttonThai.place(x=155, y=350)

    def ShowButtonEng(self):
        # button
        photo = Image.open(r"Localization\eng.png")
        resize_image = photo.resize((50, 40))
        photo = ImageTk.PhotoImage(resize_image)
        self.buttonEng = Button(self, image=photo, command=self.ChangetoEng)
        self.buttonEngimage = photo
        self.buttonEng.place(x=90, y=350)

    def button_clicked(self):
        threading.Thread(target=self.RandomFood).start()

    def RandomFood(self):
        import random as rd
        import time
        if self.LocalLang == "TH":
            self.MenuFile = open("MenuName_TH.txt", "r", encoding="utf-8")
        elif self.LocalLang == "ENG":
            self.MenuFile = open("MenuName_ENG.txt", "r", encoding="utf-8")
        self.MenuFile = self.MenuFile.read()
        self.MenuList = []
        self.MenuFile = self.MenuFile.split()
        self.labelNameFood['font'] = ("Sawasdee", 10)
        self.button["state"] = "disabled"
        for i, value in enumerate(self.MenuFile):
            self.MenuList.append(value)
            print(i)
            self.ShowImage(i)
            time.sleep(0)
            self.labelNameFood['text'] = value

        self.AfterRandomFood = rd.choice(self.MenuList)
        for index, word in enumerate(self.MenuList):
            if word == self.AfterRandomFood:
                self.ShowImage(index)

        self.labelNameFood['text'] = self.AfterRandomFood
        self.button["state"] = "normal"
        print(self.AfterRandomFood)
        messagebox.showinfo(None, f"{self.TitleAlert} {self.AfterRandomFood}")

    def ChangetoThai(self):
        self.button['text'] = "กดเพื่อสุ่มอาหาร"
        self.labelNameFood['text'] = 'ไม่รู้จะกินอะไรลองกดสุ่มอาหารดูสิ!'
        self.button['font'] = font.Font(family="Sawasdee", size=11)
        self.labelNameFood['font'] = ("Sawasdee", 13)
        self.LocalLang = "TH"
        self.title('โปรแกรมสุ่มอาหาร')
        self.ShowImage("Main_Img")
        self.TitleAlert = "อาหารของคุณคือ"

    def ChangetoEng(self):
        self.button['text'] = "Click for Random Food"
        self.button['font'] = font.Font(family="Sawasdee", size=8)
        self.labelNameFood['text'] = """If you don't know what to eat try 
  pressing random food button !"""
        self.labelNameFood['font'] = ("Sawasdee", 8)
        self.LocalLang = "ENG"
        self.title('Random Food Appication')
        self.ShowImage("Main_Img")
        self.TitleAlert = "Your food is"


if __name__ == "__main__":
    app = App()
    app.mainloop()
