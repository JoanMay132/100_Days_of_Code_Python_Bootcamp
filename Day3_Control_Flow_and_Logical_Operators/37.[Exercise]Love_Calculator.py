# 🚨 Don't change the code below 👇



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
'''
Take both people's names and check for the number of times 
the letters in the word TRUE occurs. Then check for the
number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.'''

#Write your code below this line 👇
#Concatenate
concatenate_stri=(name1+name2).lower()
#Contador para true
t=concatenate_stri.count("t")
r=concatenate_stri.count("r")
u=concatenate_stri.count("u")
e=concatenate_stri.count("e")
true=t+r+u+e
#Counting love
l=concatenate_stri.count("l")
o=concatenate_stri.count("o")
v=concatenate_stri.count("v")
e=concatenate_stri.count("e")
love=l+o+v+e
#cambiando de str a int
love_score=str(true)+ str(love)
love_score=int(love_score)
#Using logical operators.
if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score>40) and (love_score<50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Ustedes son compatibles porque su puntaje es de: {love_score}.")