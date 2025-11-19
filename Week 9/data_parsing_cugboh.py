"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 07.1 - Data Parsing
Date: 10/16/2023

Description:
This program uses the provided module data.py to calaculate the average retail price of gas every decade.

Contributors:
   Hanna hletzrin@purdue.edu
My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
        without helping me plan my solution.
    [Y] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import modules below this line (starting with unit 6)."""

import data # Calling on the external data
"""Write new functions below this line (starting with unit 4)."""

def main():
    print('          :  Price')    
    print('  Decade  : in 2021')
    print('          : Dollars')
    print('-------------------')
    gas = data.data 
    #print(gas) #Type is a list
    #print(gas[3:288:4]) #
    i=0
    decade = ['1950-1959', '1960-1969', '1970-1979','1980-1989',
               '1990-1999','2000-2009','2010-2019','2020-2029'] #8 elements
    entire = gas[3:288:4] # all of column 4
    for dec in range(0,71,10): #0 to 7
        L = entire[dec:dec+10] #Lower bound:upperbound
        avg = sum(L)/len(L)
        print(f"{decade[i]} :  ${avg:,.3f}")
        i+=1
    


   

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

