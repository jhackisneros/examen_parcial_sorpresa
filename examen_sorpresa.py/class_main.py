from class_punto import Punto
from class_rectangulo import Rectangulo

if __name__ == "__main__":
    a = Punto(2, 3)
    b = Punto(5, 5)
    c = Punto(-3, -1)
    d = Punto(0, 0)

    print("Los puntos son:")
    print(f"El punto a es {a}")
    print(f"El punto b es {b}")
    print(f"El punto c es {c}")
    print(f"El punto d es {d}")

    print("\nDistancias:")
    print(f"La distancia entre a y b es {a.distancia(b):.2f}")
    print(f"La distancia entre b y a es {b.distancia(a):.2f}")

    distancias = {a: a.distancia(b), b: b.distancia(a), c: c.distancia(d), d: d.distancia(a)}
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano es {punto_mas_lejano} y su distancia es {distancias[punto_mas_lejano]:.2f}")

    rectangulo = Rectangulo(a, b)
    print("\nRectángulo:")
    print(f"La base es {rectangulo.base()}")
    print(f"La altura es {rectangulo.altura()}")
    print(f"El área es {rectangulo.area()}")