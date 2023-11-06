import random

"""The Hangman Project"""

print("HANGMAN\nThe game will be available soon.\n")


def choose_random_word():
    pr_language = ["python", "java", "kotlin", "pascal"]
    return random.choice(pr_language)


def initialize_game(word):
    return "-" * len(word), list(word), 8, []


def get_guess():
    return input("Input a letter:")


def is_valid_guess(guess, letters_guessed):
    return guess.isalpha() and guess.islower() and len(guess) == 1 and guess not in letters_guessed


def check_answer(answer_code, answer_list, guess_answer):
    for i in range(len(answer_list)):
        if answer_list[i] == guess_answer:
            answer_code = answer_code[:i] + guess_answer + answer_code[i + 1:]
    return answer_code


def play_hangman():
    while True:
        print('Type "play" to play the game, "exit" to quit:')
        user_choice = input()

        if user_choice == "play":
            answer = choose_random_word()
            answer_code, answer_list, attempts_left, letters_guessed = initialize_game(answer)

            while attempts_left > 0:
                print(answer_code)
                guess_answer = get_guess()

                if not is_valid_guess(guess_answer, letters_guessed):
                    print("Invalid input. Please enter a lowercase English letter.")
                    continue

                if guess_answer in letters_guessed:
                    print("You already guessed this letter.")
                    continue

                letters_guessed.append(guess_answer)

                if guess_answer in answer_list:
                    answer_code = check_answer(answer_code, answer_list, guess_answer)
                    if "-" not in answer_code:
                        print("You guessed the word! \nYou survived")
                        break
                else:
                    attempts_left -= 1
                    print("That letter doesn't appear in the word")

            else:
                print("You lost!")

        elif user_choice == "exit":
            break


if __name__ == "__main__":
    play_hangman()
