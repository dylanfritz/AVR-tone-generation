import math

TONE_FREQ = input("tone frequency?")

def calculate_y(x):
    return (((((8*math.pow(10,6))/TONE_FREQ)-12)/x)-3)/3

def calculate_x(y):
    return (((8*math.pow(10,6))/TONE_FREQ)-12)/(3*y+3)



def pick_best_yvalues():
    best_y = 0.9999999999
    best_x = 255
    for i in reversed(range(1,256)):
        this_y = calculate_y(i)
        if(this_y > 255):
            continue
        if(this_y % 1 < best_y % 1):
            best_y = this_y
            best_x = i
    return (best_x,int(math.floor(best_y)), best_y)

def pick_best_xvalues():
    best_x = 0.9999999999
    best_y = 255
    for i in reversed(range(1,256)):
        this_x = calculate_x(i)
        if(this_x > 255):
            continue
        if(this_x % 1 < best_x % 1):
            best_x = this_x
            best_y = i
    return (int(math.floor(best_x)), best_y, best_x)

print(pick_best_yvalues())
print(pick_best_xvalues())
