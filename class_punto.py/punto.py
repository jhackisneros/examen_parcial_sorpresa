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

if __name__== "__main__":
    class_punto =punto()