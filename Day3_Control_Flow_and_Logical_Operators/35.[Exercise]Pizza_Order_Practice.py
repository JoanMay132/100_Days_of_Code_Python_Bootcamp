# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill= 0 #Add a variable to store data

if size=="S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
if add_pepperoni=="Y": #I add an if for store if we want to add pepperoni   
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y": #Finally i´ve added another if for store extra_cheese into the variable
    bill+=1
print(f"Your final bill is ${bill}")