from pokemon import Pokemon
import json
import random 
class Combat():



    def pokemonDead(self, pokemon1, pokemon2):
        if pokemon1.getPdv() <= 0:
            return pokemon1.getNom()
        elif pokemon2.getPdv() <= 0:
            return pokemon2.getNom()
        else:
            return False

    def winner(self, pokemon1, pokemon2):
        print(pokemon.getNom(), "a gagné le combat !")


    def loser(self, pokemon):
        print(pokemon.getNom(), "a perdu le combat !")


    def randomMiss(self):
        return(random.randint(0, 1))


    def getPuissance(self, pokemon1, pokemon2, typeInteract):
        for i in typeInteract:
            if pokemon1.type == i[0]:
                if pokemon2.type == "Eau":
                    pokemon1.puissance *= i[1]
                elif pokemon2.type == "Feu":
                    pokemon1.puissance *= i[2]
                elif pokemon2.type == "Terre":
                    pokemon1.puissance *= i[3]
                elif pokemon2.type == "Normal":
                    pokemon1.puissance *= i[4]

    def getHurt(self, pokemon1, pokemon2):
        if pokemon1.defense <= 0:
            pokemon1.setPdv(-(pokemon2.puissance))
        elif pokemon1.defense > 0:
            if pokemon2.puissance - pokemon1.defense > 0:
                pokemon1.setPdv(-(pokemon2.puissance - pokemon1.defense))
                print(pokemon1.getNom(), "à bloqué une partie de l'attaque !")
            else:
                pokemon1.setPdv(0)
                print(pokemon1.getNom(), "à bloqué l'attaque !")

    def addPokedex(self, Pokemon):
        temp = 0
        with open("pokedex.json", "r") as file:
            data = json.load(file)
        for pokemon in data:
            if pokemon["Nom : "] == Pokemon.getNom():
                temp+=1
        if temp == 0:        
            entry = {
                        "Nom : " : Pokemon.getNom(),
                        "Type : " : Pokemon.type,
                        "Points de vie : " : str(Pokemon.getPdv()),
                        "Niveau : " : str(Pokemon.niveau),
                        "Puissance : " : str(Pokemon.puissance), 
                        "Defense : " : str(Pokemon.defense),
                    }


            data.append(entry)

            with open("pokedex.json", "w") as file:
                json.dump(data, file)
        else:
            print("Ce pokemon est déjà dans votre pokedex")

    def changeStats(self, pokemon):
            with open("pokedex.json", "r") as file:
                data = json.load(file)
            for i in data:
                if i["Nom : "] == pokemon.getNom():
                    if i["Points de vie : "] != pokemon.getPdv():
                        i["Points de vie : "] : str(pokemon.getPdv())
                    if i["Niveau : "] != pokemon.niveau:
                        i["Niveau : "] = str(pokemon.niveau)
                    if i["Puissance : "] != pokemon.puissance:
                        i["Puissance : "] = str(pokemon.puissance)
                    if i["Defense : "] != pokemon.defense:
                        i["Defense : "] = str(pokemon.defense)
            with open("pokedex.json", "w") as file:
                json.dump(data, file)

    def lookPokedex(self):
        with open("pokedex.json", "r") as file:
            json_object = json.load(file)
            for i in json_object:
                print(i["Nom : "], i["Type : "], "Points de vie :", i["Points de vie : "], "Niveau :", i["Niveau : "], "Puissance :",  i["Puissance : "], "Defense :", i["Defense : "])


    def changePokemon(self, str, list):
        for i in list:
            if i.getNom() == str:
                print(i.pokemonGetIinfos())
                return i
            else:
                print("Ce pokemon n'est pas dans votre pokedex !")