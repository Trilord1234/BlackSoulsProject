# -*- coding: utf-8 -*-
"""
dialogue.py
===============
Tous les gros blocs de texte "narratifs" du jeu (écran d'intro, tutoriel,
phrases aléatoires de la fée Leaf). Les isoler ici évite de polluer main.py
et bonfire.py avec des pavés de texte au milieu de la logique du jeu.
"""

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

TUTORIAL = (
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

    "And with that’s I wish you good luck, and die well~ ♪\n"
)

# Phrases piochées au hasard quand on parle à Leaf au feu de camp (voir bonfire.py)
LeafRandomFact = [
    "Blocking always cuts the meanie’s attack in half... even if you're tiny like me~",
    "Dodging only works 70% of the time, so why not be a brave little wall, hm~?",
    "Victoria made the dev cry real tears. She was *that* much of a headache, ufufu~",
    "They *said* there’d be a secret boss at the end... but now it's just empty whispers~",
    "Did you know fairies never truly die? We just nap very, very deeply... like corpses~",
    "My favorite writer? Grimm, of course! His tales are so *cozy*. Maybe you're in one of them~?",
    "I ran out of ideas... so here's some nonsense to fill the void: nya nya blah blah~",
]
