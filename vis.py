from colorsys import hls_to_rgb
import math

import matplotlib.pyplot as plt
import numpy as np
import os
import cmath
import sys
os.system("cls")

function_limits = {'sqrt': cmath.sqrt, 'exp': cmath.exp, 'log': cmath.log, 'ln': cmath.log, 'sin': cmath.sin, 'cos': cmath.cos, 'tan': cmath.tan, 'pi': cmath.pi, 'e': cmath.e, 'arg': cmath.phase}

def rect_to_polar(z):
    r = math.sqrt(z.real ** 2 + z.imag ** 2)
    theta = math.atan2(z.imag, z.real)
    return [r, theta]

def polar_to_rect(z):
    real = z[0] * math.cos(z[1])
    im = z[0] * math.sin(z[1])
    return complex(real, im)

def graph_function(func, name, inverted):
    vals_to_plot = []

    reals = []
    imags = []
    colors = []

    r = 0
    theta = 0

    while r < 2:
        while theta < 2 * math.pi:
            vals_to_plot.append(cmath.rect(r, theta))
            theta += 0.005
        theta = 0
        r += 0.01


    for val in vals_to_plot:
        reals.append(val.real)
        imags.append(val.imag)

        try:
            z = func(val)
            abs_val = cmath.polar(z)[0]
            arg = cmath.polar(z)[1]

            while arg < 0:
                arg += 2 * math.pi

            while arg > 2 * math.pi:
                arg -= 2 * math.pi

            hsl = []
            if not inverted:
                hsl = [(arg) / (2 * math.pi), 1, (2 / math.pi) * (math.atan(abs_val))]
            else:
                hsl = [(arg) / (2 * math.pi), 1, 1 - ((2 / math.pi) * (math.atan(abs_val)))]

            colors.append(hls_to_rgb(hsl[0], hsl[2], hsl[1]))
        except:
            if not inverted:
                colors.append(hls_to_rgb(1, 1, 1))
            else:
                colors.append(hls_to_rgb(0,0,0))

    
    return (np.array(reals), np.array(imags), [5 for i in range(len(reals))], np.array(colors))
#func, name, inverted = False
def plot_function(func = "lambda z: z ** 3 - 1", name = "z^3 - 1", inverted = False):
    values = {
        'func': complex_function(func),
        'name': name,
        'inverted': inverted
    }
        

    key = graph_function(lambda z: z, "z", values["inverted"])
    new = graph_function(values["func"], values["name"], values["inverted"])

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Complex Function Visualizer')

    ax1.scatter(key[0], key[1], s = key[2], c = key[3])
    ax1.grid()
    ax1.axis('equal')
    ax1.set_title("f(z) = z")

    ax2.scatter(new[0], new[1], s = new[2], c = new[3])
    ax2.grid()
    ax2.axis('equal')
    ax2.set_title(f"f(z) = {values['name']}")

    plt.show()

def help(*argv):
    print("python vis.py {function} {name} {inverted}")
    print("function - Lambda expression detailing a complex function. (In quotes)")
    print("   Example: \"lambda z: z ** 3 + 1\" (For math functions and constants, use keyword math.")

    print("name - Name of the expression. (In quotes)")
    print("   Example: \"z^3 + 1\"")

    print("inverted - Are poles colored black?")
    print("   Example: True")

def complex_function(s):
    return eval(s, function_limits)

def math_help(*argv):
    print("Available complex functions/constants:")
    for k in function_limits.keys():
        print(k)

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'help':
            help()
        elif sys.argv[1] == 'math':
            math_help()
        else:
            plot_function(*sys.argv[1:])
    except:
        print("Issue valid command.")
        print()
        help()