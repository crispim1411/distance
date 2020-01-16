import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from math import sqrt
from sympy import *


def build_functions(p):
    """
    Constroi funções usando variável simbólica e lambda

    :param p: ponto para o qual é calculada distância
    :type p: tuple
    :return: curva f(x), derivada da curva f(x), derivada da distância
    :rtype: list
    :raises: Falha ao construir funções: Erro
    """
    try:
        x = Symbol('x')
        f_symbol = eval(input("Enter the function: ").lower())
        f = lambdify(x, f_symbol)
        f1_symbol = f_symbol.diff(x)
        f1 = lambdify(x, f1_symbol)
        dist1_symbol = x - p[0] + f1_symbol * (f_symbol - p[1])
        dist1 = lambdify(x, dist1_symbol)

        return f, f1, dist1
    except Exception as e:
        raise Exception(f"Falha ao construir funções: {e}")


def get_distance(p1, p2):
    """
    Retorna a distância entre os pontos P1 e P2.

    :param p1: coordenadas (x,y) do ponto P1
    :param p2: coordenadas (x,y) do ponto P2
    :type p1: tuple
    :type p2: tuple
    :return: distância
    :rtype: float
    :raises: Não foi possível obter distância entre p1 e p2: Erro
    """
    try:
        distance = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return distance
    except Exception as e:
        raise Exception(f"Não foi possível obter distância entre {p1} e {p2}: {e}")


def fplot(f, distance, p, q):
    """
    Plota o gráfico de f(x) e uma reta traçando a distância do ponto P à curva.

    :param f: curva f(x)
    :param distance: distância de P à f(x)
    :param p: ponto P
    :param q: ponto sobre a curva
    :type f: function
    :type distance: float
    :type p: tuple
    :type q: tuple
    """
    try:
        t = np.arange(0.1, 1000, 0.1)
        plt.plot(t, f(t))
        plt.plot([p[0], q[0]], [p[1], q[1]])  # plotada linha entre os pontos
        plt.plot([p[0]], [p[1]], marker='o', markersize=5, color='red')  # ponto escolhido
        plt.plot([q[0]], [q[1]], marker='o', markersize=5, color='blue')  # ponto na curva
        plt.axis([0, 1.5*p[0], 0, 1.5*p[1]])
        plt.title(f"Distância: {distance}")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Não foi possível plotar o gráfico: {e}")


if __name__ == '__main__':
    try:
        a = float(input("coord x: "))
        b = float(input("coord y: "))
        p = (a, b)
        f, f1, dist1 = build_functions(p)

        xmin = newton(dist1, a, tol=10 ** -10, maxiter=50)
        if isinstance(xmin, complex):
            raise Exception("Nenhuma resposta real encontrada.")
        fmin = f(xmin)

        distance = get_distance(p, (xmin, fmin))
        distance = round(distance, 2)
        print(f"Distância: {distance:.2f}")

        fplot(f, distance, p, (xmin, fmin))
    except Exception as e:
        print(f"Erro: {e}")
