# -*- coding: utf-8 -*-
"""
bonfire.py
==============
Le Feu de Camp : le hub entre chaque combat où le joueur soigne son
personnage et peut parler à 5 PNJ différents. Chaque PNJ a sa propre
fonction (talk_to_xxx) pour que BoneFire() reste un simple aiguillage
lisible plutôt qu'un unique bloc de 400 lignes.

PNJ et ce qu'ils font :
    - Elisabeth : vend des Souls de montée de niveau (talk_to_elisabeth)
    - Victoria  : gère armes/anneaux équipés (talk_to_victoria)
    - Leaf      : raconte une anecdote au hasard (talk_to_leaf)
    - Catherine : affiche les stats actuelles du joueur (talk_to_catherine)
    - Dorothy   : vend des sorts (talk_to_dorothy)
"""

from random import randint

import game_state as gs
import ui
from data_souls import LV_UP_SOULS, SoulsListName, SoulsExplanation
from data_equipment import WEAPON, RINGS, EquipementExplain
from data_spells import SPELLS, SpellsListName, SpellsListName2, SpellsListCost, SpellsExplain
from dialogue import LeafRandomFact


def talk_to_elisabeth():
    """Boutique des Souls de montée de niveau (augmentent Max_Stats)."""
    print("Soul Lady Elisabeth :")
    print("Ah... Sir undead. Do you have business with me ?")
    print("1- I want to buy souls \n2- What do they do ? \n3- Nevermind")
    choice = ui.ask_int("___ : ", "Oh dear... Words have no value here. Only numbers carry weight.")

    if choice == 1:
        print("Fufufu. Here, please look at them.To you, I'll show them any number of time.")
        for i in range(len(SoulsListName)):
            print(f"{i + 1}-", SoulsListName[i], "--- Souls Cost :", abs(LV_UP_SOULS[SoulsListName[i]][gs.SOULS]))
        print("                     Souls :", gs.Stats[gs.SOULS])

        buychoice = ui.ask_int("\nWich one caught your eyes ? : ", "Oh dear... Words have no value here. Only numbers carry weight.")
        if buychoice < 1 or buychoice > len(SoulsListName):
            print("I'm sorry but look like I can't provide you that...")
            return

        NumberOfSouls = ui.ask_int("How many souls will you claim? : ", "Oh dear... Words have no value here. Only numbers carry weight.")
        soul_name = SoulsListName[buychoice - 1]
        total_cost = abs(LV_UP_SOULS[soul_name][gs.SOULS]) * NumberOfSouls

        if gs.Stats[gs.SOULS] >= total_cost:
            for _ in range(NumberOfSouls):
                for i in range(len(gs.Max_Stats)):
                    gs.Max_Stats[i] += LV_UP_SOULS[soul_name][i]
                gs.Stats[gs.SOULS] += LV_UP_SOULS[soul_name][gs.SOULS]
            print("May the power of Souls dwell withing you")
        else:
            print("Look like you don't have enough, dear~")

    elif choice == 2:
        print("Here some explication my dear~ : ")
        for explanation in SoulsExplanation:
            print(explanation)

    elif choice == 3:
        print("Fufufu~ Then come back to me once you've cleared your mind.")

    else:
        print("Where do you even get that idea ?")


def talk_to_victoria():
    """Gestion de l'équipement : changer d'arme, changer d'anneau, voir l'équipement actuel."""
    print("Maid Victoria :")
    print("Welcome back, Master\nCan I do something for you ?")
    print("1- Help me change my Weapon \n2- Help me change my Rings \n3- Whats my Equipement ? \n4- Witch effects do they have? \n5- No everything fine")
    error = "Forgive me, Master, but… I believe you should enter a number… if that’s alright."
    choice = ui.ask_int("___ : ", error)

    if choice == 1:
        _change_weapon(error)
    elif choice == 2:
        _change_ring(error)
    elif choice == 3:
        print("Here it is Master ! :\n")
        print("--- Your Equipment ---")
        print(f"- Weapon : {gs.Gear[0] if gs.Gear[0] != 0 else 'None'}")
        print(f"- Ring 1 : {gs.Gear[1] if gs.Gear[1] != 0 else 'None'}")
        print(f"- Ring 2 : {gs.Gear[2] if gs.Gear[2] != 0 else 'None'}")
        print("----------------------\n")
    elif choice == 4:
        allequipment = []
        nbequipped = 0
        for i in range(len(gs.WeaponsInventory)):
            allequipment.append(gs.WeaponsInventory[i])
        for i in range(len(gs.RingsInventory)):
            allequipment.append(gs.RingsInventory[i])
        for i in range(len(gs.Gear)):
            if gs.Gear[i] != 0:
                allequipment.append(gs.Gear[i])
                nbequipped += 1
        print("Here's the explanation about the equipment you have on you Master. :")
        for i in range(len(allequipment)):
            if i >= len(allequipment) - nbequipped:
                print("[EQUIPPED]",allequipment[i]," : ",EquipementExplain[allequipment[i]])
            else:
                print(allequipment[i]," : ",EquipementExplain[allequipment[i]])
        
    elif choice == 5:
        print("Then be safe on your journey Master\n")
    else:
        print("Master do you really feel allright ? Maybe will it be better if you rest ?")


