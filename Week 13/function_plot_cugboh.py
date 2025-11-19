"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 10.4 Function plot
Date: 11/09/2023

Description:
Create the a copy of the given plot in the assignment.

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
import numpy as np
"""Write new functions below this line (starting with unit 4)."""
 
def main():

    # Generate x values
    x = np.linspace(0, 2 * np.pi, 1000)  #set x to to have 100 values between 0 to 2pi, works like MatLab

    # Calculate y values for the two functions
    y1 = ((5 * np.sin(x))**2) - 10
    y2 = 10 * np.cos(x**2) + x**2 - 20

    # Create a line plot with multiple lines
    fig, ax = plt.subplots()
    ax.plot(x, y1, color='g') #line 1
    ax.plot(x, y2, color='b') #line 2

    # Set title
    ax.set_title('10.4 Function Plot (cugboh)')


    # Set x-axis using LaTeX notation
    ax.set_xticks([np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"]) #([0, pi/2, pi, 3pi/2, 2pi ])
    

    # Need a legend
    ax.legend(['$(5\\sin{x})^2 - 10$', '$10\\cos{(x^2)} + x^2 - 20$'], loc='lower right')

    #Set Limits
    ax.set_yticks([-20, -10, 10, 20])

    # Remove spines
    for spine in ['top','right']: 
        ax.spines[spine].set_visible(False)
     #Need to center x-axis
    for spine in ['bottom','left']: 
        ax.spines[spine].set_position('zero')
    
   


    plt.show()

        

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

