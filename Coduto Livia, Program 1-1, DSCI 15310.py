#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 1 - 1
#Name of Program -- New Salary/Wages
#Due Date -- 2/7/2020

#The purpose of this program is to determine the new salary of an employee who just earned a raise.
#Get the current salary of the employee.
salaryNow = float(input("Current Salary?\t\t"))
#Percentage of the raise
raisePercent = float(input("Using Decimals, what is the percentage of the raise?\t\t"))
#New Salary
raiseMoney = salaryNow * raisePercent
print ('Your new salary is', raiseMoney + salaryNow)
