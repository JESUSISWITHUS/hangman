import random

def hangman():
    word_list = ['country', 'express', 'frame', 'people', 'signal']
    secret_word = random.choice(word_list)
    guesses_left = 6
    warnings_left = 3
    guessed_word = ['-' for _ in secret_word]
    guessed_letters = set()

    while guesses_left > 0 and '-' in guessed_word:
        print(f"Guesses left: {guesses_left}")
        print(f"Warnings left: {warnings_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print("Current word: " + ''.join(guessed_word))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha():
            warnings_left -= 1
            print("That's not a letter.")
            if warnings_left <= 0:
                guesses_left -= 1
            continue

        if guess in guessed_letters:
            warnings_left -= 1
            print("You already guessed that letter.")
            if warnings_left <= 0:
                guesses_left -= 1
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            guesses_left -= 1 if guess not in 'aeiou' else 2

    if '-' not in guessed_word:
        unique_letters = len(set(secret_word))
        score = guesses_left * unique_letters
        print(f"You won! Your score is {score}.")
    else:
        print(f"You lost! The word was {secret_word}.")

if __name__ == "__main__":
    hangman()
    
#SAKINDI MIRIMO MOISE REG:223009383
#MUNYEMANA GAD REG:223022866
#KAGORORA MUGISHA PATRICK REG: 223014444
