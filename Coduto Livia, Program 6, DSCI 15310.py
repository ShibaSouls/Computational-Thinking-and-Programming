#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 6
#Name of Program -- The "for" Loop 
#Due Date -- 3/14/2020

#The purpose of this program is to practice the use of the "for" loop, by making a program that displays all odd numbers between 1 and 12.
print("Here are the odd numbers from 1 to 12.")

for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]:
    oddNum = num % 2
    if oddNum == 1:
        print(num)
    else:
        num +=1
