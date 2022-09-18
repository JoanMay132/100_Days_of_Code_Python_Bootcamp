'''
A class is a just a blueprint for creating objects.

The name of the class should have the first letter capitalized or every word. (PascalCase)

An attribute is a variable that is associated with an object.

Self is the actual object that is being created.
'''
# Create a class
class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username 
        self.followers=0

user_1 = User("001","Joan") # Create an object
user_2 = User("002","Bob") # Create an object
print(user_1.id) # Access the attribute
