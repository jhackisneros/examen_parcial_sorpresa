from main import Punto
from main import Rectangulo

if __name__ == "__main__":
    class_punto = Punto()
    class_rectangulo = Rectangulo()
a = Punto(2, 3)
b = Punto(5, 5)
c = Punto(-3, -1)
d = Punto(0, 0)
    
print("los puntos son")
print(f"el punto a es {a}")
print(f"el punto b es {b}")
print(f"el punto c es {c}")
print(f"el punto d es {d}")
print(f"la base es {class_rectangulo.base()}")
print(f"la altura es {class_rectangulo.altura()}")
print(f"el area es {class_rectangulo.area()}")
print(f"el vector ba es {b.vector(a)}")

print("\n Distancias")
print(f"la distancia entre ab es {a.distancia(b)}")
print(f"la distancia entre ba es {b.distancia(a)}")


distancias = {a: a.distancia(b), b: b.distancia(a), c: c.distancia(d), d: d.distancia(a)}
punto_mas_lejano = max(distancias, key=distancias.get)  # Find the point with the maximum distance
rectangulo = Rectangulo(a, b)
print(f"el punto mas lejano es {punto_mas_lejano} y su distancia es {distancias[punto_mas_lejano]}")
print("\nRectangulo")
print(f"la base es {rectangulo.base}()")
print(f"la altura es {rectangulo.altura}()")
print(f"el area es {rectangulo.area}()")
print(f"el punto mas lejano es {punto_mas_lejano} y su distancia es {distancias[punto_mas_lejano]}")