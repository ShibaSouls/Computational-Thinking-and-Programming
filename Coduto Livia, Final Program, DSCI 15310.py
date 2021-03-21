#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. Final
#Name of Program -- Final Exam Program
#Due Date -- 5/7/2020
print("Note: answers requiring decimals will only need to be\n rounded to the first 2 decimal points.")
print ("Hello! My name is Livia, welcome to my quiz!")
name = input("Please enter your name.\t")
print("it is so nice to meet you,", name, "! Good luck on the quiz!")

def main():
    score = 0
    qone = input("What is the value of π?\t")
    if qone == "3.14":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 3.14")


    qtwo = input("What is the value of φ?\t")
    if qtwo == "1.61":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 1.61")


    qthree = input("What is the value of e, the Euler number?\t")
    if qthree == "2.72":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 2.72")


    qfour = input("What is the value of What is the value of C, the Euler constant?\t")
    if qfour == "0.58":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 0.58")


    qfive = input("What is the largest digit in Base 2?\t")
    if qfive == "1":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 1")


    qsix = input("What is the largest digit in Base 8?\t")
    if qsix == "7":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 7")


    qseven = input("What is the largest digit in Base 16?\t")
    if qseven == "f":
        score += 1
        print("Correct! Good job,", name)
    elif qseven == "F":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is f or F")


    qeight = input("What is the value of the multiplier effect in economics?\t")
    if qeight == "2.50":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 2.50")


    qnine = input("If 100 is reduced by 10%, what is the result?\t")
    if qnine == "90":
        score += 1

    qten = input("If the result of question 9 is increased by 10%, what is the new result?\t")
    if qten == "99":
        score += 1
        print("Correct! Good job,", name)
    else:
        print("Incorrect,", name,". The correct answer is 99")

    print (name, ", you got", score, "out of 10 points.")

    if score <= int("5"):
        print ("You did not pass,", name, ". Go study!")
    else:
        print ("Good job,", name, "you passed!")

main()    



