import tkinter as tk
from tkinter import messagebox
from User import User
import Main_Window
import database


class Delete_Results(tk.Frame):


    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.master.title("Usuń Pozycje")
        self.master.geometry("{}x{}".format(500,430))
        self.__user = user
        self.create_widgets()


    def create_widgets(self):

        self.list_result = tk.Listbox(self.master,width=55,height=15)
        self.button_powrot = tk.Button(self.master,text="Powrót",command=self.Powrot,width=20,height=2)

        self.button_usun = tk.Button(self.master,text="Usuń",command=self.Usun,width=20,height=2)


        self.list_result.grid(row=0,columnspan=3,padx=40,pady=20)
        self.button_powrot.grid(row=1,column=0)

        self.button_usun.grid(row=1,column=2)


        self.complete_the_list()

    def Powrot(self):
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()


    def Usun(self):
        value = self.list_result.get(self.list_result.curselection())
        database.delete_results(self.__user.get_id(),value[0:10])
        messagebox.showinfo("Sukces","Pomyslnie usunięto wynik!")
        self.master.destroy()
        root = tk.Tk()
        self.child = Main_Window.Main_Window(self.__user,master=root)
        self.child.mainloop()



    def complete_the_list(self):
        self.__list_weight_data = database.get_all_results(self.__user.get_id())
        print(self.__list_weight_data)
        for index in range(len(self.__list_weight_data)):
            str_ =   str(self.__list_weight_data[index][2]) + " | Przysiad: " + str(self.__list_weight_data[index][3]) + " | Wyciskanie: " + str(self.__list_weight_data[index][4]) + " | Martwy Ciąg: " + str(self.__list_weight_data[index][5])
            self.list_result.insert('end',str_)


def main():
    root = tk.Tk()
    user = User.get_account("tomek2212","tomek2212")
    app = Delete_Results(user[0],master=root)
    app.mainloop()


if __name__ == "__main__":
    main()