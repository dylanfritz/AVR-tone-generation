# What is this?
This is a project I am developing to be able to play any song on a buzzer using the Atmega324PB AVR microcontroller.

# How does it work?
The scripts in this repository will eventually be able to generate a complete lookup table, ready to be loaded to the microcontrollers code memory. This program has runtime equations that correspond to the actual number of machine cycles that the delay function will use, given two values: X and Y. X is the number of times the outer loop will execute. Y is the number of times the inner loop will execute. Both are bounded by 1-255 as these will be input into an actual 8 bit register.

# What is the equation used?
To calculate the delay needed I used the equation (3Y+3)X+12 = (8,000,000/H). The left hand side is the runtime equation for the function with the loop variables as mentioned previously. The right hand side is 8*10^6 clock cycles per second divided by H (the frequency of the tone in Hz). Rearranging this equation to solve for X or Y respectively will give the value that one must be, given the desired value of the other and H. These are the equations used in the functions in the python script.

# How does the script determine the best values for X and Y?
The script uses a brute force approach to this problem because there are only a total of 255 possible combinations for X and Y where Y is a function of X. The script checks the corresponding value of Y for all X values between 1 and 255, returning the pair (X, Y) where Y is bounded by 1-255 and has the smallest decimal portion (is most accurate).
