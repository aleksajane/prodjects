import numpy as np
import matplotlib.pyplot as plt

def y_true(x):
    return 2 - np.cos(x)

def f(x):
    return np.sin(x)

def runge_kutta_6th_order(x0, y0, a, b, dx):
    n = int((b - a) / dx)
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        k1 = f(x_vals[i])
        k2 = f(x_vals[i] + 0.2 * dx)
        k3 = f(x_vals[i] + 0.3 * dx)
        k4 = f(x_vals[i] + 3 * dx / 5)
        k5 = f(x_vals[i] + dx)
        k6 = f(x_vals[i] + 7 * dx / 8)

        y_vals.append(y_vals[i] + dx * ((16.0/135) * k1 + (6656.0/12825) * k3 + (28561.0/56430) * k4 - (9.0/50) * k5 + (2.0/55) * k6))
        x_vals.append(x_vals[i]+dx)

    return x_vals, y_vals

def runge_kutta_2nd_order(x0, y0, a, b, dx):
    n = int((b - a) / dx)
    x_vals = [x0]
    y_vals = [y0]
    for i in range(n):
        k1 = dx * f(x_vals[i])
        k2 = dx * f(x_vals[i] + dx)

        y_vals.append(y_vals[i] + (k1 + k2) / 2)
        x_vals.append(x_vals[i] + dx)

    return x_vals, y_vals

if __name__ == "__main__":
    x_vals_1_6th, y_vals_1_6th = runge_kutta_6th_order(0.0, 1.0, 0, 100, 0.1)
    x_vals_1_2nd, y_vals_1_2nd = runge_kutta_2nd_order(0.0, 1.0, 0, 100, 0.1)
    x_vals_2_6th, y_vals_2_6th = runge_kutta_6th_order(0.0, 1.0, 0, 100, 1)
    x_vals_2_2nd, y_vals_2_2nd = runge_kutta_2nd_order(0.0, 1.0, 0, 100, 1)
    x_vals_3_6th, y_vals_3_6th = runge_kutta_6th_order(0.0, 1.0, 0, 100, 10)
    x_vals_3_2nd, y_vals_3_2nd = runge_kutta_2nd_order(0.0, 1.0, 0, 100, 10)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals_1_6th, y_vals_1_6th, label="6th h=0.1")
    plt.plot(x_vals_1_2nd, y_vals_1_2nd, label="2nd h=0.1")
    plt.plot(x_vals_2_6th, y_vals_2_6th, label="6th h=1")
    plt.plot(x_vals_2_2nd, y_vals_2_2nd, label="2nd h=1")
    plt.plot(x_vals_3_6th, y_vals_3_6th, label="6th h=10")
    plt.plot(x_vals_3_2nd, y_vals_3_2nd, label="2nd h=10")
    x_vals_sin = np.linspace(0, 100, 1000)
    plt.plot(x_vals_sin, y_true(x_vals_sin), label="аналитическое решение", linestyle='--')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Runge-Kutta Method")
    plt.legend()
    plt.grid(True)
    plt.show()
