from operator import indexOf
import numpy as np
from numpy.random import choice as np_choice

class ACO(object):
    def __init__ (self, distancias, iteraciones , n_hormigas, alfa = 1, beta = 1, epsilon = 0.5, dseta = 0.03): 
        self.distancias = distancias
        self.feromonas = np.ones(self.distancias.shape) / 10 #para que sea 0.1
        self.iteraciones = iteraciones
        self.n_hormigas = n_hormigas
        self.alfa = alfa
        self.beta = beta
        self.epsilon = epsilon
        self.nv = len(distancias) #i = 1,2,3....nv -> la variables designadas i (las posiciones de cada letra del motif)
        self.npool = len(distancias[1]) # j = 1,2,3 ... npool -> los posibles valores de i (para el caso de los motifs son 4 ACTG)
        self.dseta = dseta
        self.evapo = 0.1 #ρ
        self.zeta_k = 0.9 #penalizacion de los valores de la función objeto 

    def run(self):
        log_rutas = []
        mejor_ruta = []
        mayor_ruta = None
        self.print_ACO()
        for i in range(self.iteraciones):
            todos_caminos = self.moverHormigas()
            self.espar_feromonas(todos_caminos)
            mayor_ruta = max(todos_caminos, key=lambda x: x[(len(todos_caminos[0])-1)])
            #self.feromonas_mejor_camino(mejor_ruta)
            if i == 0:
                mejor_ruta = mayor_ruta
            elif mayor_ruta[len(mejor_ruta)-1] > mejor_ruta[len(mejor_ruta)-1]:
                mejor_ruta = mayor_ruta
            log_rutas.append([mejor_ruta[1],mejor_ruta[3]])
            self.print_iteración(i,todos_caminos, mejor_ruta)

        return mejor_ruta, log_rutas

    def espar_feromonas(self,todos_caminos):
        self.feromonas = np.copy(self.feromonas * (1-self.evapo))
        #rutas_ordenadas = sorted(todos_caminos, key = lambda x: x[3])
        for ruta in todos_caminos:
            for i,j,c in ruta[:(len(ruta)-1)]:
                self.feromonas[i][j] += 1/self.zeta_k

    def feromonas_mejor_camino(self, mejor_camino):
        for i, j, c in mejor_camino[:(len(mejor_camino)-1)]:
            self.feromonas[i][j] += 1/self.zeta_k

    def moverHormigas(self):
        todos_caminos = []
        for h in range(self.n_hormigas):
            local_camino = self.prob_camino()
            todos_caminos.append(local_camino)

        return todos_caminos

    def prob_camino(self):
        local_camino_pos = []
        cost_camino = 0

        for j in range(len(self.distancias[0])):
            d_j = self.distancias[:, j] ** self.alfa
            f_j = self.feromonas[:, j] ** self.beta
            m_j = d_j * f_j

            s_pij = np.sum(m_j)

            pij = m_j/s_pij 

            c = np_choice(self.distancias[:, j], 1, p=pij)[0]
            pos = indexOf(self.distancias[:, j],c) 
            
            cost_camino = cost_camino + c
            local_camino_pos.append([pos,j,c])
            
            self.feromonas[pos][j] = self.feromonas[pos][j] * self.dseta
        
        local_camino_pos.append(cost_camino)

        return local_camino_pos
    

    def print_ACO(self):
        print("Distancias: ",self.distancias)
        print("Iteraciones: ",self.iteraciones)
        print("Hormigas: ", self.n_hormigas)

    def print_iteración(self, n ,todos_caminos, mejor_camino):
        print("Iteración: ", n+1)
        #print("Ferononas: \n", self.feromonas)
        #print("Caminos: \n ", todos_caminos)
        print("Mejor camino: \n", mejor_camino)
        print("----------------------------------\n")





distancia = np.array([[3, 1, 5, 7, 3, 6, 4, 7, 1, 9, 8, 5, 4, 2],
                     [1, 1, 2, 0, 0, 0, 1, 0, 8, 0, 0, 0, 0, 3],
                     [4, 1, 1, 1, 0, 0, 4, 1, 0, 0, 1, 3, 0, 2],
                     [1, 6, 1, 1, 6, 3, 0, 1, 0, 0, 0, 1, 5, 2]])
    #def limitaciones(self):



def feromonas_mejor_camino(camino):
    string_motif = ''
    for i, j, c in camino[:(len(camino)-1)]:
        if i == 0:
            string_motif += 'A'
        elif i == 1:
            string_motif += 'C'
        elif i == 2:
            string_motif += 'G'
        elif i == 3:
            string_motif += 'T'

    return string_motif


#Con refuerzo del mejor camino
hormigas = ACO(distancia, 50, 25, 1, 0.6, 0.3, 0.1) #GTAATAAACAAATC
#hormigas = ACO(distancia, 50, 50)  # GTAATAAACAAGAC

#Sin refuerzo 

#hormigas = ACO(distancia, 50, 50)  # GTAATAAACAAGAC
caminos, logs = hormigas.run()
print("caminos: ", caminos)
motif = feromonas_mejor_camino(caminos)
print("motif candidato: ",motif)
print("puntuación: ", caminos[len(caminos)-1])

#if main = __name__:
#    run()

# def run():
#     variables = np.array([])
#     pool = np.array()
#     alfa = 1
#     beta = 1
#     iter =
#     ants

