class Animal:
    def __init__(self,nom):
        self.nom=nom

    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "woof"
    
class Chat(Animal):
    def parler(self):
        return "meow"
    

chien1 = Chien("buddy")
print(chien1.nom)
print(chien1.parler())

chat1= Chat("n")
print(chat1.nom)
print(chat1.parler())

def faire_parler(animal):
    print(animal.parler())

animal1 = Animal("Créature")

print(faire_parler(animal1)) # logique car animal1 ne possede pas de fonction parler
