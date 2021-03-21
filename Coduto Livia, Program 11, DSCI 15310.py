#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 11
#Name of Program -- Prime Numbers
#Due Date -- 5/1/2020

import random
def main ():
    qount = int(input("How many random numbers would you like?\t"))
    for count in range (qount):
        number = random.randint (1,100)
        if number == 1:
            print ("The number", number, "is not a prime number.")
        elif number == 2 or number == 3 or number == 5 or number == 7:
            print ("The number", number, "is a prime number.")
        elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            print ("The number", number, "is a prime number.")
        else:
            print ("The number", number, "is not a prime number.")

main()

            

    

