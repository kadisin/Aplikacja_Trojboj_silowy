import pymysql
import pylab
import datetime
import matplotlib.pyplot as plt


def Wykres_Liniowy(argumenty,wartosci):

    #argumenty = krotka_arg_wart[0]
    #wartosci = krotka_arg_wart[1]
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.2,0.8,0.8])
    ax.bar(argumenty,wartosci)
    #plt.show()

    plt.plot(argumenty,wartosci,linestyle='--',marker='o',color='b')
    plt.legend(["Szacunkowy Postęp","Dokładne wartości"])
    plt.xticks(rotation=90)
    pylab.show()



