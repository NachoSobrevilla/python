def funcion(x,y):
    return -x*(y**2)


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
        print("k"+str(i+1)+" = "+str(kf[i]))
        if i == 0 or i == len(kf)-1:
            k = k+kf[i]
        else:
            k = k+(2*kf[i])

    return k


def rk(x,xf,y,h):
    i = aux = 0
    print("x0 = "+str(x)+",   y0 = "+str(y))
    while(x <xf):
        i = i+1
        print("iteracion "+str(i))
        aux = y
        y = y + ((h/6)*kn(x,y,h))
        print("y"+str(i+1)+" = "+str(y))
        x = x+h
        print("x"+str(i+1)+" = "+str(x))
        e = ((aux-y)/y) * 100
        print("error relativo de y"+str(i+1) + " = "+str(e))

    return y
        

def run():
    x0 = float(input("Ingrese el valor del punto inicial en X0: "))
    xn = float(input("Ingrese el valor final Xn: "))
    y0 = float(input("Ingrese el valor del punto inicial en Y0: "))
    h = float(input("Ingrese el valor del intervalo: "))
    yn = rk(x0,xn,y0,h)
    print("Valor final de yn: "+ str(yn))

if __name__ == "__main__":
    run()
