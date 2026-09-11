# -*- coding: utf-8 -*-
"""
data_equipment.py
======================
Toutes les données STATIQUES (qui ne changent jamais pendant une partie)
liées aux armes et aux anneaux, + la construction des "tiers" de loot.

Chaque arme/anneau est une liste de bonus de stats dans l'ordre habituel :
    [HP, MP, ATK, MAG, DEF, SPD, LCK]
(voir constants.py)

Exception : "Hornet Ring" et "Snipers Ring" ne contiennent qu'UN seul nombre
car ils ne boostent pas une stat normale mais directement CritDamage /
CritChance. Ce nombre est lu à la main partout où ces deux anneaux sont
équipés (voir bonfire.py, fonction talk_to_victoria).

Pour ajouter une nouvelle arme ou un nouvel anneau : il suffit d'ajouter une
entrée dans WEAPON ou RINGS ci-dessous, et de l'ajouter dans le bon Tier plus
bas (Tier_One / Tier_Two / Tier_Three / Legendary).
"""

from constants import HP, MP, ATK, MAG, DEF, SPD, LCK
import game_state as gs

# ------------------------------ Armes ------------------------------
# Rangées dans l'ordre : Tier 1 (x3), Tier 2 (x3), Tier 3 (x3), Legendary (x1)
# Si tu changes l'ordre ici, il faut aussi changer la répartition par tier
# plus bas (la boucle "for" suppose que l'ordre du dict = ordre des tiers).
WEAPON = {
    "Knights Sword": [0, 0, 18, 0, 10, 0, 0],       # T1
    "Thiefs Dagger": [0, 0, 8, 0, 0, 20, 0],        # T1
    "Sorcerers Staff": [0, 0, 2, 5, 0, 0, 0],       # T1
    "Partisan": [0, 0, 30, 0, 10, 0, 0],            # T2
    "Hunters Bow": [0, 0, 16, 0, 0, 30, 0],         # T2
    "Andor Sword": [0, 0, 5, 15, 0, 0, 0],          # T2
    "Drake Sword": [0, 0, 50, 0, 20, 0, 0],         # T3
    "Demons Catalyst": [0, 10, 0, 40, 0, 0, 0],     # T3
    "Shadowmoon Blade": [0, 0, 20, 0, 0, 35, 0],    # T3
    "Moonlight Greatsword": [0, 0, 40, 15, 15, 0, 0],  # Legendary
}
WeaponsListName = list(WEAPON.keys())

# ------------------------------ Anneaux ------------------------------
# Tier 1 = +10% d'une stat, Tier 2 = +20%, Tier 3 = +30% (pas encore ajoutés)
RINGS = {
    "Ring of Life": [round((10 / 100) * gs.Max_Stats[HP]), 0, 0, 0, 0, 0, 0],
    "Ring of Enduring": [0, 0, 0, 0, round((10 / 100) * gs.Max_Stats[DEF]), 0, 0],
    "Wind Gods Ring": [0, 0, 0, 0, 0, round((10 / 100) * gs.Max_Stats[SPD]), 0],
    "Ring of Broken Shackles": [0, 0, round((10 / 100) * gs.Max_Stats[ATK]), 0, 0, 0, 0],
    "Four leafed Clover Ring": [0, 0, 0, 0, 0, 0, round((10 / 100) * gs.Max_Stats[LCK])],
    "Ring of the Good Witch": [0, 0, 0, round((10 / 100) * gs.Max_Stats[MAG]), 0, 0, 0],
    "Ring of Heaven": [0, round((10 / 100) * gs.Max_Stats[MP]), 0, 0, 0, 0, 0],
    "Hornet Ring": [50],     # T2 : +50 CritDamage (cas spécial, voir en haut du fichier)
    "Snipers Ring": [20],    # T2 : +20 CritChance (cas spécial, voir en haut du fichier)
}
RingsListName = list(RINGS.keys())

# ------------------------- Tiers de drop (loot) -------------------------
# Chaque Tier est une liste de NOMS d'objets (armes et/ou anneaux).
# loot.py pioche dedans en fonction de l'étage où se trouve le joueur.
Tier_One = []
Tier_Two = []
Tier_Three = []
Legendary = []
ItemTier = [Tier_One, Tier_Two, Tier_Three, Legendary]

# Répartition des armes : 3 par tier pour T1/T2/T3, la dernière est Legendary
x = 0
for i in range(len(ItemTier)):
    nb = 3 if i < 3 else 1
    for _ in range(nb):
        ItemTier[i].append(WeaponsListName[x])
        x += 1

# Répartition des anneaux : 7 en Tier 1, 2 en Tier 2, aucun en Tier 3/Legendary pour l'instant
x = 0
for i in range(len(ItemTier)):
    if i == 0:
        nb = 7
    elif i == 1:
        nb = 2
    else:
        nb = 0
    for _ in range(nb):
        ItemTier[i].append(RingsListName[x])
        x += 1

#------------------------- Explication (Arme&Anneau) -------------------------

#[HP, MP, ATK, MAG, DEF, SPD, LCK]

EquipementExplain = {
    "Knights Sword": "+18 ATK, +10 DEF, [T1]",
    "Thiefs Dagger": "+8 ATK, +20 SPD, [T1]",
    "Sorcerers Staff": "+2 ATK, +5 MAG, [T1]",
    "Partisan": "+30 ATK, +10 DEF, [T2]",
    "Hunters Bow": "+16 ATK, +30 SPD, [T2]",
    "Andor Sword": "+5 ATK, +15 MAG, [T2]",
    "Drake Sword": "+50 ATK, +20 DEF, [T3]",
    "Demons Catalyst": "+10 MP, + 40 MAG, [T3]",
    "Shadowmoon Blade": "+20 ATK, +35 SPD, [T3]",
    "Moonlight Greatsword": "+40 ATK, +15 MAG, +15 DEF, [Legendary]",
    "Ring of Life": "+10% HP, [T1]",
    "Ring of Enduring": "+10% DEF, [T1]",
    "Wind Gods Ring": "+10% SPD, [T1]",
    "Ring of Broken Shackles": "+10% ATK, [T1]",
    "Four leafed Clover Ring": "+10% LCK, [T1]",
    "Ring of the Good Witch": "+10% MAG, [T1]",
    "Ring of Heaven": "+10% MP, [T1]",
    "Hornet Ring": "+50% Critical damage, [T2]",
    "Snipers Ring": "+20% Critical chance, [T2]",
}