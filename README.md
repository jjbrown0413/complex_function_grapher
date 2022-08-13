# Complex Function Grapher
Uses domain coloring to plot a complex function inputted via lambda expression. (Requires python to be installed and in PATH)

Complex functions are functions that both input and output complex numbers. Each complex number is composed of a real and imaginary component. Therefore, effective visualization of these functions require four dimensions.
To circumvent this issue, domain coloring is used. Each point on the complex plane is given a certain hue and lightness. After inputting the original point into the complex function, the output's argument (angle) and modulus (distance from origin), the complex number's polar representation.
It's resulting argument determines it's hue and the resulting modulus determines it's lightness as given by the following equations:

Hue = argument / (2 * pi)
Lightness = (2 / pi) * arctan(modulus)

With this, values circling the origin follow the color spectrum, large numbers are close to white, and zero is black, with a smooth gradient between.

Through this we can visualize an otherwise difficult to imagine function. The program graphs anything within the unit circle, utilizing a branch cut along the positive real axis if applicable.

vis.py produces illustrations according to these relationships. In the terminal, the following command produces an illustration along with a comparison to f(z) = z

function - Lambda expression detailing a complex function. (In quotes)
   Example: "lambda z: z ** 3 + 1" (For math functions and constants, use keyword math.
name - Name of the expression. (In quotes)
   Example: "z^3 + 1"
inverted - Are poles colored black?
   Example: True
   
Example command: python vis.py "lambda z: exp(1 / z)" "Essential Singularity"

![e1z](https://user-images.githubusercontent.com/28418992/184466181-abca84ef-72d1-4f22-b94d-eb9108c85d4d.png)
