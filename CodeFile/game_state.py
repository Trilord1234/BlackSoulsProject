# -*- coding: utf-8 -*-
"""
game_state.py
=================
La "sauvegarde en mémoire" du jeu. C'est ici, et nulle part ailleurs, que
vivent : les stats du joueur, son équipement, l'étage où il se trouve, et
les infos sur le monstre actuellement combattu.

POURQUOI CE FICHIER EXISTE
---------------------------
Presque tous les systèmes (combat, boutique, loot...) ont besoin de lire ou
modifier "les HP du joueur", "l'étage actuel", etc. Plutôt que de faire
passer toutes ces infos en paramètre de fonction en fonction (ce qui serait
illisible avec autant de variables), on les centralise ici, et chaque autre
fichier fait `import game_state as gs` puis lit/écrit `gs.Stats`, `gs.Floor`...

COMMENT MODIFIER CES VARIABLES DEPUIS UN AUTRE FICHIER (IMPORTANT)
--------------------------------------------------------------------
Fais TOUJOURS `import game_state as gs`, jamais `from game_state import Stats`.

    BON  :  import game_state as gs
            gs.Stats[gs.HP] -= 10     # OK : on modifie un élément DANS la liste
            gs.Floor += 1             # OK : on modifie l'attribut du module

    MAUVAIS :  from game_state import Stats, Floor
               Stats[HP] -= 10        # "marche" par chance (une liste peut
                                       # être modifiée sur place)
               Floor += 1             # CASSÉ : ça ne fait que changer une
                                       # copie locale de Floor dans ton fichier,
                                       # le vrai game_state.Floor ne bouge pas.

Pourquoi cette différence ? Une liste/dict peut être modifiée "sur place"
(on change un élément à l'intérieur, l'objet reste le même). Un int/bool/str
en revanche est remplacé entièrement à chaque fois qu'on fait "Floor += 1" ou
"Dead = True" : Python doit alors savoir qu'on veut modifier l'ORIGINAL, pas
une copie locale, d'où l'ancien mot-clé "global" utilisé dans un seul fichier.
En passant par `gs.NomDeLaVariable`, ce problème disparaît tout seul : on ne
manipule jamais une copie, on va lire/écrire directement dans le module.
"""

from constants import HP, MP, ATK, MAG, DEF, SPD, LCK, SOULS

# ------------------------- Identité du joueur -------------------------
Name = "Grimm"

# ------------------------- Stats du joueur -------------------------
# Rappel de l'ordre (voir constants.py) : [HP, MP, ATK, MAG, DEF, SPD, LCK]
Max_Stats = [350, 50, 35, 10, 15, 40, 10]     # Plafond actuel de chaque stat (augmenté par les Souls achetées)
Stats = [350, 50, 35, 10, 15, 40, 10, 0]      # Valeurs actuelles + Souls (index SOULS)

# ------------------------- Équipement -------------------------
Gear = [0, 0, 0]          # [Arme, Anneau slot 1, Anneau slot 2] ; 0 = emplacement vide
WeaponsInventory = []     # Armes possédées mais pas équipées
RingsInventory = []       # Anneaux possédés mais pas équipés
Spells = []               # Sorts appris

# ------------------------- Stats de coup critique -------------------------
CritChance = 5 + (Stats[LCK] // 2)   # % de chance de faire un coup critique
CritDamage = 100                     # % de dégâts bonus sur un coup critique

# ------------------------- Progression dans le donjon -------------------------
Floor = 0                # Étage actuel (0 à 10)
OldFloor = 0              # Sert à détecter un changement d'étage dans la boucle principale
MonsterKill = 0           # Monstres tués sur l'étage actuel
NbMonsterToKill = 0        # Nombre de monstres à tuer avant d'accéder au boss de l'étage
Dead = False               # True juste après que le joueur soit mort
BossFight = False          # True quand le prochain combat est contre le boss de l'étage
END = False                # Passera à True quand le jeu sera terminé (boss final vaincu)

# ------------------------- Combat en cours -------------------------
# Ces variables sont (re)remplies juste avant chaque combat, voir dungeon.py
Monster_Name = None
Monster_Stats = None
HP_max_Monster = 0
MP_max_Monster = 0
CritChanceMonster = 0
CritDamageMonster = 100

# Action défensive choisie par le joueur pour le prochain coup de l'ennemi
Dodge = False
Guard = False
Flee = False   # True si le joueur vient de fuir le combat


def reset_after_death():
    """
    À appeler quand le joueur meurt : retour à l'étage 0, perte des Souls,
    Sorts et objets non équipés (les stats gagnées via Max_Stats restent,
    elles) - exactement comme perdre ses Souls/objets dans Dark Souls.
    """
    global Floor, MonsterKill, Dead, BossFight
    Floor = 0
    MonsterKill = 0
    Stats[SOULS] = 0
    Spells.clear()
    RingsInventory.clear()
    WeaponsInventory.clear()
    Dead = False
    BossFight = False


def heal_at_bonfire():
    """Remet HP/MP au max (et annule les debuffs) : appelé à chaque passage au Feu de Camp."""
    Stats[:len(Max_Stats)] = Max_Stats
