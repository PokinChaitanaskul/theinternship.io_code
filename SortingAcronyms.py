def sort_acronyms(acronyms):
    acronyms.sort(key=lambda acronyms: (-len(acronyms), acronyms))


def begins_with_capital(word, index):
    return (word[index].isupper() and word[index - 1] == " " and index - 1 > 0) or (word[index].isupper() and index == 0)

def main():
    numberOfInputs = int(input(""))
    acronyms = []

    for i in range(numberOfInputs):
        currentInput = str(input())
        current_acronym = ""
        words = currentInput.split()

        for word in words:
            first_char = word[0]
            if first_char.isupper():
                current_acronym += first_char

        acronyms.append(current_acronym)

    sort_acronyms(acronyms)

    print(acronyms)

if __name__ == "__main__":
    main()