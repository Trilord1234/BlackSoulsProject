# -*- coding: utf-8 -*-
"""
combat.py
=============
Le coeur du système de combat au tour par tour basé sur une "jauge de
vitesse" (chaque personnage agit quand sa jauge est pleine, les plus rapides
agissent plus souvent).

3 fonctions principales :
    - MonsterAttack()   : l'ennemi attaque le joueur
    - ActionSysteme()   : menu d'action du joueur (Attack/Spells/Dodge/...)
    - FightSysteme(...) : la boucle de combat complète, appelée une fois par
                          rencontre (voir dungeon.py + main.py)
"""

import time
from random import randint

import game_state as gs
import ui
from loot import Loot
from data_spells import SPELLS


def MonsterAttack():
    """
    L'ennemi (gs.Monster_Name / gs.Monster_Stats) attaque le joueur.
    Calcule si le coup est critique, puis applique Dodge/Guard/rien selon
    ce que le joueur a choisi lors de son tour (voir ActionSysteme).
    """
    x = randint(0, 100)
    is_critical = x <= gs.CritChanceMonster

    base_damage = max(1, (gs.Monster_Stats[gs.ATK] - gs.Stats[gs.DEF]))
    if is_critical:
        damage = round(base_damage + base_damage * (gs.CritDamageMonster / 100))
    else:
        damage = base_damage

    print(f"{gs.Monster_Name} Attack !")
    if is_critical:
        print("Critical Strike !")

    if gs.Dodge:
        chance = randint(0, 100)
        if chance <= 70:
            print("He deal : ", damage, "Damage !")
            print("But you dodge !")
        else:
            gs.Stats[gs.HP] -= damage
            print("He deal : ", damage, "Damage !")
    elif gs.Guard:
        half_damage = damage // 2
        gs.Stats[gs.HP] -= half_damage
        print("He deal : ", half_damage, "Damage !")
    else:
        gs.Stats[gs.HP] -= damage
        print("He deal : ", damage, "Damage !")

    ui.wait()


def ActionSysteme():
    """
    Affiche le menu d'action du joueur et applique le choix fait.
    Boucle tant que le joueur n'a pas choisi une action valide (Action=True
    la fait sortir de la boucle).
    """
    Action = False
    while not Action:
        print("________Your turn________")
        print("-Attack           -Spells\n-Dodge            -Guard\n-Check            -Flee\n")
        choice = input("Choose your action : ")
        gs.Dodge = False
        gs.Guard = False

        # Le critique du joueur est tiré une seule fois par tour, avant de
        # savoir quelle action est choisie (Attack ou Spells d'attaque en profitent).
        CriticalHit = randint(0, 100) <= gs.CritChance

        if choice == "Attack":
            Damage = gs.Stats[gs.ATK]
            print("You Attack !", gs.Monster_Name)
            base = max(1, Damage - gs.Monster_Stats[gs.DEF])
            if not CriticalHit:
                gs.Monster_Stats[gs.HP] -= base
                print("You did :", base, "Damage !")
            else:
                total = round(base + base * (gs.CritDamage / 100))
                gs.Monster_Stats[gs.HP] -= total
                print("CriticalHit !!!")
                print("You did :", total, "Damage !")
            Action = True
            ui.wait()

        elif choice == "Spells":  # Les effets (Poison/Burn/Freeze) n'ont pas encore été ajoutés
            if len(gs.Spells) == 0:
                print("you don't have any spells")
            else:
                for i in range(len(gs.Spells)):
                    print(f"{i + 1}-", gs.Spells[i], "--- Mana Cost :", SPELLS[gs.Spells[i]]["mana_cost"])
                spellschoice = ui.ask_int("Wich one do I use ? : ", "Please enter the Number, not the Action")

                if spellschoice > len(gs.Spells) or spellschoice < 1:
                    print("I don't have this Spells...")
                    ui.wait()
                elif gs.Stats[gs.MP] < SPELLS[gs.Spells[spellschoice - 1]]["mana_cost"]:
                    print("I don't have enought MP...")
                    ui.wait()
                else:
                    spell_name = gs.Spells[spellschoice - 1]
                    spell = SPELLS[spell_name]

                    if spell["type"] == "Attack":
                        print("Spells Use !")
                        if not CriticalHit:
                            gs.Monster_Stats[gs.HP] -= spell["power"]
                            gs.Stats[gs.MP] -= spell["mana_cost"]
                            print("You did :", spell["power"], "Damage !")
                        else:
                            total = round(spell["power"] + spell["power"] * (gs.CritDamage / 100))
                            gs.Monster_Stats[gs.HP] -= total
                            gs.Stats[gs.MP] -= spell["mana_cost"]
                            print("CriticalHit !!!")
                            print("You did :", total, "Damage !")
                        Action = True
                        ui.wait()

                    elif spell["type"] == "Heal":
                        print("Spells Use !")
                        BeforeHeal = gs.Stats[gs.HP]
                        if not CriticalHit:
                            gs.Stats[gs.HP] += spell["power"]
                            gs.Stats[gs.MP] -= spell["mana_cost"]
                        else:
                            print("CriticalHeal !!!")
                            gs.Stats[gs.HP] += spell["power"] + spell["power"] * (gs.CritDamage / 100)
                            gs.Stats[gs.MP] -= spell["mana_cost"]
                        if gs.Stats[gs.HP] > gs.Max_Stats[gs.HP]:
                            gs.Stats[gs.HP] = gs.Max_Stats[gs.HP]
                        print("You heal :", gs.Stats[gs.HP] - BeforeHeal, "HP !")
                        Action = True
                        ui.wait()

        elif choice == "Check":
            print(gs.Monster_Name, " : ")
            print("HP :", gs.HP_max_Monster)
            print("MP :", gs.MP_max_Monster)
            print("ATK :", gs.Monster_Stats[gs.ATK])
            print("MAG :", gs.Monster_Stats[gs.MAG])
            print("DEF :", gs.Monster_Stats[gs.DEF])
            print("SPD :", gs.Monster_Stats[gs.SPD])
            print("LCK :", gs.Monster_Stats[gs.LCK])
            Action = True
            ui.wait()

        elif choice == "Flee":
            escape = randint(0, 100)
            if escape <= 25:
                print(f"{gs.Name} starts running away !")
                gs.Flee = True
                Action = True
                ui.wait()
            else:
                print(f"{gs.Name} starts running away ! \nBut the escape path was blocked!")
                Action = True
                ui.wait()

        elif choice == "Dodge":
            gs.Dodge = True
            Action = True

        elif choice == "Guard":
            gs.Guard = True
            Action = True

        else:
            print("I can't do that...")
            ui.wait()


