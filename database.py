import pymysql




def last_index(select_):

    connection = pymysql.connect(host="localhost",user="root",passwd="",database="trojboj_baza")
    cursor = connection.cursor()

    retrive = select_

    cursor.execute(retrive)
    rows = cursor.fetchall()

    for row in rows:
        last_index_ = row[0]


    connection.commit()
    connection.close()
    return last_index_

def check_if_egzist_data_in_database(select_,new_record,list_of_unique_indeks):

    """

    :param select_: string select send to sql
    :param new_record: tuple of new_record
    :return: true if egzist the same tuple / false if not egzist
    """

    connection = pymysql.connect(host="localhost",user="root",passwd="",database="trojboj_baza")
    cursor = connection.cursor()

    retrive = select_

    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(new_record[0] > last_index(select_)):
        for row in rows:
            for indeks in range(len(list_of_unique_indeks)):
                if(row[list_of_unique_indeks[indeks]] == new_record[list_of_unique_indeks[indeks]]):
                    return True



    connection.commit()
    connection.close()
    return False


def list_of_tuples_in_database(select_):

    """
    :param select_: string select send to sql
    :return: list of touples in database
    """

    connection = pymysql.connect(host="localhost",user="root",passwd="",database="trojboj_baza")
    cursor = connection.cursor()

    retrive = select_
    list = []

    cursor.execute(retrive)
    rows = cursor.fetchall()
    for row in rows:
        list.append(row)
    connection.commit()
    connection.close()

    return list

def check_user_in_base(select_,login,password):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()

    retrive = select_

    cursor.execute(retrive)
    rows = cursor.fetchall()
    for row in rows:
        if(row[1] == login and row[2] == password):
            connection.commit()
            connection.close()
            return True

    connection.commit()
    connection.close()
    return False
def delete_weight(id,date):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()

    retrive = "DELETE FROM `weight` WHERE `date`='" + str(date) + "' AND `idUser`= " + str(id)
    print(retrive)
    cursor.execute(retrive)
    connection.commit()
    connection.close()

def delete_results(id,date):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()

    retrive = "DELETE FROM `results` WHERE `date`='" + str(date) + "' AND `idUser`= " + str(id)
    print(retrive)
    cursor.execute(retrive)
    connection.commit()
    connection.close()


def get_weights(id):

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()

    ask = "SELECT * FROM `weight` WHERE `idUser` = " + str(id) + " ORDER BY `date`"
    cursor.execute(ask)
    rows = cursor.fetchall()

    return rows
    # return :
    # (id, idUser, weight, date)
    #print(rows)


def get_results(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()


    #select * FROM `results`
    #where `squat` IS NOT NULL AND `bench_press` IS NOT NULL AND `deadlift` IS NOT NULL and `idUser` = 1

    ask = "SELECT * FROM `results` WHERE `squat` IS NOT NULL AND `bench_press` IS NOT NULL AND `deadlift` IS NOT NULL and `idUser` = " + str(id) + " ORDER BY `date`"
    cursor.execute(ask)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def get_squat(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()


    #select * FROM `results`
    #where `squat` IS NOT NULL AND `bench_press` IS NOT NULL AND `deadlift` IS NOT NULL and `idUser` = 1

    ask = "SELECT * FROM `results` WHERE `squat` IS NOT NULL AND `idUser` = " + str(id) + " ORDER BY `date`"
    cursor.execute(ask)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def get_bench(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()


    ask = "SELECT * FROM `results` WHERE `bench_press` IS NOT NULL AND  `idUser` = " + str(id) + " ORDER BY `date`"

    cursor.execute(ask)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def get_deadlift(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()


    ask = "SELECT * FROM `results` WHERE `deadlift` IS NOT NULL AND `idUser` = " + str(id) + " ORDER BY `date`"
    cursor.execute(ask)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def get_all_results(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="trojboj_baza")
    cursor = connection.cursor()


    ask = "SELECT * FROM `results` WHERE  `idUser` = " + str(id) + " ORDER BY `date`"
    cursor.execute(ask)
    rows = cursor.fetchall()
    #print(rows)
    return rows