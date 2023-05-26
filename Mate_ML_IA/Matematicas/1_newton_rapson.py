def funcion(c,xn):
    return (c-(xn**2))/(2 * xn)


def NewtonRapzon(c, x0):
    aux1 = aux2 = 0
    xn = x0 
    count = 0
    err = 1
    ex = 10 **-5
    while((err > (ex)) or (count == 10)):
        aux1 = xn
        xn = funcion(c,xn)
        aux2 = aux1 + xn
        print("Δx"+str(count)+"= "+str(aux2)+" = "+str(aux1)+" + "+str(xn))
        err = abs((aux2 - aux1)/(aux2))
        print("Error relativo de Δx"+str(count)+"= "+str(err) +
              " = ("+str(aux1)+"-"+str(aux2)+")"+"/"+str(aux1)+"\n")
        xn = aux2
        count = count + 1
    
    return xn


def run():
    c = float(input("Ingrese un valor para calcular su raiz: "))
    x = float(input("Ingrese un valor para aproximado a la raiz del valor: "))
    r = NewtonRapzon(c,x)
    print("El resultado es:"+str(r))



if __name__ == "__main__":
    run()
