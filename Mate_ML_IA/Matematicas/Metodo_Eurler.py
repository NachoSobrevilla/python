import math

def funcion(x,y):
    return math.sin(x) - math.log(y)



def euler(x,xf,y,n):
    i = aux = e = 0
    h = ((xf-x)/n)
    print("h = "+str(h)+",   x0 = "+str(x)+",   y0 = "+str(y))
    for i in range(n):
        aux = y
        print("Iteracion: "+str(i+1))
        y = y + (h * funcion(x,y))
        print("y"+str(i+1)+" = "+str(y))
        x = x+h
        print("x"+str(i+1)+" = "+str(x))
        e = ((aux-y)/y) * 100
        print("error relativo de y"+str(i+1) +" = "+str(e))


    return y




def run():
    print("Metodo de Euler")
    x0 = float(input("Ingrese el valor del punto inicial en X0: "))
    xn = float(input("Ingrese el valor final Xn: "))
    y0 = float(input("Ingrese el valor del punto inicial en Y0: "))
    n = int(input("Ingrese el numero de intervalo: "))
    yn = euler(x0,xn,y0,n)
    print("Valor final de Yn es igual a "+str(yn))




if __name__ == "__main__":
    run()
