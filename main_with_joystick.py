from machine import Pin,PWM,ADC
import time
from time import sleep_ms
import random
from neopixel import NeoPixel


# Joystick Pins
xVal=ADC(Pin(5))
yVal=ADC(Pin(4))
zVal=Pin(12,Pin.IN,Pin.PULL_UP) 

xVal.atten(ADC.ATTN_11DB)
yVal.atten(ADC.ATTN_11DB)
xVal.width(ADC.WIDTH_12BIT)
yVal.width(ADC.WIDTH_12BIT)

roll_button = Pin(9, Pin.IN, Pin.PULL_UP) #button to press when you want to roll the wheel(neopixel)
finished_button = Pin(10, Pin.IN, Pin.PULL_UP) #button to press when you finished your turn

star_a_button = Pin(2, Pin.IN, Pin.PULL_UP)
star_b_button = Pin(12, Pin.IN, Pin.PULL_UP)
star_c_button = Pin(13, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(14), freq=100)

pin = Pin(45, Pin.OUT)
neo = NeoPixel(pin, 15)

player_count = 0

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

'''while True:
    for num in range(10):
        display_number_score(num)
        sleep_ms(1000)
    for num in range(10):
        display_number_player(num)
        sleep_ms(1000)# to check the 7-segment display
'''
waitingfortheplayerchoice=True
while True:
    while waitingfortheplayerchoice==True:
        #print('running')
        y_value = xVal.read()
        x_value = yVal.read()
        
        time.sleep(0.2)
        if x_value< 100:
            print('choice made')
            waitingfortheplayerchoice=False
        elif x_value> 3995:
            print('up')
            display_number_player(3)
            player_count = 3
            print(player_count)
        elif y_value< 100:
            print('right')
            display_number_player(2)
            player_count = 2
            print(player_count)
        elif y_value> 3995:
            print('left')
            display_number_player(4)
            player_count = 4
            print(player_count)
    


