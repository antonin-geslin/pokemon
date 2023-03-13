from pokemon import Pokemon


class Normal(Pokemon):

    def __init__(self, nom, niveau, puissance, type):
        Pokemon.__init__(self, nom, niveau, puissance, type)
        self.puissance += 10
        self.defense = 10