#Password Generator Project
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','x','y','z'
'A','B','C','D','E','F','G','H','I','J','K','L','M','Ñ','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers=['1','2','3','0','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to the Password Generator!")
nr_letters=int(input("How many letters would you like in your password\n"))
nr_symbols=int(input(f"How many symbols would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n "))

#Easy level
password_list=[]
#nr_letters=4
for char in range(1,nr_letters+1):
    password_list+=random.choice(letters)
print(password_list)
for char in range(1, nr_symbols+1):
    password_list+=random.choice(symbols)
print(password_list)
for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)
print(password_list)

random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your password is: {password}")