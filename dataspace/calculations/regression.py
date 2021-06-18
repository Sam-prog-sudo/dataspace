import numpy as np


class Regression:
    def __init__(self):
        pass

    def find_sum(l, p):
        res = 0

        for i in l:
            res += i ** p

        return res

    def find_mul_sum(l1, l2):
        res = 0

        for i in range(len(l1)):
            res += l1[i] * l2[i]

        return res

    def solve_equ(sum_x, sum_x2, sum_y, sum_xy):
        # Equation no 1
        # Ey = a * Ex + b * n

        # Equation no 2
        # Exy = a * Ex^2 + b * Ex

        n = 30

        p = np.array([[sum_x, n], [sum_x2, sum_x]])
        q = np.array([sum_y, sum_xy])

        res = np.linalg.solve(p, q)

        return res

    def predict(x, res):
        y_pred = []

        for i in x:
            y_pred.append(res[0] * i + res[1])

        return y_pred


def _regression(x, y):
    r = Regression
    sum_x = r.find_sum(x, 1)
    sum_y = r.find_sum(y, 1)
    sum_x2 = r.find_sum(x, 2)
    sum_xy = r.find_mul_sum(x, y)
    res = []
    res = r.solve_equ(sum_x, sum_x2, sum_y, sum_xy)
    return r.predict(x, res)
