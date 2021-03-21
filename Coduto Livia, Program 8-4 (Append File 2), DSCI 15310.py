#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 8-4 
#Name of Program -- Append File 2
#Due Date -- 4/6/2020

def main():
    outfile = open ('math.txt', 'a')

    outfile.write ('David Hilbert\n')
    outfile.write ('Henri Poincaré\n')
    outfile.write ('Bernhard Riemann\n')
    outfile.write ('Niels Henrik Abel\n')

    outfile.close()

main()

    

