def pig(word):
    return word[-3] + word[:-3]

def main():
    pig_latin_sentence = input("Enter a string in Pig Latin: ").strip().lower()
    words = pig_latin_sentence.split()
    translated_words = [pig(word) for word in words]
    translated_sentence = " ".join(translated_words).capitalize()
    print("Translation:", translated_sentence)

if __name__ == "__main__":
    main()