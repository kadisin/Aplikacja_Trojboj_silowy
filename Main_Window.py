import tkinter as tk
from tkinter import messagebox

import Add_Waga
import pylab
import User
import database
import Wykresy
import Add_Wyniki
import Autoryzacja
import Delete_Weight
import Delete_Results

from User import User

class Main_Window(tk.Frame):

    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.__user = user
        self.master.geometry("{}x{}".format(500,500))
        self.master.title("Trojboj Silowy - Wyniki")
        self.create_widgets()



    def create_widgets(self):

       #menu test
        self.menu_ = tk.Menu(self.master)

        self.fileMenu = tk.Menu(self.menu_)
        self.menu_.add_cascade(label='Program', menu=self.fileMenu)

        self.fileMenu.add_command(label='Pomoc',command=self.pomoc)
        self.fileMenu.add_command(label='Wyloguj się',command=self.wylogujSie)
        self.fileMenu.add_command(label="Zamknij",command=self.Zamknij)

        self.editMenu = tk.Menu(self.menu_)
        self.menu_.add_cascade(label='Usuń Dane', menu=self.editMenu)
        self.editMenu.add_command(label='Usuń Wagę', command=self.deleteWeight)
        self.editMenu.add_command(label='Usuń Wyniki', command=self.deleteResults)


        self.master.config(menu=self.menu_)
      #/menutest
        self.napis_dodaj_usun = tk.Label(self.master,text= "Dane:")
        self.dodaj_wage_button = tk.Button(self.master,width=20,height=5)
        self.dodaj_wyniki_button = tk.Button(self.master,width=20,height=5)

        self.dodaj_wage_button["text"] = u"Dodaj Wage"
        self.dodaj_wyniki_button["text"] = u"Dodaj Wyniki"


        self.napis_dodaj_usun.grid(row=0,column=0)
        self.dodaj_wage_button.grid(row=1,column=0)
        self.dodaj_wyniki_button.grid(row=2,column=0)

        self.napis_pokaz_wykresy = tk.Label(self.master, text="Pokaz Wykresy:")
        self.waga_wykres = tk.Button(self.master,width=20,height=5)
        self.total_wykres = tk.Button(self.master, width=20, height=5)
        self.pojedyncze_boje = tk.Label(self.master,text="Pojedyncze Boje")
        self.squat_wykres = tk.Button(self.master, width=20, height=5,text="Przysiad",command=self.squatWykres)
        self.bench_wykres = tk.Button(self.master, width=20, height=5,text="Wyciskanie",command=self.benchWykres)
        self.deadlift_wykres = tk.Button(self.master, width=20, height=5,text="Martwy Ciag",command=self.deadliftWykres)

        self.waga_wykres["text"] = u"Waga"
        self.total_wykres["text"] = u"Total"


        self.dodaj_wage_button["command"] = self.dodaj_wage
        self.dodaj_wyniki_button["command"] = self.dodaj_wyniki

        self.waga_wykres["command"] = self.pokazWykresWaga
        self.total_wykres["command"] = self.pokazWykresTotal

        self.napis_pokaz_wykresy.grid(row=0,column=1)
        self.waga_wykres.grid(row=1,column=1)
        self.total_wykres.grid(row=2,column=1)
        self.pojedyncze_boje.grid(row=0,column=2)
        self.squat_wykres.grid(row=1,column=2)
        self.bench_wykres.grid(row=2,column=2)
        self.deadlift_wykres.grid(row=3,column=2)


    def pomoc(self):
        messagebox.showinfo("Pomoc!", "Aplikacja przeznaczona dla zawodników sportów siłowych\n"
                                      "W tym najbardziej dla Zawodników Trójboju Siłowego\n"
                                      "Pozwala ona na dokumentacje postępów - wagi oraz wyników\n"
                                      "A także na weryfikację ww. postępów - przy pomocy wykresów\n"
                                      "Zarejestruj się lub jeśli już posiadasz konto zaloguj się\n"
                                      "          Miłej Zabawy!")
    def wylogujSie(self):
        self.master.destroy()
        root = tk.Tk()
        app = Autoryzacja.Autoryzacja(master=root)
        app.mainloop()
    def Zamknij(self):
        messagebox.showinfo("Zamkniecie!","Pomyślnie zamknięto aplikację")
        self.master.destroy()



    def dodaj_wage(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Add_Waga.Add_Waga(self.__user,master=root)
        self.child.mainloop()

    def dodaj_wyniki(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Add_Wyniki.Add_Wyniki(self.__user,master=root)
        self.child.mainloop()


    def pokazWykresWaga(self):
        list = database.get_weights(self.__user.get_id())

        list_arg = []
        list_wart = []

        #print(list[0][2])
        #   print(list[0][3])
        for index in range(len(list)):
            list_arg.append(list[index][3])
            list_wart.append(list[index][2])
        Wykresy.Wykres_Liniowy(list_arg,list_wart)


    def pokazWykresTotal(self):
        messagebox.showwarning("Uwaga!","Pokazane zostana tylko dane z uzupelnionymi wszystkimi trzema bojami!")
        list = database.get_results(self.__user.get_id())

        list_arg = []
        list_total = []

        for index in range(len(list)):
            list_arg.append(list[index][2])
            total = list[index][3] + list[index][4] + list[index][5]
            list_total.append(total)
        Wykresy.Wykres_Liniowy(list_arg,list_total)

    def squatWykres(self):
        list = database.get_squat(self.__user.get_id())

        list_arg = []
        list_squat = []
        for index in range(len(list)):
            list_arg.append(list[index][2])
            list_squat.append(list[index][3])
        Wykresy.Wykres_Liniowy(list_arg,list_squat)


    def benchWykres(self):
        list = database.get_bench(self.__user.get_id())

        list_arg = []
        list_bench = []
        for index in range(len(list)):
            list_arg.append(list[index][2])
            list_bench.append(list[index][4])
        Wykresy.Wykres_Liniowy(list_arg, list_bench)
    def deadliftWykres(self):
        list = database.get_deadlift(self.__user.get_id())

        list_arg = []
        list_deadlift = []
        for index in range(len(list)):
            list_arg.append(list[index][2])
            list_deadlift.append(list[index][5])
        Wykresy.Wykres_Liniowy(list_arg,list_deadlift)

    def deleteWeight(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Delete_Weight.Delete_Weight(self.__user,master=root)
        self.child.mainloop()


    def deleteResults(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Delete_Results.Delete_Results(self.__user,master=root)
        self.child.mainloop()


def main():
    root = tk.Tk()
    user = User.get_account("tomek2212","tomek2212")
    app = Main_Window(user[0],master=root)
    app.mainloop()


if __name__ == "__main__":
    main()

