import sys

def main():
    NUMBER_OF_DIGITS = 12

    digits = str(input("Please enter 12 digits separated by a space: ")).split()
    if len(digits) != 12:
        print("The input must contain 12 digits!")
        sys.exit()

    score = 0
    guesses = ["_"] * NUMBER_OF_DIGITS
    wrong_guesses = ""
    turn = 5

    while True:
        for j in range(NUMBER_OF_DIGITS):
            print(guesses[j], end=" ")

        print(wrong_guesses)

        if turn == 0:
            break

        guess = str(input())
        count = 0
        correct = False
        # is_repeated = False

        if guess in guesses or guess in wrong_guesses:
            print("You already entered this number")
            print()
            continue

        for j in range(NUMBER_OF_DIGITS):
            if guess == digits[j] and guesses[j] == "_":
                guesses[j] = digits[j]
                count += 1
                correct = True
            # elif guess == digits[j] and guesses[j] != "_":
            #     print("You already entered this number")
            #     is_repeated = True
            #     break

        # if is_repeated:
        #     continue

        # if guess in wrong_guesses:
        #     continue

        if not correct:
            wrong_guesses += " " + guess

        score += count
        turn -= 1

    print(score)

if __name__ == "__main__":
    main()