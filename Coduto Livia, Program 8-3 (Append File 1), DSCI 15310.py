#Livia Coduto
#DSCI 15310 -- Computational Thinking and Programming
#Program No. 8-3
#Name of Program -- Append File 1
#Due Date -- 4/6/2020

def main():
    outfile = open ('math.txt', 'a')

    outfile.write ('John Venn\n')
    outfile.write ('Pierre de Fermat\n')
    outfile.write ('Maria Gaetana Agnesi\n')

    outfile.close()

main()

    

