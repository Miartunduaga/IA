import random
import numpy as np
import matplotlib.pyplot as plt

class PerceptronProfe:
    
    def __init__(self, n):
        self.n = n
        self.bias =np.random.rand()
        self.peso1 =np.random.rand()
        self.peso2 =np.random.rand()
        self.peso3 =np.random.rand()
        self.tasaAprendizaje=0.5
        self.k = 0
        self.kmax = 0
        self.E = 0.01
        self.erroresIterar=[]
        
        #ESCALON
    def propagacion(self,entradaPeso1,entradaPeso2,entradaPeso3):
        
        respuesta = self.peso1 * entradaPeso1 + self.peso2 * entradaPeso2 + self.peso3 * entradaPeso3 + self.bias
        
        '''
        respuesta[respuesta >= 0] = 1
        respuesta[respuesta < 0] = 0
        '''
        if respuesta>=0:
            respuesta=1
        elif(respuesta<0):
            respuesta=0      
        print(respuesta)  
        return respuesta
    
    def entrenador(self, entradaPesoR,entradaPesoG,entradaPesoB,respuestaDeseada):
        
        global bias,respuestaActual
        numeroDeEpocas =10
        errores =0
        for epoca in range(numeroDeEpocas):
            
            for i in range(len(respuestaDeseada)):
                respuestaActual = self.propagacion(entradaPesoR[i],entradaPesoG[i],entradaPesoB[i])
               
                error = respuestaDeseada[i]- respuestaActual
                #Actualizacion de bias

                self.bias -= self.tasaAprendizaje*error
                
                #Actualizacion de pesos r g b
                self.peso1 = self.peso1 + (self.tasaAprendizaje * error * entradaPesoR[i])#R
                self.peso2 = self.peso2 + (self.tasaAprendizaje * error * entradaPesoG[i])#G
                self.peso3 = self.peso3 + (self.tasaAprendizaje * error * entradaPesoB[i])#B
                
                if not np.array_equal(respuestaActual,respuestaDeseada[i]):
                    print(f"Respuesta del pc   {respuestaActual} es diferente de  respuestaActual {respuestaDeseada[i]}")
                  
                    errores+=1
                else:
                    print("NO HUBO CAMBIO")
                print("     FALLOS    " ,errores,"   bias  " ,self.bias)
            
                
    
  