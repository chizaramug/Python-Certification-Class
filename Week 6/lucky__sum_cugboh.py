"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/18/2023

Description:
    This program askes user to inser two numbers and the two numbers will be in a range. The code will then add up all the numbers divisble by 7 in that range. 
Contributors:
    lili brush (lbrush)

My contributor(s) helped me:
    [Y] understand the assignment expectations without
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
def lucky_sum(a, b): # Creation of the function
    sum = 0  #For any loop you must initialize any variables that you have.
    for t in range(min(a,b),max(a,b)+1):  #This asigns the var. t a range of numbers a to b
      if  t%7 == 0:
         sum += t #This adds up the acceptable t values.
    return sum

def main():
    x = int(input('Enter the first integer: ')) 
    y = int(input('Enter the second integer: '))
    s = lucky_sum(x,y) #Function in use
    print(f'The sum of the lucky numbers is {s:,}.')

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()