# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:13:11 2025

@author: tristabe
"""

#___________________Black Souls My Ver________________

#Import__________________________________
import time
from random import randint
import random
import os

#Add color after ? Too shity avec Spider, la même encore, visual studio code
#Bon déja je vais switch sur visual studio code vu que Spider se chie dessus avec les clear constant
#Je switch entre le français et l'anglais dans mon programme je fait nimporte quoi XD
#On parle même pas des variables bourré de majuscule, heuresement que je bosse tout seul dessus c'est un coup a donner des crise cardiaque a certain XD...
#Bon ça va bien faire +12h que je dois trvailler dessus, j'ai pas compter mais j'ai passer presque mon weekend dessus
#Le Crit et tout marche bien pour aujourd'hui, donc demain faudra que j'essaye de faire en sorte de camper dans la zone de départ.
#Bon j'arrête de me parler a moi même ici, je sauvegarde et dodo !
#Ok on avance super bien, les boss marche, Dorothy fonctionne, j'ai rebidouiller le dic des sort pour qu'il soit embriquer ou jsp quoi
#Donc 2 énorme truc important a faire, 1- le systeme de loot, 2- Faire en sorte que les items et sort qui proque sur les stats se mette a jour.
#Ah et aussi revisiter les Stats que donne les armes et tout le tralala. Le jeux risque d'être un chouilla dure si je m'en occupe pas.
#Ah et les couleurs je laisse tomber pour le momment, je vais me focaliser pour jouer les musique pendant le jeux, sa sera un peu beaucoup plus fun
#Bref voila voila on avance on avance.
#Le loot c'est clean, manque plus que la mise a jour des loots et les phases des boss.
#Mais je peux présenter le tout ça marche normalement.
#Victoria marche enfin correctement !!!! Je l'aime mais putain elle m'en a fait voir de toutes les couleurs :/


#Better Systeme__________________________
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    input("✿...")

#___________Stat character + Other___________
#BASES = [0, 0, 0, 0, 0, 0, 0, 0]
Name = "Grimm"
Max_Stats = [350, 50, 35, 10, 15, 40, 10] #On a pas les Souls pour pas avoir de problème pour le remplacement
Stats = [350, 50, 35, 10, 15, 40, 10, 0]
Gear = [0 , 0, 0]
WeaponsInventory = []
RingsInventory = []
Spells = []
HP = 0
MP = 1
ATK = 2
MAG = 3
DEF = 4
SPD = 5
LCK = 6

SOULS = 7

CritChance = 5 + (Stats[LCK]//2)
CritDamage = 100


#___________ Rings and Weapon and Spells___________

#BASES=[0, 0, 0, 0, 0, 0, 0]

#Weapon_________________________________________
WEAPON = { #On les laisse dans l'ordre car Tier 1 = 3 ière, T2 = 3 autre, T3 = 3autre, Legendary = Last 
    "Knights Sword" : [0, 0, 18, 0, 10, 0, 0], #T1
    "Thiefs Dagger" : [0, 0, 8, 0, 0, 20, 0], #T1
    "Sorcerers Staff" : [0, 0, 2, 5, 0, 0, 0], #T1
    "Partisan" : [0, 0, 30, 0, 10, 0, 0], #T2
    "Hunters Bow" : [0, 0, 16, 0, 0, 30, 0], #T2
    "Andor Sword" : [0, 0, 5, 15, 0, 0, 0], #T2
    "Drake Sword" : [0, 0, 50, 0, 20, 0, 0], #T3
    "Demons Catalyst" : [0, 10, 40, 0, 0, 0, 0], #T3 
    "Shadowmoon Blade" : [0, 0, 20, 0, 0, 35, 0], #T3
    "Moonlight Greatsword" :  [0, 0, 40, 15, 15, 0, 0] #T4
} #En gros si je veux en rajouter je devrais m'occuper de tout le tralal dans le Sort

WeaponsListName = list(WEAPON.keys())

#Rings_________________________________________

RINGS = {  #9, Euh ils vont se drop, mais essayer d'en rajouter jusqu'a Tier 3 (En gros Tier 1 = 10%,Tier 2 = 20%, Tier 3 = 30%)
    "Ring of Life" : [round((10/100)*Max_Stats[HP]), 0, 0, 0, 0, 0, 0], 
    "Ring of Enduring" : [0, 0, 0, 0, round((10/100)*Max_Stats[DEF]), 0, 0],
    "Wind Gods Ring" :  [0, 0, 0, 0, 0, round((10/100)*Max_Stats[SPD]), 0],
    "Ring of Broken Shackles" : [0, 0, round((10/100)*Max_Stats[ATK]), 0, 0, 0, 0],
    "Four leafed Clover Ring" : [0, 0, 0, 0, 0, 0, round((10/100)*Max_Stats[LCK])],
    "Ring of the Good Witch" : [0, 0, 0, round((10/100)*Max_Stats[MAG]), 0, 0, 0],
    "Ring of Heaven" : [0, round((10/100)*Max_Stats[MP]), 0, 0, 0, 0, 0],
    "Hornet Ring" : [50], #+50 sur les CritDamage T2
    "Snipers Ring" : [20] #+20 sur CritChance T2
} #Pour le momment on a que du Tier 1 et Tier 2

RingsListName = list(RINGS.keys())

#Spells_______________________________________

SPELLS = {
    "Soul Arrow": {
        "type": "Attack",
        "power": 10 + round((25/100) * Stats[MAG]),
        "mana_cost": 10,
        "effect": None
    },
    "Soul Light": {
        "type": "Heal",
        "power": (Stats[MAG] // 4) + round((10/100) * Stats[HP]),
        "mana_cost": 12,
        "effect": None
    },
    "Soul Radiance": {
        "type": "Attack",
        "power": 20 + round((25/100) * Stats[MAG]),
        "mana_cost": 15,
        "effect": None
    },
    "Omniblow": {
        "type": "Attack",
        "power": 15 + round((25/100) * Stats[ATK]),
        "mana_cost": 12,
        "effect": None
    },
    "Poison": {
        "type": "Attack",
        "power": 10 + round((25/100) * Stats[MAG]),
        "mana_cost": 20,
        "effect": "Poison"
    },
    "Flame": {
        "type": "Attack",
        "power": 10 + round((25/100) * Stats[MAG]),
        "mana_cost": 20,
        "effect": "Burn"
    },
    "Frozen Magic Bullet": {
        "type": "Attack",
        "power": 10 + round((25/100) * Stats[MAG]),
        "mana_cost": 20,
        "effect": "Freeze"
    },
    "Heavy Soul Discharge": {
        "type": "Attack",
        "power": 50 + round((25/100) * Stats[MAG]),
        "mana_cost": 40,
        "effect": None
    },
    "Restore": {
        "type": "Heal",
        "power": (Stats[MAG] // 4) + round((30/100) * Stats[HP]),
        "mana_cost": 25,
        "effect": None
    }
}

SpellsListName = list(SPELLS.keys())
SpellsListName2 = list(SPELLS.keys())
SpellsListCost = [100, 100, 500, 500, 600, 600, 600, 1500, 1500]

SpellsExplain = { #Plus simple a utiliser un dic quand ya plein de long texte que plutot une liste comme pour les LV UP SOULS
    "Soul Arrow" :              "Shoot a soul arrow at the target enemy.\n               The power scales with the caster's Magic. Dealing 10+ damage\n",
    "Soul Light" :              "Soul healing restoring the HP of the caster.\n               The amount restored scales with the caster's Magic. Healing 10% or more\n",
    "Soul Radiance" :           "Pour soul arrows upon all enemies.\n               The power scales with the caster's Magic. Dealing 20+ damage\n",
    "Omniblow" :                "Deal unavoidable damage to the target enemy.\n               The power scales with the caster's Strengh. Dealing 15+ damage\n",
    "Poison" :                  "Infect all enemies with a deadly poison.\n               The power scales with the caster's Magic. Dealing 10+ damage and poisoning the ennemy\n",
    "Flame" :                   "Release flames and set the target enemy on fire \n               The power scales with the caster's Magic. Dealing 10+ and burning the ennemy\n",
    "Frozen Magic Bullet" :     "Unleash a fragment of winter’s wrath \n               The power scales with the caster's Magic. Dealing 10+ damage and freezing the ennemy\n",
    "Heavy Soul Discharge" :    "Shoot a heavy soul arrow at the target enemy.\n               The power scales with the caster's Magic. Dealing 50+ damage\n",
    "Restore" :                 "Call back the warmth of life from the silence of the grave.\n               The power scales with the caster's Magic. Healing 30% or more\n"
}

#_______________________LV UP SOULS_________________________

LV_UP_SOULS = {  #8, L'ordre correspond a l'ordre d'apparition dans le shop
    "Green Soul" : [30, 0, 0, 0, 0, 0, 0, -350],
    "Purple Soul" : [0, 10, 0, 0, 0, 0, 0, -350],
    "Red Soul" : [0, 0, 3, 0, 0, 0, 0, -350],
    "Blue Soul" : [0, 0, 0, 0, 3, 0, 0, -350],
    "Yellow Soul" : [0, 0, 0, 0, 0, 3, 0, -350],
    "Ashen Soul" : [0, 0, 0, 3, 0, 0, 0, -350],
    "Four Leafed CLover" : [0, 0, 0, 0, 0, 0, 3, -350],
    "Black Soul" : [10, 5, 1, 1, 1, 1, 1, -1000]
}

SoulsListName = list(LV_UP_SOULS.keys())
SoulsExplanation = ["Green Soul : +30 HP", "Purple Soul : +10 MP", "Red Soul : +3 ATK", "Blue Soul : +3 DEF", "Yellow Soul : +3 SPD", "Ashen Soul : +3 MAG", "Four Leafed CLover : +3 LCK", "Black Soul : +10 HP | +5 MP | +1 ALL"]

#__________________________BESTIARY__________________________

#MOBS_________________________________________________

MOBS = { #40, cela on peut les mettre dans le désordre, j'ai fait un algo de tri
    "Hollow" : [85, 0, 30, 6, 5, 10, 8, 5],
    "Executioner Pig" : [200, 0, 40, 6, 10, 25, 8, 10],
    "Mandragora" : [125, 0, 30, 10, 10, 30, 8, 30],
    "Dark Fairy" : [145, 200, 21, 250, 10, 25, 8, 45],
    "Slime" : [290, 20, 50, 10, 60, 30, 10, 80],
    "Gutter Rat" : [100, 200, 55, 10, 10, 55, 10, 50],
    "Cadaver" : [500, 40, 65, 10, 35, 15, 10, 200],
    "Werewolf" : [600, 0, 70, 10, 30, 70, 10, 280],
    "Centaur" : [250, 0, 42, 10, 15, 50, 8, 90],
    "Corpse eater Chicken" : [120, 200, 43, 10, 15, 10, 30, 40],
    "Alpaca" : [40, 0, 15, 10, 10, 200, 8, 40],
    "Man eating Ant" : [300, 0, 50, 10, 20, 40, 10, 150],
    "Toxic Butterfly" : [690, 300, 60, 10, 20, 47, 10, 230],
    "Ghoul" : [900, 0, 90, 10, 15, 30, 10, 400],
    "Bloodsucker" : [690, 300, 60, 160, 30, 55, 10, 300],
    "Skeleton" : [400, 300, 80, 10, 30, 50, 10, 250],
    "Iron Knight" : [900, 40, 70, 10, 55, 60, 10, 380],
    "Sorcerer" : [550, 80, 37, 70, 20, 44, 10, 300],
    "Sphinx" : [2400, 200, 78, 70, 88, 70, 10, 700],
    "Hippogriff" : [1200, 300, 80, 190, 30, 90, 10, 700],
    "Snow Angel" : [3500, 80, 125, 80, 100, 95, 10, 1050],
    "White Rabbit" : [800, 9000, 5, 800, 100, 200, 200, 10000],
    "Wraith" : [3600, 800, 75, 140, 120, 99, 10, 1700],
    "T Rex" : [8000, 800, 170, 50, 160, 180, 10, 3000],
    "El Monstro" : [6000, 800, 170, 130, 110, 100, 10, 3000],
    "Cerberus" : [4000, 800, 120, 70, 88, 95, 10, 1500],
    "One Who_Lurks" : [5000, 800, 100, 80, 100, 100, 10, 1480],
    "One Who Drains" : [5000, 800, 95, 150, 80, 95, 10, 1500],
    "Cyclops" : [13000, 800, 180, 40, 30, 60, 10, 6000],
    "Daedalus" : [7500, 800, 160, 50, 115, 75, 10, 3000],
    "Seraphim" : [9000, 800, 50, 240, 100, 105, 10, 3500],
    "Failure" : [1100, 100, 75, 70, 40, 60, 10, 390],
    "Orthrus" : [1300, 0, 85, 10, 44, 75, 10, 800],
    "Murder Doll" : [900, 70, 75, 10, 20, 60, 10, 600],
    "Gigas" : [25000, 800, 800, 40, 200, 200, 900, 40000],
    "Pixie" : [1900, 800, 80, 180, 70, 280, 300, 10000],
    "Imp" : [2800, 700, 180, 80, 100, 300, 300, 10000],
    "Kraken" : [30000, 5000, 300, 90, 250, 250, 100, 40000],
    "Unfathomable Knight" : [13000, 400, 290, 100, 270, 300, 10, 17000],
    "Black Saint" : [15500, 9000, 285, 320, 100, 350, 10, 18000]
}

#BOSS__________________________________________________

BOSS = { #14 ou #11 sans les phases, Dans l'ordre pour pas tout casser.
    "Hyena of Hunger" : [5300, 40, 85, 10, 25, 65, 10, 7500],
    "Naked King" : [10000, 2000, 110, 110, 10, 40, 10, 15000],
    "Cat in Armor" : [19000, 5000, 120, 10, 90, 70, 10, 22000],
    "Devourer Patrasche" : [17000, 9000, 135, 100, 85, 100, 100, 24000],
    "Monster Behemoth" : [20000, 8000, 150, 10, 110, 50, 90, 25500],
    "Singing Bone" : [19800, 2000, 110, 150, 140, 110, 150, 32000],
    "Iron Hans" : [75000, 7000, 550, 550, 560, 700, 900, 78000],
    "Bandersnatch" : [99999, 9999, 670, 600, 300, 500, 100, 1000000],
    "Drake Helkaiser" : [20000, 7000, 125, 10, 10, 10, 10, 12000], #Lui 1
    "Rotting Drake Helkaiser" : [36000, 9000, 180, 10, 10, 60, 90, 29000], #2
    "Undead Drake Helkaiser" : [60000, 9000, 290, 10, 1, 95, 10, 44000], #3 phase
    "Pumpkin Carriage" : [60000, 7000, 200, 200, 200, 280, 200, 78000],
    "Ash-clad Princess Cinderella" : [23000, 9999, 220, 270, 100, 150, 10, 60000], #Elle 1
    "Demon Queen Cinderella" : [80000, 9999, 320, 300, 240, 200, 200, 100000] #2 phase
}

#____________________LEAF RANDOM FACT_______________________

LeafRandomFact = [
    "Blocking always cuts the meanie’s attack in half... even if you're tiny like me~",
    "Dodging only works 70% of the time, so why not be a brave little wall, hm~?",
    "Victoria made the dev cry real tears. She was *that* much of a headache, ufufu~",
    "They *said* there’d be a secret boss at the end... but now it's just empty whispers~",
    "Did you know fairies never truly die? We just nap very, very deeply... like corpses~",
    "My favorite writer? Grimm, of course! His tales are so *cozy*. Maybe you're in one of them~?",
    "I ran out of ideas... so here's some nonsense to fill the void: nya nya blah blah~"
]

#_______________________DROP TIER SORT_______________________

Tier_One = []
Tier_Two = []
Tier_Three = []
Legendary = []

ItemTier = [Tier_One, Tier_Two, Tier_Three, Legendary]

#Weapon_________________________________________
x = 0
for i in range(len(ItemTier)) :
    nb = 3 if i<3 else 1 
    for y in range(nb) :
        ItemTier[i].append(WeaponsListName[x])
        x+=1    

#Ring_________________________________________
x = 0
for i in range(len(ItemTier)) :
    if i == 0 :
        nb = 7
    elif i == 1 :
        nb = 2
    else :
        nb = 0
    for y in range(nb) :
        ItemTier[i].append(RingsListName[x])
        x+=1

#______________________DROP TIER______________________

def ItemLoot (Floor) :
    x = randint(0,100)
    if x <= 30 :
        if 0 <= Floor <= 2:
            lootTier = random.choices([ItemTier[0], ItemTier[1]], weights=[80, 20])[0]

        elif 3 <= Floor <= 5:
            lootTier = random.choices([ItemTier[0], ItemTier[1], ItemTier[2]], weights=[40, 50, 10])[0]

        elif 6 <= Floor <= 8:
            lootTier = random.choices([ItemTier[1], ItemTier[2], ItemTier[3]], weights=[30, 60, 10])[0]

        elif 9 <= Floor :
            lootTier = random.choices([ItemTier[2], ItemTier[3]], weights=[70, 30])[0]
            
        if len(lootTier) > 0:
            item = random.choice(lootTier)
            return item
        else:
            return None

    else :
        return None

#______________________DROP ITEM______________________

def Loot (Floor) :
    Stats[SOULS] += Monster_Stats[SOULS]
    print(f"You gain {Monster_Stats[SOULS]} Souls !")
    Item = ItemLoot(Floor)
    if Item in RingsListName :
        RingsInventory.append(Item)
    elif Item in WeaponsListName :
        WeaponsInventory.append(Item)
    if Item != None :
        print(f"You gain {Item} ! Check Victoria to equip yourself with")
    wait()
    return

#____________________MONSTER SYSTEME________________________

#Floor______________________________

Floor_0 = []
Floor_1 = []
Floor_2 = []
Floor_3 = []
Floor_4 = []
Floor_5 = []
Floor_6 = []
Floor_7 = []
Floor_8 = []
Floor_9 = []
Floor_10 = []

Dungeon = [Floor_0, Floor_1, Floor_2, Floor_3, Floor_4, Floor_5, Floor_6, Floor_7, Floor_8, Floor_9, Floor_10]
Boss_Room = [Floor_0, Floor_1, Floor_2, Floor_3, Floor_4, Floor_5, Floor_6, Floor_7, Floor_8, Floor_9, Floor_10]

#______________________Sort______________________

#Mobs______________________________
Monster_Name_List = list(MOBS.keys())
Monster_Value  = sorted(MOBS.keys(), key=lambda name: MOBS[name][7])
x=0 #Pour attraper les mobs

for i in range(len(Dungeon)) :
    nb = 3 if i<4 else 4 
    for y in range(nb) :
        Dungeon[i].append(Monster_Value[x])
        x+=1

#Boss_____________________________
Boss_Name_List = list(BOSS.keys())
x=0 #Pour attraper les boss

for i in range(len(Boss_Room)) :
    nb = 1
    if i == 8 :
        nb = 3
    if i == 10 :
        nb = 2
    for y in range(nb) :
        Boss_Room[i].append(Boss_Name_List[x])
        x+=1

#___________________Mobs Random Choose___________________

def MonsterToFight (Floor) :
    x = randint(0, len(Dungeon[Floor])-2)                          
    Monster_Name = Dungeon[Floor][x]
    Monster_Stats = MOBS[Monster_Name].copy()
    return Monster_Name, Monster_Stats

#___________________Number of Mobs to Fight___________________
def NumberOfMonsterToFight () :
    NbMonster = 5
    More = True
    x = 1
    while More == True :
        chance = randint(0, 100)
        if chance <= 50//x :
            NbMonster += 1
            x +=1
        else :
            More = False
    return NbMonster

#___________________Monster Attack___________________
def MonsterAttack ():
    global Dodge, Guard
    x = randint(0, 100)
    if x <= CritChanceMonster :
        print(f"{Monster_Name} Attack !")
        print ("Critical Strike !")
        if Dodge == False and Guard == False :
            Stats[HP] -= round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100)))
            print("He deal : ",round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100))),"Damage !")
        elif Dodge == True :
            x = randint(0, 100)
            if x <= 70 :
                print("He deal : ",round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100))),"Damage !")
                print("But you dodge !")
            else :
                Stats[HP] -= round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100)))
                print("He deal : ",round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100))),"Damage !")
        elif Guard == True :
            Stats[HP] -= round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100))) // 2
            print("He deal : ",round(max(1, (Monster_Stats[ATK]-Stats[DEF])) + (max(1, (Monster_Stats[ATK]-Stats[DEF])) * (CritDamageMonster/100))) // 2,"Damage !")
    else : 
        print(f"{Monster_Name} Attack !")
        if Dodge == False and Guard == False :
            print("He deal : ",max(1, (Monster_Stats[ATK]-Stats[DEF])),"Damage !")
            Stats[HP] -= max(1, (Monster_Stats[ATK]-Stats[DEF]))
        elif Dodge == True :
            x = randint(0, 100)
            if x <= 70 :
                print("He deal : ",max(1, (Monster_Stats[ATK]-Stats[DEF])),"Damage !")
                print("But you dodge !")
            else :
                print("He deal : ",max(1, (Monster_Stats[ATK]-Stats[DEF])),"Damage !")
                Stats[HP] -= max(1, (Monster_Stats[ATK]-Stats[DEF]))
        elif Guard == True :
            print("He deal : ",max(1, (Monster_Stats[ATK]-Stats[DEF])) // 2,"Damage !")
            Stats[HP] -= max(1, (Monster_Stats[ATK]-Stats[DEF])) // 2
    wait()


#____________________Vitesse Systeme____________________

#Display of progression_________________________________
def SpeedSysteme (fill, size=30):
    progress = int(fill / 100 * size)
    return "[" + "█" * progress + " " * (size - progress) + "]"

#____________________HP and Mana Systeme____________________

#Display of progression Grimm_________________________________
def HPMPSystemeGrimm () :
    HP_ratio = Stats[HP] / Max_Stats[HP]
    HP_filled = int(20 * HP_ratio) #HP_bar_length * HP_ratio
    HP_bar = '█' * HP_filled + '-' * (20 - HP_filled)
    
    MP_ratio = Stats[MP] / Max_Stats[MP]
    MP_filled = int(10 * MP_ratio) #mp_bar_length * mp_ratio
    MP_bar = '▓' * MP_filled + '-' * (10 - MP_filled)
    
    # Affichage : nom | barre vie | PV | barre mana | MP
    print(f"{Name:10} |HP|{HP_bar}| {Stats[HP]}/{Max_Stats[HP]} |MP|{MP_bar}| {Stats[MP]}/{Max_Stats[MP]}")

#Display of progression Monster_________________________________
def HPMPSystemeMonster (HP_max, MP_max) :

    HP_ratio = Monster_Stats[HP] / HP_max
    HP_filled = int(20 * HP_ratio) #HP_bar_length * HP_ratio
    HP_bar = '█' * HP_filled + '-' * (20 - HP_filled)
    
    MP_ratio = Monster_Stats[MP] / max(1,MP_max)
    MP_filled = int(10 * MP_ratio) #mp_bar_length * mp_ratio
    MP_bar = '▓' * MP_filled + '-' * (10 - MP_filled)
    
    # Affichage : nom | barre vie | PV | barre mana | MP
    print(f"{Monster_Name:10} |HP|{HP_bar}| {Monster_Stats[HP]}/{HP_max} |MP|{MP_bar}| {Monster_Stats[MP]}/{MP_max}")
    
#_____________________Combat Systeme_____________________

#Display of fight interface ____________________________
Flee = False
def FightSysteme (speed_grimm, speed_monster, size=30):
    global MonsterKill, Dead, Flee
    max_speed = max(speed_grimm, speed_monster)
    filling_speed_grimm = max_speed / speed_grimm
    filling_speed_monster = max_speed / speed_monster
    grimm_systeme = 0
    monster_systeme = 0

    while Stats[HP]>0 and Monster_Stats[HP]>0 :
        
        grimm_systeme += 0.05 * (100 / filling_speed_grimm)
        monster_systeme += 0.05 * (100 / filling_speed_monster)
        
        clear_screen()
        
        print(f"_______Floor {Floor}_______")
        print("                   ",MonsterKill,"/",NbMonsterToKill,"\n\n")
        
        HPMPSystemeGrimm()
        print(f"      |AP|{SpeedSysteme(grimm_systeme, size)}\n\n")
        
        HPMPSystemeMonster(HP_max_Monster, MP_max_Monster)
        print(f"      |AP|{SpeedSysteme(monster_systeme, size)}\n\n")
        
        # Vérification des AP
        if grimm_systeme >= 100 and monster_systeme >= 100: # Les deux barres pleines en même temps

            if speed_grimm >= speed_monster:
                print("Grimm turn")
                ActionSysteme()
                if Flee == True:
                    Flee = False
                    return
                grimm_systeme -= 100
                time.sleep(0.5)
                
                if monster_systeme >= 100:
                    print("Monster turn")
                    MonsterAttack()
                    monster_systeme -= 100
                    wait()
            else:
                print("Monster turn")
                MonsterAttack()
                monster_systeme -= 100
                time.sleep(0.5)
                if grimm_systeme >= 100:
                    print("Grimm turn")
                    ActionSysteme()
                    if Flee == True:
                        Flee = False
                        return
                    grimm_systeme -= 100
                    wait()

        else:
            if grimm_systeme >= 100:
                print("Grimm turn")
                ActionSysteme()
                if Flee == True:
                    Flee = False
                    return
                grimm_systeme -= 100
                time.sleep(0.5)
            if monster_systeme >= 100:
                print("Monster turn")
                MonsterAttack()
                monster_systeme -= 100
                time.sleep(0.5)
        
        time.sleep(0.016)

    if Stats[HP] <= 0 :
        print("You have been slain...")
        Dead = True
    elif Monster_Stats[HP] <=0 :
        print(f"{Monster_Name} have been slain !")
        MonsterKill +=1
        Loot(Floor)
    time.sleep(1)

#_____________Action Systeme________________
Dodge = False
Guard = False
def ActionSysteme () :
    global Flee, HP_max_Monster, MP_max_Monster, Dodge, Guard
    Action = False
    while Action == False :
        print("________Your turn________")
        print("-Attack           -Spells\n-Dodge            -Guard\n-Check            -Flee\n")
        choice = input("Choose your action : ")
        Dodge = False
        Guard = False

        #On calcule a l'avance si ce tour l'attaque du joueur est Critique
        CriticalHit = False
        x = randint(0, 100)
        if x <= CritChance :
            CriticalHit = True
            
        if choice == "Attack" :
            Damage = Stats[ATK]
            print("You Attack !", Monster_Name)
            if CriticalHit == False :
                Monster_Stats[HP] -= max(1, (Damage - Monster_Stats[DEF]))
                print("You did :",max(1, (Damage - Monster_Stats[DEF])),"Damage !")
            else :
                Monster_Stats[HP] -= round(max(1, (Damage - Monster_Stats[DEF]))+ (max(1, (Damage - Monster_Stats[DEF]))*(CritDamage/100)))
                print("CriticalHit !!!")
                print("You did :",round(max(1, (Damage - Monster_Stats[DEF]))+ (max(1, (Damage - Monster_Stats[DEF]))*(CritDamage/100))),"Damage !")
            Action = True
            wait()
            
        elif choice == "Spells" : #Les effet n'on pas encore été ajouter
            if len(Spells) == 0 :
                print("you don't have any spells")
            else :
                for i in range(len(Spells)) :
                    print(f"{i+1}-", Spells[i],"--- Mana Cost :", SPELLS[Spells[i]]["mana_cost"])
                while True :
                    try :
                        spellschoice = int(input("Wich one do I use ? : "))
                        break
                    except ValueError :
                        print("Please enter the Number, not the Action")
                if spellschoice > len(Spells) or spellschoice < 1 :
                    print("I don't have this Spells...")
                    wait()
                elif Stats[MP] < SPELLS[Spells[spellschoice-1]]["mana_cost"] :
                    print("I don't have enought MP...")
                    wait()
                else :
                    TypeSpells = SPELLS[Spells[spellschoice-1]]["type"]
                    if TypeSpells == "Attack" :
                        print("Spells Use !")
                        if CriticalHit == False :
                            Monster_Stats[HP] -= SPELLS[Spells[spellschoice-1]]["power"]
                            Stats[MP] -= SPELLS[Spells[spellschoice-1]]["mana_cost"]
                            print("You did :",SPELLS[Spells[spellschoice-1]]["power"], "Damage !")
                        else :
                            Monster_Stats[HP] -= round(SPELLS[Spells[spellschoice-1]]["power"] + (SPELLS[Spells[spellschoice-1]]["power"]*(CritDamage/100)))
                            Stats[MP] -= SPELLS[Spells[spellschoice-1]]["mana_cost"]
                            print("CriticalHit !!!")
                            print("You did :",round(SPELLS[Spells[spellschoice-1]]["power"] + (SPELLS[Spells[spellschoice-1]]["power"]*(CritDamage/100))), "Damage !")
                        Action = True
                        wait()
                    elif TypeSpells == "Heal" :
                        print("Spells Use !")
                        if CriticalHit == False :
                            BeforeHeal = Stats[HP]
                            Stats[HP] +=  SPELLS[Spells[spellschoice-1]]["power"]
                            Stats[MP] -= SPELLS[Spells[spellschoice-1]]["mana_cost"]
                        else :
                            print("CriticalHeal !!!")
                            BeforeHeal = Stats[HP]
                            Stats[HP] +=  SPELLS[Spells[spellschoice-1]]["power"] + (SPELLS[Spells[spellschoice-1]]["power"]*(CritDamage/100))
                            Stats[MP] -= SPELLS[Spells[spellschoice-1]]["mana_cost"]
                        if Stats[HP] > Max_Stats[HP] :
                            Stats[HP] = Max_Stats[HP]
                        print("You heal :",Stats[HP]-BeforeHeal,"HP !")
                        Action = True
                        wait()
                        
        elif choice == "Check" :
            print (Monster_Name, " : ")
            print("HP :",HP_max_Monster)
            print("MP :",MP_max_Monster)
            print("ATK :",Monster_Stats[ATK])
            print("MAG :",Monster_Stats[MAG])
            print("DEF :",Monster_Stats[DEF])
            print("SPD :",Monster_Stats[SPD])
            print("LCK :",Monster_Stats[LCK])
            Action = True
            wait()

        elif choice == "Flee" :
            escape = randint(0, 100)
            if escape <= 25 :
                print(f"{Name} starts running away !")
                Flee = True
                Action = True
                wait()
            else :
                print(f"{Name} starts running away ! \nBut the escape path was blocked!")
                Action = True
                wait()

        elif choice == "Dodge" :
            Dodge = True
            Action = True

        elif choice == "Guard" :
            Guard = True
            Action = True
        else :
            print("I can't do that...")
            wait()

#_______________BonFire (Shop) Systeme_______________

def BoneFire ():
    global CritChance, CritDamage, Stats, Max_Stats
    Continue = False
    Stats[:len(Max_Stats)] = Max_Stats #Heal and cancle Debuff
    while Continue == False :
        wait()
        clear_screen()
        print("___________________BonFire ♨___________________")
        print("-Upgrade           -Equipement\n-Facts             -Status\n-Spells Shop \n                                   Continue -->\n")  
        choice = input("What do you want to do ? : ")


#_________________________________
        if choice == "Upgrade" :
            print("Soul Lady Elisabeth :")
            print("Ah... Sir undead. Do you have business with me ?")
            print("1- I want to buy souls \n2- What do they do ? \n3- Nevermind")
            while True :
                try :
                    choiceElisabeth = int(input("___ : "))
                    break
                except ValueError:
                    print("Oh dear... Words have no value here. Only numbers carry weight.")
            if choiceElisabeth == 1 :
                print("Fufufu. Here, please look at them.To you, I'll show them any number of time.")
                for i in range(len(SoulsListName)):
                    print(f"{i+1}-", SoulsListName[i],"--- Souls Cost :",abs(LV_UP_SOULS[SoulsListName[i]][SOULS]))
                print("                     Souls :",Stats[SOULS])
                while True :
                    try :
                        buychoice= int(input("\nWich one caught your eyes ? : "))
                        break
                    except ValueError :
                        print("Oh dear... Words have no value here. Only numbers carry weight.")
                if buychoice < 1 or buychoice > len(SoulsListName):
                    print("I'm sorry but look like I can't provide you that...")
                else :
                    while True :
                        try :
                            NumberOfSouls = int(input("How many souls will you claim? : "))
                            break
                        except ValueError :
                            print("Oh dear... Words have no value here. Only numbers carry weight.")
                    if Stats[SOULS] >= abs(LV_UP_SOULS[SoulsListName[buychoice-1]][SOULS])*NumberOfSouls :
                        for y in range(NumberOfSouls) :
                            for i in range(len(Max_Stats)) :
                                Max_Stats[i] += LV_UP_SOULS[SoulsListName[buychoice-1]][i]
                            Stats[SOULS] += LV_UP_SOULS[SoulsListName[buychoice-1]][SOULS]
                        print("May the power of Souls dwell withing you")
                    else :
                        print("Look like you don't have enough, dear~")
                        
            elif choiceElisabeth == 2 :
                print("Here some explication my dear~ : ")
                for i in range(len(SoulsExplanation)):
                    print(SoulsExplanation[i])
                    
            elif choiceElisabeth == 3 :
                print("Fufufu~ Then come back to me once you've cleared your mind.")
            else :
                print("Where do you even get that idea ?")
#_________________________________       
        elif choice == "Equipement" :
            print("Maid Victoria :")
            print("Welcome back, Master\nCan I do something for you ?")
            print("1- Help me change my Weapon \n2- Help me change my Rings \n3- Whats my Equipement ? \n4- No everything fine")
            while True :
                try :
                    choiceVictoria = int(input("___ : "))
                    break
                except ValueError:
                    print("Forgive me, Master, but… I believe you should enter a number… if that’s alright.")
                
            if choiceVictoria == 1 : # Help me change my Weapon
                if len(WeaponsInventory) == 0 :
                    print("Sorry Master, but you have no weapons to equip yourself with...")
                else :
                    print("Of course Master let me Help you\n")
                    for i in range(len(WeaponsInventory)) :
                        print(f"{i+1}-", WeaponsInventory[i])
                    while True :
                        try :
                            equipchoice = int(input("I want... :"))
                            break
                        except ValueError :
                            print("Forgive me, Master, but… I believe you should enter a number… if that’s alright.")
                    if 1 <= equipchoice <= len(WeaponsInventory) :
                        new_weapon = WeaponsInventory.pop(equipchoice-1)
                        if Gear[0] != 0 :
                            WeaponsInventory.append(Gear[0])
                            for i in range(len(Max_Stats)):
                                Max_Stats[i] -= WEAPON[Gear[0]][i]
                        Gear[0] = new_weapon
                        for i in range(len(Max_Stats)):
                            Max_Stats[i] += WEAPON[Gear[0]][i]  
                        print(f"You equipped {new_weapon} !")
                    else :
                        print("Sorry Master but that not possible...")  
                        
            elif choiceVictoria == 2 : #Help me change my Rings
                if len(RingsInventory) == 0 :
                    print("Sorry Master, but you have no rings to equip yourself with...")
                else :
                    print("Of course Master let me Help you\n")
                    for i in range(len(RingsInventory)) :
                        print(f"{i+1}-", RingsInventory[i])
                    while True :
                        try :
                            equipchoice = int(input("I want... :"))
                            break
                        except ValueError :
                            print("Forgive me, Master, but… I believe you should enter a number… if that’s alright.")
                    if 1 <= equipchoice <= len(RingsInventory) :
                        new_ring = RingsInventory.pop(equipchoice-1)
                        while True :
                            try :
                                slotchoice = int(input("In wich slot do you want your ring Master ?"))
                                break
                            except ValueError :
                                print("Forgive me, Master, but… I believe you should enter a number… if that’s alright.")
                        if slotchoice in [1, 2] :
                            if Gear[slotchoice] != 0 :
                                RingsInventory.append(Gear[slotchoice])
                                if Gear[slotchoice] == "Hornet Ring" :
                                    CritDamage -= 50
                                elif Gear[slotchoice] == "Snipers Ring" :
                                    CritChance -= 20
                                else :
                                    for i in range(len(Max_Stats)) :
                                        Max_Stats[i] -= RINGS[Gear[slotchoice]][i]
                                if new_ring == "Hornet Ring" :
                                    CritDamage += 50
                                elif new_ring == "Snipers Ring" :
                                    CritChance += 20
                                else :
                                    for i in range(len(Max_Stats)) :
                                        Max_Stats[i] += RINGS[new_ring][i]
                                print(f"You equipped {new_ring} !")
                                Gear[slotchoice] = new_ring
                            else :
                                if new_ring == "Hornet Ring" :
                                    CritDamage += 50
                                elif new_ring == "Snipers Ring" :
                                    CritChance += 20
                                else :
                                    for i in range(len(Max_Stats)) :
                                        Max_Stats[i] += RINGS[new_ring][i]
                                print(f"You equipped {new_ring} !")
                                Gear[slotchoice] = new_ring

                        else :
                            print("Sorry Master but that not a valid number...")
                            RingsInventory.append(new_ring)
                    else :
                        print("Sorry Master but that not a valid number...")

            elif choiceVictoria ==3 : #Whats my Equipement ?
                print("Here it is Master ! :\n")
                print("--- Your Equipment ---")
                print(f"- Weapon : {Gear[0] if Gear[0] != 0 else 'None'}")
                print(f"- Ring 1 : {Gear[1] if Gear[1] != 0 else 'None'}")
                print(f"- Ring 2 : {Gear[2] if Gear[2] != 0 else 'None'}")
                print("----------------------\n")
                
            elif choiceVictoria ==4 : #No everything fine
                print("Then be safe on your journey Master\n")
            else :
                print("Master do you really feel allright ? Maybe will it be better if you rest ?")
                
#_________________________________                
        elif choice == "Facts" :
            print("Fairy Leaf :")
            print("Hey Grimm, wanna hear some random facts? ♪")
            print("1- Yes \n2- No")
            while True :
                try :
                    choiceLeaf = int(input("___ : "))
                    break
                except ValueError:
                    print("Umm… I think you're supposed to type a number, not words…")
                    print("Unless… is this some kind of secret code?")

            if choiceLeaf == 1 : #Yes
                x = randint(0, len(LeafRandomFact)-1)
                print("Perfect ♡!")
                print(LeafRandomFact[x])

            elif choiceLeaf == 2 : #No
                print("Well to bad for you ~♡")
            else :
                print("Come on, you can’t even hit 1 or 2 properly? Geez, what are we gonna do with you? ♪")
                
#_________________________________                
        elif choice == "Status" :
            print("Saint Catherine :")
            print("Welcome back, sir Grimm.\nPlease don't overwork yourself, alright?\nIts fine to rest a little")
            print("Shall I examine your stats, if it pleases you?")
            print("1- Yes please \n2- No no need")
            while True :
                try :
                    choiceCatherine = int(input("___ : "))
                    break
                except ValueError:
                    print("Oh… Only numbers, please, Sir Grimm.")
                    print("The Lord teaches patience, and so shall I wait as long as needed.")
            if choiceCatherine == 1 :
                print("Very well here you go... :\n")
                print (Name, " : ")
                print("HP :",Max_Stats[HP])
                print("MP :",Max_Stats[MP])
                print("ATK :",Max_Stats[ATK])
                print("MAG :",Max_Stats[MAG])
                print("DEF :",Max_Stats[DEF])
                print("SPD :",Max_Stats[SPD])
                print("LCK :",Max_Stats[LCK])
                print("Souls :",Stats[SOULS])
            elif choiceCatherine == 2 :
                print("Radiance of God's beauty surpasses the sun\nand the intellect governs all creation.")
                print("I pray for your return sir Grimm, may you come back safely")
            else :
                print("My, my... You must be utterly exhausted. Please, take all the time you need to rest.")

#_________________________________
        elif choice == "Spells Shop" :  
            print("Witch Dorothy :")
            print("Oh? its you apprentice. What's the matter?")
            print("1- I want to buy spells \n2- Teach me more about magic \n3- Just passing by")
            while True :
                try :
                    choiceDorothy = int(input("___ : "))
                    break
                except ValueError :
                    print("Tch. Use numbers, not your imagination.")

            if choiceDorothy == 1 : #Buy
                if len(SpellsListName)!=0 :
                    print("Stare all you want")
                    for i in range(len(SpellsListName)):
                        print(f"{i+1}-", SpellsListName[i],"--- Souls Cost :", SpellsListCost[i])
                    print("                     Souls :",Stats[SOULS],"\n")
                    while True :
                        try :
                            buychoice = int(input("So, which incantation catches your eye, hmm? : "))
                            break
                        except ValueError :
                            print("Tch. Use numbers, not your imagination.")
                    if buychoice < 1 or buychoice > len(SpellsListName) :
                        print("I could pretend to sell you something that doesn’t exist… but even I have standards.")
                    elif SpellsListCost[buychoice-1] > Stats[SOULS] :
                        print("Foolish apprentice you don't have enough Souls.\nQuickly gather them then.")
                    else :
                        Spells.append(SpellsListName[buychoice-1])
                        Stats[SOULS] -= SpellsListCost[buychoice - 1]
                        SpellsListName.pop(buychoice-1)
                        SpellsListCost.pop(buychoice-1)
                        print("All yours now. Don’t say I never gave you anything")
                else :
                    print("Looks like my spells have all found a new home. Hope you use them well.")

            elif choiceDorothy == 2 : #What the spell do
                print("Trying to make sense of it all? How cute")
                print("Fine, I’ll spill the secrets. Don’t blame me if it’s confusing.\n")
                for i in range(len(SpellsListName2)) :
                    print(SpellsListName2[i], " : ", SpellsExplain[SpellsListName2[i]])

            elif choiceDorothy == 3 : #Nevermind just passing by
                print("Wandering without purpose again? You’ll end up hexed by your own confusion.")

            else :
                print("What nonsense are you babbling now?")
                print("Honestly... Did you hit your head again, apprentice?")
#_________________________________
        elif choice == "Continue" :
            Continue = True
        else :
            print("Nuh Uh you can't do that ~♪")
    Stats[:len(Max_Stats)] = Max_Stats #Heal and cancle Debuff mais cette fois a la sortie du bonfire

#____________________________________Start of the Game____________________________________

clear_screen()
print("\n\n\n\n\n\n")
time.sleep(0.5)

#Loading____________________________________________________________________
for i in range(0, 101, 5):
    time.sleep(0.1)
    print(f"\rLoading game... {SpeedSysteme(i)} {i}%", end='', flush=True)

#Intro______________________________________________________________________
time.sleep(0.5)
clear_screen()

INTRO = (
    "_________ A Black Souls-Inspired Game _________\n\n"
    "You are an Undead. That means you can't truly die — you fall, and rise again.\n"
    "Again and again, you face death, and again and again, you return.\n"
    "In this world, a mysterious white fog has appeared, and people have started turning into Demonbeasts...\n\n"
    "The source of this madness? The Demon Queen, Cinderella.\n"
    "After a long journey filled with despair, you finally stand before the gates of the Lost Empire.\n"
    "You're close — so very close — to confronting her and ending this nightmare once and for all...\n\n"
    "But patience is required.\n"
    "Ten floors lie ahead, each filled with countless struggles and horrors.\n"
    "So now, you — Grimm — must rise.\n"
    "Face the Demonic Princess Cinderella. You may die on the way. Again and again.\n"
    "But remember this: even in death, do not give up...\n\n"
    "With that said... I wish you good luck in the battle that awaits you.\n"
)

for char in INTRO:
    print(char, end='', flush=True)
    time.sleep(0.005)
print("\n")

#___________
wait()
#____________

#Tutorial__________________________________________________________________
clear_screen()

print("_______ Tutorial _______")
Tutorial = (
    "Your goal is to reach the 10th floor of the Dungeon and defeat the Demon Queen, Cinderella.\n"
    "To do that, you'll have to clear 11 floors in total, starting from Floor 0 up to Floor 10.\n"
    "Each floor contains a powerful Boss, but before facing it, you'll need to defeat at least 5 Demonbeasts.\n"
    "Once a floor is cleared, you cannot return to it—unless you've been slain.\n\n"
    
    "But fear not. Between each battle, you'll find a Bonfire. There, different companions will be waiting to assist you:\n"
    "- Elisabeth, who sells precious souls to help you grow stronger,\n"
    "- Victoria, who manages your equipment,\n"
    "- Catherine, who will show you your current stats,\n"
    "- Dorothy, who will sell a wide variety of powerful spells.\n"
    "- And Leaf... who’s just there to chat with you.\n\n"

    "During your fights, you'll earn Souls which can be used to buy items.\n"
    "You may also find new Weapons, Rings, or powerful Spells to aid you.\n\n"

    "Combat is turn-based and driven by a speed bar: when your bar is full, it’s your turn.\n"
    "When an enemy’s bar is full, they will act.\n\n"

    "On your turn, you can:\n"
    "- Attack the enemy,\n"
    "- Use a Spell,\n"
    "- Check the enemy’s stats,\n"
    "- Dodge the next attack,\n"
    "- Defend yourself from the newt attack,\n"
    "- Or flee, to fight another day.\n\n"

    "If you happen to die, you’ll lose your Spells, Equipment, and Souls...\n"
    "But your stat boosts will remain, making you stronger each time.\n"
    "So die as many times as needed to overcome the challenge.\n\n"

    "And with that’s I wish you good luck, and die well~ ♪\n")

for char in Tutorial:
    print(char, end='', flush=True)
    time.sleep(0.005)

#_________________
wait()
#_________________

#Start____________________________________________________________________

clear_screen()

print("_________Welcome to the Lost Empire_________")

choice = input("Enter the lost Empire ? (Yes/No) : ")

if choice != "Yes" :
    print("Do you really think you have a choice here ?")
    print("Anyway...")
    
print("You open the gate and enter the First Floor of the Lost Empire...\n")

#_________________
wait()
#_________________

clear_screen()

END = False
Floor = 0
MonsterKill = 0
NbMonsterToKill = NumberOfMonsterToFight()
OldFloor = 0
Dead = False
BossFight = False

while END != True :
    if OldFloor != Floor :
        NbMonsterToKill = NumberOfMonsterToFight()
        MonsterKill = 0
        OldFloor = Floor
    print(f"_________Floor {Floor}_________")

    if MonsterKill >= NbMonsterToKill :
        MonsterKill = NbMonsterToKill

    print("                   ",MonsterKill,"/",NbMonsterToKill,"\n")

#Faut que je m'occupe des Boss qui on plusieur phase, c'est pas top top :/
#Et la fin et pas fini... Je veux rajouter le boss Secret

    if MonsterKill >= NbMonsterToKill :
        FightBoss = input("Do you want to enter the boss Room ? (Yes/No) : ")
        if FightBoss == "Yes" :
            BossFight = True
            Monster_Name = Dungeon[Floor][len(Dungeon[Floor])-1]
            Monster_Stats = BOSS[Monster_Name].copy()
            HP_max_Monster = Monster_Stats[HP]
            MP_max_Monster = Monster_Stats[MP]
            CritChanceMonster = 5 + (Monster_Stats[LCK]//2)
            CritDamageMonster = 100

    if BossFight == False :
        Monster_Name, Monster_Stats = MonsterToFight(Floor)
        HP_max_Monster = Monster_Stats[HP]
        MP_max_Monster = Monster_Stats[MP]
        CritChanceMonster = 5 + (Monster_Stats[LCK]//2)
        CritDamageMonster = 100

    for i in range(5) :
        for dots in [".", "..", "..."]:
            print(f"\rYou walk along the dark corridor{dots}   ", end='', flush=True)
            time.sleep(0.3)

    print("Ennemy found !")
    FightSysteme(Stats[SPD], Monster_Stats[SPD])
    clear_screen()
    if Dead == True :
        Floor = 0
        MonsterKill = 0
        Stats[SOULS] = 0
        Spells = []
        RingsInventory = []
        WeaponsInventory = []
        Dead = False
        BossFight = False
    elif BossFight == True :
        BossFight = False
        Floor +=1

    BoneFire()
    clear_screen()