from pokemon import Pokemon
from combat import Combat
from feu import Feu
from normal import Normal
from eau import Eau
from terre import Terre
import json
import random
import time

Rattata = Normal("Rattata", 1, 5, "Normal")
Pikachu = Normal("Pikachu", 2, 10, "Normal")
Dracaufeu = Feu("Dracaufeu", 5, 30, "Feu")
Tortank = Eau("Tortank", 5, 30, "Eau")
Herbizarre = Terre("Herbizarre", 3, 20, "Terre")
Roucool = Normal("Roucool", 1, 5, "Normal")
Miaouss = Normal("Miaouss", 2, 10, "Normal")
Vipélierre = Terre("Vipélierre", 3, 15, "Terre")
Moustillon = Eau("Moustillon", 2, 10, "Eau")
Pyroli = Feu("Pyroli", 4, 25, "Feu")
Evoli = Normal("Evoli", 3, 20, "Normal")
Carapagos = Terre("Carapagos", 1, 5, "Terre")
Staryu = Eau("Staryu", 1, 5, "Eau")
Ponyta = Feu("Ponyta", 2, 15, "Feu")
Osselait = Terre("Osselait", 4, 20, "Terre")
Magicarpe = Eau("Magicarpe", 0, 0, "Eau")
Tauros = Normal("Tauros", 5, 30, "Normal")

listePokemon = []
listePokemon.append(Rattata)
listePokemon.append(Pikachu)
listePokemon.append(Dracaufeu)
listePokemon.append(Tortank)
listePokemon.append(Herbizarre)
listePokemon.append(Roucool)
listePokemon.append(Miaouss)
listePokemon.append(Vipélierre)
listePokemon.append(Moustillon)
listePokemon.append(Pyroli)
listePokemon.append(Evoli)
listePokemon.append(Carapagos)
listePokemon.append(Staryu)
listePokemon.append(Ponyta)
listePokemon.append(Osselait)
listePokemon.append(Magicarpe)
listePokemon.append(Tauros)

combat = Combat()

typeInteract = [["Eau", 1, 0.5, 2, 1], ["Feu", 2, 1, 0.5, 1], ["Terre", 0.5, 2, 1, 1], ["Normal", 1, 1, 1, 1]]

pokedexBis = []

menu = True

while menu:
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Bienvenue dans le jeu Pokemon !")
    print("Lancer une partie (1)")
    print("Ajouter un pokemon à combattre (2)")
    print("Accéder au pokedex (3)")
    choix = input()
    if choix == str(1):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Choisissez votre starter : ")
        print("Sabelette (1)")
        print("Salameche (2)")
        print("Carapuce (3)")
        choixStarter = input()
        if choixStarter == str(1):
            pokemonJoueur = Terre("Sabelette", 1, 10, "Terre")
            combat.addPokedex(pokemonJoueur)
            pokedexBis.append(pokemonJoueur)
        elif choixStarter == str(2):
            pokemonJoueur = Feu("Salameche", 1, 10, "Feu")
            combat.addPokedex(pokemonJoueur)
            pokedexBis.append(pokemonJoueur)
        elif choixStarter == str(3):
            pokemonJoueur = Eau("Carapuce", 1, 10, "Eau")
            combat.addPokedex(pokemonJoueur)
            pokedexBis.append(pokemonJoueur)
        menu = False
    elif choix == str(2):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Pour ajouter un pokemon à combattre, veuillez entrer les informations suivantes : ")
        entry1 = input("Nom : ")
        entry2 = input("Niveau : ")
        entry3 = input("Puissance : ")
        entry4 = input("Type : ")
        if entry5 == "Eau" or entry5 == "eau":
              pokemon:entry1 = Eau(entry1, int(entry2), int(entry3), entry4)
        elif entry5 == "Feu" or entry5 == "feu":
            pokemon:entry1 = Feu(entry1, int(entry2), int(entry3), entry4)
        elif entry5 == "Terre" or entry5 == "terre":
            pokemon:entry1 = Terre(entry1, int(entry2), int(entry3), entry4)
        elif entry5 == "Normal" or entry5 == "normal":
            pokemon:entry1 = Normal(entry1, int(entry2), int(entry3), entry4) 
        else:                    
            pokemon:entry1 = Pokemon(entry1, int(entry2) ,int(entry3), entry4)
        listePokemon.append(pokemon)
        for i in listePokemon:
            print(i.getNom(), i.type, "Points de vie :", i.getPdv(), "Niveau :", i.niveau, "Puissance :",  i.puissance, "Defense :", i.defense)
            input("Appuyez sur entrée pour revenir au menu principal")
    elif choix == str(3):
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Votre pokedex : ")
        combat.lookPokedex()

        input("Appuyez sur entrée pour revenir au menu principal")
            


