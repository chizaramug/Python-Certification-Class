"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 03.3 - rainfall
Date: 09/18/2023

Description:
    This program collects data and calculates the average rainfall over a period of years. 
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
    Month = ['Jan.','Feb.', 'Mar.','Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
    i=0
    Total = 0 
    Avg = 0
    Years = int(input("Enter the number of years: ")) #Request of the amount of Years
    if Years <= 0:
        print ("Invalid input; years must be greater than 0.") 
    else:
        for OL in range(0,Years):
            print(f"  For year No. {OL+1}")
            for IL in range(12):
                
                Rain = float(input(f"    Enter the rainfall for {Month[IL]}: ")) #Request of the amount of Rain
                while Rain < 0:
                    print ("    Invalid input; rainfall cannot be negative.")
                    Rain = float(input(f"    Enter the rainfall for {Month[IL]}: ")) #Request of the amount of Rain
                i += 1
                Total += Rain
                Avg = float(Total/i) 

        print(f'There are {i} months.')
        print(f'The total rainfall was {Total:,.2f} inches.')
        print(f"The monthly average rainfall was {Avg:,.2f} inches." )
   
        
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()