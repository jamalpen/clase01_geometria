import math

def volumen_paralelepipedo(largo, ancho, alto):
    """Calcula el volumen de una caja/paralelepípedo."""
    return largo * ancho * alto

def volumen_cono(radio, altura):
    """Calcula el volumen de un cono (pi * r^2 * h / 3)."""
    return (math.pi * (radio**2) * altura) / 3

def volumen_esfera(radio):
    """Calcula el volumen de una esfera (4/3 * pi * r^3)."""
    return (4/3) * math.pi * (radio**3)
