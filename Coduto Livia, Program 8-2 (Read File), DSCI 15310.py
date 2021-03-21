#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 8-2 
#Name of Program -- Read File
#Due Date -- 4/6/2020

def main():
    infile = open ('math.txt', 'r')

    fileContents = infile.read()

    infile.close()

    print (fileContents)

main()

    

