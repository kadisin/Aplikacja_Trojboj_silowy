from tkinter import messagebox

import pymysql as pymysql
from pymysql import IntegrityError, OperationalError

from database import *


class User:

    def __init__(self,id,login,password,imie,nazwisko,wzrost):
        self.__id = id
        self.__login = login
        self.__password = password
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wzrost = wzrost



    def get_id(self):
        return self.__id

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password


    def save_to_database(self):



        connection = pymysql.connect(host="localhost",user="root",passwd="",database="trojboj_baza")
        cursor = connection.cursor()

        self.__id = last_index("SELECT * from user")
        self.__id += 1
        ask = (self.__id,self.__login,self.__password,self.__imie,self.__nazwisko,self.__wzrost)

        index = check_if_egzist_data_in_database("SELECT * from user",ask,[1])

        if(index):
            print("dupl")
            return False
        insert1 = "INSERT INTO `user` VALUES ('"+str(self.__id)+"','"+self.__login+"', '"+self.__password+"', '"+self.__imie+"', '"+self.__nazwisko+"', '"+str(self.__wzrost)+"');"
        #print(insert1)
        cursor.execute(insert1)


        connection.commit()
        connection.close()
        return True

    @staticmethod
    def get_account(login, password):


        connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
        cursor = connection.cursor()


        retrive = "SELECT * from user"




        cursor.execute(retrive)



        rows = cursor.fetchall()

        for row in rows:
            if (row[1] == login and row[2] == password):
                user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                return (user, True)
        user = User(-1, "", "", "", "", "")
        return (user, False)
