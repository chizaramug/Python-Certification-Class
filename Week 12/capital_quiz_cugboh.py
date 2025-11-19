"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 10/30/2023

Description:
This program utilizes data from a text file to be uses a U.S. state capital quiz. It askes the user
for the capital after saying the state.

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
import random as r
"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    with open('state_capitals.txt','r') as fo:
            all = fo.read() #load state-capital data into a variable
            pair = all.split('\n') #split data by lines
            
            #Create an empty dictionary
            CS = {}

            for air in pair:
                part = air.split(',') #Split each line into key and value using a comma-> idea: meaning = all.replace(',',' =')
                
                if len(part) == 2: #Have to put b/c of ValueError: not enough values to unpack (expected 2, got 1)
                    #create physical pair ny assigning the first index to be capital and second state
                    capital, state = part 
                    # capital is value and state is key
                    CS[state.strip()] = capital.strip()

    return CS 


def main():
    #quiz  time
    a = get_state_data()
    check = list(a.keys()) 
    count = 0
    run = 0
    while True:
        state = r.choice(check)# randomize state values chosen
        user = input(f'What is the capital of {state} (enter 0 to quit)? ')
        correct = get_state_data.get(state)
        run += 1
        if user == correct.lower():
            count += 1
            print('  That is correct!')
        elif user == '0' :
           percent = (count/run)*100
            print(f"You answered {percent:.1f}% of the questions correctly.")
            
        elif user == '' :
            print(f"That is incorrect.\nThe capital of {state} is {correct}.")
           
            print("You didn't answer any questions.")
            
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

