"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/16/2023

Description:
This program calculates the precentage a specific number in a dice roll.

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

"""Import modules below this line (starting with unit 6)."""
import random as r
"""Write new functions below this line (starting with unit 4)."""
def roll_d6():
    a = r.randint(1,6) #takes no arguments and returns a random integer bet 1-6(inclusive)
    return a

def get_2d6_rolls(Roll):
    r = []
    for dices in range(Roll):
        r1 = roll_d6()
        r2 = roll_d6()
        r.append(r1 + r2)
    return r  
 

def main():
    Roll = 1000000 #how many times you drop the dice
    outcome = get_2d6_rolls(Roll) #results from roll
  
    
    #Setting up title
    print('Roll  Frequency')
    
   #Calculating frequency
    for i in range(2,13):
            F = ((outcome.count(i))/Roll)*100
            print(f' {i:>2}    {F:>5.2f}%')
   

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

