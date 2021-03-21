#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 3 - 2 
#Name of Program -- 1089 and All That
#Due Date -- 2/15/2020

#The purpose of this program is to show that the sum of two three-digit numbers, derived from the difference of two other three-digit numbers, is 1089.
#Ask the user to input a number.
mainNum = str(input("Please enter a three digit number.\n Make sure that the difference between the first and\n third number is a postitive difference\n of at least 2.\t"))
#Swap the first and last digits of the number, and subtract the difference.
swapOne = str(mainNum)[::-1]
differenceOne = int(mainNum) - int(swapOne)
print("First step, your number swapped around is", swapOne)
print ("Subtracting the original and swapped number gives you", differenceOne)
#Take the difference and switch its first and third digits.
swapTwo = str(differenceOne) [::-1]
print ("Swapping the difference number gets you", swapTwo)
#Add the difference and the second swapped number.
endTotal = (differenceOne) + int(swapTwo)
#Print results depending on if the endTotal is equal to 1089 or not.
if endTotal == 1089:
    print ("Your end total is 1089, Congrats!")

else:
    print("Your number did not equal 1089,\n please check to make sure the first and\n third digits of your number\n have a positive difference of at least 2.") 





    

