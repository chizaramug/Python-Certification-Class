"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 06.4 - Spiral
Date: 10/09/2023

Description:
    Using a python prgram to draw the Archimedean spiral.

Contributors:
    Hanna, hletzrin@purdue.edu 

My contributor(s) helped me:
    [Y ] understand the assignment expectations without
        telling me how they will approach it.
    [ N] understand different ways to think about a solution
        without helping me plan my solution.
    [ N] think through the meaning of a specific error or
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
import math


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
   #Initialize the system, loops 
   speed (10) 
   x = 0
   y = 0
   theta = 1
   for theta in range(0,2160+1):# Need 6 360s so 6*360 = 2160
    #Need to convert  theta into radians for trif functions to work 
        x =(((theta)/(math.pi**2))*math.cos(theta*((math.pi)/180)))
        y =(((theta)/(math.pi**2))*math.sin(theta*((math.pi)/180)))
        goto(x,y)
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
