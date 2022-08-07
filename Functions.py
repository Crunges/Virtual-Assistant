import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x
from sympy.utilities.lambdify import lambdastr


# разбор математического выражения
def parse_math(expr):
    if expr != '':
        # вот здесь самая главная часть программы
        res = lambdastr(x, expr)
        res = eval(res)
        # ----------
        return res
    else:
        return False


# постройка графика
def plot_graph(func, a, b, st):
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    xrange = np.arange(a, b, (b-a)/st)
    yrange = [func(i) for i in xrange]
    plt.plot(yrange)
    plt.show()


def main():
    text = input('input_function(x)>')
    expr = parse_math(text)
    if expr:
        x0 = float(input('x0>'))
        x1 = float(input('x1>'))
        steps = float(input('steps>'))
        plot_graph(expr, x0, x1, steps)


main()
