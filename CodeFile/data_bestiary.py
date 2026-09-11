# -*- coding: utf-8 -*-
"""
data_bestiary.py
=====================
Uniquement les données brutes des monstres et des boss.
La logique qui répartit ces monstres/boss entre les étages du donjon vit
dans dungeon.py (c'est de la LOGIQUE, pas de la donnée figée).

Chaque monstre/boss est une liste [HP, MP, ATK, MAG, DEF, SPD, LCK, SOULS]
(voir constants.py). SOULS = nombre de Souls gagnées en le tuant, et c'est
aussi ce qui sert à les trier du plus faible au plus fort (voir dungeon.py).
"""

MOBS = {
    "Hollow": [85, 0, 30, 6, 5, 10, 8, 5],
    "Executioner Pig": [200, 0, 40, 6, 10, 25, 8, 10],
    "Mandragora": [125, 0, 30, 10, 10, 30, 8, 30],
    "Dark Fairy": [145, 200, 21, 250, 10, 25, 8, 45],
    "Slime": [290, 20, 50, 10, 60, 30, 10, 80],
    "Gutter Rat": [100, 200, 55, 10, 10, 55, 10, 50],
    "Cadaver": [500, 40, 65, 10, 35, 15, 10, 200],
    "Werewolf": [600, 0, 70, 10, 30, 70, 10, 280],
    "Centaur": [250, 0, 42, 10, 15, 50, 8, 90],
    "Corpse eater Chicken": [120, 200, 43, 10, 15, 10, 30, 40],
    "Alpaca": [40, 0, 15, 10, 10, 200, 8, 40],
    "Man eating Ant": [300, 0, 50, 10, 20, 40, 10, 150],
    "Toxic Butterfly": [690, 300, 60, 10, 20, 47, 10, 230],
    "Ghoul": [900, 0, 90, 10, 15, 30, 10, 400],
    "Bloodsucker": [690, 300, 60, 160, 30, 55, 10, 300],
    "Skeleton": [400, 300, 80, 10, 30, 50, 10, 250],
    "Iron Knight": [900, 40, 70, 10, 55, 60, 10, 380],
    "Sorcerer": [550, 80, 37, 70, 20, 44, 10, 300],
    "Sphinx": [2400, 200, 78, 70, 88, 70, 10, 700],
    "Hippogriff": [1200, 300, 80, 190, 30, 90, 10, 700],
    "Snow Angel": [3500, 80, 125, 80, 100, 95, 10, 1050],
    "White Rabbit": [800, 9000, 5, 800, 100, 200, 200, 10000],
    "Wraith": [3600, 800, 75, 140, 120, 99, 10, 1700],
    "T Rex": [8000, 800, 170, 50, 160, 180, 10, 3000],
    "El Monstro": [6000, 800, 170, 130, 110, 100, 10, 3000],
    "Cerberus": [4000, 800, 120, 70, 88, 95, 10, 1500],
    "One Who_Lurks": [5000, 800, 100, 80, 100, 100, 10, 1480],
    "One Who Drains": [5000, 800, 95, 150, 80, 95, 10, 1500],
    "Cyclops": [13000, 800, 180, 40, 30, 60, 10, 6000],
    "Daedalus": [7500, 800, 160, 50, 115, 75, 10, 3000],
    "Seraphim": [9000, 800, 50, 240, 100, 105, 10, 3500],
    "Failure": [1100, 100, 75, 70, 40, 60, 10, 390],
    "Orthrus": [1300, 0, 85, 10, 44, 75, 10, 800],
    "Murder Doll": [900, 70, 75, 10, 20, 60, 10, 600],
    "Gigas": [25000, 800, 800, 40, 200, 200, 900, 40000],
    "Pixie": [1900, 800, 80, 180, 70, 280, 300, 10000],
    "Imp": [2800, 700, 180, 80, 100, 300, 300, 10000],
    "Kraken": [30000, 5000, 300, 90, 250, 250, 100, 40000],
    "Unfathomable Knight": [13000, 400, 290, 100, 270, 300, 10, 17000],
    "Black Saint": [15500, 9000, 285, 320, 100, 350, 10, 18000],
}

# Boss classés dans l'ordre où ils apparaissent (étage 0 à 10).
# Certains boss ont plusieurs "phases" (ex : Drake Helkaiser -> Rotting -> Undead)
# qui sont juste des entrées séparées dans ce dict, combattues à la suite
# (le TODO "gérer les boss à plusieurs phases" concerne l'enchaînement de ces
# phases, pas encore automatisé dans dungeon.py / combat.py).
BOSS = {
    "Hyena of Hunger": [5300, 40, 85, 10, 25, 65, 10, 7500],
    "Naked King": [10000, 2000, 110, 110, 10, 40, 10, 15000],
    "Cat in Armor": [19000, 5000, 120, 10, 90, 70, 10, 22000],
    "Devourer Patrasche": [17000, 9000, 135, 100, 85, 100, 100, 24000],
    "Monster Behemoth": [20000, 8000, 150, 10, 110, 50, 90, 25500],
    "Singing Bone": [19800, 2000, 110, 150, 140, 110, 150, 32000],
    "Iron Hans": [75000, 7000, 550, 550, 560, 700, 900, 78000],
    "Bandersnatch": [99999, 9999, 670, 600, 300, 500, 100, 1000000],
    "Drake Helkaiser": [20000, 7000, 125, 10, 10, 10, 10, 12000],           # phase 1
    "Rotting Drake Helkaiser": [36000, 9000, 180, 10, 10, 60, 90, 29000],   # phase 2
    "Undead Drake Helkaiser": [60000, 9000, 290, 10, 1, 95, 10, 44000],     # phase 3
    "Pumpkin Carriage": [60000, 7000, 200, 200, 200, 280, 200, 78000],
    "Ash-clad Princess Cinderella": [23000, 9999, 220, 270, 100, 150, 10, 60000],  # phase 1
    "Demon Queen Cinderella": [80000, 9999, 320, 300, 240, 200, 200, 100000],      # phase 2
}
