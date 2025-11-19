"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/06/2023

Description:
This program collects monthly sales data aand turns it into a pie chart.

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

    sales = []
    months = ['January', 'February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
   # Collects monthly sales data from the user and stores it as a list
    for x in months: #x iterates over each of the 12 months 
        user = int(input(f"Enter the sales for {x}: "))
        sales.append(user) 

    #print (sales)

    #Create pie plot
    fig, ax = plt.subplots()
    #set colors and labels
    color = ('#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11',
          '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A')
    labels = ('January', 'Feburary','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

    ax.pie(sales, colors=color, labels=months) #(value, colors=, labels=,)
    ax.set_title("Monthly Sales Values (cugboh)")  
    plt.show()

    # Don't forget to make the pie chart as a PDF file
 


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

