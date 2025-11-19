"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/25/2023

Description:
    This program askes user to enter a series of non negative numbers. 
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
    a = int(input ('Enter the first integer: '))
    b = int(input ('Enter the second integer: '))
    def lucky_sum (c,d): #Accepts 2 intergers
        if c%7 == 0 and d%7 == 0 :
            sum = float(c)+ float(d) #calculates the sum 
            return sum
    s = lucky_sum (a,b)
    print (f"The sum of the lucky numbers is {s:,}.")

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()