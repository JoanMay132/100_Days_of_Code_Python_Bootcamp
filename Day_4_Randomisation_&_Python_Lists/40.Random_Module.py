import random #random module is a python module
# import my_module

random_integer=random.randint(1,10)
print(random_integer) 

# print(my_module.pi) #we are calling my_module

# Generating random floating point numbers

#We need to use random.random() -> Returns the next random floating point number between [0.0 to 1.0]

random_float = random.random() # will give me output some sort of numbers in the interval between 0 and 1, but
# not including one.
print(random_float)

#How to create a random decimal number between 0 and 5.
random_number= random.randint(1,5)+random.random()
print(random_number)

#another way
randomFloat= random.random()*5
# 0.00000... - 4.999
print(randomFloat)

love_score=random.randint(1,100)
print(f"Your love score is {love_score}")