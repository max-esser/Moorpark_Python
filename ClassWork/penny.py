'''
!/usr/bin/python
-*- coding: utf-8 -*-
===============================================================================

         FILE: penny.py 

        USAGE: python3 penny.py

  DESCRIPTION: program that calculates the amount of money a person would 
                earn over a period of time if his or her salary is one penny 
                the first day, two pennies the second day, and continues to 
                double each day.
       
       AUTHOR: Max Esser 
      VERSION: 1.0
      CREATED: 01/28/2019
     REVISION: 1.0
===============================================================================
'''
day = int(input('How many days did you work?: '))
start = 1
end = day
amount_start = 0.01

print()
print('Day     Amount ($)')
print('---     ----------')

for day in range(start, end + 1):
    amount_end = amount_start * 2
    print('{0:.2f}  |   {1:.2f}'.format(day, amount_end))
    amount_start = amount_end