# print("Hello World")

# import sys
# from termcolor import colored, cprint

# text = colored("Hello World!", "yellow", attrs=["bold","concealed"])
# print(text)
# cprint("Hello World!", "blue", "on_yellow")

# print_yellow_on_cyan = lambda x: cprint(x, "yellow", "on_cyan")
# print_yellow_on_cyan("Hello, World!")
# print_yellow_on_cyan("Hellom Universe!")

# import sys
# from termcolor import colored

# print(colored("Hello World", "red"))
# print(colored("Hello World", "blue"))
# print(colored("Hello World", "green"))
# print(colored("Hello World", "yellow"))
# print(colored("Hello World", "cyan"))

# print("Hello Universe")

# in Python there is a data structures, integer, string, boolean.
#insert append for adding some data into our existing variable.
# my_list = [1, 2, 3, 4, 5, 9, 200, 300]
# my_list.append(6)
# my_list_2 = my_list
# print(my_list_2)

# # to insert the number in the middle use insert() function
# my_list = [1, 2, 3, 4, 5, 9, 200, 300]

# # Insert the number 6 at index 4 (between 5 and 9)
# my_list.insert(4, 6)

# print(my_list)

# # check_list = {1,2} == {3,2}
# # print(check_list)

# #an example of dictonary
# my_dictionary = {"apple": "sometimes a great fruit", "orange": "a citrus fruit", "banana": "a yellow fruit"}
# my_dictionary_2 = "apple"
# print(my_dictionary[my_dictionary_2])

# a = True
# b = True
# c = True
# if a :
#     print("it is true")
#     print("also print this")
#     if b :
#         print("it is very true")
#     elif c:
#         print("all of this are true")
# else :
#     print("it is false")
    
# print("which ones that true ")

# a = [1,2,3,4,5]
# for numbers in a :
#     print(numbers)
    
# a = 0
# while a < 5 :
#     print(a)
#     a = a + 1

# class dog : 
#     def __init__(self, name) :
#         self.name = name
#         self.legs = 4
        
#     def speak(self) :
#         print(self.name + "says : Bark!")
        
# my_dog = dog("Rovers")
# another_dog = dog("Husky")

# my_dog.speak()
# another_dog.speak()
    
import os
import time
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)
            
    def drawSquare(self, size) :
        i = 0
        while i < size :
            self.right()
            i = i + 1
        i = 0
        while i < size :
            self.down()
            i = i + 1
        i = 0
        while i < size :
            self.left()
            i = i + 1
        i = 0
        while i < size :
            self.up()
            i = i + 1
    

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

# Create a new Canvas instance that is 30 units wide by 30 units tall 
canvas = Canvas(30, 30)

# Create a new scribe and give it the Canvas object
scribe = TerminalScribe(canvas)

# Draw a small square
scribe.right()
scribe.right()
scribe.right()
scribe.down()
scribe.down()
scribe.down()
scribe.left()
scribe.left()
scribe.left()
scribe.up()
scribe.up()
scribe.up()

scribe.drawSquare(20)




     






