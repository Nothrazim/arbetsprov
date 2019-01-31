import random
from card import *
# from map import Map

class Creature:
    def __init__(self, name, hp, defense, attack, attack_range, movement, ability="none"):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.attack_range = attack_range
        self.movement = movement
        self.current_movement = movement
        self.ability = ability


class Hero(Creature):
    def __init__(self, name, hp, defense, attack, attack_range, movement, hero_ability, energy_cap, energy_regen):
        Creature.__init__(self, name, hp, defense, attack, attack_range, movement, ability="none")
        self.hero_ability = hero_ability
        self.energy_cap = energy_cap
        self.energy_regen = energy_regen


hero_jarax = Hero("Jarax", 30, 2, 3, 1, 4, "berzerk", 100, 0)
hero_stalin = Hero("Stalin", 20, 0, 1, 1, 4, "beast_shape", 11, 3)
hero_stalin_bear = Hero("Stalin Bear", 20, 1, 2, 1, 5, "beast_shape", 11, 3)
hero_hitler = Hero("Hitler Nechromancer", 10, 0, 2, 4, 4, "raise_dead", 12, 3)
hero_hitler_horror = Hero("Hitler Necrotech Horror", 10, 1, 2, 6, 5, "raise_horror", 14, 4)

creature_jarax_chosen = Creature("Chosen", 1, 3, 3, 1, 3, "chosen_fury")
# creature_jarax all others

creature_hitler_zombie = Creature("Zombie", 1, 0, 2, 1, 2)
creature_hitler_horror = Creature("Undead Horror", 1, 1, 3, 1, 3)
creature_hitler_fiend = Creature("Technofused Fiend", 1, 3, 4, 2, 4)
creature_hitler_behemoth = Creature("Necrological Behemoth", 1, 5, 3, 2, 4)
creature_hitler_turret = Creature("Necrotech Turret", 1, 3, 3, 5, 1)  # Flying
creature_hitler_forge = Creature("Necrotech Forge", 1, 5, 0, 0, 0)  # Pulse dmg, gain charges
creature_hitler_cloning = Creature("Cloning Vats", 1, 5, 0, 0, 0)  # Animate zombie

player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []

hero_list = [hero_jarax, hero_hitler, hero_stalin]

#draw_card(player1_hand, jarax_deck)
#print(player1_hand[0].name)

#print_cards_in_deck(jarax_deck)
#shuffle_deck(jarax_deck)

#draw_card(player1_hand, jarax_deck)

#print_cards_in_deck(jarax_deck)

#dungeon = Map(4)

#dungeonmap = Map.draw_map(0, hero_jarax, dungeon)

#dungeon.draw_map(hero_jarax, dungeon)
