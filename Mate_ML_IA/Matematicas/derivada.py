# import numpy as np



def fun(x):
    return 2*(x**2)


def deriv(x):
    h = 0.00000000001
    print("valor de h: "+str(h))
    print("funcion: 2x²")
    return (-3*fun(x)+4*fun(x+h)-fun(x+2*h))/(2*h)



def derivA(x):
    return 4*x


# def derivpy(x):


def run():
    print("Evaluacion de derivadas")
    x = int(input("Ingrese un valor: "))
    d = deriv(x)
    da = derivA(x)
    print("La derivada de 2x² evaluada en "+str(x)+" es igual a "+str(d))
    print("Derivada Analitica: "+str(da))
    print("Error "+str(abs(da-d)/da))




if __name__ == "__main__":
    run()
