def sort_acronyms(acronyms):
    acronyms.sort(key=lambda acronyms: (-len(acronyms), acronyms))

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

    for acronym in acronyms:
        print(acronym)

if __name__ == "__main__":
    main()