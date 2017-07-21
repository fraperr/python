#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import monPremierPackage.nombre

mise = monPremierPackage.nombre.saisirEntier("Combien voulez-vous miser: ")

# Choisir un nombre entre 0 et 49
# On vérifie si la saisie est un entier
# On vérifie que le nombre est compris entre 0 et 50
entreeCorrecte = False
while not entreeCorrecte:
    nombreJoueur = monPremierPackage.nombre.saisirEntier(
        "Choisissez un nombre entre 0 et 49: ")
    if 0<= nombreJoueur <= 50:
        entreeCorrecte = True

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

