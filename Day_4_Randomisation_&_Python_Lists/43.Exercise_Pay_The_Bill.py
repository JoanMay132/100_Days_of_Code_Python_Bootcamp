# Split string method
import random
names_string=input("Give me everybody`s names, separated by a comma. ")
names=names_string.split(", ")  # class 'list'

#Get the total number of items in list.
count=len(names)

aleatorio= random.randint(0, count-1)
person_who_will_pay=names[aleatorio]
print(person_who_will_pay + " is going to buy the meal today")

#another way

who_will_pay=random.choice(names)
print(who_will_pay+ " is going to pay the bill")