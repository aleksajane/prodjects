# include <iostream>
# include <cmath>

using
namespace
std;

// Функция
для
вычисления
производной
double
derivative(double
x, double
y) {
return sin(x); // Производная
y
'=sin(x)
}

// Метод
Рунге - Кутты
void
rungeKutta(double
x0, double
y0, double
h, double
limit) {
double
x = x0;
double
y = y0;
cout << "x\ty" << endl;
while (x <= limit) {
cout << x << "\t" << y << endl;
double k1 = h * derivative(x, y);
double k2 = h * derivative(x + h / 2, y + k1 / 2);
double k3 = h * derivative(x + h / 2, y + k2 / 2);
double k4 = h * derivative(x + h, y + k3);

y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
x += h;
}
}

int
main()
{
double
x0 = 0; // Начальное
значение
x
double
y0 = 1; // Начальное
значение
y
double
steps[] = {0.1, 1, 10}; // Шаги

for (double step: steps) {
    cout << "Step: " << step << endl;
rungeKutta(x0, y0, step, 100); // Вызов метода Рунге-Кутты с различными шагами
}

return 0;
}
