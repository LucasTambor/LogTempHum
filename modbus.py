
##############################################################################
#Classe efetua configuracao do modbus e retorna lista dos sensores conectados#
##############################################################################



class Configuracao:
    
    def __init__(self):

        '''Configura 32 sensores automaticamente
        (comecando em 1, pois ID=0 = todos)
        cada sensor eh salvo na lista de acordo com seu ID
        sensor 1 = sensor [1], sensor 2 = sensor [2], etc...'''
        
        for x in range (1,33):
            
            self.sensor[x] = minimalmodbus.Instrument('/dev/RS485',x)
            #talvez tenha de configurar timeout

    '''testa cada uma das conexões
    retorna uma lista dos sensores devidamente conectados'''

    def pega_lista(self):
       
        self.lista_sensores = []
        index_lista = 0

        for x in range (1, 33):
            try:
                teste = sensor[x].read_register (0,2)
                index_lista += 1
                self.lista_sensores[index_lista] = x
            
            '''Em caso de erro nao faz nada
            somente passa para proxima iteracao'''
            except IOError: 
                pass

        return self.lista_sensores

            
        



