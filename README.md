![Logo_python](https://user-images.githubusercontent.com/86384221/194611654-1cdbbac3-b784-466a-a198-4a081ad008fb.png)
--------------------------------------------------------------------------------
**GumbUI is an ascii ui building tool.**<br>
It's name stands for **G**eneral **U**se **M**atrix **B**ased **U**ser **I**nterface.

![opsded](https://github.com/nonn-a/GumbUI/assets/86384221/60e76ad4-2a1a-4b0e-9853-99f761b652b2)

**This project is dead.** It always more or less was, it was just a little thingy I did when I was fifteen - had a lot of fun building and mantaining it for a while.
The project **won't** be updated anymore by me, but feel free to take it and make something even cooler out of it.

It's incredible how many things I'd change if I were to program it now - I guess that's a good thing.

The code is published under **MIT license**, feel free to do anything you want within the limits of what the license allows.
--------------------------------------------------------------------------------
<p align="center">
<img src="https://user-images.githubusercontent.com/86384221/194616763-da784ee2-4dec-474f-bb8c-5383e72dadfa.png" width="350">
</p>

- `clear()` Clears the screen, like a system("clear") would.

- `within_matrix(x, y)` Checks if the point (x, y) is within the matrix's surface.

- `view()` Prints out the UI.

- `point(x, y, symbol)` Draws the point (symbol) at coords (x, y).

- `segment(x, y, theta, lenght, symbol)` Draws a segment starting at (x, y), of `lenght` lenght and `theta` degrees.

- `circle(x, y, radius, symbol)` Draws a circle with center at (x, y) of radius `radius`.

- `func(user_input, symbol)` function plotter. `user_input` is a string.
Example: to plot the function y = 3 * x^3 * sin(x)
func("3 * (x ** 3) * sin(x)", #)

- `polygon(x, y, sides, lenght, symbol)` Draws a polygon of given sides and lenght starting at (x, y).

- `phrase(x, y, user_input, autoline)` Writes the string on the screen, starting at (x, y).
If `autoline` is set to `True`, it will automatically create a newline when the end of the surface is reached.

<p align="center">
<img src="https://user-images.githubusercontent.com/86384221/194620353-108b79cb-e70d-425c-9fa3-71680455ec53.png" width="500">
</p>

`Schematics` are a new kind of object I'm trying to introduce. (Edit: not anymore. See above.)

It's supposed to be a way to save and load matrix surface states, even partially.
Schematics will allow to make quicker and easier scripts.
They will be implemented to be indepentent to the background.

TL;DR? They are great.

**Tips**
```
- Treat the UI as a cartesian plane.
  The bottom-left point is (0, 0), NOT (1, 1)
- Remember to always print what you are working with.
  Printing is NOT automatic.
``` 
