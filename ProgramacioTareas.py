import sched
from datetime import datetime, date, timedelta
from datetime import time as tm
import time

# Función que es llamada por los eventos
def Leer(dato):
    print('TIEMPO:{}'.format(dato)) ##mover datos
    comienzo = time.time()
    tiempoEjecuecion = 5
    final = comienzo + tiempoEjecuecion
    cant = 0;
    while final > time.time():
      cant = cant +1
      pass
    print (cant)
    pass
    

mañana = tm(23,55,0) #Mañana
tarde = tm(23,56,0) #Tarde
noche = tm(23,57,0) #Noche
horarios ={} #Defino un diccionario para los horarios
horarios["nuevo día"] = tm(23,59,58)
horarios["mañana"] = mañana
horarios["tarde"] = tarde
horarios["noche"] = noche
horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
print("\tHora1 < Hora2:",horarios["actual"] < horarios["noche"])




print('PROGRAMADOR INICIADO:')
mañana = False
tarde = False
noche = False
test =True
while test :
  time.sleep(1)
  horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
  if horarios["actual"] >= horarios["mañana"] :
    Leer("mañana")
    mañana = True
    while mañana :
      time.sleep(1)
      horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
      if horarios["actual"] >= horarios["tarde"] :
        Leer("tarde")
        mañana = False
        tarde = True
        while tarde:
          time.sleep(1)
          horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
          if horarios["actual"] >= horarios["noche"] :
            tarde = False
            noche = True
            Leer("noche")
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