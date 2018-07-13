from ptpulse import ledmatrix
from time import sleep
from random import randint

#color
r = randint(0,255)
rinc = randint(25,50)
g = randint(0,255)
ginc = randint(25,50)
b = randint(0,255)
binc = randint(25,50)


#wait time for pixel appearance
wait = 0
meh = 0.5


#make lines

#horizontal line left to right
def horzLine(startx, endx, y):
    r = randint(0,255)
    rinc = randint(25,50)
    g = randint(0,255)
    ginc = randint(25,50)
    b = randint(0,255)
    binc = randint(25,50)
    
    for x in range(startx, endx):
        #red value incrementation
        if r + rinc > 255 or r + rinc < 0:
            rinc = -rinc
        else:
            r += rinc
        #green value incrementation  
        if g + ginc > 255 or g + ginc < 0:
            ginc = -ginc
        else:
            g += ginc
        #blue value incrementation
        if b + binc > 255 or b + binc < 0:
            binc = -binc
        else:
            b += binc
            
        ledmatrix.set_pixel(x, y, r, g, b)
        ledmatrix.show()
        sleep(wait)

#vertical line bottom to top
def vertLine(starty, endy, x):
    r = randint(0,255)
    rinc = randint(25,50)
    g = randint(0,255)
    ginc = randint(25,50)
    b = randint(0,255)
    binc = randint(25,50)
    
    for y in range(starty, endy):
        #red value incrementation
        if r + rinc > 255 or r + rinc < 0:
            rinc = -rinc
        else:
            r += rinc
        #green value incrementation  
        if g + ginc > 255 or g + ginc < 0:
            ginc = -ginc
        else:
            g += ginc
        #blue value incrementation
        if b + binc > 255 or b + binc < 0:
            binc = -binc
        else:
            b += binc
            
        ledmatrix.set_pixel(x, y, r, g, b)
        ledmatrix.show()
        sleep(wait)
        
#diagonal line bottom left to top right
def NELine(startx, endx, y):
    r = randint(0,255)
    rinc = randint(25,50)
    g = randint(0,255)
    ginc = randint(25,50)
    b = randint(0,255)
    binc = randint(25,50)
    
    for x in range(startx, endx):
        #red value incrementation
        if r + rinc > 255 or r + rinc < 0:
            rinc = -rinc
        else:
            r += rinc
        #green value incrementation  
        if g + ginc > 255 or g + ginc < 0:
            ginc = -ginc
        else:
            g += ginc
        #blue value incrementation
        if b + binc > 255 or b + binc < 0:
            binc = -binc
        else:
            b += binc
            
        ledmatrix.set_pixel(x, y, r, g, b)
        ledmatrix.show()
        sleep(wait)
        y += 1
        
#diagonal line top left to bottom right
def SELine(startx, endx, y):
    r = randint(0,255)
    rinc = randint(25,50)
    g = randint(0,255)
    ginc = randint(25,50)
    b = randint(0,255)
    binc = randint(25,50)
    
    for x in range(startx, endx):
        #red value incrementation
        if r + rinc > 255 or r + rinc < 0:
            rinc = -rinc
        else:
            r += rinc
        #green value incrementation  
        if g + ginc > 255 or g + ginc < 0:
            ginc = -ginc
        else:
            g += ginc
        #blue value incrementation
        if b + binc > 255 or b + binc < 0:
            binc = -binc
        else:
            b += binc
            
        ledmatrix.set_pixel(x, y, r, g, b)
        ledmatrix.show()
        sleep(wait)
        y -= 1
        

#clear board
def clear():
    for x in range(0,7):
        for y in range(0,7):
            ledmatrix.set_pixel(x,y,0,0,0)
    ledmatrix.show()
    sleep(meh)


#letters
        
def A():
    vertLine(0,4,1)
    NELine(1,4,4)
    SELine(3,6,6)
    vertLine(0,4,5)
    horzLine(1,6,3)
    ledmatrix.clear()
    sleep(meh)
    

def B():
    vertLine(0,6,1)
    horzLine(1,4,6)
    SELine(3,5,6)
    vertLine(4,5,4)
    NELine(3,5,3)
    horzLine(2,3,3)
    vertLine(1,3,4)
    horzLine(2,4,0)
    ledmatrix.clear()
    sleep(meh)
    
    
def C():
    vertLine(2,5,1)
    NELine(1,4,4)
    SELine(1,4,2)
    horzLine(4,5,6)
    horzLine(4,5,0)
    ledmatrix.clear()
    sleep(meh)
    

def D():
    vertLine(0,6,1)
    horzLine(1,4,6)
    horzLine(1,4,0)
    SELine(4,6,6)
    NELine(4,6,0)
    vertLine(2,5,5)
    ledmatrix.clear()
    sleep(meh)
    

def E():
    vertLine(0,6,1)
    horzLine(1,6,6)
    horzLine(1,4,3)
    horzLine(1,6,0)
    ledmatrix.clear()
    sleep(meh)


def F():
    vertLine(0,6,1)
    horzLine(1,6,6)
    horzLine(1,4,3)
    ledmatrix.clear()
    sleep(meh)
    
    
def G():
    vertLine(2,5,1)
    NELine(1,4,4)
    SELine(1,4,2)
    horzLine(4,5,6)
    horzLine(4,5,0)
    vertLine(1,4,5)
    horzLine(3,6,3)
    ledmatrix.clear()
    sleep(meh)
    

def H():
    vertLine(0,7,1)
    vertLine(0,7,5)
    horzLine(1,6,3)
    ledmatrix.clear()
    sleep(meh)
    
    
