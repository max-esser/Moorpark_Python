'''
!/usr/bin/python
-*- coding: utf-8 -*-
===============================================================================

         FILE: paint_estimator.py 

        USAGE: python3 paint_estimator.py

  DESCRIPTION: This program estimates the Gallons of paint, Hours of labor,
                paint charges, labor charges, and the total cost. For a room 
                to be painted, by taking the user input values for Wall space 
                in square feet, and price per gallon of paint. 
       
       AUTHOR: Max Esser 
      VERSION: 1.0
      CREATED: 01/22/2019
     REVISION: 1.0
===============================================================================
'''
# Set varibales for feet per gallon, labor hours, and labor charge
ft_per_gal = 115
labor_hrs = 8
labor_charge = 20

# Function for user input for squar feet, and paint cost.
def main():
  sqrFt = int(input("Enter wall space in square feet: "))
  paintCost = float(input("Enter paint price per gallon: "))
  
  
  paint(sqrFt, paintCost)
 
 # Defined Function for Calculation. 
def paint(sqrFt, paintCost):
  paintGals = sqrFt / ft_per_gal
  labor = labor_hrs * paintGals
  paintCharge = paintGals * paintCost
  laborCost = labor * labor_charge
  total = paintCharge + laborCost
  
  totalCost(paintGals, labor, paintCharge, laborCost, total)
  
# Output fucntion   
def totalCost(paintGals, labor, paintCharge, laborCost, total): 
  print('Gallons of paint: {0:.0f}'.format(paintGals))
  print('Hours of labor: {0:.0f}'.format(labor))
  print('Paint charges: ${0:.2f}'.format(paintCharge)) 
  print('Labor charges: ${0:.2f}'.format(laborCost))  
  print('Total cost: ${0:.2f}'.format(total))  

# Call main   
main()