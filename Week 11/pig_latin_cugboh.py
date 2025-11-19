"""
Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/23/2023

Description:
    This program accepts pig latin as an argument and returns another string with the translated version. 
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
def pig(PigLatin): #Every input is automatically a string thanks to the input function
    text = PigLatin.split() #returns a list of string separated at white spaces
    Trans = []  

    for x in text:
        #Remove the last two characters at the end
        if x[-2:] == "ay": 
            #Move the third to last letter ([-3]) in the word to the beginning
            #text.replace(text[-3],text[0])
            switch =  x[-3] + x[:-3]
            Trans.append(switch)
        else:
            # Last two characters will always be "ay".
           Trans.append(x)
        correction = " ".join(Trans).capitalize()
    return correction
"""Write new functions below this line (starting with unit 4)."""
def main():
    PigLat =  input("Enter a string in Pig Latin: ") #user's input
     #Formatting output
    T = pig(PigLat)
    print(f'Translation: {T}')

    """Do not change anything below this line."""
if __name__ == "__main__":
    main()