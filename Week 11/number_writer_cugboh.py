"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.4 - Number Writer
Date: 10/23/2023

Description:
    This program spits out a certain number of randomly called numbers dependent on the user's input.
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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def not_13(number): 
    string = str(number) #convert number to string
    check = []
    # Ensure each character is a number
    for c in string:
        # Convert the character into an integer 
        digit = int(c) 
        # add it to the list
        check.append(digit)
    #What the number inputted is calculated as
    return sum(check)

def main():
    user = int(input('How many numbers would you like? '))
    
    count = 0 #iterations counter

    with open('random_numbers.txt', 'w') as fo: #open file to begin writing
        while count < user:
            num = r.randint(1119, 1217)
            if not_13(num) != 13:
                fo.write(str(num) + '\n')
                count += 1
        
        print(f"{user} numbers have been written to 'random_numbers.txt'.")

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()