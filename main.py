import random
import time
from card import *
from creature import *
from player import *


def handle_input():
    return input(">> ")


def choose_map():
    print("Choose your map!\n"
          "\t1. Acid Woods\n"
          "\t2. Blasted Lands\n"
          "\t3. Temple of the Elements\n"
          "\t4: Shrine of Past Gods")
    # Something goes here to either fetch map generation or just make fancy name print
    map_choice = int(handle_input())
    return map_choice


def choose_hero():
    while True:
        x = 0
        print("")
        for hero in hero_list:
            x += 1
            print(str(x)+".", hero.name)
        print(str(x+1)+". Random Hero")
        try:
            hero_choice = int(handle_input()) - 1
            if hero_choice == len(hero_list):  # Randomizes hero
                hero_choice = random.randrange(0, len(hero_list)-1)
                print("You have randomized:", hero_list[hero_choice].name)
            else:
                print("You have chosen to play as", hero_list[hero_choice].name)
            break
        except IndexError:
            print("That does not correspond to any hero i know. Try again.")
    return hero_choice


def choose_num_heroes():
    while True:
        print("You can play up to 4 players at one time. How many players do you want?")
        try:
            num_heroes = int(handle_input())
            if num_heroes >= 2:
                if num_heroes > 2:
                    if num_heroes < 5:
                        print("Player #3 added to the game.")
                        # p_list.append(player3)
                        if num_heroes == 4:
                            print("Player #4 added to the game.")
                            # p_list.append(player4)
                            break
                        else:
                            break
                    else:
                        print("Too many heroes. Try again.")
                else:
                    break  # Don't add additional heroes if there are only 2
            else:
                print("You need more heroes. Try again.")
        except ValueError:
            print("Enter a valid number.")
    return num_heroes


def show_player_list(p_list):
    print("Player list:")
    for p in p_list:
        print(p.name)
        if p.hero is not "":
            print("Hero:", p.hero.name + "\n")
        else:
            print(p.name, "has not selected a Hero yet.\n")


def apply_hero(player, choice):
    if choice == 0:
        player.hero = Hero("Jarax", 30, 2, 3, 1, 4, "berzerk", "Brute", 999, 0)
        player.deck = jarax_deck
    elif choice == 1:
        player.hero = Hero("Hitler Nechromancer", 10, 0, 2, 4, 4, "raise_dead", "Adept", 12, 3)
        player.deck = hitler_deck
    elif choice == 2:
        player.hero = Hero("Stalin", 20, 0, 1, 1, 4, "beast_shape", "Adept", 11, 3)
        player.deck = stalin_deck
    else:
        print("ended in else on Apply Hero, not good")


def main_menu():
    p_list = [player1, player2]
    map_choice = 0  # Default

    menu_dict = {
        "Game Start": [1987, "Start the Game!", init_game],
        "Map": [500, "Choose Map", choose_map],
        "Player #1 Hero": [22000, "Choose player #1 Hero", choose_hero],
        "Player #2 Hero": [1546, "Choose player #2 Hero", choose_hero],
        "Player #3 Hero": [16798, "Choose player #3 Hero", choose_hero],
        "Player #4 Hero": [1876, "Choose player #4 Hero", choose_hero],
        "Num of Heroes": [1100, "Choose number of Heroes", choose_num_heroes],
        "Player List": [154, "Show List of Players", show_player_list],
        "Quit": [6871, "Quit", quit],
    }

    # Should there be neutral deck choices?

    while True:
        x = 0
        for value in menu_dict:
            if value == "Player #3 Hero":
                if len(p_list) < 3:  # No third hero added
                    menu_dict[value][0] = 20000
                else:
                    x += 1
                    menu_dict[value][0] = x
            elif value == "Player #4 Hero":
                if len(p_list) is not 4:  # No fourth hero added
                    menu_dict[value][0] = 2000
                else:
                    x += 1
                    menu_dict[value][0] = x
            else:
                x += 1
                menu_dict[value][0] = x

        # Clear screen needed
        for val in menu_dict:
            # print(menu_dict[val])
            if menu_dict[val][0] < 100:  # Doesn't show 'hidden' options (with arbitrarily high values)
                print(str(menu_dict[val][0])+".", menu_dict[val][1])
        try:
            usr_choice = int(handle_input())

            for val in menu_dict:
                if usr_choice == menu_dict[val][0]:

                    if val == "Game Start":
                        if map_choice > 0:  # Map must be chosen
                            p_number = 0
                            for p in p_list:
                                if p.hero == "":
                                    pass
                                else:
                                    p_number += 1
                            if p_number == len(p_list):
                                init_game(p_list, map_choice)
                            else:
                                for p in p_list:
                                    if p.hero == "":
                                        print(p.name, "has yet to choose a hero!")
                        else:
                            print("You must select a map before starting the game!")

                    elif val == "Player List":
                        menu_dict[val][2](p_list)

                    elif val == "Map":
                        map_choice = menu_dict[val][2]()
                        print("map chosen is", map_choice)
                    elif menu_dict[val][2] is choose_hero:
                        return_value = menu_dict[val][2]()
                        if val == "Player #1 Hero":
                            apply_hero(player1, return_value)
                        elif val == "Player #2 Hero":
                            apply_hero(player2, return_value)
                        elif val == "Player #3 Hero":
                            apply_hero(player3, return_value)
                        elif val == "Player #4 Hero":
                            apply_hero(player4, return_value)
                        else:
                            print("ended in else for resolution for choose hero")
                    elif val == "Num of Heroes":
                        return_value = menu_dict[val][2]()
                        p_list = [player1, player2]
                        if return_value >= 3:
                            p_list.append(player3)
                            if return_value == 4:
                                p_list.append(player4)
                    else:
                        menu_dict[val][2]()

        except ValueError:
            print("Please enter a number.")


