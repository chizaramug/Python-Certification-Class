"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/11/2023

Description:
    This program sees if the year entered by the user is a leap year. 

Contributors:
    Kanari Hirano, hirano0purdue.edu
    
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
    Year = int(input ("Enter a year: "))
    #Input = ['1900','2000','2020','2020','2022'] #1st condition:divisble by 100 and by 400
    if Year%100 == 0 and Year%400==0: #The modulus symbol divides the year by the conditions and prints out a remaninder. If that remainder doesn't equal zero than it isn't a leap year.
        print(f"The year {Year} is a leap year.\nFebruary of {Year} has 29 days.")
        
    elif Year%100 != 0 and Year%4==0: #2nd condition: Not divisble by 100 but divisble by 4
        print(f"The year {Year} is a leap year.\nFebruary of {Year} has 29 days.")
    else: #For Everything else
        print(f"The year {Year} is not a leap year.\nFebruary of {Year} has 28 days.")

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()