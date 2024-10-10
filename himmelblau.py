import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definimos la función de Himmelblau
def himmelblau(x):
    x1 = x[0]
    x2 = x[1]
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

# Buscamos los mínimos
initial_guesses = [(0, 0), (-4, 4), (4, -4), (4, 4)]
results = []

for guess in initial_guesses:
    res = minimize(himmelblau, guess, method='BFGS')
    if res.success:
        results.append(res.x)

# Mostramos los resultados
for i, result in enumerate(results):
    print(f"Mínimo {i+1}: x = {result[0]}, y = {result[1]}")

# Graficar la función de Himmelblau para visualizar los mínimos
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Evaluamos la función en la malla de puntos
Z = himmelblau([X, Y])


Z = (X**2 + Y - 11)**2 + (X + Y**2 - 7)**2

plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Función de Himmelblau')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
