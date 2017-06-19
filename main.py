################################################################################
#main do programa                                                              #
#aqui sao chamadas as classes:                                                 # 
#-configurar_modbus(configura e acha o numero de sensores conectados ao modulo)#
#-leitura(le os valores obtidos pelos sensores)                                #
#-banco_de_dados(efetua as queries do banco)                                   #
################################################################################

import modbus
import RP.GPIO as GPIO
import leitura

def main(self):
    
     
    #Instancia criada da classe Configuracao
    config = modbus.Configuracao()

    #Lista de sensores conectados
    sensores = config.pega_lista
    print (sensores)

    #LEITURA TEMPERATURA

    #intancia da classe Leitura
    ler = leitura.Leitura()

    #Lista de temperaturas (lista de sensores conectados)
    temperaturas = ler.leitura_temperatura(sensores)
    print (temperaturas)

    #LEITURA UMIDADE

    umidades = ler.temperatura_umidade(sensores)
    print (umidades)





