from math import *
from os import name, system
import time

width, height = 20, 20 #Size of matrix (x, y)
background = "·" #Background of matrix
matrix = [[background for j in range(width)] for i in range(height)] #Matrix initialization

class state:
    def save(state_name: str):
        global matrix, width, height
        if width == 0 or height == 0:
            return
        output = ""
        for i in range(height):
            for j in matrix[i]:
                output += j + " "
            if i != width - 1:
                output += "\n"
        f = open(state_name + ".state", "w")
        f.write(output)
        f.close()
    
    backup = []
    def temp_save():
        #Saves current matrix state for undo function
        global matrix
        schematic.backup = [row[:] for row in matrix]

    def load(state_name: str):
        global matrix, width, height
        set_matrix(len(matrix[0]), len(matrix))
        f = open(state_name + ".state", 'r')
        content = f.readlines()
        output = []
        for i, line in enumerate(content):
            output.append(line.split(" "))
        matrix = output

    def clear():
        global matrix, width, height, background
        matrix = [[background for j in range(width)] for i in range(height)]        

def set_matrix(new_width: int, new_height: int, new_background = background):
    #Sets the matrix's height, width and background.
    global matrix, width, height, background
    if new_width < 1 or new_height < 1: #If either new_width or new_height are too small
        width, height = 0, 0
        matrix = []               #Emtpy matrix
        return
    if new_height > height:             #Y Axis
        for j in range(new_height - height):
            matrix.append([background for j in range(width)])
    elif new_height < height:
        for j in range(height - new_height):
            matrix.pop()
    height = len(matrix)      #New height value
    if new_width != width:              #X Axis
        for i in matrix:
            if new_width > width:
                for j in range(new_width - width):
                    i.append(background)
            elif new_width < width:
                for j in range(width - new_width):
                    i.pop()
        width = len(matrix[0]) #New width value
    for i in range(height):    #Old background -> New background
            for j in range(width):
                if matrix[i][j] == background:
                    matrix[i][j] = new_background[0]
    background = new_background[0]

def clear():
    #Clears screen
    if name == 'nt':        #For windows
        system('cls')
    else:                   #For Unix
         system('clear')

def within_matrix(x: int, y: int):
    #Checks if a point P(x, y) is within
    #the representable area of points
    if(x < width and x >= 0) and (y < height and y >= 0):
        return True
    return False

def view():
    clear()
    for i in range(height - 1, -1, -1):
        for j in range(width):
            print(matrix[i][j], end = " ")
        print()

def point(x: int, y: int, symbol = ""):
    x, y = round(x), round(y)
    if within_matrix(x, y):
        if not symbol:
            return matrix[y][x]
        matrix[y][x] = symbol[0]
        return True
    return False

def segment(x: int, y: int, theta: float, length: float, symbol: str):
    theta *= pi / 180           #Degrees -> Radians
    successful = False          #If the segment leaves the matrix, the function stops as successful
    for l in range(round(length)):
        if point(x + l * cos(theta), y + l * sin(theta), symbol):
            successful = True
        elif successful:
            return True

def circle(x: int, y: int, radius: float, symbol: str):
    if radius ** 2 > width ** 2 + height ** 2 or radius <= 0:
        return False

    theta = 0
    alpha = pi * 2 / (radius * 48)      #Angle change unit per iteration.
                                        #Needed to not approximate too much on bigger circles
    
    while theta < 2 * pi:               #Circle building
        point(x + radius * cos(theta), y + radius * sin(theta), symbol)
        theta += alpha

class schematic:
    def save(xA: int, yA: int, xB: int, yB: int, schem_name: str):

        # Correct corners:    # # <- B
        #                A -> # #
        # xA < xB and yA < yB

        # Wrong corners: B -> # #          A -> # #               # # <- A
        #                     # # <- B          # # <- A     B -> # #
        # xA > xB and yA < yB             xA < xB and yA > yB            xA > xB and yA > yB

        global matrix, height, width, background

        xA = min(max(xA, 0), width - 1)
        yA = min(max(yA, 0), height - 1)
        xB = min(max(xB, 0), width - 1)
        yA = min(max(yB, 0), height - 1)

        if xA > xB:                 #Fixing corners
            xA, xB = xB, xA
        if yA > yB:
            yA, yB = yB, yA

        content, temp = [], ""
        for i in range(height):
            for j in range(width):
                if(j <= xB and j >= xA) and (i <= yB and i >= yA): #Similar to within_matrix function
                    temp += matrix[i][j]
            if temp:        #if temp isn't empty
                content.append(temp)
            temp = ""       #Reinizialization of temp

        content.reverse()                           #Correctly flips the matrix upside-down

        open(schem_name + ".schem", "w").close()    #Overrides saves with same schem_name
        with open(schem_name + ".schem", "a") as f:
            for i in range(len(content)):               #Writes content on file
                f.write(" ".join(content[i]) + "\n")
            f.write("background = " + background)

    def undo():
        global matrix                                   #Applies changes saved in backup
        matrix = [row[:] for row in state.backup]

    def load(x: int, y: int, schematic_name: str):
        global matrix, background
        state.temp_save()
        f = open(schematic_name + ".schem", 'r')
        content = f.readlines()             #Reads content from schematic file

        schem_background = content[-1][-1]  #Reads wich symbol represents the background
                                            #The last character of a file will always be set as 
                                            #the schematic's background. Once loaded, the schematic's
                                            #Background will be considered transparent

        content.pop()                       #Removes the last line containing background information

        for i, line in enumerate(content):
            content[i] = line.strip().split(" ")    #Removes \n from file and splits all elements into a matrix
        content.reverse()                           #Correctly flips the matrix upside-down

        for i, val in enumerate(content):           #Putting point on matrix
            for j, val in enumerate(val):
                if val != schem_background:         #Allows for schematic background transparency
                    point(x + j, y + i, val)

def func(user_input: str, symbol: str):
    if "y" in user_input:
        return False
    linear = True
    if "^" in user_input:
        user_input = user_input.replace("^", "**")
    for i in ["pow", "sqrt", "**"]: #Approximation
        if i in user_input:
           linear = False
           break
    try:
        x = 0
        while x < width:
            y = eval(user_input)
            if within_matrix(x, y):
                point(x, y, symbol)
            x = x + 0.1 if linear else x + 0.01
    except:
        pass

def polygon(x: int, y: int, sides: int, length: int, symbol: str):
    if sides <= 2:
        return False
    mirrorAxis = x + length / 2 - 0.5
    theta = (2 * pi) / sides #Radians!
    for i in range(round(sides / 2) + 1):
        for l in range(round(length)): #Segment creation
            calcX, calcY = x + l * cos(theta * i), y + l * sin(theta * i)
            point(calcX, calcY, symbol[0])                  #Right side
            point(mirrorAxis * 2 - calcX, calcY, symbol[0]) #Mirroring
            if calcX <= mirrorAxis and i:
                break
        x = round(x + (length - 1) * cos(theta * i))
        y = round(y + (length - 1) * sin(theta * i))

def phrase(x: int, y: int, user_input: str, allow_space = False, autoline = True):
    if not allow_space:
        temp = user_input
        user_input = []
        for letter in temp:
            user_input.append(letter if letter != ' ' else background)
        user_input = ''.join(user_input)

    for letter in user_input:
        if (x == width and autoline) or letter == "\n":
            x, y = 0, y - 1
        if letter != "\n":
            point(x, y, letter)
            x += 1