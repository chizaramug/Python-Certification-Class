"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/18/2023

Description:
    This program askes user to enter a series of non negative numbers. 
Contributors:
    

My contributor(s) helped me:
    [n] understand the assignment expectations without
        telling me how they will approach it.
    [n] understand different ways to think about a solution
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
    Input = float(input(("Enter a non-negative number (negative to quit): "))) #Askess user for inputs
    Total = 0
    i = 0
    while Input >= 0: #Loop used to collect inputs and amount of inputs
        i += 1
        Total += Input
        Input = float(input(("Enter a non-negative number (negative to quit): ")))
        
    if i == 0:
        print("  You didn't enter any numbers.") #Placed here for when a number other than 0 or postive is placed. 
    else:
        Avg = Total/i
        print(f"  You entered {i} numbers.")
        print(f"  Their sum is {Total:,.3f} and their average is {Avg:,.3f}." )


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()