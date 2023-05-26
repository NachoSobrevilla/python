import random as rn
import numpy as np
import random as rn
from numpy.random import choice as np_choice
from math import sqrt


class AntColony(object):
    def __init__ (self, distancias, n_hor, n_mejor, iteraciones, decay, alfa=1, beta=1):
        self.distancias = distancias
        self.feromona = np.ones(self.distancias.shape) / len(distancias)
        self.todos_ids = range(len(distancias))
        self.n_hor = n_hor
        self.n_mejor = n_mejor
        self.iteraciones = iteraciones
        self.decay = decay
        self.alfa = alfa
        self.beta = beta


    def run(self):
        logs_distancia = []
        ruta_corta = None
        mejor_ruta_cortas = ("bandera", np.inf)
        for i in range(self.iteraciones):
            todas_rutas = self.gen_todas_rutas()
            self.feromona_esparcida(todas_rutas,self.n_mejor,ruta_corta=ruta_corta)
            ruta_corta = min(todas_rutas, key = lambda x:x[1])
            if ruta_corta[1] < mejor_ruta_cortas[1]:
                mejor_ruta_cortas = ruta_corta
            logs_distancia.append(mejor_ruta_cortas[1])
        return mejor_ruta_cortas, logs_distancia
            
    def feromona_esparcida (self, todas_rutas, n_mejor, ruta_corta):
        rutas_ordenadas = sorted(todas_rutas, key=lambda x: x[1])
        for ruta, dist in rutas_ordenadas[:n_mejor]:
            for mover in ruta:
                self.feromona[mover] += 1.0 / self.distancias[mover]




    def gen_ruta_dist(self, ruta):
        total_dist = 0
        for r in ruta:
            total_dist += self.distancias[r]
        return total_dist

    def gen_todas_rutas(self):
        todas_rutas = []
        for i in range(self.n_hor):
            ruta = self.gen_ruta(0)
            todas_rutas.append(ruta, self.gen_ruta_dist(ruta))
        return todas_rutas

    def gen_ruta(self, inicio):
        ruta = []
        visitado = set()
        visitado.add(inicio)
        prev=inicio
        for i in range(len(self.distancias) - 1):
            mover = self.mover_hormiga(self.feromona[prev], self.distancias[prev], visitado)
            ruta.append((prev, mover))
            prev = mover
            visitado.add(mover)
        ruta.append((prev,inicio))
        return ruta



    def mover_hormiga(self, feromona, dist, visitado): #seleccion de las varibales de decision
        feromona = np.copy(feromona)
        feromona[list(visitado)] = 0

        fila = (feromona ** self.alfa) * ((1.0/dist)** self.beta)

        p_fila = fila/fila.sum()
        mover = np_choice(self.todos_ids, 1, p = p_fila)[0]
        return mover
        

