from abc import ABC , abstractmethod

class Forme(ABC):

    def aire(self):
        pass

class Rectangle(Forme):
    def __init__(self, longueur , largeur ):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur
    
    