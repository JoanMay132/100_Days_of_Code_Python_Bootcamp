'''
68.Challenge 1 - Picking a Random Words and Checking Answers
'''
import random
#Step 1

word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
guess=input("Guess a letter: ").lower()
print(guess)
for letter in chosen_word:
    if letter == guess: #Va recorriendo caracter x caracter
        print("Right")
    else:
        print("Wrong")
'''
Todo-1-Randomly choose a word from the word_list and
assign it to a variable called chosen_word.

Todo-2-Ask the user to guess a letter and assign
their answer to a variable called guess. Make guess lowecase.

Todo-3-Check if the letter the user guessed (guess)
is one of the letters in the chosen_word
'''