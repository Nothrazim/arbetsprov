import random
import time
from card import *
from creature import *
from map import Map
from player import *


def handle_input():
    return input(">>: ")


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
                        print("add hero 3")
                        # p_list.append(player3)
                        if num_heroes == 4:
                            print("add hero 4")
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
    print("player list is:")
    for p in p_list:
        print(p.name)
        if p.hero is not "":
            print("Hero:", p.hero.name)
        else:
            print("no hero selected")


def apply_hero(player, choice):
    if choice == 0:
        player.hero = hero_jarax
    elif choice == 1:
        player.hero = hero_hitler
    elif choice == 2:
        player.hero = hero_stalin
    else:
        print("ended in else on Apply Hero, not good")


def main_menu():
    p_list = [player1, player2]
    map_choice = 0  # Default

    menu_dict = {
        "Map": [500, "Choose Map", choose_map],
        "Player #1 Hero": [22000, "Choose player #1 Hero", choose_hero],
        "Player #2 Hero": [1546, "Choose player #2 Hero", choose_hero],
        "Player #3 Hero": [16798, "Choose player #3 Hero", choose_hero],
        "Player #4 Hero": [1876, "Choose player #4 Hero", choose_hero],
        "Num of Heroes": [1100, "Choose number of Heroes", choose_num_heroes],
        "Quit": [6871, "Quit", quit],
        "Game Start": [1987, "Start the Game!", game_loop],
        "Player List": [154, "Show List of Players", show_player_list],
    }
    # Something needs to check that all players have chosen hero.

    # +neutral deck shenanigans?

    while True:
        menu_options = []
        x = 0
        for value in menu_dict:
            if value == "Player #3 Hero":
                if len(p_list) < 3:  # No third hero added
                    menu_dict[value][0] = 20000
                else:
                    menu_options.append(menu_dict[value])
                    x += 1
                    menu_dict[value][0] = x
            elif value == "Player #4 Hero":
                if len(p_list) is not 4:  # No fourth hero added
                    menu_dict[value][0] = 2000
                else:
                    menu_options.append(menu_dict[value])
                    x += 1
                    menu_dict[value][0] = x
            else:
                menu_options.append(value)
                x += 1
                menu_dict[value][0] = x

        print("\n Val printing:")
        for val in menu_dict:
            # print(menu_dict[val])
            if menu_dict[val][0] < 10:  # Doesn't show 'hidden' options arbitrary high
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
                                game_loop(p_list, map_choice)
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


def game_loop(player_list):
    print("I am a game loop!")
    for player in player_list:
        print(player.name+", it is your turn.")
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


main_menu()
