# prueba.py

from geometria import area_circulo, area_rectangulo, area_triangulo
import matplotlib.pyplot as plt

print("Área del círculo:", area_circulo(1))
print("Área del rectángulo:", area_rectangulo(4, 5))
print("Área del triángulo:", area_triangulo(4, 5))






radios = [1, 2, 3, 4, 5]
areas = []

for radio in radios:
    area = area_circulo(radio)
    areas.append(area)

plt.plot(radios, areas, marker="o")
plt.xlabel("Radio")
plt.ylabel("Área")
plt.title("Área de un círculo")
plt.grid(True)

plt.show()