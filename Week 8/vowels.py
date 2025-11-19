"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/09/2023

Description:
   This program picks a random vowel from the english language. This is the module file.

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

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *


"""Write new functions below this line (starting with unit 4)."""


def draw_a():
    goto(-250,0)
    pendown()
    circle(25)
    penup()
    forward(25)
    setheading(90)
    pendown()
    forward(50)
    print(position(),"a")
    penup() 
    backward(50)
    setheading(0)
    print(position(),"a")



def draw_e():
    setheading(90)
    forward(25)
    setheading(0)
    pendown()
    forward(47)
    left(90)
    circle(25,310)
    penup() 
    setheading(0)
    print(position(),"e")


def draw_i():
    setheading(90)
    backward (6)
    pendown()
    forward(40)
    penup()
    forward (20)
    pendown()
    circle(1)
    setheading(0)
    penup()

def draw_o():
    penup()
    setheading(90)
    forward (20)
    setheading(270)
    backward(-60)
    pendown()
    circle(25)
    print(position(),"o")
    setheading(0)
    penup()


def draw_u():
    penup()
    setheading(90)
    forward(23)
    setheading(270)
    pendown()
    forward(35)
    circle(15,180)
    forward(35)
    backward(50)
    setheading(0)  
    print(position(),"u")
    penup()


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
    speed (10)
    penup()
    forward(50)
    draw_a()
    forward(65)
    draw_e()
    forward(59)
    draw_i()
    forward(70)
    draw_o()
    forward(100)
    draw_u()
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
