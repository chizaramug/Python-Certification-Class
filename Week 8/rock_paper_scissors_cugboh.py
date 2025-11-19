"""
Author: Chizaram, cugboh@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/09/2023

Description:
    This code enables the computer to play the old children's game: Rock, Paper, Scissors.

Contributors:
    Lili lbrush@purdue.edu

My contributor(s) helped me:
    [Y] understand the assignment expectations without
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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def  get_computer_choice():
    compin = ['rock', 'paper', 'scissors'] #Giving the computer options
    return r.choice(compin)

def get_player_choice():
     while True:
        youin = input(("Choose rock, paper, or scissors: ")) #Collecting the player's "You" input.
        if youin in ['rock', 'paper', 'scissors']:
            return youin
        else:
            print("You made an invalid choice. Please try again.") #Incase anything else was given

def get_winner(compin,youin): #Determining who will win: rock beats scissors, paper beats rock, scissor beats paper
    if compin == youin: #ROCK, ROCK
        return 'tie'
    elif compin == 'rock' and youin == 'scissors': #Rock beats scissors
        return 'computer'
    elif compin == 'scissors' and youin == 'paper':
        return 'computer'
    elif compin == 'paper' and youin == 'rock':
       return 'computer'
        #NOW THE REVERSAL
    elif compin == 'scissors' and youin == 'rock': 
        return 'player'
    elif compin == 'paper' and youin == 'scissors':
        return 'player'
    elif compin == 'rock' and youin == 'paper':
        return 'player'
        
      
"""Start of actual code"""
def main():
    #Initializing variables 
    w = "tie"
    while w == "tie":
        c = get_computer_choice()
        p = get_player_choice()
        w = get_winner(c,p)
        if w == "computer":
            print(f"  The computer chose {c}, and you chose {p}.\n  {c} beats {p}\n  You lost.  Better luck next time.\nThanks for playing.")
        elif w == "player":  
            print(f"  The computer chose {c}, and you chose {p}.\n  {p} beats {c}\n  You won the game!\nThanks for playing.")
        elif w == "tie": 
            print(f"  The computer chose {c}, and you chose {p}.\n  It's a tie. Starting over.\n")
        


                     
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()