# -*- coding: utf-8 -*-
"""
loot.py
===========
Tout ce qui concerne ce que le joueur récupère après avoir tué un monstre :
les Souls (monnaie) et, avec une petite chance, une arme ou un anneau.
"""

from random import randint
import random

import game_state as gs
import ui
from data_equipment import ItemTier, RingsListName, WeaponsListName


def ItemLoot(Floor):
    """
    Tire au sort si le joueur obtient un objet, et lequel.

    30% de chance d'obtenir un objet. Si oui, on choisit d'abord un TIER
    (Tier_One/Two/Three/Legendary) selon l'étage actuel (les étages hauts
    ont plus de chance de donner du bon matériel), puis un objet au hasard
    dans ce tier.

    Retourne le NOM de l'objet (str), ou None si rien n'est obtenu.
    """
    x = randint(0, 100)
    if x <= 30:
        if 0 <= Floor <= 2:
            lootTier = random.choices([ItemTier[0], ItemTier[1]], weights=[80, 20])[0]
        elif 3 <= Floor <= 5:
            lootTier = random.choices([ItemTier[0], ItemTier[1], ItemTier[2]], weights=[40, 50, 10])[0]
        elif 6 <= Floor <= 8:
            lootTier = random.choices([ItemTier[1], ItemTier[2], ItemTier[3]], weights=[30, 60, 10])[0]
        else:  # 9 <= Floor
            lootTier = random.choices([ItemTier[2], ItemTier[3]], weights=[70, 30])[0]

        if len(lootTier) > 0:
            return random.choice(lootTier)
        return None
    return None


def Loot(Floor):
    """
    À appeler juste après avoir vaincu un monstre : donne au joueur les Souls
    du monstre (gs.Monster_Stats), tente un tirage d'objet (voir ItemLoot),
    et range l'objet obtenu dans le bon inventaire.
    """
    gs.Stats[gs.SOULS] += gs.Monster_Stats[gs.SOULS]
    print(f"You gain {gs.Monster_Stats[gs.SOULS]} Souls !")

    Item = ItemLoot(Floor)
    if Item in RingsListName:
        gs.RingsInventory.append(Item)
    elif Item in WeaponsListName:
        gs.WeaponsInventory.append(Item)

    if Item is not None:
        print(f"You gain {Item} ! Check Victoria to equip yourself with")

    ui.wait()
