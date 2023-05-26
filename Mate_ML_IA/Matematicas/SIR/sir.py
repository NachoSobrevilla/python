import math
import pandas as pd 
from matplotlib import pyplot



def ploteo(tiempo, sus, inf, rc):
    pyplot.title("Modelo SIR Susceptibles - Infectados- Recuperados") 
    pyplot.plot(tiempo, sus, color="blue", label="Susceptibles")
    pyplot.plot(tiempo, inf, color="green", label="Infectados")
    pyplot.plot(tiempo, rc, color="red", label="Recuperados")
    pyplot.xlabel("tiempo")
    pyplot.ylabel("población")
    pyplot.legend()
    pyplot.grid(True)

    pyplot.show()


    # pyplot.title("Modelo SIR - Recuperados")
    
    # pyplot.xlabel("tiempo")
    # pyplot.ylabel("población")
    # pyplot.legend()
    # pyplot.grid(True)

    # pyplot.show()


    # i = 0
    # for i in range(0, len(tiempo),40):
    #     print("\n")

    #     pyplot.text(tiempo[i], sus[i], "("+str(round(tiempo[i], 2)) + ","+str(round(sus[i], 2))+")", fontsize=5)
    #     pyplot.text(tiempo[i], inf[i], "("+str(round(tiempo[i], 2)) + ","+str(round(inf[i], 2))+")", fontsize=5)
    #     pyplot.text(tiempo[i], inf[i], "("+str(round(tiempo[i], 2)) + ","+str(round(inf[i], 2))+")", fontsize=5)

    # pyplot.xlabel("tiempo")
    # pyplot.ylabel("población")
    # pyplot.legend()
    # pyplot.grid(True)

    # pyplot.show()

def crear_excel(tiempo, suscep, infec, rec):
    data = {'Tiempo': tiempo, 'Susceptibles':suscep, 'Infectados': infec, 'Recuperados': rec} #diccionario de los datos
    df = pd.DataFrame(data,columns=['Tiempo', 'Susceptibles', 'Infectados', 'Recuperados']) #ingreso de los datos a hoja
    # Creacion del archivo excel por lo general esta en las la carpeta raiz del usuario C:\Users\nombre_user en windows
    df.to_excel('./modelo_sir.xlsx', sheet_name='SIR')


def show_resultados(dias, suscep, infec, rec):
    print("|    dias   |   susceptibles   |   infectados   |    recuperados  |")

    for i in range(len(dias)):
        print("----------------------------------------------------------------------------------")
        print("|    "+str(dias[i])+"  |   "+str(suscep[i]) +
              "  |   " + str(infec[i])+"    |   " + str(rec[i])+"    |   ")

    print("-------------------------------------------------------------------------------")


def fs(s,i,beta,p_total):# Susceptibes
    return -((beta*s*i)/p_total)


def fi(s,i,beta,gama,p_total):# Infectados
    return (((beta*s*i)/p_total) - (gama*i))


def fr(i,gama): # recuperados
    return i*gama


def sir(s,i,r):
    dias = 180
    t = 0
    h = 0.01
    h2 = h/2
    h6 = h/6
    beta = (2.5/14)
    gama = (1/14)  #Taza de recuperación
    p_total = s+i+r

    suscep = []
    infec = []
    rec = []
    tiempo = []

    suscep.append(s)
    infec.append(i)
    rec.append(r)
    tiempo.append(t)

    while(t<=dias):
        
        k1=fs(s,i,beta,p_total)
        l1=fi(s,i,beta,gama,p_total)
        m1=fr(i,gama)

        k2=fs(s+(h2*k1), i+(h2*k1),beta,p_total)
        l2=fi(s+(h2*l1), i+(h2*l1),beta,gama,p_total)
        m2 = fr(i+(h2*m1),gama)

        k3 = fs(s+(h2*k2), i+(h2*k2), beta, p_total)
        l3 = fi(s+(h2*l2), i+(h2*l2), beta, gama, p_total)
        m3 = fr(i+(h2*m2),gama)

        k4 = fs(s+(h*k3), i+(h*k3), beta, p_total)
        l4 = fi(s+(h*l3), i+(h*l3), beta, gama, p_total)
        m4 = fr(i+(h*m3),gama)

        s = s + ((h6)*(k1 + (2*k2) + (2*k3) + k4 ))
        suscep.append(round(s,2))
        i = i + ((h6)*(l1 + (2*l2) + (2*l3) + l4 ))
        infec.append(round(i,2))
        r = r + ((h6)*(m1 + (2*m2) + (2*m3) + m4 ))
        rec.append(round(r,2))
        t=t+h
        tiempo.append(round(t,2))


    #show_resultados(tiempo,suscep,infec,rec) #mostrar los resultados de consola
    crear_excel(tiempo, suscep, infec, rec) #creacion de archivo excel
    print("Población Total: "+str(p_total))
    ploteo(tiempo,suscep,infec,rec) #graficación de los datos

        
def run():
    s = 129000000
    i = 26025
    r = 16180
    s = s - (i+r)
    sir(s,i,r)
   


if __name__ == "__main__":
    run()
    
