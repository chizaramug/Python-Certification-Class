"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/06/2023

Description:
Create a graph of the average price of gas over weeks.

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
import matplotlib.pyplot as plt
"""Write new functions below this line (starting with unit 4)."""

def main():
    
    y = [] 
    with open('2008_Weekly_Gas_Averages.txt') as fo:
    #There are 52 lines in the file, one for each week of the year
        lines = fo.readlines() #read out lines including '\n\'
      
        for i in lines:
            sep = float(i.strip())
            y.append(sep)

    # and uses matplotlib to plot the data as a line graph
    fig, ax = plt.subplots()#Create line plot

    #set x and y values 
    x = range(1,53)

    #set titles and organize plot
    ax.plot(x,y,color ='b')
    ax.grid()
    ax.set_title("2008 Weekly Gas Prices (cugboh)")
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)")

    #Setting ticks
    ax.set_yticks([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
    ax.set_xticks([10,20,30,40,50])

    #Set Limits
    ax.set_xlim(1, max(x))
    ax.set_ylim(1.5, 4.25)

    plt.show()

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

