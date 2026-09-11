# -*- coding: utf-8 -*-
"""
constants.py
================
Indices utilisés pour lire/écrire une valeur dans une liste de stats.

Beaucoup de listes dans ce jeu (Stats, Max_Stats, les stats d'une arme,
d'un anneau, d'un monstre, d'un boss...) respectent TOUJOURS le même ordre :

    [HP, MP, ATK, MAG, DEF, SPD, LCK]

(et parfois un 8ème élément, SOULS, pour Stats / LV_UP_SOULS / MOBS / BOSS)

Plutôt que d'écrire Stats[0], Stats[1]... (ce qu'on appelle des "nombres
magiques", illisibles pour n'importe qui - toi y compris dans 6 mois),
on écrit Stats[HP], Stats[MP], etc. C'est strictement la même chose pour
Python, mais tellement plus lisible pour un humain.

Comment réutiliser ça :
    from constants import HP, MP, ATK, MAG, DEF, SPD, LCK, SOULS
    une_liste_de_stats[ATK]  # -> la valeur d'attaque de cette liste
"""

HP = 0
MP = 1
ATK = 2
MAG = 3
DEF = 4
SPD = 5
LCK = 6

# Uniquement présent dans Stats, LV_UP_SOULS, MOBS et BOSS
SOULS = 7
