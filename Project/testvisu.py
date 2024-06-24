import numpy as np
import matplotlib.pyplot as plt

# Generowanie przykładowych danych
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, x.size)

# Tworzenie figury i wykresu 2D
fig, ax = plt.subplots()

# Rysowanie punktów na wykresie
ax.scatter(x, y, color='blue', label='Punkty danych')

# Rysowanie linii na wykresie
ax.plot(x, np.sin(x), color='red', label='Sinusoidalna linia')

# Ustawienia osi
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Prosty wykres 2D')
ax.legend()

# Wyświetlenie wykresu
plt.show()
