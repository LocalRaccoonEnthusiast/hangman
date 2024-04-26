import random, os, time

correct_letters = []
guesses = ''
start = input("Do you want to begin?(y/n)")
if start == "y":
    print('Selecting random word from list...')
    time.sleep(1.5)
    word_list = open("words.txt", 'r')
    data = word_list.read()
    word_py_list = data.replace('\n', ' ').split(" ")
    chosen_word = random.choice(word_py_list)
    for char in chosen_word:
        correct_letters.append(char)
    print('Word selected!')
    time.sleep(1.0)
    os.system('clear')
    print('Starting Game...')
    time.sleep(1.0)
    os.system('clear')
    turns = 10
elif start == 'n':
    print('Better luck next time')
    time.sleep(1.5)
    os.system('clear')
    exit()
else:
    print('Error: Invalid Input')
    os.system('clear')
    exit()
while turns > 0:
    sorted_guesses = sorted(guesses)
    print('Turns Left:',turns)
    print('\nAlready guessed letters: \n',sorted_guesses)
    no_letter = 0
    for char in chosen_word:
        if char in guesses:
            print(char,end=" "),
        else:
            print("_",end=" "),
            no_letter =+ 1
    
    if no_letter == 0:
        print("\nYou did it! The word was: ", chosen_word)
        time.sleep(5.0)
        break
    guess = input('Guess a letter: ')
    lc_guess = guess.lower()
    guesses += lc_guess
    if lc_guess not in correct_letters:
        turns -= 1
    if turns == 0:
        print('\nToo bad! The word was: ',chosen_word)
        time.sleep(2.0)
        break
    os.system('clear')