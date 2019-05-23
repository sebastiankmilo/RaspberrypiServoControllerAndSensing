
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep
import ServoRaspberry


Servo = ServoRaspberry.Servo


GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
#GPIO.setup(8,GPIO.OUT)    #Ponemos el pin 21 como salida
#p = GPIO.PWM(8,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
#p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo
print ("hola")
servo = Servo(puerto=8)

try:                 
    while True:      #iniciamos un loop infinito
 
        servo.angle(grados=4.5) #p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        servo.angle(grados=10.5)#p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo
        servo.angle(grados=7.5)#p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
        time.sleep(0.5)           #pausa de medio segundo
 
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    servo.stop()                      #Detenemos el servo 
    GPIO.cleanup() 

