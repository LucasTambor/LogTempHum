################################################################################
#main do programa                                                              #
#aqui sao chamadas as classes:                                                 # 
#-configurar_modbus(configura e acha o numero de sensores conectados ao modulo)#
#-leitura(le os valores obtidos pelos sensores)                                #
#-banco_de_dados(efetua as queries do banco)                                   #
################################################################################

import modbus

sensores = modbus.Configuracao()


print (sensores.sensores)


