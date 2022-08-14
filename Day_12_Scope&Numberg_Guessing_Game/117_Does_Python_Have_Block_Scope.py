################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#There is no Block Scope

game_level=3
def create_enemy():
  enemies=["Skeleton","Zombie","Alien"]
  if game_level < 5:
    new_enemy=enemies[0]

  print(new_enemy)

create_enemy()