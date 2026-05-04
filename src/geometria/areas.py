import math

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo (b * h)."""
    return base * altura

def area_circulo(radio):
    """Calcula el área de un círculo (pi * r^2)."""
    return math.pi * (radio ** 2)

def area_triangulo(base, altura):
    """Calcula el área de un triángulo (b * h / 2)."""
    return (base * altura) / 2
