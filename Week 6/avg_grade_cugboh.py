"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/2/2023

Description:
    This program accepts scores from 0-100 and averages them out into numbers and letter grades. 
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
def get_valid_score (): # Every user defined function will be out of main
        g = float(input("Enter a score: ")) #Asks the user to enter in a score 
        while g < 0 or g > 100:
                print ('  Invalid Input. Please try again.')
                g = float(input("Enter a score: ")) #Asks the user to enter in a score
        return g

def calc_average(List): #There will always be 5 scores to calculate
    sume = 0
    for run in List:
        sume += run

    Avg = sume/len(List)
    return Avg

def determine_grade(let):
        if let >= 92 and let <= 100:
            let = 'A'
        elif let >= 82 and let <= 92:
             let = 'B'
        elif let >= 73 and let <= 82: 
             let = 'C'
        elif let >= 64 and let <= 73: 
              let ='D'
        elif let >= 0 and let <= 64:
             let = 'F'
        return let
def main():
    List = [] #Initiated a list
    for count in range(5): # runs the function "get_valid_score" 5 times
            value = get_valid_score() 
            List.append(value) # adding 
            print (f'  The letter grade for {value:,.1f} is {determine_grade(value)}.')

    Avg = calc_average(List)

  
            
    
    print (f"\nResults:\n  The average score is {Avg:,.2f}.\n  The letter grade for {Avg:,.2f} is {determine_grade(Avg)}.") #The end
    
    
    """Do not change anything below this line."""
if __name__ == "__main__":
    main()