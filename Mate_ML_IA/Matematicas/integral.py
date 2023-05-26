def func(x):
    return (x**2)/2


# def integral2(x0,x1,n):
#     h = (x1-x0)/5
#     d1 = d =  (x1-x0)/n
#     d0 = x0 + h
#     f = r = 0
#     print("\nDistancia entre los intervalos "+str(x0)+" y "+str(x1)+" dividido en "+str(n-2)+ " Evaluaciones")
#     print("Distancia: "+str(d))
#     while (d00 < x1-h):
#         if (d0 != x0):
#             #  f = ((h*(55*func(d1+h)+5*func(d1+2*h)+5*func(d1+3*h)+55*func(d1+4*h)))/24) - \
#             f = ((h*(55*func(d0+h)+5*func(d0+2*h)+5*func(d0+3*h)+55*func(d0+4*h)))/24)
#             print("Evaluacion de x0 = "+str(d0)+" es igual a "+str(f))
#             r = r + f
        

#         d0 = d0 + d
#         d1 = d1 + d
        
        
            
#     return r


def integral(x0, x1):
    h = (x1-x0)/5

    print("\nEvaluacion de los intervalos "+str(x0)+" y " + str(x1))
    return ((h*(55*func(x0+h)+5*func(x0+2*h)+5*func(x0+3*h)+55*func(x0+4*h)))/24)
    #return  ((h*(55*func(x1-h)+5*func(x1+2*h)+5*func(x1+3*h)+55*func(x1+4*h)))/24) - ((h*(55*func(x0+h)+5*func(x0+2*h)+5*func(x0+3*h)+55*func(x0+4*h)))/24)


def integral_A(x1,x0):
    return ((x1**3)/6) - ((x0**3)/6)


def run():
    x_0 = 0
    x_1 = 1
    
    print("Evaluacion integral")
    x_0 = int(input("Ingresa el pirmer valor del intervalo: "))
    x_1 = int(input("ingresa el segundo valor del intervalo: "))
    n = int(input("Ingresa el numero de evaluaciones: "))
    # i_2 = integral2(x_0,x_1,n)
    x = integral(x_0, x_1)
    i_1 = integral_A(x_1, x_0)
    print("\n Funcion: (x²)/2")
    print("Integral: "+str(x))
    #  print("Integral compuesta: "+str(i_2))
    print("Integral Analitica: "+str(i_1))
    print("Error: "+str(abs(i_1 - x)/i_1))


    

if __name__ == "__main__":
    run()
