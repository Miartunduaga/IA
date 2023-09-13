import numpy as np
import matplotlib.pyplot as plt



class perceptron:
    
    #inicializar los pesos
    def __init__(self,n):
        #calcular pesos
        self.pesos =np.random.randn(n)
        self.n =n
    
    
    #Propagacion
    def propagacion(self,entradas):
        self.salida = 1*(self.pesos.dot(entradas)>0)
        self.entradas =entradas
    
    #Actualizacion
    def actualizacionCoeficiente(self,ritmoAprendizaje,salidad):
        for i in range(0,self.n):
            self.pesos[i]=self.pesos[i]+ritmoAprendizaje*(salidad-self.salida)*self.entradas[i]


'''  
perceptron_tres_entradas =perceptron(3)
print(perceptron_tres_entradas.pesos)

#propagacion
perceptron_tres_entradas.propagacion([1,0,1])
print(perceptron_tres_entradas.salida)

#Actualizacion
perceptron_tres_entradas.actualizacionCoeficiente(0.5,1)
print(perceptron_tres_entradas.pesos)

perceptron_and = perceptron(3)

#ejemplo de aprendizaje
ejemplos=np.array([[0,0,1,0],[0,1,0,0],[1,0,1,0],[1,1,1,1]])

grad_pesos = [perceptron_and.pesos]
for epoca in range (0,100):
    for i in range(0,4):
        perceptron_and.propagacion(ejemplos[i,0:3])
        perceptron_and.actualizacionCoeficiente(0.5,ejemplos[i,3])
        # para recorrer la tabla 
        grad_pesos = np.concatenate((grad_pesos,[perceptron_and.pesos]),axis =0)

plt.plot(grad_pesos[:,0],'k')
plt.plot(grad_pesos[:,1],'r')
plt.plot(grad_pesos[:,2],'b')
plt.show()
'''