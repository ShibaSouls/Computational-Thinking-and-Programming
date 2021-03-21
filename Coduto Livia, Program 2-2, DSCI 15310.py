#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 2 - 2
#Name of Program -- Student Grade Average
#Due Date -- 2/14/2020

#The purpose of this program is to determine a student's final grade after a curve is given.
#Ask the student what the highest and lowest score was, as well as their own score.
highScore = float(input("What was the highest test score in the class? "))
lowScore = float(input("What was the lowest test score in the class? "))
youScore = float(input("What was your test score? "))
#This is the formula for the curve in the class.
curve = (highScore - lowScore) / 4
#This determines what the student's score is, as well as the highest possible score.
yourCurved = youScore + curve
topGrade = highScore + curve
#These are the values that will print, depending on the student's final grade.
if yourCurved < 60:
    print ("Must feel good to have wasted the semester taking this class\n just to get an F.\n Or maybe, you just didn't apply yourself?\n Your score is", yourCurved,)
 

elif yourCurved < 70:
    print ("Your score was", yourCurved, "\nYou know,\n if you're taking a class that accepts a D as acceptable,\n you should be very grateful.")

elif yourCurved < 80:
    print ("C's get degrees lmao, your score was\n", yourCurved)

elif yourCurved < 90:
    print ("B is pretty good I guess, your score is\n", yourCurved)

elif yourCurved < 100:
    print ("I can't really think of any witty things to say anymore,\n Congrats on your A,\n your score is", yourCurved)

elif yourCurved > 100 and yourCurved < topGrade:
 print ("Wowwwww, an A+. You must think you're really special huh?\n Don't let it go to your head.\n Your score is", yourCurved)

else:
 print ("Bro, go find some hobbies or something.\n Don't you have other things to do besides schoolwork?\n Anyways your score is", topGrade)
 
