"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/04/2023

Description:
    This program askes the user for the distance of their trip, the average price of fuel and the fuel efficency of their vehicle.
    Once the several inputs are entered into the program, a calculation of the cost of your trip is outputted.

Contributors:
    Hanna Letzring, hletzrin@purdue.edu [repeat for each]

My contributor(s) helped me:
    [N] understand the assignment expectations without
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
def main():
    #Code Starts Below:
    print ("Road trip fuel cost estimator:")
    #Asking for inputs
    distance  = input ("  How far away is your destination (miles)? ")
    price = input ("  What is the average price of gas (dollars per gallon)? ")
    mpg = input ("  What is the fuel efficiency of your vehicle (mpg)? ")
    # Calculation of costs
    cost = (2 * float(distance))*(float(price))/(float(mpg)) 
    # Showing the ending statement with inserted and calculated values.
    print (f"\nThe fuel cost for this trip is approximately ${int(cost):d}.")
 
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
