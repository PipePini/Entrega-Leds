from machine import Pin as pin
from utime import sleep
led1=pin(2,pin.OUT)
led2=pin(15,pin.OUT)
led3=pin(4,pin.OUT)
led4=pin(16,pin.OUT)
led5=pin(17,pin.OUT)
led6=pin(5,pin.OUT)
led7=pin(18,pin.OUT)
led8=pin(19,pin.OUT)


def print_led(a,b,c,d,e,f,g,h):
  led1.value(a)
  led2.value(b)
  led3.value(c)
  led4.value(d)
  led5.value(e)
  led6.value(f)
  led7.value(g)
  led8.value(h)
  
  sleep(0.5)
while True:
  print_led(0,0,0,0,0,0,0,0)
  print_led(0,0,0,0,0,0,0,1)
  print_led(0,0,0,0,0,0,1,0)
  print_led(0,0,0,0,0,1,0,0)
  print_led(0,0,0,0,1,0,0,0)
  print_led(0,0,0,1,0,0,0,0)
  print_led(0,0,1,0,0,0,0,0)
  print_led(0,1,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0)
  