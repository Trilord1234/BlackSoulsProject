# -*- coding: utf-8 -*-
"""
data_souls.py
=================
Les "Souls de montée de niveau" vendues par Elisabeth au feu de camp.
Chaque entrée est une liste [HP, MP, ATK, MAG, DEF, SPD, LCK, SOULS] où :
    - les 7 premiers nombres sont ajoutés à Max_Stats quand on achète 1 Soul
    - le dernier nombre (SOULS) est le coût en Souls-monnaie, en négatif
      (ex: -350 veut dire "coûte 350 Souls")

L'ordre de ce dict correspond à l'ordre d'apparition dans la boutique.
"""

from constants import SOULS

LV_UP_SOULS = {
    "Green Soul": [30, 0, 0, 0, 0, 0, 0, -350],
    "Purple Soul": [0, 10, 0, 0, 0, 0, 0, -350],
    "Red Soul": [0, 0, 3, 0, 0, 0, 0, -350],
    "Blue Soul": [0, 0, 0, 0, 3, 0, 0, -350],
    "Yellow Soul": [0, 0, 0, 0, 0, 3, 0, -350],
    "Ashen Soul": [0, 0, 0, 3, 0, 0, 0, -350],
    "Four Leafed CLover": [0, 0, 0, 0, 0, 0, 3, -350],
    "Black Soul": [10, 5, 1, 1, 1, 1, 1, -1000],
}

SoulsListName = list(LV_UP_SOULS.keys())

SoulsExplanation = [
    "Green Soul : +30 HP",
    "Purple Soul : +10 MP",
    "Red Soul : +3 ATK",
    "Blue Soul : +3 DEF",
    "Yellow Soul : +3 SPD",
    "Ashen Soul : +3 MAG",
    "Four Leafed CLover : +3 LCK",
    "Black Soul : +10 HP | +5 MP | +1 ALL",
]
