#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import monPremierPackage.nombre

estUnEntier = True
# import pdb; pdb.set_trace()
while estUnEntier:
    mise = input("Combien voulez-vous miser: ")
    test = monPremierPackage.nombre.verifEntier(mise)
    if test == False:
        estUnEntier = False

mise = int(mise)
nombreJoueur = input("Choisissez un nombre entre 0 et 49: ")

estUnEntier = monPremierPackage.nombre.verifEntier(nombreJoueur)
if estUnEntier:
    nombreJoueur = int(nombreJoueur)
    nombreRoulette = random.randrange(50)

    print("Votre choix: ", nombreJoueur, "\n", "Numéro sortant: ", nombreRoulette)
    if nombreJoueur == nombreRoulette:
        print("Vous avez gagné: ", 3 * mise)
    elif nombreJoueur % 2 == nombreRoulette % 2:
        print("La banque vous remet: ", math.ceil(mise / 2))
    else:
        print("Désolé, vous avez perdu votre mise: ", mise)

