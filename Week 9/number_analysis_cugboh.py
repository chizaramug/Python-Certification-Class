"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/16/2023

Description:
This program collects floating point numbers and returns them as list.

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

"""Write new functions below this line (starting with unit 4)."""
def get_number_list():
    l = []
    for x in range(1,10+1): 
        user = float(input(f'  number {x:>2} of 10: '))#user input
       # To ensure we collect 10 floating numbers
        l.append(user) #turn the inputs into a list
    return l #what the func will give when called
def main():
    print('Enter 10 numbers:')
    #start
    list = get_number_list()
    HN = max(list) #calculate max
    print(f'Highest number: {HN:.2f}')
    LN = min(list) #calculate min
    print(f'Lowest number: {LN:.2f}')
    T = sum(list) #calculate total
    print(f'Total: {T:,.2f}')
    A = T / len(list) #calculate average
    print(f'Average: {A:,.2f}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

