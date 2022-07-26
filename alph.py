from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

unt = 0.2

CHARS_CODES = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

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

def encryptMsg(msg):
    encrypted = ''
    for c in msg.upper():
        if c != ' ':
            encrypted = encrypted + CHARS_CODES[c] + ' '
        else:
            encrypted = encrypted + ' '
            
    for code in encrypted:
        if code == '.':
            dot()
        elif code == '-':
            dash()
        else:
            space()
