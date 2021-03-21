#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 4
#Name of Program -- Function Calculations
#Due Date -- 2/22/2020

#The purpose of this program is to calculate different roots, as well as other math calculations, using functions.
#First, we import math in order to get an accurate value of pi.
import math

#The purpose of this first function is to be able to give a result for the variable "answer".
def allCalc (number, exponent):
    answer = number ** exponent
    print ("your answer is: ", answer)

#This next function determines the area of a circle, based on given diameter.
def CircleA (constant, dimension, exponent):
    answer = constant * dimension ** exponent
    print ("Your answer is %.2f " %(answer))

#This next section is where the user inputs their desired numbers, in order to get specific calculations.
numOne = int(input("Put input the number you want squared.\t"))
allCalc (numOne, 2)

numTwo = int(input("Please input the number that you want cubed.\t"))
allCalc (numTwo, 3)

numThree = int(input("Please inout a number you would like the dquare root of.\t"))
allCalc (numThree, (1/2))

numFour = int(input("Please input a number you would like the cube root of.\t"))
allCalc (numFour, (1/3))

circDiam = int(input("Please input the diameter of a circle you want the area of.\t"))
CircleA(math.pi, circDiam / 2, 2)
