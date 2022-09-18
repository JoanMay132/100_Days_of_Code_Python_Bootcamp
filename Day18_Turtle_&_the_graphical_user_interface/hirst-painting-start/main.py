###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from hashlib import new
import colorgram

rgb_colors = []
colors = colorgram.extract('a:/OneDrive - Universidad Autonoma del Carmen/UNACAR_Joan_May/Programacion/100_Days_of_Code_Python/python_exercises/Day18_Turtle_&_the_graphical_user_interface/hirst-painting-start/image.jpg', 30)
#for color in colors:
#    rgb_colors.append(color.rgb)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b 
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
color_list=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]    