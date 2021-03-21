#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 2 - 1
#Name of Program -- Temperature - Fahrenheit/Celsius
#Due Date -- 2/14/2020

#The purpose of this program is to calculate temperature in celsius (if value in entered in fahrenheit), and vice versa.
#Ask the user to input what temperature they are trying to calculate.
tempRate = float(input("Please enter a numerical value for the temperature that you are trying to\n measure. "))
#Ask the user to input if they are converting to celsius or fahrenheit.
cOrf = input("If you are converting your temperature to celsius, please enter C. If you are\n converting your temperature to fahrenheit, please enter F. ")
#These are the formulas for finding temperatures in celsius/fahrenheit.
cel = (5/9) * (tempRate - 32)
far = (9/5) * tempRate + 32
if cOrf == 'C':
    print("Your temperature in Celsius is", cel)
else:
    print("Your temperature in Fahrenheit is", far)
