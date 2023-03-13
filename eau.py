from pokemon import Pokemon



class Eau(Pokemon):

    def __init__(self, nom, niveau, puissance, type):
        Pokemon.__init__(self, nom, niveau, puissance, type)
        self.puissance += 20
        self.setPdv(-20)