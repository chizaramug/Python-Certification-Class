"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 07.4 - Magic Square 
Date: 10/16/2023

Description:
This program uses two functions to check that a inputted matrix  is a Lo Shu Magic Square. 

Contributors:
   Ruth, rsugiart@purdue.edu
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

"""Import modules below this line (starting with unit 6)."""

"""Write new functions below this line (starting with unit 4)."""
def print_square(sq):
    for comp in sq:
        print(' ', end = '')
        for com in comp:
            print(f" {com}",end = '')
        print()
        

def is_magic(sq): #this coment helps with creating the matrix
    newList = []
    for comp in sq:
        for com in comp:
            newList.append(com)
    #all numbers 1-9 must be present
    if sorted(newList) == [1,2,3,4,5,6,7,8,9]: 
        check1 = True
    else: 
        check1 = False
#this check ensures that if you add up the elements diagonally or up or down it equals 15
    if sq[0][0]+sq[0][1]+sq[0][2] == 15 and sq[1][0]+sq[1][1]+sq[1][2] == 15 and sq[2][0]+sq[2][1]+sq[2][2] == 15 and sq[0][0]+sq[1][0]+sq[2][0] == 15 and sq[0][1]+sq[1][1]+sq[2][1] == 15 and sq[0][2]+sq[1][2]+sq[2][2] == 15 and sq[2][0]+sq[1][1]+sq[0][2] == 15 and sq[0][0]+sq[1][1]+sq[2][2] == 15 :   
        check2 = True  
    else: 
        check2 = False
    #both checks must be true for it to be a magic square
    if check1 == True and check2 == True:
        return True
    else:
        return False

def main():
    #Provided Squares/ Test Trials
    F1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    F2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    F3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    
    check = is_magic(F1)
    #1st List
    print(f"Your square is:")
    print_square(F1)
    if check is False:
        print("It is not a Lo Shu magic square.")
    if check is True:
        print("It is a Lo Shu magic square!")
    #2nd List
    check = is_magic(F2)
    print(f"Your square is:")
    print_square(F2)
    if check is False:
        print("It is not a Lo Shu magic square.")
    if check is True:
        print("It is a Lo Shu magic square!")
    #3rd List
    check = is_magic(F3)
    print(f"Your square is:")
    print_square(F3)
    if check is False:
        print("It is not a Lo Shu magic square.")
    if check is True:
        print("It is a Lo Shu magic square!")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

