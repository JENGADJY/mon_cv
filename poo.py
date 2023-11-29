class Voiture:
    def __init__(self, marque ,modele):
        self.__marque = marque
        self.__modele = modele

    def obtenir_marque(self):
        return self.__marque
    
    def definir_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

ma_voiture = Voiture("Merco","classe A")
print(ma_voiture.obtenir_marque())
ma_voiture.definir_marque("MERCEDES")
print(ma_voiture.obtenir_marque())