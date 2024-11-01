import math

TONE_FREQ = input("tone frequency?")

def calculate_y(x,h):
    return (((((8*math.pow(10,6))/h)-12)/x)-3)/3

def calculate_x(y,h):
    return (((8*math.pow(10,6))/h)-12)/(3*y+3)

def calc_mcs(x, y): #gives number of machine cycles produced by a combo of x and y
    return (3*y+3)*x+12

def calc_time(x, y): #calculates time delay (in microseconds) of a combo of x and y
    return calc_mcs(x,y)/8

def calc_periods(x, y, s): # calculates the number of periods of an x and y combo to play a tone for s seconds
    ms_desired = s*math.pow(10, 6)
    return ms_desired/calc_time(x,y)




def pick_best_yvalues(h): # will determine the "best" combination of x and y for a given hertz where both are in the range 0-255 and best is determined by smallest decimal part where y is the approximated value
    best_y = 0.9999999999
    best_x = 255
    for i in reversed(range(1,256)):
        this_y = calculate_y(i,h)
        if(this_y > 255):
            continue
        if(this_y % 1 < best_y % 1):
            best_y = this_y
            best_x = i
    return (best_x,int(math.floor(best_y)), best_y)

def pick_best_xvalues(h): # will determine the "best" combination of x and y for a given hertz where both are in the range 0-255 and best is determined by smallest decimal part where x is the approximated value
    best_x = 0.9999999999
    best_y = 255
    for i in reversed(range(1,256)): 
        this_x = calculate_x(i,h)
        if(this_x > 255):
            continue
        if(this_x % 1 < best_x % 1):
            best_x = this_x
            best_y = i
    return (int(math.floor(best_x)), best_y, best_x)

esty = pick_best_yvalues(TONE_FREQ)
estx = pick_best_xvalues(TONE_FREQ)
print(esty)
print(calc_time(esty[0],esty[1]))
print(calc_periods(esty[0], esty[1], 1))
print(estx)
print(calc_time(estx[0],estx[1]))
