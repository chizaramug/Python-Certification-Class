"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 10/23/2023

Description:
    This program changes the letters used in a telephone line  to actual phone numbers that can be called from the user. 
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
def convert_number(AlphaNum): #function needed for the transformation to occur
    Num = "" #creating a string for a list that will be returned
    for extra in AlphaNum: #Transformation starts
        if extra.isalpha():#iteraring making sure each character is a letter

            if extra in 'ABCabc':
                Num += '2'
            elif extra in 'DEFdef':
                Num += '3'
            elif extra in 'GHIghi':
                Num += '4'
            elif extra in 'JKLjkl':
                Num += '5'
            elif extra in 'MNOmno':
                Num += '6'
            elif extra in 'PQRSpqrs':
                Num += '7'
            elif extra in 'TUVtuv':
                Num += '8'
            elif extra in 'WXYZwxyz':
                Num += '9'
        else: #If regular numbers are used keep them the same
            Num += extra
    return Num

"""Write new functions below this line (starting with unit 4)."""
def main():
    AlphaNum = input('Enter a telephone number: ')#Askes user for a telephone number
    PhoneNum = convert_number(AlphaNum) #conversin to all numrical numbers
    print(f'  {AlphaNum}')
    print(f'  {PhoneNum}')

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()