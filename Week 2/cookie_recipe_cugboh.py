"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/04/2023

Description:
    This program askes the user for the amount of cookies they want to make and from that, the program releases the 
    ratio of flour, sugar and butter to make the amount of cookies requested. 

Contributors:
    Hanna Letzring, hletzrin@purdue.edu [repeat for each]

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
    #Code Starts Below:
    import math 
    cookies = round(float(input ("How many cookies do you want to make? ")))

    #Initially creating the variables. Use math to find the appropriate values
    butter = (1.25/48)*cookies #x
    sugar = (1.50/48)*cookies #y
    flour = (2.50/48)*cookies #z
    equ = butter+sugar+flour
    # print out statement
    print (f"To make {cookies:,.0f} cookies, you will need:\n{butter:>10,.2f} cups of butter\n{sugar:>10,.2f} cups of sugar\n{flour:>10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
