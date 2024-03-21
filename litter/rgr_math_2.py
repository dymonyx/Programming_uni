import numpy as np
import matplotlib.pyplot as plt

# Уравнение гиперболы
def hyperbola(x):
    return 6.5 / x

# Функция поверхности
def surface_function(x):
    return 2*x + 13/x

# Значения x для построения графика
x_values = np.linspace(1, 4, 400)
y_values_hyperbola = hyperbola(x_values)
y_values_surface = surface_function(x_values)

# Минимум функции
min_x = np.sqrt(13/2)
min_y = 2*np.sqrt(13/2) + 13/np.sqrt(13/2)

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_hyperbola, label='xy = 6.5 (Гипербола)')
plt.plot(x_values, y_values_surface, label='S = 2x + 13/x (Поверхность)')
plt.scatter(min_x, min_y, color='red', label='Минимум S')
plt.scatter(min_x, surface_function(min_x), color='red')  # Добавление красной точки на график S
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(2, 12)  # Изменение диапазона по оси y
plt.legend()
plt.grid(True)
plt.title('Графики уравнения гиперболы и функции поверхности')
plt.show()
