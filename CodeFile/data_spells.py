# -*- coding: utf-8 -*-
"""
data_spells.py
==================
Toutes les données concernant les sorts : leurs effets/dégâts, leur coût en
Souls dans la boutique de Dorothy, et leur texte d'explication.

Chaque sort est un dict avec :
    "type"      : "Attack" ou "Heal"
    "power"     : dégâts infligés ou HP soignés (dépend des stats du joueur
                  AU MOMENT DU CHARGEMENT du fichier, voir la remarque
                  "ATTENTION" ci-dessous)
    "mana_cost" : coût en MP pour lancer le sort
    "effect"    : None, ou un effet de statut ("Poison", "Burn", "Freeze")
                  -> ces effets de statut ne sont pas encore appliqués en jeu,
                  c'est une des choses qu'il reste à coder (TODO Loot/Effets).

ATTENTION - piège classique à connaître pour la suite du projet :
    "power" est calculé UNE SEULE FOIS, au moment où Python lit ce fichier
    (donc avec les stats de départ du joueur). Si tu veux qu'un sort devienne
    plus puissant quand le joueur monte en Magie/Force, il faudra recalculer
    "power" à chaque lancer de sort (dans combat.py) plutôt que de lire cette
    valeur figée. C'est justement un des 2 gros trucs que tu avais notés à
    faire ("mettre à jour les stats des sorts/objets qui scalent").
"""

import game_state as gs
from constants import MAG, ATK, HP

SPELLS = {
    "Soul Arrow": {
        "type": "Attack",
        "power": 10 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 10,
        "effect": None,
    },
    "Soul Light": {
        "type": "Heal",
        "power": (gs.Stats[MAG] // 4) + round((10 / 100) * gs.Stats[HP]),
        "mana_cost": 12,
        "effect": None,
    },
    "Soul Radiance": {
        "type": "Attack",
        "power": 20 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 15,
        "effect": None,
    },
    "Omniblow": {
        "type": "Attack",
        "power": 15 + round((25 / 100) * gs.Stats[ATK]),
        "mana_cost": 12,
        "effect": None,
    },
    "Poison": {
        "type": "Attack",
        "power": 10 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 20,
        "effect": "Poison",
    },
    "Flame": {
        "type": "Attack",
        "power": 10 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 20,
        "effect": "Burn",
    },
    "Frozen Magic Bullet": {
        "type": "Attack",
        "power": 10 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 20,
        "effect": "Freeze",
    },
    "Heavy Soul Discharge": {
        "type": "Attack",
        "power": 50 + round((25 / 100) * gs.Stats[MAG]),
        "mana_cost": 40,
        "effect": None,
    },
    "Restore": {
        "type": "Heal",
        "power": (gs.Stats[MAG] // 4) + round((30 / 100) * gs.Stats[HP]),
        "mana_cost": 25,
        "effect": None,
    },
}

# Ces 2 listes contiennent au départ les mêmes noms, mais SpellsListName va être
# vidée au fur et à mesure des achats chez Dorothy (elle utilise .pop()), donc
# les 2 listes finissent par diverger. SpellsListName2 sert uniquement à
# afficher les explications de TOUS les sorts, même déjà achetés (voir
# bonfire.py -> talk_to_dorothy, option 2).
SpellsListName = list(SPELLS.keys())
SpellsListName2 = list(SPELLS.keys())

# Coût en Souls, dans le même ordre que SpellsListName au démarrage du jeu.
# ATTENTION : comme SpellsListName perd des éléments avec .pop() quand on
# achète un sort, SpellsListCost doit être "poppé" exactement pareil pour
# rester aligné (c'est déjà fait dans bonfire.py).
SpellsListCost = [100, 100, 500, 500, 600, 600, 600, 1500, 1500]

SpellsExplain = {
    "Soul Arrow": "Shoot a soul arrow at the target enemy.\n               The power scales with the caster's Magic. Dealing 10+ damage\n",
    "Soul Light": "Soul healing restoring the HP of the caster.\n               The amount restored scales with the caster's Magic. Healing 10% or more\n",
    "Soul Radiance": "Pour soul arrows upon all enemies.\n               The power scales with the caster's Magic. Dealing 20+ damage\n",
    "Omniblow": "Deal unavoidable damage to the target enemy.\n               The power scales with the caster's Strengh. Dealing 15+ damage\n",
    "Poison": "Infect all enemies with a deadly poison.\n               The power scales with the caster's Magic. Dealing 10+ damage and poisoning the ennemy\n",
    "Flame": "Release flames and set the target enemy on fire \n               The power scales with the caster's Magic. Dealing 10+ and burning the ennemy\n",
    "Frozen Magic Bullet": "Unleash a fragment of winter’s wrath \n               The power scales with the caster's Magic. Dealing 10+ damage and freezing the ennemy\n",
    "Heavy Soul Discharge": "Shoot a heavy soul arrow at the target enemy.\n               The power scales with the caster's Magic. Dealing 50+ damage\n",
    "Restore": "Call back the warmth of life from the silence of the grave.\n               The power scales with the caster's Magic. Healing 30% or more\n",
}
