#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 1 - 3
#Name of Program -- Paint
#Due Date -- 2/7/2020

#The purpose of this program is to determine how many cans of paint the Abernathys will need to paint their home.
#Input general information about all of the rooms.
wallWidth = float(input("What is the width of the wall? "))
roomNumber = float(input("How many rooms are being painted? "))
#Give a name for each room.
roomOne = (input("What is the name of the first room? "))
roomTwo = (input("What is the name of the second room? "))
roomThree = (input("What is the name of the third room? "))
roomFour = (input("What is the name of the fourth room? "))
roomFive = (input("What is the name of the fifth room? "))
roomSix = (input("What is the name of the sixth room? "))
#Calculate how many buckets of paint each room will need.
feetOne = (wallWidth * 12 * 5) / 350
feetTwo = (wallWidth * 12 * 5) / 350
feetThree = (wallWidth * 12 * 5) / 350
feetFour = (wallWidth * 12 * 5) / 350
feetFive = (wallWidth * 12 * 5) / 350
feetSix = (wallWidth * 12 * 5) / 350
#Calculate how many buckets of paint the whole house will need.
totalPaint = (wallWidth * 12 * 5 * roomNumber) / 350
#Show the total amount of paint for each room, as well as for the whole house.
print("The total buckets of paint", roomOne, "will need is", feetOne)
print("The total buckets of paint", roomTwo, "will need is", feetTwo)
print("The total buckets of paint", roomThree, "will need is", feetThree)
print("The total buckets of paint", roomFour, "will need is", feetFour)
print("The total buckets of paint", roomFive, "will need is", feetFive)
print("The total buckets of paint", roomSix, "will need is", feetSix)
print("The total buckets of paint for the whole house is", totalPaint)

