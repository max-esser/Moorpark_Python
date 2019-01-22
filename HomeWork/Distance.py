'''
    Program Name: Distance.py
    Programmer: Max Esser
    Date: 01-09-2019
    Version: 1.0
    Taking the user input of speed and time to calulate distance (distance=speed*time)
'''

#user input varibles. 
speed=int(input('Enter the speed that you are traveling: '))
time=int(input('Enter the first duration travled: '))
time_2=int(input('Enter the second duration travled: ' ))
time_3=int(input('Enter the third duration travled: '))

# varibles.
total = speed * time
total2 = speed * time_2
total3 = speed * time_3

#printing a chart rows list  Hours and the distance traveld.
print 'Hours | Distnace Traveled'
print'---------------------------------'

#printing the sum of speed * time = distance using format function to sanitize string.
print("{0}   | {1} miles".format(time, total))
print("{0}   | {1} miles".format(time_2, total2))
print("{0}   | {1} miles".format(time_3, total3))



