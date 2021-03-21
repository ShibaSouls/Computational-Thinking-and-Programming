#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. Midterm
#Name of Program -- Temperature - Fahrenheit/Celsius/Kelvin
#Due Date -- 3/7/2020

#The purpose of this program is to calculate temperature in celsius (if value in entered in fahrenheit), and vice versa. Additonally, convert temperatures to Kelvin.
#Ask the user to input what temperature they are trying to calculate.
tempRate = float(input("Please enter a numerical value for the temperature that you are trying to\n measure. "))
#Ask the user to input if they are converting to celsius, fahrenheit, or Kelvin.
tempType = input("Please input the following based on temperature type:\n Fahrenheit to Celsius - Please enter C\n Celsius to Fahrenheit - Please enter F\n Kelvin to Fahrenheit - Please enter KF\n Kelvin to Celsius - Please enter KC\n Fahrenheit to Kelvin - Please enter FK\n Celsius to Kelvin - Please enter CK \t")
#These are the formulas for finding temperatures in celsius/fahrenheit/Kelvin.
fartocel = (5/9) * (tempRate - 32)
celtofar = (9/5) * tempRate + 32
kelfar = (tempRate - 273.15) * (9 / 5) + 32
kelcel = tempRate - 273.15
farkel = (tempRate - 32) * (5 / 9) + 273.15
celkel = tempRate + 273.15
if tempType == 'C':
    print("Your temperature in Celsius is", fartocel)

elif tempType == 'F':
    print("Your temperature in Fahrenheit is", celtofar)

elif tempType == 'KF':
    print("Your temperature in Fahrenheit is", kelfar)

elif tempType == 'KC':
    print("Your temperature in Celsius is", kelcel)

elif tempType == 'FK':
    print("Your temperature in Kelvin is", farkel)

else:
    print("Your temperature in Kelvin is", celkel)
