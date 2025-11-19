"""
Author:  Chizaram, cugboh@purdue.edu
Assignment: 05.2 - Spiral
Date: 10/02/2023

Description:
   Creates a spiral using a for loop

Contributors:
   TA, didn't catch name

My contributor(s) helped me:
    [Y] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
        without helping me plan my solution.
    [N ] think through the meaning of a specific error or
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
from turtle import * # import all the objects of the turtle module

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)
    

def main():
    speed(10)

    for spiral in range(1, 43): #using loops we can make geometric patterns, in this case a spiral
        forward(spiral*4)
        left (45)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
