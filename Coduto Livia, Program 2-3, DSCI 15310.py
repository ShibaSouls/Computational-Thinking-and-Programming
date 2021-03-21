#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 2 - 3
#Name of Program -- Name Game
#Due Date -- 2/14/2020

#The purpose of this program is to print out the "Name Game", using any name.
#Input the person's name.
yourName = input("What is your name?\t")
#This is the beginning of the Name Game, which just states the person's name.
print (yourName + "!")
print (yourName, yourName)
#This code changes what letters appear in front of the name if it starts with a vowel.
if yourName[0] == "A" or yourName[0] == "E" or yourName[0] == "I" or yourName[0] == "O" or yourName[0] == "U":
    yourName2 = yourName.lower()
    print ("Bo B" + yourName2)
    print ("Banana Fanna Fo F" + yourName2)
    print ("Fee Fi Mo M" + yourName2)
    print (yourName + "!")

#This section of code is for the "Contrary Rule", in which a person's name starts with the letter B, F, or M.
elif yourName[0] == "B":
    yourNameB = yourName[1:]
    print ("Bo-" + yourNameB)
    print ("Banana Fanna Fo F" + yourNameB)
    print ("Fee Fi Mo M" + yourNameB)
    print (yourName + "!")


elif yourName[0] == "F":
    yourNameF = yourName[1:]
    print ("Bo B" + yourNameF)
    print ("Banana Fanna Fo-" + yourNameF)
    print ("Fee Fi Mo M" + yourNameF)
    print (yourName + "!")


elif yourName[0] == "M":
    yourNameM = yourName[1:]
    print ("Bo B" + yourNameM)
    print ("Banana Fanna Fo F" + yourNameM)
    print ("Fee Fi Mo-" + yourNameM)
    print (yourName + "!")

#This section of code is the part of the Name Game that will appear if the person's name does not begin with a vowel, B, F, or M.
else:
    yourNameother = yourName[1:]
    print ("Bo B" + yourNameother)
    print ("Banana Fanna Fo F" + yourNameother)
    print ("Fee Fi Mo M" + yourNameother)
    print (yourName + "!")
