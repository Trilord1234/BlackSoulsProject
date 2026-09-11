# -*- coding: utf-8 -*-
"""
dungeon.py
==============
Construit la structure du donjon (quels monstres/boss sur quel étage) et
fournit les fonctions pour piocher un ennemi à combattre.

ASTUCE DE CONCEPTION À CONNAÎTRE (piège si tu la touches sans faire gaffe) :
------------------------------------------------------------------------------
`Dungeon` et `Boss_Room` pointent vers les MÊMES listes en mémoire
(Floor_0, Floor_1, ...). Ce n'est pas une erreur : c'est voulu !
Résultat : quand on ajoute les boss dans Boss_Room, ils atterrissent aussi
à la fin de la liste Dungeon[Floor] correspondante. Du coup :
    - Dungeon[Floor][-1]                -> toujours le nom du boss de l'étage
    - Dungeon[Floor][0 : -1]            -> tous les monstres normaux de l'étage
C'est exactement ce qu'exploite MonsterToFight() ci-dessous (elle tire un
index qui exclut volontairement le dernier élément).
Si un jour tu veux découpler les deux, il faudra faire
`Boss_Room = [list(f) for f in Dungeon]` (des copies) au lieu d'une simple
recopie des références, et adapter le `[-1]` utilisé ailleurs (main.py).
"""

from random import randint

from data_bestiary import MOBS, BOSS

# ------------------------- Répartition par étage -------------------------
Floor_0, Floor_1, Floor_2, Floor_3, Floor_4 = [], [], [], [], []
Floor_5, Floor_6, Floor_7, Floor_8, Floor_9, Floor_10 = [], [], [], [], [], []

Dungeon = [Floor_0, Floor_1, Floor_2, Floor_3, Floor_4,
           Floor_5, Floor_6, Floor_7, Floor_8, Floor_9, Floor_10]
Boss_Room = [Floor_0, Floor_1, Floor_2, Floor_3, Floor_4,
             Floor_5, Floor_6, Floor_7, Floor_8, Floor_9, Floor_10]

# --- Monstres normaux : triés par "puissance" (valeur en Souls) puis répartis
# 3 monstres par étage sur les 4 premiers étages, 4 par étage ensuite.
Monster_Name_List = list(MOBS.keys())
Monster_Value = sorted(MOBS.keys(), key=lambda name: MOBS[name][7])  # 7 = index SOULS

x = 0
for i in range(len(Dungeon)):
    nb = 3 if i < 4 else 4
    for _ in range(nb):
        Dungeon[i].append(Monster_Value[x])
        x += 1

# --- Boss : 1 par étage, sauf étage 8 (3 phases) et étage 10 (2 phases, boss final)
Boss_Name_List = list(BOSS.keys())
x = 0
for i in range(len(Boss_Room)):
    nb = 1
    if i == 8:
        nb = 3
    if i == 10:
        nb = 2
    for _ in range(nb):
        Boss_Room[i].append(Boss_Name_List[x])
        x += 1


def MonsterToFight(Floor):
    """
    Tire un monstre normal au hasard sur l'étage donné (jamais le boss,
    voir l'explication tout en haut du fichier sur l'astuce Dungeon/Boss_Room).

    Retourne (Monster_Name, Monster_Stats) où Monster_Stats est une COPIE
    (.copy()) des stats de base : on peut donc les modifier librement pendant
    le combat sans abîmer les données d'origine dans data_bestiary.MOBS.
    """
    x = randint(0, len(Dungeon[Floor]) - 2)
    Monster_Name = Dungeon[Floor][x]
    Monster_Stats = MOBS[Monster_Name].copy()
    return Monster_Name, Monster_Stats


def NumberOfMonsterToFight():
    """
    Calcule combien de monstres il faudra tuer sur l'étage avant d'accéder
    au boss : 5 de base, avec une chance décroissante d'en rajouter un de
    plus à chaque fois (50% la 1ère fois, puis 50/2=25%, puis 50/3=16%...).
    """
    NbMonster = 5
    More = True
    x = 1
    while More:
        chance = randint(0, 100)
        if chance <= 50 // x:
            NbMonster += 1
            x += 1
        else:
            More = False
    return NbMonster
