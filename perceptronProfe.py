import random
import numpy as np
class PerceptronProfe:
    
    def __init__(self, n):
        self.n = n
        self.bias =np.random.rand()
        self.peso1 =np.random.rand(1)
        self.peso2 =np.random.rand(1)
        self.peso3 =np.random.rand(1)
        self.tasaAprendizaje=0.5
        self.k = 0
        self.kmax = 0
        self.E = 0.01
        self.erroresIterar=[]
        
        #ESCALON
    def propagacion(self,entradaPeso1,entradaPeso2,entradaPeso3):
        
        respuesta = self.peso1 * entradaPeso1 + self.peso2 * entradaPeso2 + self.peso3 * entradaPeso3 + self.bias
        
      
        
        respuesta[respuesta >= 0] = 1
        respuesta[respuesta < 0] = 0
        print(respuesta,"ARADA SD AS DASD\n")  
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
                self.bias += self.tasaAprendizaje*error
                
                #Actualizacion de pesos r g b
                self.peso1 =(self.tasaAprendizaje * error * entradaPesoR[i])#R
                self.peso2 =(self.tasaAprendizaje * error * entradaPesoG[i])#G
                self.peso3 =(self.tasaAprendizaje * error * entradaPesoB[i])#B
                
                
                if not np.array_equal(respuestaActual,respuestaDeseada):
                    errores+=1
                #print(errores," FALLOS " ,"   bias  " ,self.bias)
            