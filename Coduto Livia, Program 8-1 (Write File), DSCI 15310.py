#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 8 - 1
#Name of Program -- Write File
#Due Date -- 4/6/2020

def main():
    outfile = open ('math.txt', 'w')

    outfile.write ('Benjamin Banneker\n')
    outfile.write ('Stefan Banach\n')
    outfile.write ('Omar Khayyam\n')

    outfile.close()

main()
    

