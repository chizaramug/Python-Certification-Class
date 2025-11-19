"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/11/2023

Description:
    This program askes the user how many packages they would like to order and then a percentage would be applied to it.

Contributors:
   

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
    Asks = int(input ("How many packages will be purchased: ")) #User inputs # of packages
    if Asks < 0:
        print ("  Invalid Input!") #Below else-if statements corresponds to the amount of percent taken off
    elif Asks <= 3:
        print (f"  No discount applied.\n  The total price to purchase {Asks} packages is ${Asks*880:,.2f}.")
    elif Asks <= 39:
        print (f"  10% discount applied.\n  The total price to purchase {Asks} packages is ${(Asks*880)*(90/100):,.2f}.")
    elif Asks <= 199:
        print (f"  15% discount applied.\n  The total price to purchase {Asks} packages is ${(Asks*880)*(85/100):,.2f}.")
    elif Asks <= 999:
        print (f"  30% discount applied.\n  The total price to purchase {Asks} packages is ${(Asks*880)*(70/100):,.2f}.")
    elif Asks >= 1000:
        print (f"  42% discount applied.\n  The total price to purchase {Asks} packages is ${(Asks*880)*(58/100):,.2f}.")


    """Do not change anything below this line."""
if __name__ == "__main__":
    main()