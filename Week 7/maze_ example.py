"""
Author: Chizaram, cugboh@purdue.edu
Assignment: 05.1 - Maze
Date: 10/02/2023

Description:
    This code works with a PNG file. It takes a *, called turtle, and moves it from the start of the maze to the end.
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
   

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
