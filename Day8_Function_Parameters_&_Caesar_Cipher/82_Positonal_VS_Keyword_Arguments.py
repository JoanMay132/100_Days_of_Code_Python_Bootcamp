# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple function
#def greet():
#  print("Hello")
#  print("How do you do?")
#  print("Isn´t the weather nice today?")

#greet()

#Function that allows for input
#def greet_with_name(name):
#  print(f"Hello {name}")
#  print(f"How do you do {name}?")

#greet_with_name("Joan")

#Functions with more than 1 inputs
#def greet_with(name,location):
#  print(f"Hello {name}")
#  print(f"What is it like in {location}?")
#greet_with("Joan","México")

#Functions with keyword arguments

def greet_keyword(name,location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_keyword(location="México",name="Joan")
  