def _change_weapon(error_message):
    if len(gs.WeaponsInventory) == 0:
        print("Sorry Master, but you have no weapons to equip yourself with...")
        return

    print("Of course Master let me Help you\n")
    for i in range(len(gs.WeaponsInventory)):
        print(f"{i + 1}-", gs.WeaponsInventory[i])
    equipchoice = ui.ask_int("I want... :", error_message)

    if not (1 <= equipchoice <= len(gs.WeaponsInventory)):
        print("Sorry Master but that not possible...")
        return

    new_weapon = gs.WeaponsInventory.pop(equipchoice - 1)
    if gs.Gear[0] != 0:
        # On range l'ancienne arme dans l'inventaire et on retire son bonus de stats
        gs.WeaponsInventory.append(gs.Gear[0])
        for i in range(len(gs.Max_Stats)):
            gs.Max_Stats[i] -= WEAPON[gs.Gear[0]][i]

    gs.Gear[0] = new_weapon
    for i in range(len(gs.Max_Stats)):
        gs.Max_Stats[i] += WEAPON[new_weapon][i]
    print(f"You equipped {new_weapon} !")


def _change_ring(error_message):
    if len(gs.RingsInventory) == 0:
        print("Sorry Master, but you have no rings to equip yourself with...")
        return

    print("Of course Master let me Help you\n")
    for i in range(len(gs.RingsInventory)):
        print(f"{i + 1}-", gs.RingsInventory[i])
    equipchoice = ui.ask_int("I want... :", error_message)

    if not (1 <= equipchoice <= len(gs.RingsInventory)):
        print("Sorry Master but that not a valid number...")
        return

    new_ring = gs.RingsInventory.pop(equipchoice - 1)
    slotchoice = ui.ask_int("In wich slot do you want your ring Master ?", error_message)

    if slotchoice not in [1, 2]:
        print("Sorry Master but that not a valid number...")
        gs.RingsInventory.append(new_ring)
        return

    if gs.Gear[slotchoice] != 0:
        # Un anneau est déjà dans ce slot : on le retire (et son bonus) avant de mettre le nouveau
        old_ring = gs.Gear[slotchoice]
        gs.RingsInventory.append(old_ring)
        _remove_ring_bonus(old_ring)

    _apply_ring_bonus(new_ring)
    print(f"You equipped {new_ring} !")
    gs.Gear[slotchoice] = new_ring


def _apply_ring_bonus(ring_name):
    """Applique le bonus d'un anneau. Hornet/Snipers Ring sont un cas spécial
    car ils boostent CritDamage/CritChance directement plutôt qu'une stat."""
    if ring_name == "Hornet Ring":
        gs.CritDamage += RINGS[ring_name][0]
    elif ring_name == "Snipers Ring":
        gs.CritChance += RINGS[ring_name][0]
    else:
        for i in range(len(gs.Max_Stats)):
            gs.Max_Stats[i] += RINGS[ring_name][i]


def _remove_ring_bonus(ring_name):
    """L'inverse exact de _apply_ring_bonus, pour déséquiper un anneau proprement."""
    if ring_name == "Hornet Ring":
        gs.CritDamage -= RINGS[ring_name][0]
    elif ring_name == "Snipers Ring":
        gs.CritChance -= RINGS[ring_name][0]
    else:
        for i in range(len(gs.Max_Stats)):
            gs.Max_Stats[i] -= RINGS[ring_name][i]


def talk_to_leaf():
    """La fée Leaf raconte une anecdote au hasard (purement cosmétique)."""
    print("Fairy Leaf :")
    print("Hey Grimm, wanna hear some random facts? ♪")
    print("1- Yes \n2- No")
    error = "Umm… I think you're supposed to type a number, not words…\nUnless… is this some kind of secret code?"
    choice = ui.ask_int("___ : ", error)

    if choice == 1:
        print("Perfect ♡!")
        print(LeafRandomFact[randint(0, len(LeafRandomFact) - 1)])
    elif choice == 2:
        print("Well to bad for you ~♡")
    else:
        print("Come on, you can’t even hit 1 or 2 properly? Geez, what are we gonna do with you? ♪")


