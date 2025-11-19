"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/06/2023

Description:
Create a ar graph of the number of COVID-19 cases across dates.

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
import datetime
import matplotlib.pyplot as plt
"""Write new functions below this line (starting with unit 4)."""


def main():
    dates = [] #dates=['2020-03-04', '2020-07-04', '2020-09-04', '2020-11-04'] from example slide
    times = [] 

    with open('indiana_covid-19_data_spring_2023.txt','r') as fo:
    #There are 52 lines in the file, one for each week of the year
        lines = fo.readlines() #read out lines including '\n\'
        for i in lines:
            sep = i.rstrip().split()
            cases = float(sep[2])
            times.append(cases)
     
       # Divide each element in times' list by 1000 to replicate the assignments y-axis
        t = [case / 1000 for case in times]

        for u in lines: #Gather dates into a list 
                sepa = u.rstrip().split()
                dat = sepa[0]
                dates.append(dat)   
     
                
    #Adding on prior weeks' case data:
    t_cases = 0
    total = []
    for n in t:
        t_cases += n
        total.append(t_cases)
    
    X = []   
    for date in dates:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        X.append(dt)
           
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(X, total, width=7, color='b')

    # Set titles and labels
    ax.set_title("Weekly Positive COVID-19 Cases in Indiana (cugboh)")  
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Cases (in thousands)")
       
    fig.autofmt_xdate()
    plt.show()
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

