import random

random_words = ["dog", "cat", "sheep", "pig", "chicken"]

while True:
    #Makes Words Random every run
    computer_secret_word = random.choice(random_words)

    #Applies Conditions To Each Word
    if computer_secret_word == 'dog':
        print("This animal barks!")
    elif computer_secret_word == 'cat':
        print("This animal meows!")
    elif computer_secret_word == 'sheep':
        print("This animal says bahhh")
    elif computer_secret_word == 'pig':
        print("This animal oinks")
    elif computer_secret_word == 'chicken':
        print("This animal mates with roosters")

    #Creating Function For Guess
    def word_func(guess, computer_secret_word):
        guess = input("Guess a word: ").lower()
        if guess == computer_secret_word:
            print("CONGRATULATIONS! You guessed the word! :)\n")
        else:
            print("No! That's incorrect!\n")

    word_func(None, computer_secret_word)

    #Asking User If They would like to play again
    replay = input("Would you like to replay? (Y/N): ").upper()
    if replay == 'N':
        print("Thanks for playing! \n")
        break



