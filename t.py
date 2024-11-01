import math

TONE_FREQ = 261.625

def calculate_y(x):
    return (((((8*math.pow(10,6))/TONE_FREQ)-12)/x)-3)/3



print(calculate_y(87))
