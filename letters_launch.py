from letters import type, clear, OWO, HEART
from time import sleep


#user input
string = input("Type your message here: ")

if string == 'owo' or string == 'OWO':
    OWO()
elif string == 'heart' or string == 'HEART':
    HEART()
else:
    chars = list(string)
    for letter in chars:
        type(letter)
        
sleep(2)
clear()

