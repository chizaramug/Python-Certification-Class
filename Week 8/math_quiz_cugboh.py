"""
Author: Chizaram, cugboh@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/09/2023

Description:
    This code spits out two random numbers that will be divided. If the user inputs the right number the code says congrats.
     If not, the right answer is ouputted.

Contributors:
    Lili lbrush@purdue.edu

My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [Y ] understand different ways to think about a solution
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
import random as r

"""Write new functions below this line (starting with unit 4)."""


def random_factor(a): #A function that returns a random integer
    b = r.randint(10 **(a-1) , 10**a - 1)
    return b


"""Start of actual code"""
def main():
    # Obtain two random variables
    one = random_factor(1) # Denominator 
    two = random_factor(2) # Numerator
    three = one*two
    
    ans = three/one

    print(f"{three:4}\n÷{one:3}\n----") # correct formatting

    guess = int(input('= ')) #Ask for users input

    if ans == guess:
       print ("Great job, that's correct!")
    else:
        print(f'Sorry, the correct answer is {round(ans)}.')
                     
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()