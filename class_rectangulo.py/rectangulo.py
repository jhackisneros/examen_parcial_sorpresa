class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def vector(self, other):
        return (other.x - self.x, other.y - self.y)

    def distancia(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"

class rectangulo():
    def __init__(self, punto1=punto(), punto2=punto()):
        super().__init__()
        self.punto1 = punto1
        self.punto2 = punto2
    def base(self):
        return "la base del rectangulo es{}".format(abs(self.punto1.x-self.punto2.x))
    def altura(self):
        return "la altura del rectangulo es{}".format(abs(self.punto1.y-self.punto2.y))
    def area(self):
        return "el area del rectangulo es{}".format(self.base()*self.altura())
    
a = punto(2,3)
b = punto(5,5)
c = punto (-3,-1)
d = punto(0,0)
    
print("los puntos son")
print(f"el punto a es {a}")
print(f"el punto b es {b}")
print(f"el punto c es {c}")
print(f"el punto d es {d}")
print(f"la base es {rectangulo.base()}")
print(f"la altura es {rectangulo.altura()}")
print(f"el area es {rectangulo.area()}")
print(f"el vector ba es {b.vector(a)}")

print("\n Distancias")
print(f"la distancia entre ab es {a.distancia(b)}")
print(f"la distancia entre ba es {b.distancia(a)}")

distancias = {"a":a.distancia(d),"b":b.distancia(d),"c":c.distancia(d)}
punto_mas_lejano = max(distancias,key=distancias.get)
print(f"el punto mas lejano es {punto_mas_lejano} y su distancia es {distancias[punto_mas_lejano]}")
rectangulo = rectangulo(a,b)
print("\nRectangulo")
print(f"la base es {rectangulo.base}()")
print(f"la altura es {rectangulo.altura}()")
print(f"el area es {rectangulo.area}()")

if __name__== "__main__":
    class_rectangulo =rectangulo()