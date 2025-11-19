"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 02.5 - Fluid Mechanics 
Date: 09/11/2023

Description:
    This program calculates a key parameter of Fluid mechanics - the Reynolds number. 

Contributors:
    Darren Lie, lied@purdue.edu

My contributor(s) helped me:
    [N] understand the assignment expectations without
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


"""Write new functions below this line (starting with unit 4)."""
def main():
    #This askes for user input
    tIn = int (input("Enter the temperature in °C as 5, 20, or 50: "))
    vIn = float (input("Enter the velocity of water in the pipe (m/s): "))
    dIn = float (input("Enter the pipe's diameter (m): "))
   # After asking for inputs the code below calculates the Reynolds number for specific temperature.
    if int (tIn) == 5:
        v = 1.52*10**-6
        Calculate = (vIn*dIn/(v) )
        print (f"At {tIn:.1f}°C, the Reynolds number for flow at {vIn} m/s in a {dIn} m diameter pipe is {Calculate:.2e}.")
        
    elif int (tIn) == 20:
        v = 1.00*10**-6
        Calculate = (vIn*dIn/(v) )
        print (f"At {tIn:.1f}°C, the Reynolds number for flow at {vIn} m/s in a {dIn} m diameter pipe is {Calculate:.2e}.")

    elif int (tIn) == 50:
        v = 5.54*10**-7
        Calculate = (vIn*dIn/(v))
        print (f"At {tIn:.1f}°C, the Reynolds number for flow at {vIn} m/s in a {dIn} m diameter pipe is {Calculate:.2e}.") #ask if degrees are correct and 6

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()