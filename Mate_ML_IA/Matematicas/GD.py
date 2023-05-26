import matplotlib.pyplot as plt
import math
import random


# Ejemplo del gradiente descendente aplicado a la función y = x^2 + 1
# La ecuación matemática para el gradiente (derivada) es = 2*x


def gd():
    #inicialización de variables
    tp = 0.5
    iteraciones =[]
    y = []
    x = []

    #añadir los valores iniciales
    iteraciones.append(0)
    x.append(50)
    #x.append(random.randint(0,50)) #x inicial
    x_i = x[0]
    y.append(x_i**2+1)

    for i in range(20): #se definen las iteraciones
        
        x_i= x_i - tp*(2*x_i) #se aplica el gradiente descendiente
        x.append(x_i)
        y.append(x_i**2+1)
        iteraciones.append(i+1)

        print('-------------------------------')
        print('Iteracion ', str(i+1), ' x = ', x_i, ' y = ', str(x_i**2+1))

    print('-------------------------------')

    plt.subplot(1,2,1)
    plt.plot(iteraciones, y)
    plt.xlabel('Iteración')
    plt.ylabel('y')
    for i in range(1,len(x),4):
        plt.text(iteraciones[i], y[i], "("+str(round(iteraciones[i], 2)) +
                 ","+str(round(y[i], 2))+")", fontsize=7)




    plt.subplot(1, 2, 2)
    plt.plot(x,y)
    plt.xlabel('x')
    # plt.ylabel('y')

    for i in range(1, len(x), 4):
        plt.text(x[i], y[i], "("+str(round(x[i], 2)) + ","+str(round(y[i], 2))+")", fontsize=7)
        # plt.text(x[len(x)-1], y[len(y)-1], "("+str(round(x[len(x)-1], 2)) + ","+str(round(y[len(y)-1], 2))+")", fontsize=5)

    plt.show()
        
        
        







if __name__ == "__main__":
    gd()
