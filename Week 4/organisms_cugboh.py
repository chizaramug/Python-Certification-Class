"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/18/2023

Description:
    This program guesses the approximate size of a population of organisms. 
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
def main():
    Start = float(input("Starting population, in thousands: "))#Request of user
    Rate = float(input("Average daily increase, in percent: "))#Request of user
    Days = int(input("Number of days to multiply: "))#Request of user
    Pop = 2.5 #assigning variable
    IP = 2.5
    print("Day   Approx. Pop")
    if  Days >= 0:
     for count in range(0, Days+1):
        Pop = Pop * (1 + (Rate/100)) #calculating equations
        count += 1
        
        print(f"{count - 1:>3}    {Pop:>10,.3f}") #formatting requirement

 
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()