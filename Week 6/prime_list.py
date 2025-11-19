"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/02/2023

Description:
    This program askes user to enter a series of postive intergers to output a prime list. 
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
def is_prime(num): # Creation of the is_prime function 
    if num == 0 or num == 1:
        return False #Starting off strong with ignoring 0 ans 1 as prime numbers
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False #not prime 
    return True 
def main():

    prime = int (input('Enter a postive interger: '))
    def is_prime(num):
        print ('The primes up to {} are: {}')


    """Do not change anything below this line."""
if __name__ == "__main__":
    main()