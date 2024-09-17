# Dylan Stitt
# Rocket Generator
# Unit 0 Lab 1

import os

# Validate the user input
def validateInput(inp):
    try:
        # Try to cast as int and return
        # If not raise the TypeError
        inp = int(inp)
        if inp >= 3: return inp
        raise TypeError
    
    except:
        # Call the function within itself to run this scenario until the user inputs a correct value (>2)
        inp = validateInput(input('Try again: '))
        return inp
        
# Drawing the top and bottom subfigures of the rocket
def drawtb(val):
    count = (2*val)-1

    for i in range((2*val)-1):
        print(' '*count + '/'*(i+1) + '**' +'\\'*(i+1))
        count -= 1

# Drawing the up-pointing triangle subfigure
def drawUp(val):
    count = 1
    triangle = '/\\'

    for i in range(val):
        print('|' + ('.'*(val-count) + triangle*count + '.'*(val-count))*2 + '|')
        count += 1

# Drawing the down-pointing triangle subfigure
def drawDown(val):
    count = 0
    tempVal = val
    triangle = '\\/'

    for i in range(val):
        print('|' + ('.'*count + triangle*tempVal + '.'*count)*2 + '|')
        count += 1
        tempVal -= 1

# Drawing the separator between middle subfigures
def drawSeparator(val):
    print('+'+'=*'*(val*2)+'+')

# Function calls to draw the full rocket
def drawRocket(val):
    for i in [drawtb, drawSeparator, drawUp, drawDown]:
        i(val)
    drawSeparator(val)
    for i in [drawtb, drawSeparator, drawUp, drawDown][::-1]:
        i(val)

# Main
# Calls upon drawRocket() once valid user imput has been given
def main():
    inp = validateInput(input('Enter an integer value for your rocket size (3 or more): '))
    os.system('cls')

    drawRocket(inp)


if __name__ == '__main__':
    main()
    