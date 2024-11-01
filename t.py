import math

TONE_FREQ = 293.665

def calculate_y(x):
    return (((((8*math.pow(10,6))/TONE_FREQ)-12)/x)-3)/3

def calculate_x(y):
    return (((8*math.pow(10,6))/TONE_FREQ)-12)/(3*y+3)



def pick_best_values():
    best_y = 0.9999999999
    best_x = 255
    for i in reversed(range(1,256)):
        this_y = calculate_y(i)
        if(this_y > 255):
            pass
        if(this_y % 1 < best_y % 1):
            best_y = this_y
            best_x = i
    return (best_x,best_y)

print(pick_best_values())
