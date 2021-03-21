#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 3 - 1
#Name of Program -- Point of Pizza
#Due Date -- 2/15/2020

#The purpose of this program is to determine if getting 2 medium pizzas instead of 1 large is a good deal or a ripoff.
#First, ask the user what the radius is of a medium and a large pizza.
largeZa = float(input("Oh no! The pizza place ran out of large pizzas,\n so they gave you 2 mediums instead.\n What is the radius of the large pizza?\t"))
mediumZa = float(input("What is the radius of one of the medium pizzas?\t"))
#This is the formula to determine the area of the pizzas.
pi = 3.141592653589793
largeArea = pi * (largeZa)**2
mediumArea = pi * (mediumZa)**2 * 2
#This section of code shows what will print if the medium pizzas have a bigger area, and vice versa.
if largeArea > mediumArea:
    print("You got ripped off!\n Call the pizza company and demand a refund!")

elif mediumArea > largeArea:
    print("Nice! The 2 medium pizzas have more area than the large,\n so you just got yourself extra pizza!")

else:
    print("Both pizzas have the same exact area,\n so it doesn't make a difference if you get 1 large or 2 mediums.")


