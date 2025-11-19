"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.6 - Step Counter
Date: 10/23/2023

Description:
    This program reads the step.txt file and calculates the average steps per month.
Contributors:
    Tyler tsiverts@purdue.edu

My contributor(s) helped me:
    [N] understand the assignment expectations without
        telling me how they will approach it.
    [N] understand different ways to think about a solution
        without helping me plan my solution.
    [Y] think through the meaning of a specific error or
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
   #365 Lines in the file, and each line contains the number of steps a person has taken each day for a year.
    with open('steps.txt', 'r') as fo:
        everything = fo.read().split('\n')
    Jan = everything[0:31] #April, June, September, and November have 30 days
    Feb = everything[31:59] #Feb has 28 days
    Mar = everything[59:90] #31 days
    Apr = everything[90:120] #30
    May = everything[120:151] #
    Jun = everything[151:181]
    Jul = everything[181:212]
    Aug = everything[212:243]
    Sep = everything[243:273]
    Oct = everything[273:304]
    Nov = everything[304:334]
    Dec = everything[334:365]

    MonthSteps = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec] #create lists for easy loops
    Month = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    i = 0 
    
    print('The average steps taken each month were:')
    for x in MonthSteps: #print 12 times
        x = [int(item) for item in x]
        avg = sum(x)/len(x)
        print(f'{Month[i]:>10} : {avg:8.2f}')
        i += 1
    
   
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()