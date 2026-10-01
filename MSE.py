import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
# MSE = sigma(g - t)^2/n
def truth(x):
    return 2 * (x ** 2) + 3


def guess(x):
    return 2 * (x ** 2) - 4


def mse(y_true, y_pred):
    return ((y_true - y_pred)**2).sum() / len(y_true)


def rmse(mse_value):
    return sqrt(mse_value)


def plot_functions(f_true, f_pred):
    x = np.linspace(1, 10, 100)
    plt.plot(x, f_true(x), label='truth')
    plt.plot(x, f_pred(x), label='guess')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    x_list = np.array([1,2,3,4,5,6,7,8,9,10])
    y_pred = guess(x_list)
    y_true = truth(x_list)
    print(rmse(mse(y_true, y_pred)))
    plot_functions(truth, guess)