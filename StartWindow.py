import tkinter as tk
from tkinter import messagebox

from Autoryzacja import Autoryzacja


class StartWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.geometry("{}x{}".format(400,150))
        self.master.title("Trójbój Siłowy")
        self.create_widgets()


    def create_widgets(self):
        self.start = tk.Button(self.master)
        self.start["text"] = u"START"
        self.start["command"] = self.start_


        self.pomoc = tk.Button(self.master)
        self.pomoc["text"] = u"O Programie"
        self.pomoc["command"] = self.pomoc_

        self.start.grid(row=0, column=0,padx=150,pady=20)
        self.pomoc.grid(row=1,column=0,padx=150)

    def start_(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Autoryzacja(root)
        self.child.mainloop()
    def pomoc_(self):
        messagebox.showinfo("Pomoc!","Aplikacja przeznaczona dla zawodników sportów siłowych\n"
                                     "W tym najbardziej dla Zawodników Trójboju Siłowego\n"
                                     "Pozwala ona na dokumentacje postępów - wagi oraz wyników\n"
                                     "A także na weryfikację ww. postępów - przy pomocy wykresów\n"
                                     "Zarejestruj się lub jeśli już posiadasz konto zaloguj się\n"
                                     "          Miłej Zabawy!")