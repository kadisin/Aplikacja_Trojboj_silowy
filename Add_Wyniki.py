import tkinter as tk
from tkinter import messagebox

from pymysql import IntegrityError

import User
import Main_Window
import pymysql
import datetime

class Add_Wyniki(tk.Frame):

    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.__user = user
        self.master.geometry("{}x{}".format(430,460))
        self.master.title("Dodaj Wyniki")
        self.create_widgets()



    def create_widgets(self):
        self.napis_przysiad = tk.Label(self.master, text="Podaj Przysiad[kg]:",width=15,height=3)
        self.napis_przysiad_enter = tk.Entry(self.master,bd=5)

        self.napis_wyciskanie = tk.Label(self.master, text="Podaj WL[kg]:", width=15, height=3)
        self.napis_wyciskanie_enter = tk.Entry(self.master, bd=5)

        self.napis_martwy = tk.Label(self.master, text="Podaj Martwy Ciag[kg]:", width=20, height=3)
        self.napis_martwy_enter = tk.Entry(self.master, bd=5)


        self.dzien = tk.IntVar()
        self.data_dzien = tk.Spinbox(self.master, from_=1, to=31, textvariable = self.dzien)

        self.miesiac = tk.IntVar()
        self.data_miesiac = tk.Spinbox(self.master, from_=1, to=12, textvariable =self.miesiac)

        self.rok = tk.IntVar()
        self.data_rok = tk.Spinbox(self.master, from_=2000, to=2030, textvariable =self.rok)

        self.napis_dzien = tk.Label(self.master, text="Podaj dzien:",width=10,height=3,padx=3)
        self.napis_miesiac = tk.Label(self.master, text="Podaj miesiac:",width=10,height=3,padx=15)
        self.napis_rok = tk.Label(self.master, text="Podaj rok:",width=10,height=3,padx=3)


        self.ok_button = tk.Button(self.master,padx=30,pady=10)
        self.back_button = tk.Button(self.master,padx=30,pady=10)

        self.ok_button["text"] = "Zapisz"
        self.back_button["text"] = "Powrot"

        self.ok_button["command"] = self.wyslij
        self.back_button["command"] = self.cofnij



        self.napis_przysiad.grid(row=0,column=0)
        self.napis_przysiad_enter.grid(row=0,column=1)

        self.napis_wyciskanie.grid(row=1,column=0)
        self.napis_wyciskanie_enter.grid(row=1,column=1)

        self.napis_martwy.grid(row=2,column=0)
        self.napis_martwy_enter.grid(row=2,column=1)


        self.napis_dzien.grid(row=3,column=0)
        self.data_dzien.grid(row=3,column=1)

        self.napis_miesiac.grid(row=4,column=0)
        self.data_miesiac.grid(row=4,column=1)

        self.napis_rok.grid(row=5,column=0)
        self.data_rok.grid(row=5,column=1)

        self.back_button.grid(row=6,column=0,padx=50)
        self.ok_button.grid(row=6,column=1)


    def wyslij(self):

        connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
        cursor = connection.cursor()

        if (self.napis_przysiad_enter.get() == "" and self.napis_wyciskanie_enter.get() == "" and self.napis_martwy_enter.get() == ""):
            messagebox.showerror("Bład!", "Wszystkie pola nie mogą być puste!")
            self.master.destroy()
            root = tk.Tk()
            app = Main_Window.Main_Window(self.__user, master=root)
            app.mainloop()



        self.__przysiad = self.napis_przysiad_enter.get()
        self.__wyciskanie = self.napis_wyciskanie_enter.get()
        self.__martwy = self.napis_martwy_enter.get()

        if(self.__przysiad.isdigit() == False and self.__przysiad != ""):
            messagebox.showerror("Bład!", "Pole przysiad musi być liczbą!")
            self.master.destroy()
            root = tk.Tk()
            app = Add_Wyniki(self.__user, master=root)
            app.mainloop()
        if (self.__wyciskanie.isdigit() == False and self.__wyciskanie != ""):
            messagebox.showerror("Bład!", "Pole wyciskanie musi być liczbą!")
            self.master.destroy()
            root = tk.Tk()
            app = Add_Wyniki(self.__user, master=root)
            app.mainloop()
        if (self.__martwy.isdigit() == False and self.__martwy != ""):
            messagebox.showerror("Bład!", "Pole martwy ciąg musi być liczbą!")
            self.master.destroy()
            root = tk.Tk()
            app = Add_Wyniki(self.__user, master=root)
            app.mainloop()

        date = datetime.datetime(self.rok.get(),self.miesiac.get(),self.dzien.get())

        if (date > datetime.datetime.now()):
            messagebox.showerror("Bład!", "Data nie może być przyszła!")
            self.master.destroy()
            root = tk.Tk()
            app = Add_Wyniki(self.__user, master=root)
            app.mainloop()


        #INSERT INTO `results` VALUES (NULL,'2','2021-03-01','200','100','300');

        insert = "INSERT INTO `results` VALUES (NULL, '" + str(self.__user.get_id()) + "' , '" + \
                   str(date) + "' , '" + str(self.__przysiad) + "' , '" + str(self.__wyciskanie) + \
                    "' , '" + str(self.__martwy) + "');"

        try:
            cursor.execute(insert)
        except IntegrityError:
            messagebox.showerror("Bład!","Data została powtórzona!")
            self.master.destroy()
            root = tk.Tk()
            app = Add_Wyniki(self.__user,master=root)
            app.mainloop()

        connection.commit()
        connection.close()

        messagebox.showinfo("Sukces!","Pomyslnie dodano wartosc!")
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()



    def cofnij(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Main_Window.Main_Window(self.__user,master=root)
        self.child.mainloop()



def main():
    u = User.User(1,"","","","","")
    root = tk.Tk()
    ap = Add_Wyniki(u,master=root)
    ap.mainloop()


if __name__ == "__main__":
    main()