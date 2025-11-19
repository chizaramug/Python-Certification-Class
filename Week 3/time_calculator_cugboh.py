"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/011/2023

Description:
    This program takes in a certain number in seconds and returns it in larger time units such as hours, minutes and days. 

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
    #Asks user to input any number and it will be represented in seconds
    Time = int(input("Please enter a time in seconds: "))
    if Time < 60:
        print (f"{Time} seconds is less than one minute.") #Anything less than 60 is in seconds
    elif Time == 60:
        print (f"{Time} seconds equals 1 minute(s).") #60 seconds is 1 min
    elif Time > 60:
        days = Time//86400
        hrs = Time % 86400 // 3600          #Trying to calculate seconds over 100
        min = Time % 86400 // 3600
        print (f"{Time} seconds equals # minute(s), # hour(s), # days(s).")
    elif Time == 3600:
        print (f"{Time} seconds equals 1 hr(s).")
    elif Time == 86400:
        print (f"{Time} seconds equals 1 day(s).")
    

        """Do not change anything below this line."""
if __name__ == "__main__":
    main()