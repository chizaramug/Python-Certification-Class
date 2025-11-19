"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 04.1 - Falling
Date: 09/25/2023

Description:
    This program calculates the distance of a falling object with respect to time. 
Contributors:
    

My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
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
def falling_dist (t):
        g = 8.87 #m/s^2, the gravational constant 
        #t = input('Please put in time') #s, the time
        d = float(0.5*g*t**2) #m, the distance in meters
        return d
def main():
    
    print("Time (s)  Distance (m)")
    print("----------------------")
    
    for time in range(5,55,5):    
        dist = falling_dist(time )      
        print (f"{time:>8}       {dist:=7.1f}")
        
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()