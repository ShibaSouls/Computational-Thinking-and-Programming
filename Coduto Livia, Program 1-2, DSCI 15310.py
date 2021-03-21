#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 1-2
#Name of Program -- Mortgage Payment
#Due Date -- 2/7/2020

#The purpose of this prgram is to determine an annual & monthly mortgage payment.
#These are initial inputs required to calculate the loan.
principal = float(input("How much money is the loan? "))
interestRate = float(input("What is the annual interest rate? Use decimals or whole numbers for your answer. "))
duration = int(input("How many years is the loan duration? "))
#This is a formula to express annual interest.
annualPayment = principal * interestRate / (1 - (interestRate + 1)**-duration)
#Show the annual mortgage payment.
print("Your annual mortgage is", annualPayment)

#Input values for the monthly principal.
monthPrincipal = float(input("How much money is the loan? "))
monthRate = float(input("What is the monthly interest rate? Use decimals or whole numbers for your answer. "))
durationMonths = int(input("How many years is the loan duration? "))
#Formula to express monthly interest.
monthlyPayment = annualPayment / 12
#Show the monthly mortgage payment.
print("Your monthly mortgage is", monthlyPayment)