def talk_to_catherine():
    """Affiche les stats actuelles (Max_Stats) et le nombre de Souls du joueur."""
    print("Saint Catherine :")
    print("Welcome back, sir Grimm.\nPlease don't overwork yourself, alright?\nIts fine to rest a little")
    print("Shall I examine your stats, if it pleases you?")
    print("1- Yes please \n2- No no need")
    error = "Oh… Only numbers, please, Sir Grimm.\nThe Lord teaches patience, and so shall I wait as long as needed."
    choice = ui.ask_int("___ : ", error)

    if choice == 1:
        print("Very well here you go... :\n")
        print(gs.Name, " : ")
        print("HP :", gs.Max_Stats[gs.HP])
        print("MP :", gs.Max_Stats[gs.MP])
        print("ATK :", gs.Max_Stats[gs.ATK])
        print("MAG :", gs.Max_Stats[gs.MAG])
        print("DEF :", gs.Max_Stats[gs.DEF])
        print("SPD :", gs.Max_Stats[gs.SPD])
        print("LCK :", gs.Max_Stats[gs.LCK])
        print("Souls :", gs.Stats[gs.SOULS])
    elif choice == 2:
        print("Radiance of God's beauty surpasses the sun\nand the intellect governs all creation.")
        print("I pray for your return sir Grimm, may you come back safely")
    else:
        print("My, my... You must be utterly exhausted. Please, take all the time you need to rest.")


def talk_to_dorothy():
    """Boutique des sorts, et rappel de ce que fait chaque sort."""
    print("Witch Dorothy :")
    print("Oh? its you apprentice. What's the matter?")
    print("1- I want to buy spells \n2- Teach me more about magic \n3- Just passing by")
    error = "Tch. Use numbers, not your imagination."
    choice = ui.ask_int("___ : ", error)

    if choice == 1:
        if len(SpellsListName) != 0:
            print("Stare all you want")
            for i in range(len(SpellsListName)):
                print(f"{i + 1}-", SpellsListName[i], "--- Souls Cost :", SpellsListCost[i])
            print("                     Souls :", gs.Stats[gs.SOULS], "\n")

            buychoice = ui.ask_int("So, which incantation catches your eye, hmm? : ", error)
            if buychoice < 1 or buychoice > len(SpellsListName):
                print("I could pretend to sell you something that doesn’t exist… but even I have standards.")
            elif SpellsListCost[buychoice - 1] > gs.Stats[gs.SOULS]:
                print("Foolish apprentice you don't have enough Souls.\nQuickly gather them then.")
            else:
                gs.Spells.append(SpellsListName[buychoice - 1])
                gs.Stats[gs.SOULS] -= SpellsListCost[buychoice - 1]
                # On retire le sort de la boutique ET son prix, dans le même ordre,
                # pour que les deux listes restent alignées (voir data_spells.py).
                SpellsListName.pop(buychoice - 1)
                SpellsListCost.pop(buychoice - 1)
                print("All yours now. Don’t say I never gave you anything")
        else:
            print("Looks like my spells have all found a new home. Hope you use them well.")

    elif choice == 2:
        print("Trying to make sense of it all? How cute")
        print("Fine, I’ll spill the secrets. Don’t blame me if it’s confusing.\n")
        for spell_name in SpellsListName2:
            print(spell_name, " : ", SpellsExplain[spell_name])

    elif choice == 3:
        print("Wandering without purpose again? You’ll end up hexed by your own confusion.")

    else:
        print("What nonsense are you babbling now?")
        print("Honestly... Did you hit your head again, apprentice?")


def BoneFire():
    """
    Boucle principale du Feu de Camp : soigne le joueur, affiche le menu, et
    redirige vers le bon PNJ jusqu'à ce que le joueur choisisse "Continue".
    """
    gs.heal_at_bonfire()
    Continue = False
    while not Continue:
        ui.wait()
        ui.clear_screen()
        print("___________________BonFire ♨___________________")
        print("-Upgrade           -Equipement\n-Facts             -Status\n-Spells Shop \n                                   Continue -->\n")
        choice = input("What do you want to do ? : ")

        if choice == "Upgrade":
            talk_to_elisabeth()
        elif choice == "Equipement":
            talk_to_victoria()
        elif choice == "Facts":
            talk_to_leaf()
        elif choice == "Status":
            talk_to_catherine()
        elif choice == "Spells Shop":
            talk_to_dorothy()
        elif choice == "Continue":
            Continue = True
        else:
            print("Nuh Uh you can't do that ~♪")

    # On soigne et on annule les debuffs une seconde fois en sortant du feu de
    # camp (comme dans le fichier d'origine) - le joueur part toujours en
    # pleine forme vers le prochain combat.
    gs.heal_at_bonfire()
