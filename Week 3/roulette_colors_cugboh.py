"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/11/2023

Description:
    This program askes user to input a number 1 to 36 and it outputs either green, red or black.
Contributors:
    

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
    Color = int(input("Please choose a pocket number: ")) #Askes user for a nuber 0 through 36
    if Color == 0:
        print (f"  Pocket number {Color} is green.") #Follow the strict rules for black and red
    elif Color in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
         print (f"  Pocket number {Color} is red.")
    elif Color in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        print (f"  Pocket number {Color} is black.")
    else: 
        print ("  Invalid Input!") #If the number is less than 0 it is invalid
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()