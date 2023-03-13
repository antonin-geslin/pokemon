from pokemon import Pokemon



class Terre(Pokemon):

    def __init__(self, nom, niveau, puissance, type):
        Pokemon.__init__(self, nom, niveau, puissance, type)
        self.defense = 20
        self.setPdv(10)