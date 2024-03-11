from scipy.integrate import solve_ivp
import numpy as np

# Определение уравнения
def equation(x, y):
    return [(y[1])**2 + np.exp(y[1]) * y[0] - np.e / np.log(x) * (y[0])**2 - 1 / x**2, y[0] - np.e]

# Метод пристрелки
def shooting_method(x_values):
    results = {}
    for x in x_values:
        sol = solve_ivp(equation, [np.e, x], [np.e, 0], method='RK45', dense_output=True)
        results[x] = sol.y[0][-1]
    return results

# Значения x для вывода результатов
x_points = [0, 5, 1, 1.5, 2, 2.5]

# Решение уравнения методом пристрелки для заданных точек x
solution = shooting_method(x_points)

# Вывод результатов
for x, y in solution.items():
    print(f"y({x}) = {y}")
