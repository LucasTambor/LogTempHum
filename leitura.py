####################################################
#Efetua a leitura dos sensores                     #
#-recebe lista dos sensores conectados             #
#-retorna lista de temperatura e lista de  umidades#
####################################################

import minimalmodbus
import serial

class Leitura:

    def leitura_temperatura (self, lista_sensores):

        temperatura = []
        self.lista_sensores = lista_sensores
        self.numero_sensores = len(lista_sensores)#comprimento da lista
        
        for x in range(self.numero_sensores):
            try:
                temperatura[x] = self.lista_sensores[x].read_register(0,2)
            except IOError:
                print ('falha de comunicacao: Sensor %d'%(self.lista_sensores[x]))
        return temperatura

    def leitura_umidade(self, lista_sensores):
        
        umidade = []
        self.lista_sensores = lista_sensores
        self.numero_sensores = len(lista_sensores)

        for x in range (self.numero_sensores):
            try:
                umidade[x] = self.lista_sensores[x].read_register(1,2)
            except IOError:
                print ('Falha de comunicacao: Sensor %d'%(self.lista_sensores[x]))
        return umidade



