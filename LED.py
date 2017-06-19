########################################
#Classe LED, acende ou apaga LED       #
#recebe porta onde esta conectado o LED#           
########################################

import RPi.GPIO as GPIO
import time

class LED:
    
    def __init__(self, porta):

        #Configuracao
        self.porta = porta
        
        #numeros de acordo com a placa fisica
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.porta,GPIO.OUT,initial = GPIO.LOW)
        
        #Avisos de porta aberta são ignorados
        GPIO.setwarnings (False)

    def acende_led (self):
        GPIO.output(self.porta,1)

    def apaga_led (self):
        GPIO.output(self.porta, 0)

    def pisca_led (self):
        GPIO.output(self.porta,1)
        time.sleep(0.5)
        GPIO.output(self.porta, 0)
        time.sleep(0.5)

        GPIO.output(self.porta,1)
        time.sleep(0.5)
        GPIO.output(self.porta, 0)
        time.sleep(0.5)

        GPIO.output(self.porta,1)
        time.sleep(0.5)
        GPIO.output(self.porta, 0)
        time.sleep(0.5)



