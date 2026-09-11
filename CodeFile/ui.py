# -*- coding: utf-8 -*-
"""
ui.py
=========
Tout ce qui concerne l'AFFICHAGE dans le terminal : nettoyer l'écran,
attendre que le joueur appuie sur une touche, dessiner les barres de
vie/mana/vitesse. Aucune de ces fonctions ne modifie les stats du joueur ou
du monstre, elles se contentent de LIRE game_state pour les afficher.
"""

import os
import msvcrt
import game_state as gs


def clear_screen():
    """Vide le terminal (fonctionne sous Windows comme sous Mac/Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    """Met le jeu en pause jusqu'à ce que le joueur appuie sur Entrée."""
    while msvcrt.kbhit():
        msvcrt.getch()
    input("✿...")


def SpeedSysteme(fill, size=30):
    """
    Construit une barre de progression texte, ex: [██████    ].

    fill : valeur actuelle (0 à 100, un pourcentage)
    size : longueur de la barre en caractères (30 par défaut)
    """
    progress = int(fill / 100 * size)
    return "[" + "█" * progress + " " * (size - progress) + "]"


def HPMPSystemeGrimm():
    """Affiche la ligne HP/MP du joueur (nom, barre de vie, barre de mana)."""
    HP_ratio = gs.Stats[gs.HP] / gs.Max_Stats[gs.HP]
    HP_filled = int(20 * HP_ratio)
    HP_bar = '█' * HP_filled + '-' * (20 - HP_filled)

    MP_ratio = gs.Stats[gs.MP] / gs.Max_Stats[gs.MP]
    MP_filled = int(10 * MP_ratio)
    MP_bar = '▓' * MP_filled + '-' * (10 - MP_filled)

    print(f"{gs.Name:10} |HP|{HP_bar}| {gs.Stats[gs.HP]}/{gs.Max_Stats[gs.HP]} |MP|{MP_bar}| {gs.Stats[gs.MP]}/{gs.Max_Stats[gs.MP]}")


def ask_int(prompt, error_message="Please enter a number, not text."):
    """
    Redemande à l'utilisateur tant qu'il n'a pas tapé un nombre entier valide.
    Évite de répéter le même bloc "while True / try / except ValueError"
    dans chaque menu du jeu (combat.py, bonfire.py...).

    prompt        : le texte affiché pour demander la saisie
    error_message : le texte affiché si ce qui est tapé n'est pas un nombre
                    (personnalisable pour garder la voix de chaque PNJ)
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


def HPMPSystemeMonster(HP_max, MP_max):
    """
    Affiche la ligne HP/MP du monstre actuellement combattu (gs.Monster_Stats).

    HP_max, MP_max : les valeurs MAX du monstre au début du combat (elles ne
    bougent pas pendant le combat, contrairement à gs.Monster_Stats qui, lui,
    diminue au fil des coups reçus - d'où le besoin des 2 valeurs séparées).
    """
    HP_ratio = gs.Monster_Stats[gs.HP] / HP_max
    HP_filled = int(20 * HP_ratio)
    HP_bar = '█' * HP_filled + '-' * (20 - HP_filled)

    MP_ratio = gs.Monster_Stats[gs.MP] / max(1, MP_max)
    MP_filled = int(10 * MP_ratio)
    MP_bar = '▓' * MP_filled + '-' * (10 - MP_filled)

    print(f"{gs.Monster_Name:10} |HP|{HP_bar}| {gs.Monster_Stats[gs.HP]}/{HP_max} |MP|{MP_bar}| {gs.Monster_Stats[gs.MP]}/{MP_max}")
