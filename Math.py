# -*- coding: utf-8 -*-
# Графики функций

import numpy as np
import math
import matplotlib.pyplot as plt
from sympy.abc import x
from sympy import sympify
from sympy.utilities.lambdify import lambdastr


def f(x):
    return math.sin(x)


def show_help():  # показ сообщения
    print('Чтобы выйти введите \'q\' или \'exit\'')


def parse_math(expr):  # разбор математического выражения
    if expr != '':
        res = lambdastr(x, expr)
        res = eval(res)
        return res
    else:
        return False


def plot_graph(func, a, b, st):  # постройка графика
    xrange=np.arange(a, b, (b-a)/st)
    yrange=[func(i) for i in xrange]
    plt.plot(yrange)
    plt.show()


def debug(v):  # debug
    for i in v:
        print(i)


def main():
    text = ''
    expr = ''
    show_help()

    while 1:
        text = input('Введите функцию(x)>')
        if text == 'q':
            break
        if text == 'exit':
            break
        if text == 'help':
            show_help()
            continue
        expr = parse_math(text)
        if expr:
            x0 = float(input('x0>'))
            x1 = float(input('x1>'))
            steps = float(input('steps>'))
            v = [expr, x0, x1, steps]
            debug(v)
            plot_graph(expr, x0, x1, steps)
        else:
            continue


if __name__ == '__main__':
    main()
