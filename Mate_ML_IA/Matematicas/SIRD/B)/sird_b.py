import math
import pandas as pd 
from matplotlib import pyplot



def ploteo(tiempo, sus, inf, rc, decesos):
    # pyplot.title("Modelo SIRD - Susceptibles")
    
    # pyplot.xlabel("tiempo")
    # pyplot.ylabel("población")
    # pyplot.legend()
    # pyplot.grid(True)
    # pyplot.show()

    pyplot.title("Modelo SIRD (Susceptibles - Infectados - Recuperados - Decesos)")
    pyplot.plot(tiempo, sus, color="blue", label="Susceptibles")
    pyplot.plot(tiempo, inf, color="green", label="Infectados")
    pyplot.plot(tiempo, rc, color="red", label="Recuperados")
    pyplot.plot(tiempo, decesos, color="orange", label="Decesos")
    # i=0
    for i in range(0, len(tiempo),2000):
        print("\n")

        pyplot.text(tiempo[i], sus[i], "("+str(round(tiempo[i], 2)) + ","+str(round(sus[i], 2))+")", fontsize=5)
        pyplot.text(tiempo[i], inf[i], "("+str(round(tiempo[i], 2)) + ","+str(round(inf[i], 2))+")", fontsize=5)
        pyplot.text(tiempo[i], rc[i], "("+str(round(tiempo[i], 2)) + ","+str(round(rc[i], 2))+")", fontsize=5)
        pyplot.text(tiempo[i], decesos[i], "("+str(round(tiempo[i], 2)) + ","+str(round(decesos[i], 2))+")", fontsize=5)

    pyplot.xlabel("tiempo")
    pyplot.ylabel("población")
    pyplot.legend()
    pyplot.grid(True)

    pyplot.show()


def crear_excel(tiempo, suscep, infec, rec, decesos): #funcion para la creación del archivo excel
    data = {'Tiempo': tiempo, 'Susceptibles':suscep, 'Infectados': infec, 'Recuperados': rec, 'Decesos': decesos}
    df = pd.DataFrame(data, columns=[
                      'Tiempo', 'Susceptibles', 'Infectados', 'Recuperados', 'Decesos'])
    df.to_excel('./modelo_sird(b).xlsx', sheet_name='SIRD')


def show_resultados(dias, suscep, infec, rec, decesos):
    print("|    dias   |   susceptibles   |   infectados   |    recuperados  |  decesos |")

    for i in range(len(dias)):
        print("----------------------------------------------------------------------------------")
        print("|    "+str(dias[i])+"  |   "+str(suscep[i]) +"  |   " + str(infec[i])+"    |   " + str(rec[i])+"    |   "+ str(decesos[i])+"    |   ")

    print("-------------------------------------------------------------------------------")


def fs(s,i,beta,p_total):# Susceptibes
    return -((beta*s*i)/p_total)


def fi(s,i,beta,gama,p_total):# Infectados
    return (((beta*s*i)/p_total) - (gama*i))


def fr(i,gama): # recuperados
    return i*gama

def fd(i,mi): # decesos
    return i*mi

def sir(s,i,r,d):
    dias = 200 #18
    t = 0
    h = 0.01
    h2 = h/2
    h6 = h/6
    beta = 0.12
    gama = 0.035  
    mi = 0.005
    p_total = s+i+r+d

    decesos = []
    suscep = []
    infec = []
    rec = []
    tiempo = []

    suscep.append(s)
    infec.append(i)
    rec.append(r)
    tiempo.append(t)
    decesos.append(d)

    while(t<=dias):
        
        k1=fs(s,i,beta,p_total)
        l1=fi(s,i,beta,gama,p_total)
        m1=fr(i,gama)
        n1=fd(i,mi)

        k2=fs(s+(h2*k1), i+(h2*k1),beta,p_total)
        l2=fi(s+(h2*l1), i+(h2*l1),beta,gama,p_total)
        m2=fr(i+(h2*m1),gama)
        n2=fd(i+(h2*n1),mi)

        k3 = fs(s+(h2*k2), i+(h2*k2), beta, p_total)
        l3 = fi(s+(h2*l2), i+(h2*l2), beta, gama, p_total)
        m3 = fr(i+(h2*m2),gama)
        n3 = fd(i+(h2*n2), mi)

        k4 = fs(s+(h*k3), i+(h*k3), beta, p_total)
        l4 = fi(s+(h*l3), i+(h*l3), beta, gama, p_total)
        m4 = fr(i+(h*m3),gama)
        n4 = fd(i+(h2*n3), mi)

        s = s + (h6*(k1 + (2*k2) + (2*k3) + k4 ))
        suscep.append(round(s,2))
        i = i + (h6*(l1 + (2*l2) + (2*l3) + l4 ))
        infec.append(round(i,2))
        r = r + (h6*(m1 + (2*m2) + (2*m3) + m4 ))
        rec.append(round(r,2))
        d = d + (h6*(n1 + (2*n2) + (2*n3) + n4 ))
        decesos.append(round(d,2))
        t=t+h
        tiempo.append(round(t,2))

    
   
    #show_resultados(tiempo,suscep,infec,rec,decesos) #muestra de resultados por consola
    #crear_excel(tiempo, suscep, infec, rec, decesos) #creación de excel
    print("Población Total: "+str(p_total))
    ploteo(tiempo,suscep,infec,rec,decesos)

        
def run():
    s = 997
    i = 3
    r = 0
    d = 0
    sir(s,i,r,d)
   


if __name__ == "__main__":
    run()