running = True

while running:
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Votre Pokemon")
    pokemonJoueur.pokemonGetIinfos()
    input("Appuyez sur entrée pour continuer")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    if input("Voulez vous voir votre pokedex ? y/n") == "y":
        combat.lookPokedex()
        input("Appuyez sur entrée pour continuer")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
    if input("Voulez vous changer de pokemon ? y/n") == "y":
        choix = input("Entrez le nom du pokemon que vous voulez changer (ne pas oublier la majuscule) : ")
        pokemonJoueur = combat.changePokemon(choix, pokedexBis)
        input("Appuyez sur entrée pour continuer")
    i = random.randint(0, len(listePokemon)-1)
    pokemonEnnemi = listePokemon[i]
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Vous allez combattre :", pokemonEnnemi.getNom(), pokemonEnnemi.type, "Points de vie :", pokemonEnnemi.getPdv(), "Niveau :", pokemonEnnemi.niveau, "Puissance :",  pokemonEnnemi.puissance, "Defense :", pokemonEnnemi.defense)
    print("il sera ajouté à votre pokedex si vous gagnez")
    puissanceJ = pokemonJoueur.puissance
    pdvJ = pokemonJoueur.getPdv()
    defenseJ = pokemonJoueur.defense
    puissanceE = pokemonEnnemi.puissance
    pdvE = pokemonEnnemi.getPdv()
    defenseE = pokemonEnnemi.defense
    combat.getPuissance(pokemonJoueur, pokemonEnnemi, typeInteract)
    combat.getPuissance(pokemonEnnemi, pokemonJoueur, typeInteract)
    print("Votre adversaire est de type:", pokemonEnnemi.type, "vous lui infligez donc", pokemonJoueur.puissance, "dégats")
    print("Vous êtes de type:", pokemonJoueur.type, "votre adversaire vous inflige donc", pokemonEnnemi.puissance, "dégats")
    input("Appuyez sur entrée pour commencer le combat")
    while pokemonEnnemi.getPdv() > 0 and pokemonJoueur.getPdv() > 0:
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Vous attaquez")
        time.sleep(1)
        if combat.randomMiss() == 1:
            print("Vous avez infligé", pokemonJoueur.puissance, "dégats à votre adversaire")
            combat.getHurt(pokemonEnnemi, pokemonJoueur)
            print("Il lui reste", pokemonEnnemi.getPdv(), "points de vie")
            if pokemonEnnemi.getPdv() <= 0:
                time.sleep(2)
                break
            input("Appuyez sur entrée pour continuer")
        else:
            print("Vous avez raté votre attaque")
            input("Appuyez sur entrée pour continuer")
        
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("Votre adversaire attaque")
        time.sleep(1)
        if combat.randomMiss() == 1:
            print("Votre adversaire vous à infligé ", pokemonEnnemi.puissance, "dégats")
            combat.getHurt(pokemonJoueur, pokemonEnnemi)
            print("Il vous reste", pokemonJoueur.getPdv(), "points de vie")
            if pokemonJoueur.getPdv() <= 0:
                time.sleep(2)
                break
            input("Appuyez sur entrée pour continuer")
        else:
            print("Votre adversaire a raté son attaque")
            input("Appuyez sur entrée pour continuer")

    
    
    if combat.pokemonDead(pokemonJoueur, pokemonEnnemi) == pokemonEnnemi.getNom():
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print(pokemonJoueur.getNom(),"à gagné un niveau !")
        print(pokemonJoueur.getNom(), "Voit sa puissance améliorée de 10 points")
        print(pokemonJoueur.getNom(), "Voit sa défense améliorée de 5 points")
        print(pokemonEnnemi.getNom(), "à été ajouté à votre pokedex")
        pokemonJoueur.niveau += 1
        pokemonJoueur.resetPdv(pdvJ)
        pokemonJoueur.puissance = puissanceJ + 10
        pokemonJoueur.defense = defenseJ + 5

        pokemonEnnemi.puissance = puissanceE
        pokemonEnnemi.resetPdv(pdvE)
        pokemonEnnemi.defense = defenseE 
        combat.changeStats(pokemonJoueur)
        combat.addPokedex(pokemonEnnemi)
        pokedexBis.append(pokemonEnnemi)
        input("Appuyez sur entrée pour continuer")
    elif combat.pokemonDead(pokemonJoueur, pokemonEnnemi) == pokemonJoueur.getNom():
        print("Vous avez perdu !")
        running = False


    

