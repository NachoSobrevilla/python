from warnings import resetwarnings
import numpy as np
from numpy.random import choice as np_choice
import random as rn
print(rn.randrange(0, 2, 1))
#print(np_choice(4))


def aletorio_negativo():
    x = rn.random()
    i = rn.randrange(0, 1, 2)
    if i == 0:
        return x*(-1)
    else:
        return x


class ABC(object):
    def __init__(self) -> None:
        super().__init__()
    
    def __init__(self, n_abejas, fuentes_comida, n_soluciones, intentos = 10 ):
        self.n_abejas = n_abejas
        self.fuentes_comida = fuentes_comida
        self.n_soluciones = n_soluciones
        self.soluciones = np.array()
        self.intentos = intentos
    
    def run(self):
        x_pi = 0
        # j es por las columnas que representan una fuente de comida
        x_pi = 0
        i = 0
        pesos_sol = self.init_soluciones()
        while (i < self.intentos): 
            x_pi =self.init_soluciones()
            self.abejas_empleadas(x_pi)
            
            i += 1
        #for j in range(len(self.soluciones[j])):
        #    fuente = np.copy(self.soluciones[j])
        #    x_pi = self.fase_init(fuente)
        #    x_pi = self.fase_init()
        #    self.abejas_empleadas(x_pi,j)
        
    def init_soluciones(self):
        sol = []
        pesos_sol = []
        for x in self.n_soluciones:
            for j in range(len(self.fuentes_comida[0])):
                k = np_choice(4)
                sol.append(self.fuentes_comida[k][j])

            if x == 0:
                self.soluciones = np.append(sol)
                pesos_sol.append(np.sum(sol))
            else:
                if np.array_equal(sol, l for l in self.soluciones) == False:
                    self.soluciones = np.append(sol)
                    pesos_sol = (np.sum(sol))
                else:
                    x -= 1
        return pesos_sol


    def fase_init(self):
        x_pi = []
        for sol in self.soluciones:
            x_li = min(sol)
            x_ui = max(sol)    
            x_i = x_li + (np.random.rand(1) * (x_ui-x_li))
        
        x_pi.append(x_i)
        return x_pi  

    def abejas_empleadas(self, x_pi):
        
        k = np_choice(len(x_pi))
        x_k = x_pi[k]
        pi = aletorio_negativo()

        v_id = x_k + pi*(x_pi-x_k)
        




