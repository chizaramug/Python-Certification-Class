"""
Author: Chizaram, cugboh@purdue.edu
Assignment: 05.1 - Maze
Date: 10/02/2023

Description:
    This code works with a PNG file. It takes a *, called turtle, and moves it from the start of the maze to the end.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
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
    setup(564, 564) #Width and height of the canvas
    bgpic("maze.png") #Sets the background as the maze picture
    shape("turtle") #Icon is a turle that is really an astrick 
    color("green") #The icon is green
    width(5) #Thickness of line


def main():
    """Write your mainline logic below this line (then delete this line)."""
    left (90) # turn north
    forward(12)#12*1 move north
    right (90) #turn right
    forward (180)# 12*18, move right
    left (90)  #turn north
    forward (72) #move north
    right (270) #turn left
    forward (72) #move left 
    left (270)  #turn north
    forward (144) #move north
    right(90) #move right
    forward (120) #move north
    right (90)# turn south
    forward(228)# move south
    right(270) #move right
    forward(12) #move to the finish line

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
