"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 00.1 - Hello User
Date: 08/21/2023

Description:
    This program askes the user for their name as an input argument. 
    Once the input is placed the program says "Hello [input]!" as the output response.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
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
 # Note 1: For code to work, code must be indented to be used. Triple quotation notes must als be indented too.
 #  "#" doesn't have to be indented.
    username = input ("What is your name? ")
    print (f"Hello {username}!") #  f-string substitutes an expression using a brace , {}, (ex: username) within an expression

 
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
