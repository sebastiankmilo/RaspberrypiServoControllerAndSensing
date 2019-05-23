
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep


GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(8,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(8,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo
print ("hola")


try:                 
    while True:      #iniciamos un loop infinito
 
        p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
        time.sleep(0.5)           #pausa de medio segundo
 
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo 
    GPIO.cleanup() 

class servo(object):
  
  def conf(self,puerto,modo):
    GPIO.setup(puerto,modo) #Ponemos el pin puerto como el modo deseado(salida o entrada)
    self.p = GPIO.PWM(puerto,50)
    self.p.start(7.5) #Enviamos un pulso del 7.5% para centrar el servo
    pass
  def angle(self, grados):
    porcentaje = grados
    self.p.ChangeDutyCycle(porcentaje)
    pass
  pass