#!/usr/bin/python3
# -*- coding: utf-8 -*-

def verifEntier(entier):
    try:
        entier = int(entier)
        assert entier > 0
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
    except AssertionError:
        print("Vous avez misé une somme négative.")
    else:
        return False
