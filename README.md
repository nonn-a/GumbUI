# GumbUI
GumbUI is an in-terminal ascii ui building tool (PYTHON).<br>
It's name stands for **G**eneral **U**se **M**atrix **B**ased **User** **I**nterface

**Output example:**<br>
![Output example :(](https://user-images.githubusercontent.com/86384221/168447498-113d2420-d2bb-4e3c-aa05-1a32e6ce7390.png)

**Tips**
```
- Treat the UI as a cartesian plane.
  The bottom-down point is (0, 0), NOT (1, 1)
- Remember to always print what you are working with.
  Printing is NOT automatic.
```

**Features**
```
Functions:
  - clear():
      Clears the screen.
      Basically system("clear"), or system("cls") for windows users
  - within_matrix(x, y):
      Checks if point (x, y) is within the matrix. returns bool.
  - view():
      Prints out the UI.
  - point(x, y, symbol):
      Draws point at coords (x, y) as given symbol.
      Example: point(2, 5, "o") sets point (2, 5) as "o".
  - segment(x, y, theta, lenght, symbol):
      Draws a segment starting at (x, y), of "lenght" lenght and ad "theta" degrees, starting at +x axis.
  - circle(x, y, radius, symbol):
      Draws a circle with center /centre/ at (x, y) of radius "radius".
  - func(user_input, symbol):
      Function plotter. user_input is the function. The function must be in explicit form (right side only).
      Example: to plot the function y = 3x^3 * sin(x)
      func("3 * (x ** 3) * sin(x)")
      ! Slow, do not use paired with frame-by-frame updates.
  - polygon(x, y, sides, lenght symbol):
      Draws a polygon of given sides and lenght starting at x, y.
  - phrase(x, y, user_input, allow_space, autoline)
      Writes given phrase (user_input) at x, y.
      allow_space is by default set to False.
      If set to True, any space in user_input will not be converted to background (empty).
      autoline is by default se to True.
      If set to true, once reached the end of the matrix, the text will automatically \n.
Objects:
  - schematic:
    Schematics (.schem) are a way to save and load matrix areas.
    - save(xA, yA, xB, yB, schematic_name):
      Saves schematic area (delimited by A(xA, yA) and B(xB, yB).
    - load(x, y, schematic_name):
      Loads schematic area (bottom left corner at x, y).
```


**Should you use this?**
```
Sure, why not. It's very easy and accessible.
It also skips many of the steps someone would have to do using a normal ui program
(like initializing the ui, writing lots of needed fuctions).
It's also easy to keep mantainable code written using GumbUI, as it's clean and fits well with most programs.
```
