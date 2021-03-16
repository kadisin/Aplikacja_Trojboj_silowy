import tkinter as tk
from tkinter import messagebox

import Register
import Main_Window
from User import User
from database import check_user_in_base


class Autoryzacja(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("{}x{}".format(400, 200))
        self.master.title("Autoryzacja")
        self.create_widgets()

    def create_widgets(self):
        self.login_1 = tk.Label(self.master, text="Login:")
        self.login_enter = tk.Entry(self.master, bd=5)

        self.password_1 = tk.Label(self.master, text="Password:")
        self.password_enter = tk.Entry(self.master, bd=5)

        self.register = tk.Button(self.master)
        self.register["text"] = u"Rejestracja"

        self.zaloguj = tk.Button(self.master)
        self.zaloguj["text"] = u"Zaloguj sie"

        self.login_1.grid(row=0, column=0, ipadx=50, ipady=20)
        self.login_enter.grid(row=0, column=1)

        self.password_1.grid(row=1, column=0)
        self.password_enter.grid(row=1, column=1)

        self.register.grid(row=2, column=0,padx=30,pady=10)
        self.zaloguj.grid(row=2, column=1,padx=10,pady=10)

        self.register["command"] = self.rejestracja
        self.zaloguj["command"] = self.logowanie

    def rejestracja(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Register.Register(root)
        self.child.mainloop()

    def logowanie(self):

        self.user_login = self.login_enter.get()
        self.user_password = self.password_enter.get()

        #sprawdzic typ uzytkownika ! admin ma lekko inne okno pewnie!

        if(check_user_in_base("SELECT * from user",self.user_login,self.user_password)):
            u = User.get_account(self.user_login,self.user_password)
            if(u[1] == True):
                #print(u[0].get_id())
                self.master.destroy()
                root = tk.Tk()
                self.child = Main_Window.Main_Window(u[0],master=root)
                self.child.mainloop()

            else:
                messagebox.showinfo("Blad!","Niepomyslne logowanie!")