from math import *
import time
from os import name, system

width, height = 10, 10
background = "."
matrix = [[background for i in range(width)] for j in range(height)]

def set_size(w: int, h: int):
    global matrix, width, height
    width, height = abs(w), abs(h)
    matrix = [[background for i in range(width)] for j in range(height)]
    
def clear():
    if name == 'nt':
        system('cls')
    else:
         system('clear')

def within_matrix(x: int, y: int):
    if(x < width and x >= 0) and (y < height and y >= 0):
        return True
    return False

def view():
    clear()
    for i in range(height - 1, -1, -1):
        for j in range(width):
            print(matrix[i][j], end = " ")
        print()

def point(x: int, y: int, symbol: str):
    x, y = round(x), round(y)
    if within_matrix(x, y):
        matrix[y][x] = symbol[0]

def segment(x: int, y: int, theta: float, length: float, symbol: str):
    theta *= pi / 180;
    for l in range(round(length)):
        point(x + l * cos(theta), y + l * sin(theta), symbol)

def circle(x: int, y: int, radius: float, symbol: str):
    if radius ** 2 > width ** 2 + height ** 2:
        return False
    theta = 0
    while theta < 2 * pi:
        point(x + radius * cos(theta), y + radius * sin(theta), symbol)
        theta += pi * 2 / (radius * 48)

def func(user_input: str):
    linear = True
    for i in ["pow", "sqrt", "**"]: #Approximation
        if i in user_input:
           linear = False
           break
    try:
        x = 0
        while x < width:
            y = eval(user_input)
            if within_matrix(x, y):
                point(x, y, "o")
            x = x + 0.1 if linear else x + 0.01
    except:
        pass

def polygon(x: int, y: int, sides: int, length: int, symbol: str):
    if sides <= 2:
        return False
    mirrorAxis = x + length / 2 - 0.5
    theta = (2 * pi) / sides #Radians!
    for i in range(ceil(sides / 2) + 1):
        for l in range(round(length)): #Segment creation
            calcX = x + l * cos(theta * i)
            calcY = y + l * sin(theta * i)
            point(calcX, calcY, symbol[0])                  #Right side
            point(mirrorAxis * 2 - calcX, calcY, symbol[0]) #Mirroring
            if calcX < mirrorAxis and i:
                break
        x = round(x + (length - 1) * cos(theta * i))
        y = round(y + (length - 1) * sin(theta * i))