def FightSysteme(speed_grimm, speed_monster, size=30):
    """
    Boucle de combat complète : fait avancer les jauges de vitesse du joueur
    et du monstre jusqu'à ce que l'un des deux tombe à 0 HP.

    speed_grimm / speed_monster : la stat SPD de chacun (détermine à quelle
    vitesse leur jauge se remplit).
    """
    max_speed = max(speed_grimm, speed_monster)
    filling_speed_grimm = max_speed / speed_grimm
    filling_speed_monster = max_speed / speed_monster
    grimm_systeme = 0
    monster_systeme = 0

    while gs.Stats[gs.HP] > 0 and gs.Monster_Stats[gs.HP] > 0:

        grimm_systeme += 0.05 * (100 / filling_speed_grimm)
        monster_systeme += 0.05 * (100 / filling_speed_monster)

        ui.clear_screen()

        print(f"_______Floor {gs.Floor}_______")
        print("                   ", gs.MonsterKill, "/", gs.NbMonsterToKill, "\n\n")

        ui.HPMPSystemeGrimm()
        print(f"      |AP|{ui.SpeedSysteme(grimm_systeme, size)}\n\n")

        ui.HPMPSystemeMonster(gs.HP_max_Monster, gs.MP_max_Monster)
        print(f"      |AP|{ui.SpeedSysteme(monster_systeme, size)}\n\n")

        # Si les deux jauges sont pleines en même temps, le plus rapide des
        # deux joue en premier.
        if grimm_systeme >= 100 and monster_systeme >= 100:

            if speed_grimm >= speed_monster:
                print("Grimm turn")
                ActionSysteme()
                if gs.Flee:
                    gs.Flee = False
                    return
                grimm_systeme -= 100
                time.sleep(0.5)

                if monster_systeme >= 100:
                    print("Monster turn")
                    MonsterAttack()
                    monster_systeme -= 100
                    ui.wait()
            else:
                print("Monster turn")
                MonsterAttack()
                monster_systeme -= 100
                time.sleep(0.5)
                if grimm_systeme >= 100:
                    print("Grimm turn")
                    ActionSysteme()
                    if gs.Flee:
                        gs.Flee = False
                        return
                    grimm_systeme -= 100
                    ui.wait()

        else:
            if grimm_systeme >= 100:
                print("Grimm turn")
                ActionSysteme()
                if gs.Flee:
                    gs.Flee = False
                    return
                grimm_systeme -= 100
                time.sleep(0.5)
            if monster_systeme >= 100:
                print("Monster turn")
                MonsterAttack()
                monster_systeme -= 100
                time.sleep(0.5)

        time.sleep(0.016)

    if gs.Stats[gs.HP] <= 0:
        print("You have been slain...")
        gs.Dead = True
    elif gs.Monster_Stats[gs.HP] <= 0:
        print(f"{gs.Monster_Name} have been slain !")
        gs.MonsterKill += 1
        Loot(gs.Floor)
    time.sleep(1)
