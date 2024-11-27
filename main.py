from machine import Pin,PWM,ADC
import time
from time import sleep_ms
import random
from neopixel import NeoPixel


# Joystick Pins
xVal=ADC(Pin(5))
yVal=ADC(Pin(4))

xVal.atten(ADC.ATTN_11DB)
yVal.atten(ADC.ATTN_11DB)
xVal.width(ADC.WIDTH_12BIT)
yVal.width(ADC.WIDTH_12BIT)

roll_button = Pin(16, Pin.IN, Pin.PULL_UP) #button to press when you want to roll the wheel(neopixel)
finished_button = Pin(17, Pin.IN, Pin.PULL_UP) #button to press when you finished your turn

star_a_button = Pin(6, Pin.IN, Pin.PULL_UP)
star_b_button = Pin(7, Pin.IN, Pin.PULL_UP)
star_c_button = Pin(15, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(18), freq=100)

pin = Pin(8, Pin.OUT)
neo = NeoPixel(pin, 16)

'''star_a = Pin(16, Pin.OUT)
star_b = Pin(17, Pin.OUT)
star_c = Pin(18, Pin.OUT)'''
#joyctock 13,14
segments_score = {
    'a': Pin(35, Pin.OUT),
    'b': Pin(0, Pin.OUT),
    'c': Pin(45, Pin.OUT),
    'd': Pin(48, Pin.OUT),
    'e': Pin(47, Pin.OUT),
    'f': Pin(21, Pin.OUT),
    'g': Pin(36, Pin.OUT),
    'dp': Pin(19, Pin.OUT)
}

segments_player = {
    'a': Pin(3, Pin.OUT),
    'b': Pin(46, Pin.OUT),
    'c': Pin(9, Pin.OUT),
    'd': Pin(10, Pin.OUT),
    'e': Pin(11, Pin.OUT),
    'f': Pin(12, Pin.OUT),
    'g': Pin(13, Pin.OUT),
    'dp': Pin(14, Pin.OUT)
}

num_to_segments = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'g', 'e', 'd'],
    3: ['a', 'b', 'g', 'c', 'd'],
    4: ['f', 'g', 'b', 'c'],
    5: ['a', 'f', 'g', 'c', 'd'],
    6: ['a', 'f', 'e', 'd', 'c', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}

def display_number_score(num):
    # Turn off all segments
    for seg in segments_score.values():
        seg.value(1)
    # Turn on the required segments
    for seg in num_to_segments[num]:
        segments_score[seg].value(0)

def display_number_player(num):
    # Turn off all segments
    for seg in segments_player.values():
        seg.value(1)
    # Turn on the required segments
    for seg in num_to_segments[num]:
        segments_player[seg].value(0)

while True:
    for num in range(10):
        display_number_score(num)
        sleep_ms(250)
    for num in range(10):
        display_number_player(num)
        sleep_ms(250)# to check the 7-segment display
waitingfortheplayerchoice=True
while True:
    while waitingfortheplayerchoice==True:
        #print('running')
        y_value = yVal.read()
        x_value = xVal.read()
        
        time.sleep(0.2)
        if x_value< 100:
            print('choice made')
            waitingfortheplayerchoice=False
        elif x_value> 3995:
            print('up')
        elif y_value< 100:
            print('left')
        elif y_value> 3995:
            print('right')
    

