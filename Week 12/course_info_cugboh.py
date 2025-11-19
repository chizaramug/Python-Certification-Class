"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 09.3 - Course Info
Date: 10/30/2023

Description:
This program gives the user information about a given course like the instructr, room and time.

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
def get_course_data():
    #manual form a dictionary using Table 1. 
    #Keys = room, instructor, time
    #Values: from table
    Fake_course_data = { "CS101": {"room": "1461", "instructor": "Django", "time": "9:00 a.m."},
        "CS102": {"room": "4815", "instructor": "Idle", "time": "11:00 a.m."},
        "CS103": {"room": "3634", "instructor": "Rich", "time": "10:00 a.m."},
        "NT110": {"room": "1188", "instructor": "Marshal", "time": "2:00 p.m."},
        "CM241": {"room": "2451", "instructor": "Pickle", "time": "12:00 p.m."}}
    return Fake_course_data


def main():
    x = get_course_data() # make function available
    user = input("Enter a course number: ") #ask for user input
    
    if user in x: #Making sure the input is a actual available class
        keys = x[user]
        print(f"  The details for course {user} are:")
        print(f"    Instructor: {keys['instructor']}")
        print(f"          Room: {keys['room']}")
        print(f"          Time: {keys['time']}")
    else:
        print(f"  {user} is an invalid course number.")
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

