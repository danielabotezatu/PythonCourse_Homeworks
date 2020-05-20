import time
from random_words import RandomWords


def play(word):
    word_array = []
    guessed_letters = []

    i = 0
    while i < len(word):
        word_array.append('_')
        word_array.append(' ')
        i = i + 1

    game_menu = True
    correct_counter = 0
    incorrect_counter = 0

    while game_menu:

        remaining_guesses = 8 - incorrect_counter

        # menu selection

        print(''.join(map(str, word_array)))
        print("Guessed Letters: " + ' '.join(map(str, guessed_letters)))
        print("Incorrect Guesses Remaining: " + str(remaining_guesses))

        try:
            selection = input(
                "(1) Guess Letter\n(2) Guess the Word [ONLY ONE CHANCE]\n(3) Quit\n\nSelect what you want to do: ")
            selection = int(selection)
        except ValueError:
            print("Please enter 1, 2 or 3!")
            time.sleep(.1)
            continue

        if selection == 1:

            time.sleep(.5)
            letter = input("\nPlease enter a letter you want to guess: ")

            # letter guessing

            i = 0
            letter_in_word = False

            while i < len(word):
                if word[i] == letter[0]:

                    # correct guess

                    letter_in_word = True
                    word_array.pop(2 * i)
                    word_array.insert(2 * i, letter[0])

                    if guessed_letters.count(letter) == 0:
                        print("\nYou guessed correctly " + letter[0] + "\n")
                        correct_counter = correct_counter + word.count(letter[0])
                        guessed_letters.append(letter[0])
                i += 1

            # incorect guess

            if not letter_in_word:
                print("\n" + letter[0] + " is not in the word")
                if guessed_letters.count(letter[0]) == 0:
                    guessed_letters.append(letter[0])
                    incorrect_counter = incorrect_counter + 1

            # if the word is complete

            if correct_counter == len(word):
                print_win()
                game_menu = False

            # if there are no more guesses

            if incorrect_counter >= 8:
                print("\nOut of guesses!")
                print_lose(word)
                gamen_menu = False

        if selection == 2:
            time.sleep(1)
            print("WARNING: If you are wrong, you automatically lose!")
            word_guess = input("\nType your word guess here: ")

            i = 0
            words_match = True

            if word != word_guess:
                words_match = False

            if words_match:
                print_win()
                game_menu = False

            else:
                print_lose(word)
                game_menu = False

        if selection == 3:
            game_menu = False


def choice():
    r = RandomWords()
    word = r.random_word()
    return word


def print_win():
    print("CONGRATULATIONS: YOU WON!")
    time.sleep(.5)
    print("CONGRATULATIONS: YOU WON!")
    time.sleep(.5)
    print("CONGRATULATIONS: YOU WON!")
    time.sleep(.5)


def print_lose(word):
    print("YOU LOST!")
    time.sleep(.5)
    print("THE WORD WAS: " + word)
    time.sleep(.5)


def menu():
    game_menu = True

    while game_menu:

        print("Welcome to Hangman game!")

        start = input("(1) Play Game\n(2) Quit\n\nSelect what you want to do: ")

        try:
            number = int(start)

        except ValueError:
            print("Please enter one of the options: ")
            time.sleep(.1)
            continue

        if number == 1:

            word = choice()

            j = 0
            while j < 5:
                countdown = 5 - j
                print("\n" + str(countdown) + "\n")
                print("GET READY!!!\n\n\n\n\n")
                countdown = 5 - j
                time.sleep(1)
                j = j + 1

            play(word)

        elif number == 2:
            print("See you soon!")
            game_menu = False

        else:
            print("Please enter a valid number")
            time.sleep(1)


menu()
