import matplotlib.pyplot as plt
import numpy as np
import math

def batman_logo():
    zoom = 20
    x_values = []
    y_values = []
    
    for xz in range(-7 * zoom, -3 * zoom, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
        x_values.append(xz)
        y_values.append(y * zoom)
    
    for xz in range(-3 * zoom, -1 * zoom - 1, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(math.fabs(absx - 1) / (absx - 1))
        x_values.append(xz)
        y_values.append(y * zoom)
    
    x_values.extend([-1 * zoom, -0.5 * zoom, 0.5 * zoom, 1 * zoom])
    y_values.extend([3 * zoom, 2.2 * zoom, 2.2 * zoom, 3 * zoom])
    
    for xz in range(1 * zoom + 1, 3 * zoom + 1, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(math.fabs(absx - 1) / (absx - 1))
        x_values.append(xz)
        y_values.append(y * zoom)
    
    for xz in range(3 * zoom + 1, 7 * zoom + 1, 1):
        x = xz / zoom
        absx = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
        x_values.append(xz)
        y_values.append(y * zoom)
    
    for xz in range(7 * zoom, 4 * zoom, -1):
        x = xz / zoom
        absx = math.fabs(x)
        if absx > 4:  # Evita valores negativos na raiz
            y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
            x_values.append(xz)
            y_values.append(y * zoom)

    for xz in range(4 * zoom, -4 * zoom, -1):
        x = xz / zoom
        absx = math.fabs(x)
        y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(absx - 2) - 1) ** 2)
        x_values.append(xz)
        y_values.append(y * zoom)

    for xz in range(-4 * zoom - 1, -7 * zoom - 1, -1):
        x = xz / zoom
        absx = math.fabs(x)
        if absx > 4:  # Evita valores negativos na raiz
            y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
            x_values.append(xz)
            y_values.append(y * zoom)

    plt.figure(figsize=(8, 6))
    plt.fill(x_values, y_values, color='black')
    plt.gca().set_facecolor('red')  # Define o fundo vermelho
    plt.axis('equal')
    plt.xticks([])
    plt.yticks([])
    plt.show()

batman_logo()
