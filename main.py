from datetime import datetime, date, timedelta
from datetime import time as tm
import time
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import ServoRaspberry

# Función que es llamada por los eventos
def Leer(servos):
    abrir(Servos=servos) ##mover los servos para ponerlos en la posición en la cual puedan tomar datos
    comienzo = time.time() ##guardo el tiempo en el cual lo servos ya estan en posición para tomar datos
    tiempoEjecuecion = 5  #defino por cuanto tiempo voy a tomar los datos
    final = comienzo + tiempoEjecuecion #defino en que momento se deja de tomar los datos
    cant = 0
    while final > time.time():
      cant = cant +1 #recivir la información del arduino
      pass
    cerrar(Servos=servos) #Muevo los servos
    pass
    
def abrir(Servos):
  for servo in Servos:
    servo.angle(grados=180)
    pass  
  time.sleep(4)
  pass

def cerrar(Servos):
  for servo in Servos:
    servo.angle(grados=90)
    pass  
  time.sleep(4)
  pass


mañana = tm(23,55,0) #Mañana
tarde = tm(23,56,0) #Tarde
noche = tm(23,57,0) #Noche
horarios ={} #Defino un diccionario para los horarios
horarios["nuevo día"] = tm(23,59,58)
horarios["mañana"] = mañana
horarios["tarde"] = tarde
horarios["noche"] = noche
GPIO.setmode(GPIO.BOARD)
#Servo1 = ServoRaspberry.Servo(puerto = 8)  #Defino donde va a estar conectado el servo 1 a los puertos GPIO  de la raspberrypi
#Servo2 = ServoRaspberry.Servo(puerto = 9)  #Defino donde va a estar conectado el servo 2 a los puertos GPIO  de la raspberrypi
#Servo3 = ServoRaspberry.Servo(puerto = 10) #Defino donde va a estar conectado el servo 3 a los puertos GPIO  de la raspberrypi
#Servo4 = ServoRaspberry.Servo(puerto = 11) #Defino donde va a estar conectado el servo 4 puertos GPIO  de la raspberrypi
#Servo5 = ServoRaspberry.Servo(puerto = 12) #Defino donde va a estar conectado el servo 5  a los puertos GPIO  de la raspberrypi

puertos=[8,10,11,12,13]
pos=0
servos = [ ServoRaspberry.Servo(puerto = puertos[i]) for i in range(4)] #array q contiene los 4 servos
#for servo in servos:
#  servo = ServoRaspberry.Servo(puerto = puertos[pos])
#  pos=pos+1
#  pass




print('PROGRAMADOR INICIADO:')
mañana = False
tarde = False
noche = False
test =True
while test :
  time.sleep(1)
  horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
  if horarios["actual"] >= horarios["mañana"] :
    print("mañana")
    Leer(servos=servos)
    mañana = True
    while mañana :
      time.sleep(1)
      horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
      if horarios["actual"] >= horarios["tarde"] :
        print("tarde")
        Leer(servos=servos)
        mañana = False
        tarde = True
        while tarde:
          time.sleep(1)
          horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
          if horarios["actual"] >= horarios["noche"] :
            tarde = False
            noche = True
            Leer(servos)
            print("noche")
            while noche :
              time.sleep(1)
              horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
              if horarios["actual"] >= horarios["nuevo día"] :
                noche = False
                time.sleep(4)
                print ("Nuevo Día")
                pass
              pass 
            pass
          pass
        pass
      pass
    pass
  pass