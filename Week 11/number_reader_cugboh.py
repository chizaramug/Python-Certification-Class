"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.5 - Number Reader
Date: 10/23/2023

Description:
    This program reads the random numbers from a text file and calculates a list of requirements, such as the number of random numbers.
Contributors:
    
Alex (green450@purdue.edu)
My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
        without helping me plan my solution.
    [Y] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


"""Import additional modules below this line (starting with unit 6)."""
import random as r

"""Write new functions below this line (starting with unit 4)."""
def main():
    with open('random_numbers.txt', 'r') as fo:
        #This part separates the text by spaces so that Python can count the separated words to tally up the total amount of words
        all = fo.read()
        word = all.split('\n')
        num =[]
        for y in word: 
            if  y.strip() != '':
                
                a = int(y.strip())
            
                num.append(a)
        count_line = len(num) #how many words present
        minn = min(num) #min amount of words
        maxn = max(num) #max amount of words
        print(f'{count_line:,} numbers were read from the file.')
       
        #program calculations for output
        sumn = sum(num) #addition of each number
        avgn = sumn/ count_line #addition of each number / total word count
        #Correct formatting of output
        print(f"Min: {minn:,d}")
        print(f"Max: {maxn:,.0f}")
        print(f"Sum: {sumn:,d}")
        print(f"Avg: {avgn:,.1f}")
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()