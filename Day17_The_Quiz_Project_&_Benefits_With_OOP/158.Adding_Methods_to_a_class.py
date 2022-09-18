'''
Class Car:
    def enter_race_mode():
        self.seats=2
'''
class User:
    def __init__(self, user_id, username):
        self.id=user_id
        self.username=username 
        self.followers=0
        self.following=0

    def follow(self,user): #method
        user.followers+=1
        self.following+=1

user_1 = User("001","Joan") # Create an object
user_2 = User("002","Bob") # Create an object
print(user_1.id) # Access the attribute

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)