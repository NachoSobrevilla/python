import math

def ImprimeMatriz(m):
    etiquetas = ["x", "y", "z", ""]
    for i in range(3):
        for j in range(4):
            #print(mtr[j][i])5
            print((" | {0}"+etiquetas[j]).format(m[i][j]), sep=',', end='')

        print("\n")
    
    print("\n")


def ImprimeResultado(matriz):
    etiquetas = ["x", "y", "z"]
    for i in range(3):
        aux = matriz[i]
        print(etiquetas[i]+" = "+str(aux[len(aux)-1]))


def gj(matriz):
    x = i = j = ai = 0
    aux = aux1 = []
    for i in range(len(matriz)): #No. de Columnas
        matriz = diagzero(matriz,i)
        aux = matriz[i]
        x = aux[i]

        # print("coeficiente "+str(i)+" = "+str(x))
        if x != 1:
            for j in range(4):
                if aux[j] != 0:
                    aux[j] = (aux[j]/x)
        
        # print("Ecuacion"+str(i)+":"+str(aux))
        # print("\n")


        matriz[i] = aux
        x = j = 0
        for ai in range(len(matriz)): #la longitud de la fila
            if ai == i:
                continue
            else:
                aux1 = matriz[ai]
                x = aux1[i]
                x = x*(-1)  #El signo contrario del coefiente en turno
                # print("E"+str(i)+"+E"+str(ai)+" = "+str(aux)+" + "+ str(aux1))
                for j in range(len(matriz[i])): 
                    aux1[j] = (aux[j]*x) + aux1[j]
                
                # print(" = "+str(aux1))
                matriz[ai] = aux1
                x = 0
                # print("\n")

        # ImprimeMatriz(matriz)
        # print("\n")


    
    return matriz


def diagzero(matriz, i):
    j = 0
    aux1 = []
    aux = matriz[i]
    if aux[i] == 0:
        for j in range(len(matriz)):
            aux1 = matriz[j]
            if aux1[j] != 0 or j != i:
                matriz[i] = aux1
                matriz[j] = aux

                print("\n Cambio de Ecuaciones entre la ecuacion "+str(i)+" y la ecuacion "+str(j))
                ImprimeMatriz(matriz)


                break

    return matriz            


def funciones(i,x,y,z):
    r = 0
    if i == 0:
        r = (math.sqrt(x)) + ((1/2)*math.cos(z)) - (math.log(1/y))
    elif i == 1:
        r = (y*math.log(4*x)) - ((2*z) - math.exp(x)) + 1
    elif i == 2:
        r = (4*x) + (y*math.sin(z)) - 1

    return r 


def crear_Mtrz(x,y,z):
    i = j = aux = f = 0
    d = 10**-5
    
    matriz = []
    for i in range(3):
        matriz.append([])
        f = funciones(i, x, y, z)
        for j in range(3):
            if j==0:
                aux = (funciones(i, x+d, y, z) - f) / d
            elif j==1:
                aux = (funciones(i, x, y+d, z) - f) / d
            elif j==2:
                aux = (funciones(i, x, y, z+d) - f) / d

            matriz[i].append(aux)
            

        matriz[i].append(f)
        f=0
        

    return matriz


def newton_rapson(x,y,z):
    i = k = 0
    aux1 = aux2 = aux3 = 0
    ex = ey = ez = 0
    print("x0 = "+str(x)+", y0 = "+str(y)+", z0 = "+str(z))
    print("-----------------------------------------------------")
    print("| # |  x  |  y  |  z  | error x | error y | error z |")
    while(i < 10 or ex == 10**-3 or ey == 10**-3 or ez == 10**-3):
        
        print("-----------------------------------------------------")
        matriz = crear_Mtrz(x,y,z)
        matriz = gj(matriz)
        
        aux1 = x
        aux2 = y
        aux3 = z


        for k in range(3):
            aux = matriz[k]
            if i==0:
                x = aux[len(aux)-1]
            elif i==1:
                y = aux[len(aux)-1]
            elif i==2:
                z = aux[len(aux)-1]
            
        ex = abs(x-aux1)/x
        ey = abs(y-aux2)/y
        ez = abs(z-aux3)/z

        print("| "+str(i)+" | "+str(round(x,2))+" | "+str(round(y,2))+" | "+str(round(z,2))+" | "+str(round(ex,7))+" | "+str(round(ey,7))+" | "+str(round(ez,7))+" |")
        i = i +1
    
    print("-----------------------------------------------------")
        
        



def run():
    vector_entrada = []
    print("Newton Rapson para ecuaciones 3x3 ")

    x0 = int(input("Ingresa el valor de X: ")) 
    y0 = int(input("Ingresa el valor de Y: "))
    z0 = int(input("Ingresa el valor de Z: "))
    newton_rapson(x0,y0,z0)

    
    
    



    


if __name__ == "__main__":
    run()
#la inicializacion
