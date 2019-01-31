import random
import time
from card import *
from creature import *
# from map import *
from player import *



def handle_input():
    return input("Choice: ")


def choose_map():
    print("Choose your map!\n"
          "\t1. Acid Woods\n"
          "\t2. Blasted Lands\n"
          "\t3. Temple of the Elements\n"
          "\t4: Shrine of Past Gods")
    # Something goes here to either fetch map generation or just make fancy name print
    map_choice = handle_input()
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
            if num_heroes > 1:
                if num_heroes < 5:
                    break
                else:
                    print("Too many heroes. Try again.")
            else:
                print("You need more heroes. Try again.")
        except ValueError:
            print("Enter a valid number.")
    return num_heroes


def main_menu():

    menu_dict = {
        "a": "Choose Map",
        "b": "Choose player #1 Hero",
        "c": "Choose player #2 Hero",
        "d": "Choose player #3 Hero",
        "e": "Choose player #4 Hero",
        "f": "Choose number of Heroes",
        "g": "Quit",
        "h": "Start Game!",
    }
    player_list = [player1, player2]
    start_game_list = [0, player_list]  # Map choice, p1 hero, p2 hero
    # Something needs to check that all players have chosen hero.

    # +neutral deck shenanigans?

    while True:
        print("There are", len(player_list), "players.")
        menu_options = []
        x = 0
        temp_menu_dict = menu_dict
        for value in temp_menu_dict:
            if menu_dict[value] == "Start Game!":
                pass
            if value is "d":
                if len(player_list) < 3:
                    print("I did not add a third hero.")
                    pass
                else:
                    print("I have appended player 3 the menu.")
                    menu_options.append(menu_dict[value])
                    x += 1
                    if len(player_list) is 4:
                        print("I have appended player 4 to the menu.")
                        menu_options.append(menu_dict[value])
                        x += 1
            elif value is "e":
                if len(player_list) is not 4:
                    print("I did not add a fourth hero.")
                    pass
                else:
                    print("I have appended value", value, "to the menu.")
                    menu_options.append(menu_dict[value])
                    x += 1
            else:
                # print("Key:", value)
                # print("Choice:", menu_dict[value])
                # print("Dict X:", menu_dict[x])
                menu_options.append(menu_dict[value])
                x += 1

        print("\nThe full player list is:")
        for val in player_list:
            print("player:", val)

        y = 0
        print("\ntime to print menu options")
        for val in menu_options:
            y += 1
            print(str(y)+".", val)

        usr_choice = handle_input()

        if usr_choice == "1":
            map_choice = choose_map()
            print("You have chosen", map_choice)

        elif usr_choice == "2":
            p1_hero = choose_hero()
        # Use AI
        elif usr_choice == "3":
            p2_hero = choose_hero()
        # Highscore

        elif usr_choice == "4":
            player_list = [player1, player2]
            num = choose_num_heroes()
            if num > 2:
                player_list.append(player3)
                if num == 4:
                    player_list.append(player4)
            else:
                print("Didn't add any heroes.")
            # self.view.print_main_menu(self.get_top_highschores(), View.enter_go_back, error=True)
            # self.view.handle_input()  # ENTER TO CONTINUE
            # self.main_menu()

        # Quit
        elif usr_choice == "5":
            print("Good bye!")
            time.sleep(1.2)
            quit()
        else:
            print("I cannot understand that. Try again.")

        """
        Replace this \/ with logic checking everything is OK, breaking when needed
        Alternatively, split into only displaying START GAME option when logic is OK
        Then  
        """
        if start_game_list is 0:
            break
    game_loop()


def game_loop():
    print("I am a game loop!")
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

player_list = [player1, player2]

main_menu()

game_loop()
