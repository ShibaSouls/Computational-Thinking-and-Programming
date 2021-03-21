#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 10
#Name of Program -- Append File for Program 9 - Dismal Scientists
#Due Date -- 4/20/2020


def main():
    numProg = int(input('How many records of programmers do you want to add?\t'))

    progFile = open ('dismalscience.txt', 'a')

    for count in range (1, numProg + 1):
        print ('Enter data for programmer #' + str(count))
        name = input('Name: ')
        nation = input ('Nationality: ')
        progInvent = input ('What They Are Known for: ')

        progFile.write (name + '\n')
        progFile.write (nation + '\n')
        progFile.write (progInvent + '\n')

        print()

    progFile.close()

    print ('Programmer records written to dismalscience.txt.')


main()   

