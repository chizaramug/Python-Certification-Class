"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 01.2 - Intrest
Date: 09/04/2023

Description:
    This program calculates the balance in an account over a certain amount of years ,t,. The inputs are the initial deposit, annual intrest rate,
      the number of times the intrest is compunded in a year, and the number of years the money will stay in the account. 

Contributors:
    Hanna Letzring, hletzrin@purdue.edu [repeat for each]

My contributor(s) helped me:
    [Y] understand the assignment expectations without
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
    #Code Starts Below:
   
    print ("Enter the following parameters.")
    # float makes the strings into numbers
    P = float (input ("  The initial deposit?"))
    r = (float (input ("  The annual intrest rate in percent?")))/ 100 #convert to a decimal
    t = float (input ("  The number of years the account earn intrest?"))
    n = float (input ("  The number of times intrest is compounded each year:"))
    #Overall calculation
    FV = P*(((1+(r/n))**(n*t)))
    # Showing the ending statement with inserted and calculated values.
    print (f"The balance of this account will be ${FV:,.2f} after {t} years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()