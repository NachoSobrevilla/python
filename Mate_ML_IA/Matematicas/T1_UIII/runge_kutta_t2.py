import math
from matplotlib import pyplot


def funcion(x,y):
    return math.sqrt(x) + (y*0)
    

def funcion_Arit(x):
    return ((x+2)**2)/4


def ploteo(px, py, pax, pay):
    pyplot.title("Runge-Kutta Caso 2")
    pyplot.plot(px, py, color="blue", label="Runge-Kutta")
    pyplot.plot(pax, pay, color="green", label="Analitico")
    k = 0
    for k in range(len(px)):
        print("\n")
       
        pyplot.text(px[k], py[k], "("+str(round(px[k], 2)) +
                    ","+str(round(py[k], 2))+")", fontsize=9)
        pyplot.text(pax[k], pay[k], "("+str(round(pax[k], 2)) +
                    ","+str(round(pay[k], 2))+")", fontsize=9)

    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.legend()
    pyplot.grid(True)

    pyplot.show()



def kn(x,y,h):
    k = i = 0
    kf=[]
    kf.append(funcion(x,y))
    for i in range(3):
        if i == 2:
           kf.append(funcion(x + h, y + (kf[i]*h)))
        else:
           kf.append(funcion(x + (h/2), y + ((kf[i]*h)/2)))
    

    i=0
    for i in range(len(kf)):
        # print("k"+str(i+1)+" = "+str(kf[i]))
        if i == 0 or i == len(kf)-1:
            k = k+kf[i]
        else:
            k = k+(2*kf[i])

    return k


def rk(x,y,h):
    i = aux = aux1 = 0
    px = [] 
    py = []
    pax = []
    pay = []
    
    px.append(x)
    pay.append(y)
    pax.append(x)
    py.append(y)
    print("t0 = "+str(x)+",   y0 = "+str(y))
    print("--------------------------------------------------------------------------")
    print("|    Iteracion   |   t   |   y   | y analitico |   Error Relativo  |   Error Absoluto  |")
    for i in range(2):
    # while(x <xf):
    #     i = i+1
        # print("iteracion "+str(i))
        print("-----------------------------------------------------------------------")
        x = x+h
        # print("x"+str(i+1)+" = "+str(x))
        px.append(x)
        pax.append(x)

        aux = y
        y = y + ((h/6)*kn(x,y,h))
        py.append(y)
        # print("y"+str(i+1)+" = "+str(y))

        e = ((aux-y)/y) * 100
        # print("error relativo de y"+str(i+1) + " = "+str(e))
        aux1 = funcion_Arit(x)
        pay.append(aux1)
        ea = ((aux1 - y)/aux1)
        # print("error aritmetico de y"+str(i+1) + " = "+str(ea))
        print("|    "+str(i)+"  |   "+str(x)+"  |   " +
              str(y)+"  |   "+str(aux1)+"  |   "+str(e)+"  |   "+str(ea)+"  |")

    print("-----------------------------------------------------------------------")



    ploteo(px,py,pax,pay)
    return y
        

def run():
    x0 = float(input("Ingrese el valor del punto inicial en t0: "))
    # xn = float(input("Ingrese el valor final Xn: "))
    y0 = float(input("Ingrese el valor del punto inicial en y0: "))
    h = float(input("Ingrese el valor del intervalo: "))
    yn = rk(x0,y0,h)
    print("Valor final de yn: "+ str(yn))

if __name__ == "__main__":
    run()
