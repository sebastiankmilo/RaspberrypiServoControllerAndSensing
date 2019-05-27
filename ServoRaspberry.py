import RPi.GPIO as GPIO

class Servo(object):
  
  def  __init__(self,puerto):
    GPIO.setup(puerto,GPIO.OUT) #Ponemos el pin puerto como el modo deseado(salida o entrada)
    self.p = GPIO.PWM(puerto,50)
    self.p.start(7.5) #Enviamos un pulso del 7.5% para centrar el servo
    pass
  def angle(self, grados):
    porcentaje = map(grados,0,225,2.25,11.25)
    self.p.ChangeDutyCycle(porcentaje)
    pass
  def stop(self):
    self.p.stop()
    GPIO.cleanup() 
    pass
  
  pass
def map(x, in_min, in_max, out_min, out_max):
    return ((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)