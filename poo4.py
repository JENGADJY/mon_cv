class Voiture :
    
    def __init__(self,marque,couleur,annee ,kilom,etat = False ):
        self.marque = marque
        self.couleur = couleur
        self.annee = annee
        self.etat = False
        self.km = kilom

    def demarrer(self):
   
        if self.etat == False:
            self.etat = True
            print("La voiture a été demarré")
            return self.etat
        else :
            print("La Voiture est deja demarré")

    def arreter(self):
        if self.etat == True:
            self.etat = False
            print("La voiture a été arreté")
            return self.etat
        else :
            print("La Voiture est deja arreté")

    def rouler(self,km_parcourue):
        if self.etat != False:
            print("brr")
            print("La voiture s'appretes a parcourir ",km_parcourue,"de kilometres.")
            return self.km + km_parcourue
            

class Humain:

    def __init__(self,nom,age,voiture = None):
        self.nom = nom
        self.age = age
        self.voiture = None


    def acquerir_voiture(self,voiture):
        if self.voiture != None:
            print("{self.nom}possède deja une voiture")
        else:
            
            self.voitur = Voiture()
        return self.voiture
    
    def demarrer_voiture(self,voiture):
        if self.voiture.etat == True :
            print("La voiture est deja demarrer")
        else:
            self.voiture.etat = True
            print("La voiture a été demarré")

    def arreter_voiture(self,voiture):
        if self.voiture.etat == False :
            print("La voiture est deja arreté")
        else:
            self.voiture.etat = False
            print("La voiture a été arreteé")
class garage:
    def __init__(self,capacite = 4 ,propriétaire= None ):
        self.proptiétaire = None
        self.capacite= 4

    def ajout_vehicule(self,new_voiture):
        if not self.place_dispo():
            print("garage est plein")
        else:
            self.ajout_vehicule.append(new_voiture)
            return len(self.vehicules) < self.capacite 
        



  #  def ajout_vehicule(self,new_Voiture):
  #    self.proptiétaire=Humain()
  #        self.proptiétaire.acquerir_voiture()
  #      new_Voiture=Voiture()
  #      garage=[]
  #      if self.taille >= 20 :
  #          garage.append(self.proptiétaire.new_Voiture)



        

        

        
        
        

    #def place_dispo(self):
    #    nb_place = 0
    #    if len(garage) <= 20 :
    #        print("Il n'y a plus de place")
    #    else:
    #        print("Il y a de la place")
    #        return ajout_vehicule(self.proptiétaire.voiture)
        


