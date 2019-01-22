'''
!/usr/bin/python
-*- coding: utf-8 -*-
===============================================================================

         FILE: bmi.py 

        USAGE: python3 bmi.py

  DESCRIPTION: This program is going to calculate a users BMI
		and tell them if they are underweight, overweight, or normal.
       
       AUTHOR: Max Esser 
      VERSION: 1.0
      CREATED: 01/15/2019
     REVISION: 1.0
===============================================================================
'''
# This is just a small intro to explain the program to the user
def bmi_intro():
    print("Welcome to BMI calculator")
    print("If you cant tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Let's Go")

# This is the main program where we get the user input and
# calculate the Body Mass Index. 
def main(): 
    bmi_intro()
    get_height = float(input('What is your height in inches: '))
    get_weight = float(input('What is your weight in lbs: '))
    get_bmi = (get_weight * 703) / (get_height ** 2)
    
    # If the vaule of get_bmi is less then 18.5 then it will print underweight
    # If the value is over 18.5 then we jump to the next statment
    if get_bmi < 18.5:    
        print('A person with a BMI of {0:.2f} is underweight'.format(get_bmi))
   
    # If the value of get_bmi is greater then 25.0 the it will print overweight
    # If the value is less then 25.0 and greater then 18.5 then we move on to the next statment
    elif get_bmi > 25.0:
        print('A person with a BMI of {0:.2f} is overweight'.format(get_bmi))
    
    # If the value of get_bmi is greater then 18.5 and less then 25.0 then 
    # we print print normal for the BMI
    else: 
        print('A person witha BMI of {0:.2f} is normal'.format(get_bmi))  

# Calling Main Function 
main()
