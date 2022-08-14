# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #list starts at 0
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
