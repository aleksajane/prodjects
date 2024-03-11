from scipy.integrate import solve_ivp
import numpy as np

# Функция, описывающая систему дифференциальных уравнений
def three_body_problem(t, x):
    mu = 0.012277471

    r = np.sqrt((x[0] + mu) ** 2 + x[1] ** 2)  # расстояние до Земли
    s = np.sqrt((x[0] - (1 - mu)) ** 2 + x[1] ** 2)  # расстояние до Луны

    dxdt = [0, 0, 0, 0]
    dxdt[0] = x[2]  # dx/dt = vx
    dxdt[1] = x[3]  # dy/dt = vy
    dxdt[2] = x[0] + 2 * x[3] - (1 - mu) * (x[0] + mu) / r ** 3 - mu * (x[0] - (1 - mu)) / s ** 3
    dxdt[3] = x[1] - 2 * x[2] - (1 - mu) * x[1] / r ** 3 - mu * x[1] / s ** 3
    return dxdt

# Начальные условия для периодичного решения
x0_periodic = [0.994, 0, 0, -2.00158510637908252240537862224]

# Интегрирование системы ОДУ для 100 периодов
t_span = [0, 100 * 17.0652165601579625588917206249]
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # увеличиваем количество точек для гладкости графика

sol = solve_ivp(three_body_problem, t_span, x0_periodic, method='RK45', t_eval=t_eval)

# Вывод результатов интегрирования
print(f"t: {sol.t}")
print(f"x: {sol.y[0]}")
print(f"y: {sol.y[1]}")
