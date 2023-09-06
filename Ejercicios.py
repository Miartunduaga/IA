import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, n):
        self.pesos = np.random.rand(n)
        self.n = n
    #SOPLA GAITAS
    def propagacion(self, entradas):

        self.salida = 1*(self.pesos.dot(entradas)>0)
        self.entradas = entradas

    def actualizacion(self,alfa,salida):

        for i in range(0, self.n):
            self.pesos[i] = self.pesos[i] + alfa* (salida - self.salida) * self.entradas[i]

Perceptron_3 = Perceptron(3)

#tabla de entrenamiento
tabla = np.array ([[0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1]])

#Historico
historico = [Perceptron_3.pesos]
for epoca in range(0,10):
    for i in range(0, 4):
        Perceptron_3.propagacion(tabla[i,0:3])
        Perceptron_3.actualizacion(0.5, tabla[i,3])
        historico = np.concatenate((historico,[Perceptron_3.pesos]),axis = 0)

plt.plot(historico[:,0],'k')
plt.plot(historico[:,1],'r')
plt.plot(historico[:,2],'b')

plt.show()
