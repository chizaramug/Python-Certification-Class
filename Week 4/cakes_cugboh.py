"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/18/2023

Description:
    This program creates a computerized star cake based on the input given.
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
    #Setting up variables 
    Layer = int(input('Enter the number of layers: ' ))
    spaces = Layer - 1
    Stars = 1
    for i in range (0, Layer):
        for j in range (spaces):
            print(' ', end ='') #Print a space
        spaces -= 1 #Makes the space indentation decrease by 1
        print('[', end ='')
        for k in range(Stars): #This loop calls for the stars and begins the loop
            print('*', end = '')
        Stars += 2 #Every row increases by 2 stars
        print(']')
            
            
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()