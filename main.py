from matplotlib import pyplot as plt
from util import print_selection_of, read_int
from data import functions, functions_strings, nodes
from newton import poly_from, divdif
import math as m

print_selection_of(functions_strings)
function_index = read_int("Function: ")
f = functions[function_index]

print_selection_of(nodes)
nodes_list_index = read_int("Nodes: ")
x = nodes[nodes_list_index]

y = f(x)  # список значений от списка аргументов

b = divdif(x, y)  # список коэффициентов

poly = poly_from(
    b, x
)  # получаем функцию, которая вычисляет значение многочлена в точке

# ось и значения
x_axis = [i / 10 for i in range(m.ceil(max(x) * 10))]
y_func = f(x_axis)
y_poly = [poly(i) for i in x_axis]

# рисуем
plt.scatter(x, y, color="red")
plt.plot(x_axis, y_func, color="blue")
plt.plot(x_axis, y_poly, color="green")
plt.show()


# меняем одно значение функции
y[2] *= 3
b = divdif(x, y)
poly = poly_from(b, x)
x_axis = [i / 10 for i in range(m.ceil(max(x) * 10))]
y_func = f(x_axis)
y_poly = [poly(i) for i in x_axis]
plt.scatter(x, y, color="red")
plt.plot(x_axis, y_func, color="blue")
plt.plot(x_axis, y_poly, color="green")
plt.show()
