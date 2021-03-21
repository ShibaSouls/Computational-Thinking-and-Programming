#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 9-2 
#Name of Program -- Dismal Scientists - Read File
#Due Date -- 4/13/2020

def main():
    progFile = open ('dismalscience.txt', 'r')
    name = progFile.readline()

    while name:

        nation = progFile.readline()
        progInvent = progFile.readline()

        name = name.rstrip('\n')
        nation = nation.rstrip('\n')
        progInvent = progInvent.rstrip('\n')

        print ('Name:', name)
        print ('Nationality:', nation)
        print ('What they are known for:', progInvent)
        print()

        name = progFile.readline()

    progFile.close()

main()
    

    

