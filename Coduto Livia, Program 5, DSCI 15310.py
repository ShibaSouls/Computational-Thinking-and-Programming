#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 5
#Name of Program -- Palindromes
#Due Date -- 3/7/2020

#The purpose of this program is to determine how many numbers in a given range of numbers are palindromes.
#Ask the user to input 2 sets of 4 digit numbers.
print ("This program will determine the number of palindromes in a range of numbers.")
setOne = int(input("Please enter the first four digit number.\t"))
setTwo = int(input("Please enter the second four digit number.\t"))
#This counter will determine how many palindromes are present within the set of numbers input.
counter = 0

while setOne <= setTwo:
    setOne = str(setOne)

    if setOne[0] == setOne[3] and setOne[1] == setOne[2]:

        counter = counter + 1
        print (setOne)

    setOne = int(setOne)
    setOne = setOne + 1

print ("There are", counter, "four-digit palindromes present in your range of numbers.")

