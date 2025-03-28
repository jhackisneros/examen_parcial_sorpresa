import math

class punto():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y=y
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def cuadrante(self):
        if self.x == 0 and self.y ==0:
            return "Origen" 
        elif self.x == 0:
            return "Eje Y"
        elif self.y == 0:
            return "Eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante 2"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante 3"
        else:
            return "Cuadrante 4"
    def vector(self,p):
        return "El vector entre {} y {} es ({},{})".format(self,p,self.x-p.x,self.y-p.y)
    def distancia(self,p):
        return "La distancia entre {} y {} es {}".format(self,p,((self.x-p.x)*2+(self.y-p.y)*2)*0.5)
class rectangulo():
    def __init__(self,punto1=punto(),punto2=punto()):
        self.punto1 = punto1
        self.punto2 = punto2
    def base(self):
        return "la base del rectangulo es{}".format(abs(self.punto1.x-self.punto2.x))
    def altura(self):
        return "la altura del rectangulo es{}".format(abs(self.punto1.y-self.punto2.y))
    def area(self):
        return "el area del rectangulo es{}".format(self.base()*self.altura())
    
a = punto(4,8)
b = punto(9,9)
c = punto (-5,-10)
d = punto(0,0)
    
print("los puntos son")
print(f"el punto a es {a}")
print(f"el punto b es {b}")
print(f"el punto c es {c}")
print(f"el punto d es {d}")

print("\n vectores")
print(f"el vector ab es {a.vector(b)}")
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


                                                                                                          
