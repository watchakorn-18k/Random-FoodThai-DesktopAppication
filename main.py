import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import threading
import os


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.SetConfigure()
        self.ShowImage("Main")
        self.TextShow()
        self.ShowButton()

    def SetConfigure(self):
        # configure the root window
        self.title('โปรแกรมสุ่มอาหาร')
        self.geometry('300x350')
        self.resizable(False, False)

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
            self, text='ไม่รู้จะกินอะไรลองกดสุ่มอาหารดูสิ!', font=(None, 13))
        self.labelNameFood.grid(row=1, column=0,)

    def ShowButton(self):
        # button
        self.button = Button(
            self, text='กดเพื่อสุ่มอาหาร', font=font.Font(size=15))
        self.button['command'] = self.button_clicked
        self.button.grid(row=4, column=0,)

    def button_clicked(self):
        threading.Thread(target=self.RandomFood).start()

    def RandomFood(self):
        import random as rd
        import time
        self.MenuFile = open("MenuName.txt", "r", encoding="utf-8")
        self.MenuFile = self.MenuFile.read()
        self.MenuList = []
        self.MenuFile = self.MenuFile.split()
        self.labelNameFood['font'] = (None, 15)
        for i, value in enumerate(self.MenuFile):
            self.MenuList.append(value)
            print(i)
            self.ShowImage(i)
            time.sleep(0.01)
            self.labelNameFood['text'] = value

        self.AfterRandomFood = rd.choice(self.MenuList)
        for index, word in enumerate(self.MenuList):
            if word == self.AfterRandomFood:
                self.ShowImage(index)

        self.labelNameFood['text'] = self.AfterRandomFood
        print(self.AfterRandomFood)


if __name__ == "__main__":
    app = App()
    app.mainloop()
