'''
!/usr/bin/python
-*- coding: utf-8 -*-
===============================================================================

         FILE: C_to_F.py 

        USAGE: python3 C_to_F.py

  DESCRIPTION: This program takes imput of Celsius and converts 
                it to Faherinte, doesnt allow values lower then -60C 
                and nothing above 200C.
       
       AUTHOR: Max Esser 
      VERSION: 1.0
      CREATED: 01/23/2019
     REVISION: 1.0
===============================================================================
'''
def conv_intro():
    print("Welcome to Temp Convertor")
    print("Tell me what temperture in Celsius")
    print("I can convert it to Farenheit")
    print("Let's Go")

def main():
    conv_intro()
    get_cels = float(input('What is the temperture in Celcius: '))
    if get_cels < -65:
        print('Not in range -65 -200')
    elif get_cels > 200: 
        print('Not in range of -65 - 200')
    else:
        conv_f = (get_cels * 1.8) + 32
        print('The temp in Fahrenheit is {0}'.format(conv_f))

# Call main
main()
