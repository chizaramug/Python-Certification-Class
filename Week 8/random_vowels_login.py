"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/09/2023

Description:
This program picks a random vowel from the english language. This is the actual program file.

Contributors:
    Lili lbrush@purdue.edu

My contributor(s) helped me:
    [Y] understand the assignment expectations without
        telling me how they will approach it.
    [Y] understand different ways to think about a solution
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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import random as r #getting my random module
import vowels as v #importing my vowels from the module file
"""Write new functions below this line (starting with unit 4)."""



def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    start()
    speed (10) 
    
    Cupid = ['a','e','i','o','u'] #shuffles the order oof the letters
    r.shuffle(Cupid)
    
    for i,l in enumerate(Cupid):  # Loop that draws the letter shuffled
        if l == 'a':
            setheading (0)
            v.draw_a()
        elif l == 'e':
            setheading (0)
            v.draw_e()
        elif l == 'i':
            setheading (0)
            v.draw_i()
        elif l == 'o':
            setheading (0)
            v.draw_o()
        elif l == 'u':
            setheading (0)
            v.draw_u()  
        forward(70)

   

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
