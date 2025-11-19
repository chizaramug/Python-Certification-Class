"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 09.2 - World Series
Date: 10/30/2023

Description:
This program utilizes data from a text file of the world series dates and lets the user 
know if a world series was hosted that year.

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
def load_winners_data():
    Teams = {} #First Key: Name of Teams,  Value = #of times they won the world series
    Years = {} #Second Key: Years,         Value = Name of the team that won that year
    with open("WorldSeriesWinners.txt", "r") as fo :#Access text file 
        lines = fo.readlines()
        start = 1903
        for x in lines:

            if x in Teams: #checks to see if x is in the Teams dictionary
                Teams[x] += 1 #counting the amount of time a specfic team name comes up
            else:
                Teams[x] = 1
        #attaches 1903 to the first team name going up to 2022
            Years[start] = x
            start += 1
        #return two dictionaries
    return Teams, Years 


def main():
    Teams, Years = load_winners_data()
    
    while True:
        Year = int(input("Enter a year in the range 1903 -- 2022: "))
        if Year < 1903 or Year > 2022:
               print(f"Data for the year {Year} is not included in this system.")
        elif Year in Years:
            Champs = Years[Year] #indent the list of years with the year the user inputted
            times = Teams.get(Champs) #obtain the value of the team's name
            print(f"The {Champs} won the World Series in {Year}.")
            print(f"They have won the World Series {times} times.")
        elif Year == 1904 or Year == 1994:
            print(f"The World Series wasn't played in the year {Year}.")
    

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

