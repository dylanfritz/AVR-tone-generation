import math

TONE_FREQ = 293.665

def calculate_y(x):
    return (((((8*math.pow(10,6))/TONE_FREQ)-12)/x)-3)/3

def calculate_x(y):
    return (((8*math.pow(10,6))/TONE_FREQ)-12)/3*y+3



print(calculate_y(87))
print(calculate_x(52))
