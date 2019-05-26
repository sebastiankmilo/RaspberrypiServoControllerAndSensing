
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time
import ServoRaspberry

GPIO.setmode(GPIO.BOARD)     #Ponemos la Raspberry en modo BOARD
Servo = ServoRaspberry.Servo #Inicializamos el servo 

servo = Servo(puerto=8) #Configuro el puerto 8 para que me mueva un servo

try:
    servo.angle(grados=4.5) #p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
    time.sleep(0.5)           #pausa de medio segundo
    servo.angle(grados=10.5)#p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
    time.sleep(0.5)           #pausa de medio segundo
    servo.angle(grados=7.5)#p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
    time.sleep(0.5) 
    while True:
        time.sleep(1)
    
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    servo.stop()                      #Detenemos el servo 
    

