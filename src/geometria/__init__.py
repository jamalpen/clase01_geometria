from .areas import area_rectangulo, area_circulo, area_triangulo
from .volumes import volumen_paralelepipedo, volumen_cono, volumen_esfera

# Esto define qué funciones cuando escribe "from geometria import *"
__all__ = [
    "area_rectangulo",
    "area_circulo",
    "area_triangulo",
    "volumen_paralelepipedo",
    "volumen_cono",
    "volumen_esfera",
]
