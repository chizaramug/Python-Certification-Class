"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 05.4 - Turtle Writing
Date: 10/02/2023

Description:
    This code draws certain # point star of the users asking.

Contributors:
    Kanari hirano0@purdue.edu

My contributor(s) helped me:
    [Y] understand the assignment expectations without
        telling me how they will approach it.
    [Y] understand different ways to think about a solution
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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    
    Asks = int(input('How many points do you want on the star: '))

    for star in range(0, Asks): #using loops we can make geometric patterns, in this case a star
        a = 360/Asks
        b = 2*a #Didn't know if I needed it
        #Starting at the bottom inner corner
        right(90-a) # getting accurate angle for first rotation
        forward(60) #length of the star line
        left(180-a) #Turning a corner
        forward(60) #length of the star line
        right(90-a) #Going back to start 
        
"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