def init_game(player_list, map_choice):
    print("I am the initiation!")

    init_list = []
    shuffle_deck(neutral_deck)
    for player in player_list:
        player.shuffle_deck()
        init = random.randrange(1, 6)
        init_list.append(init)

    for player in player_list:
        player.draw_card()
        player.draw_card()
        player.draw_card()
        player.draw_card()
        for card in player.hand:
            print(player.name, "has drawn", card.name + ".")
        print("")

    # for player in player_list:
        # choose start loc

        # draw 4 cards

    game_turn(player_list, 0)


def game_turn(player_list, turn_count):  # Also needs to receive map.
    while True:
        turn_count += 1
        print("\t\tTURN", turn_count)

        resolve_order = []

        for player in player_list:
            print("")
            print(player.name+", it is your turn.")
            print(player.name+", you have", player.hero.current_energy, player.hero.energy_type+".")
            resolve_order.append(offer_cards(player_list))

            player.draw_card()
            print(player.name, "has drawn", player.hand[-1].name + ".")

            # offer_cards(player_list)

            print("This is where start-of-turn (maintenance) effects should occur.")

            # offer_cards(player_list)

            player.hero.generate_resources(player)

            # offer_cards(player_list)

            # Movement + Attacks

            # offer_cards(player_list)

            # Resolve all effects

            print("End of turn.")
            print(player.name, "currently has", player.hero.current_energy, player.hero.energy_type+".")
            print("")

        if turn_count != 1:
            print("It is not the first turn")

        if turn_count > 1:
            print("end of turn 2")
            break

    """
    resolve_order = [offer_cards(player_list), draw_card, offer_cards(player_list), "maintenance",
                     offer_cards(player_list), "gain resources", offer_cards(player_list), "movement+attacks",
                     offer_cards(player_list), "resolve cards"]
    """


def offer_cards(player_list):
    return_list = []
    for player in player_list:
        x = 0
        if len(player.hand) > 0:
            for card in player.hand:
                if card.cost > player.hero.current_energy:
                    pass
                else:
                    x += 1
        if x > 0:
            while True:
                print(player.name + ", do you want to play any cards?"
                                    "\n[Y]es to play cards."
                                    "\n[V]iew cards to view cards")
                inp = handle_input()
                inp = inp.lower()[:1]
                if inp == "y":
                    card = player.choose_card()
                    if type(card) == Card:
                        print(player.name, "has chosen to play", card.name)
                        return_list.append(card)
                    break
                elif inp == "v":
                    player.print_cards_in_hand()
                elif inp == "":
                    pass
                else:
                    break
    return return_list


player_dummy = Player("dummy")
player_dummy.hero = Hero("Hitler Nechromancer", 10, 0, 2, 4, 4, "raise_dead", "Adept", 12, 3)
player_dummy.deck = hitler_deck
player_dummy.hand = [card_jarax_sear_soul, card_jarax_unholy_engineering, card_jarax_skull_don_throne,
                     card_jarax_blood_god, card_stalin_crown_of_ice, card_stalin_absolute_zero,
                     card_stalin_motherlands_protection, card_jarax_soulstealer_hammer]
player_dummy.hero.current_energy = 4
# card = player_dummy.choose_card()
# print("the card chosen was", card.name)

main_menu()


# Destroy all creatures
# move self
# deal damage in line
# single target damage
# AoE dmg
# draw card
# generate mana
# reduce target resource pool
# disable movement
# force movement
# heal
# destroy target equipment
#