import math
from matplotlib import pyplot


def ploteo(dias, sus, inf, rc):
    pyplot.title("Modelo SIR")
    pyplot.plot(dias, sus, color="blue", label="Susceptibles")
    pyplot.plot(dias, inf, color="green", label="Infectados")
    pyplot.plot(dias, rc, color="red", label="Recuperados")
    i = 0
    for i in range(0,len(dias),40):
        print("\n")

        pyplot.text(dias[i], sus[i], "("+str(round(dias[i], 2)) +
                    ","+str(round(sus[i], 2))+")", fontsize=5)
        pyplot.text(dias[i], inf[i], "("+str(round(dias[i], 2)) +
                    ","+str(round(inf[i], 2))+")", fontsize=5)
        pyplot.text(dias[i], inf[i], "("+str(round(dias[i], 2)) +
                    ","+str(round(inf[i], 2))+")", fontsize=5)
                

    pyplot.xlabel("dias")
    pyplot.ylabel("población")
    pyplot.legend()
    pyplot.grid(True)

    pyplot.show()


def show_resultados(dias,suscep,infec,rec):
    print("|    dias   |   susceptibles   |   infectados   |    recuperados  |")


    for i in range(len(dias)):
        print("----------------------------------------------------------------------------------")
        print("|    "+str(dias[i])+"  |   "+str(suscep[i]) +"  |   " + str(infec[i])+"    |   " + str(rec[i])+"    |   ")

    print("-------------------------------------------------------------------------------")




def funciones(x,y,fn):
    r=0
    if fn == 0: #Susceptibes: x = susceptibles, y = infectados
        r = -(beta*((x*y)/p_total))
    elif fn == 1: #Infectados: x = susceptibles y = infectados
        r = beta*((x*y)/p_total) - (gama*y)
    elif fn == 2: #recuperados: x = recuperados y =0
        r = gama*x

    return r



def kn(x,y,fk):
    k = i = 0
    kf=[]
    kf.append(funciones(x,y,fk)) #k1
    for i in range(3):
        if i == 2: #k4
            if y==0:
                kf.append(funciones(x + h*kf[i], 0, fk))
            else:
                kf.append(funciones(x + h*kf[i], y + (kf[i]*h), fk))
        else: #k2  o k3
            if y == 0:
                kf.append(funciones(x + (h/2)*kf[i], 0, fk))
            else:
                kf.append(funciones(x + ((h/2)*kf[i]), y + ((kf[i]*h)/2), fk))
    

    i=0
    for i in range(len(kf)):
        # print("k"+str(i+1)+" = "+str(kf[i]))
        if i == 0 or i == len(kf)-1:
            k = k+kf[i]
        else:
            k = k+(2*kf[i])

    
    k=(h/6)*k
    return k



def sir(s, i, r):
    k=d=0
    dias = []
    suscep = []
    infec = []
    rec = []

    dias.append(d) # tiempo = d = 0
    suscep.append(s)
    infec.append(i)
    rec.append(r)


    for d in range(180):
        dias.append(1+d) 
        for k in range(3):
            if k == 0:
                suscep.append(suscep[d] + kn(suscep[d], infec[d], k)) 
                #k
            elif k == 1:
                infec.append(infec[d] + kn(suscep[d], infec[d],k))
                #l
            elif k==2:
                rec.append(rec[d] + kn(infec[d], 0, k))
                #m


    show_resultados(dias, suscep, infec, rec)
    print("Población Total: "+str(s+i+r))
    ploteo(dias,suscep,infec,rec)
        
    
    
def run():
    global beta 
    global gama 
    global p_total 
    global h
    s = 119957795 #float(input("Ingrese el valor de la poblacion suceptible: "))
    i = 26025     # float(input("Ingrese el valor de la poblacion afectada: "))
    r = 16180     # float(input("Ingrese el valor de la poblacion inmune: "))
    # r = float(input("Ingrese el valor de los dias de analisis "))
    gama = (1/14)  # float(input("Ingrese el valor de la tasa de recuperacion: "))
    beta =  (1.9/14) #float(input("Ingrese el valor de la tasa de infeccion: "))
    p_total = s+i+r
    h=0.01
    sir(s,i,r)
    

if __name__ == "__main__":
    run()
