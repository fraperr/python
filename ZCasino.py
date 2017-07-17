#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import monPremierPackage.nombre
# On reste dans la boucle tant que l'utilisateur
# n'a pas saisi un entier
estUnEntier = True
while estUnEntier:
    mise = input("Combien voulez-vous miser: ")
    # sous-programme vériant si mise est un entier
    test = monPremierPackage.nombre.verifEntier(mise)
    if test == False:
        estUnEntier = False # permet de sortir de la boucle

mise = int(mise)

# les commentaires sont les mêmes que dans la boucle précédante
estUnEntier = True
while estUnEntier:
    nombreJoueur = input("Choisissez un nombre entre 0 et 49: ")
    test = monPremierPackage.nombre.verifEntier(nombreJoueur)
    if test == False:
        estUnEntier = False

# le jeu à roulette tourne...
nombreRoulette = random.randrange(50)

# information sur le nombre choisi par l'utilateur, et le casino
print("Votre choix: ", nombreJoueur, "\n", "Numéro sortant: ", nombreRoulette)

# les deux numéros sont identiques, le joueur gagne 3 fois la mise
if nombreJoueur == nombreRoulette:
    print("Vous avez gagné: ", 3 * mise)
# si les deux numéros sont paires ou impairs, le joueur gagne la moitié
# de sa mise
elif nombreJoueur % 2 == nombreRoulette % 2:
    print("La banque vous remet: ", math.ceil(mise / 2))
# dans les autres cas, le joueur perd sa mise
else:
    print("Désolé, vous avez perdu votre mise: ", mise)