def I():
    vertLine(0,7,3)
    horzLine(1,6,6)
    horzLine(1,6,0)
    ledmatrix.clear()
    sleep(meh)    


def J():
    vertLine(1,7,5)
    NELine(4,6,0)
    SELine(2,4,1)    
    ledmatrix.clear()
    sleep(meh) 

def K():
    vertLine(0,7,1)
    NELine(2,6,3)
    SELine(3,6,2)
    ledmatrix.clear()
    sleep(meh)


def L():
    vertLine(0,7,1)
    horzLine(1,6,0)
    ledmatrix.clear()
    sleep(meh)


def M():
    vertLine(0,7,1)
    vertLine(0,7,5)
    SELine(1,4,6)
    horzLine(4,5,5)
    ledmatrix.clear()
    sleep(meh)
    
    
def N():
    vertLine(0,7,1)
    vertLine(0,7,5)
    SELine(1,5,6)
    ledmatrix.clear()
    sleep(meh)


def O():
    vertLine(1,6,1)
    horzLine(2,4,6)
    horzLine(2,4,0)
    SELine(4,6,6)
    NELine(4,6,0)
    vertLine(2,5,5)
    ledmatrix.clear()
    sleep(meh)


def P():
    vertLine(0,7,1)
    horzLine(2,4,6)
    horzLine(2,4,3)
    vertLine(4,6,4)
    ledmatrix.clear()
    sleep(meh)


def Q():
    vertLine(1,6,1)
    horzLine(2,4,6)
    horzLine(2,4,0)
    SELine(4,6,6)
    NELine(4,6,0)
    SELine(3,7,3)
    vertLine(2,5,5)
    ledmatrix.clear()
    sleep(meh)
    

def R():
    vertLine(0,7,1)
    horzLine(2,4,6)
    horzLine(2,4,3)
    vertLine(4,6,4)
    SELine(3,7,3)
    ledmatrix.clear()
    sleep(meh)


def S():
    horzLine(1,6,0)
    vertLine(0,3,5)
    horzLine(1,6,3)
    vertLine(3,7,1)
    horzLine(1,6,6)
    ledmatrix.clear()
    sleep(meh)
    

def T():
    vertLine(0,7,3)
    horzLine(1,6,6)
    ledmatrix.clear()
    sleep(meh)
    

def U():
    vertLine(1,7,1)
    horzLine(2,4,0)
    NELine(4,6,0)
    vertLine(2,7,5)
    ledmatrix.clear()
    sleep(meh)
    
    
def V():
    vertLine(4,7,1)
    vertLine(1,4,2)
    vertLine(0,1,3)
    vertLine(1,4,4)
    vertLine(4,7,5)
    ledmatrix.clear()
    sleep(meh)
 
 
def W():
    vertLine(0,7,1)
    vertLine(0,7,5)
    NELine(1,4,0)
    horzLine(4,5,1)
    ledmatrix.clear()
    sleep(meh)
 

def X():
    NELine(0,7,0)
    SELine(0,7,6)
    ledmatrix.clear()
    sleep(meh)
    
    
def Y():
    vertLine(0,4,3)
    NELine(3,7,3)
    SELine(0,4,6)
    ledmatrix.clear()
    sleep(meh)
    
    
def Z():
    horzLine(1,6,6)
    NELine(1,6,1)
    horzLine(1,6,0)
    ledmatrix.clear()
    sleep(meh)
    
    
def OWO():
    horzLine(0,2,4)
    horzLine(0,2,5)
    SELine(1,3,2)
    NELine(2,4,1)
    NELine(4,6,1)
    horzLine(5,7,4)
    horzLine(5,7,5)
    ledmatrix.clear()
    sleep(meh)

    
def HEART():
    SELine(0,4,3)
    NELine(4,7,1)
    NELine(0,2,4)
    SELine(2,4,6)
    SELine(4,7,6)
    ledmatrix.clear()
    sleep(meh)
    

#show word in LED
def type(char):
    if char == 'A' or char == 'a':
        A()
    elif char == 'B' or char == 'b':
        B()
    elif char == 'C' or char == 'c':
        C()
    elif char == 'D' or char == 'd':
        D()
    elif char == 'E' or char == 'e':
        E()
    elif char == 'F' or char == 'f':
        F()
    elif char == 'G' or char == 'g':
        G()
    elif char == 'H' or char == 'h':
        H()
    elif char == 'I' or char == 'i':
        I()
    elif char == 'J' or char == 'j':
        J()
    elif char == 'K' or char == 'k':
        K()
    elif char == 'L' or char == 'l':
        L()
    elif char == 'M' or char == 'm':
        M()
    elif char == 'N' or char == 'n':
        N()
    elif char == 'O' or char == 'o':
        O()
    elif char == 'P' or char == 'p':
        P()
    elif char == 'Q' or char == 'q':
        Q()
    elif char == 'R' or char == 'r':
        R()
    elif char == 'S' or char == 's':
        S()
    elif char == 'T' or char == 't':
        T()
    elif char == 'U' or char == 'u':
        U()
    elif char == 'V' or char == 'v':
        V()
    elif char == 'W' or char == 'w':
        W()
    elif char == 'X' or char == 'x':
        X()
    elif char == 'Y' or char == 'y':
        Y()
    elif char == 'Z' or char == 'z':
        Z()
    else:
        clear()
        

        
###user input
##string = input("word?")
##
##if string == 'owo' or string == 'OWO':
##    OWO()
##elif string == 'heart' or string == 'HEART':
##    HEART()
##else:
##    chars = list(string)
##    for letter in chars:
##        type(letter)
##sleep(3)
##clear()
