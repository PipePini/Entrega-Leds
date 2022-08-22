from machine import Pin as pin
from utime import sleep
puerto=[2,15,4,16,17,5,18,19,21,4]
grupo=[]
for i in puerto:
    grupo.append (pin(i,pin.OUT))
print (grupo)
def derecha():
    for i in grupo:
        for j in range (2):
            i.value(not i.value())
        sleep(0.5)
def izquierda():
    for i in reversed (grupo):
        for j in range (2):
            i.value(not i.value())
        sleep(0.5)
while True:
    derecha()
    izquierda()
        