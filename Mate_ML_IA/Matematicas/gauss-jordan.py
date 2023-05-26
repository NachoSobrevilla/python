def ImprimeMatriz(m):
    etiquetas = ["x", "y", "z", ""]
    for i in range(3):
        for j in range(4):
            #print(mtr[j][i])
            print((" | {0},{0}"+etiquetas[j]).format(m[i][j]), sep=',', end='')

        print("\n")
    
    print("\n")


def ImprimeResultado(matriz):
    etiquetas = ["x", "y", "z"]
    for i in range(3):
        aux = matriz[i]
        print(etiquetas[i]+" = "+str(aux[len(aux)-1]))


def gauss_jordan(matriz):
    x = i = j = ai = 0
    aux = aux1 = []
    for i in range(len(matriz)):
        matriz = diagzero(matriz,i)
        aux = matriz[i]
        x = aux[i]

        print("coeficiente "+str(i)+" = "+str(x))
        if x != 1:
            for j in range(4):
                if aux[j] != 0:
                    aux[j] = (aux[j]/x)
        
        print("Ecuacion"+str(i)+":"+str(aux))
        print("\n")


        matriz[i] = aux
        x = j = 0
        for ai in range(len(matriz)):
            if ai == i:
                continue
            else:
                aux1 = matriz[ai]
                x = aux1[i]
                x = x*(-1)  #El signo contrario del coefiente en turno
                print("E"+str(i)+"+E"+str(ai)+" = "+str(aux)+" + "+ str(aux1))
                for j in range(4): 
                    aux1[j] = (aux[j]*x) + aux1[j]
                
                print(" = "+str(aux1))
                matriz[ai] = aux1
                x = 0
                print("\n")

        ImprimeMatriz(matriz)
        print("\n")

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


    

def ingMtrz():
    i = j = 0
    matriz = []
    etiquetas = ["del coeficiente x: ", "del coeficiente y: ",
                 "del coeficiente z: ", "de la constante de la ecuacion: "]
    for i in range(3):
        matriz.append([])
        print("ingresa la ecuacion "+str(i+1))
        for j in range(4):
            valor = float(input("ingresa el valor "+ etiquetas[j]))
            matriz[i].append(valor)
        print("\n")

    return matriz



def run():
    matriz = ingMtrz()
    print("\n Matriz Inicial")
    ImprimeMatriz(matriz)
    matriz = gauss_jordan(matriz)
    print("\n Matriz Final")
    ImprimeMatriz(matriz)
    print("\n Valores de las variables")
    ImprimeResultado(matriz)

    


if __name__ == "__main__":
    run()
