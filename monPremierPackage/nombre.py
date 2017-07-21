#!/usr/bin/python3
# -*- coding: utf-8 -*-

import monPremierPackage.nombre

def verifEntier(entier):
    try:
        entier = int(entier)
        assert entier > 0
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
    except AssertionError:
        print("Vous avez misé une somme négative.")
    else:
        return True

def saisirEntier(message):
    estUnEntier = False
    while not estUnEntier:
        mise = input(message)
        if monPremierPackage.nombre.verifEntier(mise):
            estUnEntier = True
    return int(mise)
