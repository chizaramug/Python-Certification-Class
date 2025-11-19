"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.3 - File Stats
Date: 10/23/2023

Description:
    This program reads the contents of a file and calculates the # of words, 
    # of non-blank lines and the average # of words per non-blank line within the file.
Contributors:
    AJ, ajawaji@purdue.edu

My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
        without helping me plan my solution.
    [N] think through the meaning of a specific error or
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

"""Write new functions below this line (starting with unit 4)."""
def main():
    count_line = 0
    #This part separates the text by spaces so that Python can count the separated words to tally up the total amount of words
    with open('frontiero_v_richardson.txt', 'r') as fo:
        all = fo.read()
        word = all.split()
    #This part separates the text by line, first by reading line by line and then ensuring only the that is counted and not the new line
    with open('frontiero_v_richardson.txt', 'r') as fo:
        lines = fo.readlines()
        for i in lines:
            if i!='\n':
                count_line+=1
   #Calculations     
    NW = len(word)
    NL = count_line
    Avg = NW/NL
    #Achieve correct formatting:
    print(f'Total number of words: {NW}')
    print(f'Total number of lines: {NL}')
    print(f'Average number of words per line: {Avg:.1f}')

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()