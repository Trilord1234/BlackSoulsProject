# -*- coding: utf-8 -*-
"""
Created on Tue May 27 14:13:11 2025
@author: tristabe

main.py
===========
Point d'entrée du jeu : `python main.py` pour lancer une partie.

Ce fichier ne fait QUE 3 choses :
    1. Afficher l'écran de chargement, l'intro et le tutoriel.
    2. Faire tourner la boucle principale du donjon (choisir un ennemi,
       lancer le combat, aller au feu de camp, recommencer).
    3. Rien d'autre : toute la vraie logique (combat, boutique, loot...)
       vit dans les autres fichiers du projet (voir leurs docstrings).

TODO CONNUS (repris des notes de l'auteur dans la version originale) :
    - Gérer les boss à plusieurs phases (Drake Helkaiser a 3 formes d'affilée,
      Cinderella en a 2, mais rien n'enchaîne encore les phases automatiquement).
    - Le boss secret n'est pas implémenté.
    - La victoire finale (`END = True`) n'est déclenchée nulle part encore :
      la boucle principale ci-dessous est donc actuellement sans fin.
"""

import time

import game_state as gs
import ui
import dungeon
import combat
import bonfire
from data_bestiary import BOSS
from dialogue import INTRO, TUTORIAL


def show_loading_screen():
    ui.clear_screen()
    print("\n\n\n\n\n\n")
    time.sleep(0.5)
    for i in range(0, 101, 5):
        time.sleep(0.1)
        print(f"\rLoading game... {ui.SpeedSysteme(i)} {i}%", end='', flush=True)


def type_out(text):
    """Affiche un texte lettre par lettre, pour un petit effet 'machine à écrire'."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.005)


def show_intro():
    time.sleep(0.5)
    ui.clear_screen()
    type_out(INTRO)
    print("\n")
    ui.wait()


def show_tutorial():
    ui.clear_screen()
    print("_______ Tutorial _______")
    type_out(TUTORIAL)
    ui.wait()


def enter_the_lost_empire():
    ui.clear_screen()
    print("_________Welcome to the Lost Empire_________")
    choice = input("Enter the lost Empire ? (Yes/No) : ")
    if choice != "Yes":
        print("Do you really think you have a choice here ?")
        print("Anyway...")
    print("You open the gate and enter the First Floor of the Lost Empire...\n")
    ui.wait()
    ui.clear_screen()


def prepare_next_fight():
    """
    Détermine le prochain ennemi à affronter : un boss si assez de monstres
    ont été tués sur l'étage ET que le joueur accepte d'entrer dans la salle
    du boss, sinon un monstre normal au hasard.
    Remplit gs.Monster_Name / gs.Monster_Stats / gs.HP_max_Monster / etc.
    """
    if gs.MonsterKill >= gs.NbMonsterToKill:
        FightBoss = input("Do you want to enter the boss Room ? (Yes/No) : ")
        if FightBoss == "Yes":
            gs.BossFight = True
            boss_name = dungeon.Dungeon[gs.Floor][-1]  # le boss est toujours en dernière position, voir dungeon.py
            gs.Monster_Name = boss_name
            gs.Monster_Stats = BOSS[boss_name].copy()

    if not gs.BossFight:
        gs.Monster_Name, gs.Monster_Stats = dungeon.MonsterToFight(gs.Floor)

    gs.HP_max_Monster = gs.Monster_Stats[gs.HP]
    gs.MP_max_Monster = gs.Monster_Stats[gs.MP]
    gs.CritChanceMonster = 5 + (gs.Monster_Stats[gs.LCK] // 2)
    gs.CritDamageMonster = 100


def walk_to_the_next_fight():
    for _ in range(5):
        for dots in [".", "..", "..."]:
            print(f"\rYou walk along the dark corridor{dots}   ", end='', flush=True)
            time.sleep(0.3)
    print("Ennemy found !")


def run_dungeon_loop():
    """La boucle principale du jeu : un tour = un combat + un passage au feu de camp."""
    gs.Floor = 0
    gs.MonsterKill = 0
    gs.NbMonsterToKill = dungeon.NumberOfMonsterToFight()
    gs.OldFloor = 0
    gs.Dead = False
    gs.BossFight = False

    while not gs.END:
        if gs.OldFloor != gs.Floor:
            gs.NbMonsterToKill = dungeon.NumberOfMonsterToFight()
            gs.MonsterKill = 0
            gs.OldFloor = gs.Floor

        print(f"_________Floor {gs.Floor}_________")

        if gs.MonsterKill >= gs.NbMonsterToKill:
            gs.MonsterKill = gs.NbMonsterToKill
        print("                   ", gs.MonsterKill, "/", gs.NbMonsterToKill, "\n")

        prepare_next_fight()
        walk_to_the_next_fight()

        combat.FightSysteme(gs.Stats[gs.SPD], gs.Monster_Stats[gs.SPD])
        ui.clear_screen()

        if gs.Dead:
            gs.reset_after_death()
        elif gs.BossFight:
            gs.BossFight = False
            gs.Floor += 1

        bonfire.BoneFire()
        ui.clear_screen()


def main():
    show_loading_screen()
    show_intro()
    show_tutorial()
    enter_the_lost_empire()
    run_dungeon_loop()


if __name__ == "__main__":
    main()
