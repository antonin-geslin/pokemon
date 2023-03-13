

class Pokemon():


    def __init__(self,nom, niveau, puissance, type):
        self.__nom = nom
        self.__pdv = 100
        self.niveau = niveau
        self.puissance = puissance
        self.defense = 0
        self.type = type


    def pokemonGetIinfos(self):
            print("Nom : ", self.__nom)
            print("Type : ", self.type)
            print("Points de vie : ", self.__pdv)
            print("Niveau : ", self.niveau)
            print("Puissance : ", self.puissance)
            print("Defense : ", self.defense)


    def getPdv(self):
            return self.__pdv
        
    def setPdv(self, pdv):
        if self.__pdv + pdv <= 100:
            self.__pdv += pdv
    def resetPdv(self, pdv):
        self.__pdv = pdv

    def getNom(self):
            return self.__nom



