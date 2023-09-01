![Logo_python](https://user-images.githubusercontent.com/86384221/194611654-1cdbbac3-b784-466a-a198-4a081ad008fb.png)
--------------------------------------------------------------------------------

**This project is dead. See below.**

GumbUI is an ascii ui building tool.<br>
It's name stands for **G**eneral **U**se **M**atrix **B**ased **U**ser **I**nterface.


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

`Schematics` are a new kind of object I'm trying to introduce. (Edit: not anymore. See below.)

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



![opsded](https://github.com/nonn-a/GumbUI/assets/86384221/32b144c4-5538-4ecd-966e-2790bf5bbe43)

**The project is dead. It always more or less was, it was just a little thingy I did when I was fifteen - had a lot of fun building and mantaining it :)
The project WON'T be updated anymore (by me).
The code is published under MIT license.**
