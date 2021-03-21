#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 7 
#Name of Program -- Another for Loop 
#Due Date -- 3/20/2020

#The purpose of this program is to practice using a for loop defined by a range.
#Print the number and its square root, cube root, square, and cube.
def main():
    print('number\tsqroot\tcuberoot square\tcube')
    print('-----------------------------------------------------------------')
    for num in range (1,16,2):
        sqroot = round((num ** (1/2)),2)
        cuberoot = round((num ** (1/3)),2)
        square = num ** 2
        cube = num ** 3
        print(num, '\t', sqroot, '\t', cuberoot, '\t', square, '\t', cube, '\t')

main()
    

