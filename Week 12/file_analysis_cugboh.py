"""Author: Chizaram Ugboh, cugboh@purdue.edu
Assignment: 09.4 - File Analysis
Date: 10/30/2023

Description:
This program processes the provided text and outputs a specific outcome.

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
def get_words_from_file(filename):
    with open(filename, "r") as fo:
        text = fo.read().lower()  # use file and have contents become lowercase
        # Remove leading and trailing punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
    return words


def count_word_frequencies(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def main():
    python_1_words = get_words_from_file("python_1.txt")
    python_2_words = get_words_from_file("python_2.txt")

    python_1_word_count = count_word_frequencies(python_1_words)
    python_2_word_count = count_word_frequencies(python_2_words)

    # Find common words
    common_words = set(python_1_word_count.keys()) & set(python_2_word_count.keys())

    # Find either-but-not-both words
    either_but_not_both = (set(python_1_word_count.keys()) | set(python_2_word_count.keys())) - common_words

    # Write output files
    with open("python_1_word_frequency.txt", "w") as file:
        for word in sorted(python_1_word_count.keys()):
            file.write(f"{word}: {python_1_word_count[word]}\n")

    with open("python_2_word_frequency.txt", "w") as file:
        for word in sorted(python_2_word_count.keys()):
            file.write(f"{word}: {python_2_word_count[word]}\n")

    with open("common_words.txt", "w") as file:
        for word in sorted(common_words):
            file.write(f"{word}\n")

    with open("eitherbutnotboth.txt", "w") as file:
        for word in sorted(either_but_not_both):
            file.write(f"{word}\n")
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

