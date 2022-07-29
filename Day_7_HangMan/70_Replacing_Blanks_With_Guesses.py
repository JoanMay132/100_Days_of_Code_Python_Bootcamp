'''
70. Replacing Blanks with Guesses

'''

#Step 2

import random 
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)

#Testing code
print(f"Pssst, the solution is {chosen_word}. ")

'''
#Todo-1: -Create an empty list called display.
#For each letter in the chosen_word, add a "_" to
'display'
#So if the chosen_word was "apple", display should be 
["_","_","_","_","_"] with 5 "_" representing each letter to guess.


'''
display=[]
word_length=len(chosen_word)
for _ in range(chosen_word): #loop
    display+= "_"

print(display)
guess=input("Guess a letter: ").lower()

'''
#Todo-2: -Loop through each position in the chosen_word;
#if the letter at that position matches 'guess' then
reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was
"apple", then display should be ["_","p","p","_","_"].
'''
for position in range(word_length):
  letter=chosen_word[position]
  if letter == guess: #Va recorriendo caracter x caracter
    display[position]=letter

'''
#Todo-3: - Print 'display' and you should see the guessed
lett er in the correct position and every other letter
replace with "_".
#Hint- Do not worry about getting the user to guess the next letter.
We will tackle that in step 3.
'''
print(display)