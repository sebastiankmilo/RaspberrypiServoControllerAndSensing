import RPi.GPIO as GPIO

class Servo(object):
  
  def  __init__(self,puerto):
    GPIO.setup(puerto,GPIO.OUT) #Ponemos el pin puerto como el modo deseado(salida o entrada)
    self.p = GPIO.PWM(puerto,50)
    self.p.start(7.5) #Enviamos un pulso del 7.5% para centrar el servo
    pass
  def angle(self, grados):
    porcentaje = grados
    self.p.ChangeDutyCycle(porcentaje)
    pass
  def stop(self):
    self.p.stop()
    pass
  pass