"""
Author:  Chizaram Ugboh, cugboh@purdue.edu
Assignment: 05.4 - Turtle Writing
Date: 10/02/2023

Description:
   This code uses the turtle module to spell out the word 'Hammer Down"

Contributors:
   Prof. Cole jhcole@purdue.edu

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


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")


def draw_D():
    pendown()
    setheading (270) 
    forward (100) #Stem of the D
    print(position(),"Dh")
    left(90)
    forward (20)
    #Create curve of D
    circle(50,180)
    setheading(180)
    forward (20)
    print(position(),"D")
    penup()
    



def draw_H():
    """Write this function."""
    
    right (90) 
    forward (100) 
    penup()
    goto(-250,100) #moving towards horizontal line
    pendown()
    left(90)
    forward(50) 
    right(90)
    forward (50) #First Half of 2nd leg
    penup()
    goto(-200,100)
    pendown()
    left(180)
    forward (50)
    print(position(),"H")
    penup()

def draw_a():
    goto(-125,75)
    pendown()
    circle(25)
    penup()
    goto(-125,50)
    pendown()
    forward(50)
    print(position(),"a")
    penup() 

def draw_e():
    goto (70,75)
    pendown()
    left(90)
    forward(47)
    print(position(),"e")
    left(90)
    circle(25,310)
    penup()
    
   
    

def draw_m():
    goto(-100,50)
    pendown()
    forward(35)
    circle(-15,180)
    right(0)
    forward(35)
    penup()
    right(180)
    forward(35)
    pendown()
    circle(-15,180)
    forward(35)
    print(position(),"m1")
    penup()
    
    # writing m again
    goto(-15,50)
    pendown()
    right(180)
    forward(35)
    circle(-15,180)
    right(0)
    forward(35)
    penup()
    right(180)
    forward(35)
    pendown()
    circle(-15,180)
    forward(35)
    print(position(),"m")
    penup()

def draw_n():
    goto(-6,-100)
    setheading(90)
    pendown()
    forward(50)
    penup()
    backward(19)
    pendown()
    circle (-15,180)
    forward(31)
    print(position(),"n")
    penup()

def draw_o():
    goto(-140,-50)
    pendown()
    circle(25)
    print(position(),"o")
    penup()
    
def draw_r():
    goto(145,50)
    pendown()
    setheading(90)
    forward(50)
    penup()
    backward(25)
    pendown()
    circle (-15,140)
    penup()

def draw_w():
    penup()
    setheading(270)
    goto(-93,-50)
    pendown()
    forward(35)
    circle(15,180)
    forward(35)
    penup()
    backward(35)
    pendown()
    print(position(),"w")
    circle(-15,-180)
    forward(-35)
    penup()

def main():
    
    speed (10)
    penup()
    goto(-250,150)
    pendown()
    #Spell out Hammer
    draw_H()
    draw_a()
    draw_m()
    draw_e()
    draw_r() 
    #Spell out Down
    penup()
    goto(-250,0)
    pendown()
    draw_D()
    draw_o()
    draw_w()
    draw_n()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
