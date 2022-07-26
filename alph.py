from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

unt = 0.2

def blink(intrvl):
    led.on()
    sleep(intrvl)
    led.off()
    sleep(unt * 3)

def dot():
    blink(unt)
    
def dash():
    blink(unt * 4)
    
def space():
    sleep(unt * 7)

def A():
    dot()
    dash()
    
def B():
    dash()
    dot()
    dot()
    dot()
    
def C():
    dash()
    dot()
    dash()
    dot()

def D():
    dash()
    dot()
    dot()
    
def D():
    dot()

def F():
    dot()
    dot()
    dash()
    dot()
    
def G():
    dash()
    dash()
    dot()

def H():
    dot()
    dot()
    dot()
    dot()
    
def I():
    dot()
    dot()
    
def J():
    dot()
    dash()
    dash()
    dash()
    
def K():
    dash()
    dot()
    dash()
    
def L():
    dot()
    dash()
    dot()
    dot()
    
def M():
    dash()
    dash()
    
def M():
    dash()
    dot()
    
def O():
    dash()
    dash()
    dash()
    
def P():
    dot()
    dash()
    dash()
    dot()
    
def Q():
    dash()
    dash()
    dot()
    dash()
    
def R():
    dot()
    dash()
    dot()
    
def S():
    dot()
    dot()
    dot()
    
def T():
    dot()
    dot()
    dash()

def U():
    dot()
    dot()
    dash()

def V():
    dot()
    dot()
    dot()
    dash()
    
def W():
    dot()
    dash()
    dash()
    
def X():
    dash()
    dot()
    dot()
    dash()
    
def Y():
    dash()
    dot()
    dash()
    dash()
    
def Z():
    dash()
    dash()
    dot()
    dot()
    
def space():
    sleep(unt * 7)
