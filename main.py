import random
import time
import socket
from creature import *
from player import *
from threading import *

HOST = ""  # Standard loopback interface address (localhost)
PORT = 55555        # Port to listen on (non-privileged ports are > 1023)


def handle_input(conn):
    data = conn.recv(2048)
    return data


def choose_map(conn):
    while True:
        maps = ("Choose your map!\n"
                "\t1. Acid Woods\n"
                "\t2. Blasted Lands\n"
                "\t3. Temple of the Elements\n"
                "\t4: Shrine of Past Gods\n")
        conn.send(str.encode(maps))
        # Something goes here to either fetch map generation or just make fancy name print
        try:
            map_choice = int(handle_input(conn))
            if map_choice > 0:
                if map_choice < 5:
                    print("player chose map", map_choice)
                    return map_choice
                else:
                    conn.send(str.encode("Please choose a valid map.\n"))
            else:
                conn.send(str.encode("Please choose a valid map.\n"))
                print("Please choose a valid map.")
        except ValueError:
            print("That is not a map.")
            conn.send(str.encode("That is not a map. Try again.\n"))


def choose_hero(conn, player):
    while True:
        x = 0
        for hero in hero_list:
            x += 1
            print(str(x)+".", hero.name)
            conn.send(str.encode(str(x)+". " + hero.name + "\n"))
        print(str(x+1)+". Random Hero")
        conn.send(str.encode(str(x+1)+". Random Hero\n"))
        try:
            hero_choice = int(handle_input(conn))
            if hero_choice == 1:
                player.hero = Hero("Jarax", 30, 2, 3, 1, 4, "berzerk", "Brute", 999, 0)
                player.deck = jarax_deck
                print(player.name, "chose", player.hero.name)
                conn.send(str.encode("You have chosen " + player.hero.name + "\n"))
                break
            elif hero_choice == 2:
                player.hero = Hero("Hitler Nechromancer", 10, 0, 2, 4, 4, "raise_dead", "Adept", 12, 3)
                player.deck = hitler_deck
                print(player.name, "chose", player.hero.name)
                conn.send(str.encode("You have chosen " + player.hero.name + "\n"))
                break
            elif hero_choice == 3:
                player.hero = Hero("Stalin", 20, 0, 1, 1, 4, "beast_shape", "Adept", 11, 3)
                player.deck = stalin_deck
                print(player.name, "chose", player.hero.name)
                conn.send(str.encode("You have chosen " + player.hero.name + "\n"))
                break
            elif hero_choice == 4:
                rand = random.randrange(0, len(hero_list))
                if rand == 0:
                    player.hero = Hero("Jarax", 30, 2, 3, 1, 4, "berzerk", "Brute", 999, 0)
                    player.deck = jarax_deck
                elif rand == 1:
                    player.hero = Hero("Hitler Nechromancer", 10, 0, 2, 4, 4, "raise_dead", "Adept", 12, 3)
                    player.deck = hitler_deck
                elif rand == 2:
                    player.hero = Hero("Stalin", 20, 0, 1, 1, 4, "beast_shape", "Adept", 11, 3)
                    player.deck = stalin_deck
                print(player.name, "randomized", player.hero.name)
                conn.send(str.encode("You have randomized " + player.hero.name + "\n"))
                break
            else:
                conn.send(str.encode("That is not a valid choice. Try again.\n"))
        except ValueError:
            conn.send(str.encode("That is not a valid choice. Try again.\n"))


def choose_num_heroes(conn):  # Needs to be rewritten to account for connection of new players
    while True:
        print("You can play up to 4 players at one time. How many players do you want?")
        conn.send(str.encode("You can play up to 4 players at one time. How many players do you want?"))
        try:
            num_heroes = int(handle_input(conn))
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


def show_player_list(conn, p_list):  # Needs to be rewritten to account for new players
    print("Player list:")
    for p in p_list:
        print(p.name)
        if p.hero is not "":
            print("Hero:", p.hero.name + "\n")
            conn.send(str.encode("Hero: " + p.hero.name + "\n"))
        else:
            print(p.name, "has not selected a Hero yet.\n")
            conn.send(str.encode(p.name + " has not selected a Hero yet.\n"))


def main_menu(conn):
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
        "Add Player": [5312, "Add Player", Connector.add_player]
    }

    # Should there be neutral deck choices?

    """Fix so that it traps player if incorrect input (too high number)"""
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
        dummy_handler = 0
        for val in menu_dict:
            if menu_dict[val][0] < 100:  # Doesn't show 'hidden' options (with arbitrarily high values)
                dummy_handler += 1
                if val.endswith("Hero"):
                    for obj in p_list:
                        if obj.hero == "":
                            print(str(menu_dict[val][0]) + ".", menu_dict[val][1])
                            conn.send(str.encode(str(menu_dict[val][0])+". "
                                                 + menu_dict[val][1] + "\n"))
                            print(obj.name, "added this to menu list.")
                        else:
                            print(str(menu_dict[val][0]) + ".", menu_dict[val][1],
                                  "\t- [x]\t", obj.hero.name)
                            conn.send(str.encode(str(menu_dict[val][0]) + ". " + str(menu_dict[val][1])
                                                 + "\t- [x]\t" + obj.hero.name + "\n"))
                            print(obj.name, "added this to menu list.")
                else:
                    print(str(menu_dict[val][0])+".", menu_dict[val][1])
                    conn.send(str.encode(str(menu_dict[val][0])+". " + menu_dict[val][1] + "\n"))
        try:
            usr_choice = int(handle_input(conn))
            if usr_choice > dummy_handler:
                conn.send(str.encode("That is not a valid menu choice. Try again.\n"))
                break

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
                                init_game(conn, p_list, map_choice)
                            else:
                                for p in p_list:
                                    if p.hero == "":
                                        print(p.name, "has not selected hero")
                                        conn.send(str.encode(p.name + " has yet to choose a hero!\n"))
                        else:
                            conn.send(str.encode("You have yet to choose a map!\n"))
                            print("Error: no map chosen")

                    elif val == "Player List":
                        menu_dict[val][2](conn, p_list)

                    elif val == "Map":
                        map_choice = menu_dict[val][2](conn)
                        print("map chosen is", map_choice)
                    elif menu_dict[val][2] is choose_hero:
                        # return_value = menu_dict[val][2]()
                        if val == "Player #1 Hero":
                            choose_hero(conn, player1)
                        elif val == "Player #2 Hero":
                            choose_hero(conn, player2)
                        elif val == "Player #3 Hero":
                            choose_hero(conn, player3)
                        elif val == "Player #4 Hero":
                            choose_hero(conn, player4)
                        else:
                            print("ended in else for resolution for choose hero")
                    elif val == "Num of Heroes":
                        return_value = menu_dict[val][2](conn)
                        p_list = [player1, player2]
                        if return_value >= 3:  # False alarm, return_val is always int for this choice
                            p_list.append(player3)
                            if return_value == 4:
                                p_list.append(player4)
                    elif val == "Add Player":
                        connecter.add_player()
                    else:
                        menu_dict[val][2]()
        except ValueError:
            print("ValueError in main_menu.")
            conn.send(str.encode("That is not a number. Please enter a valid menu choice.\n"))
        except TypeError:
            print("TypeError in main_menu.")


def init_game(conn, player_list, map_choice):
    print("I am the initiation!")

    # init_list = []

    shuffle_deck(neutral_deck)
    for player in player_list:
        player.shuffle_deck()
        # init = random.randrange(1, 6)
        # init_list.append(init)
        """init_list not used right now"""

    for player in player_list:
        player.draw_card()
        player.draw_card()
        player.draw_card()
        player.draw_card()
        for card in player.hand:
            conn.send(str.encode(player.name + " has drawn " + card.name + ".\n"))

    # for player in player_list:
        # choose start loc

        # draw 4 cards

    game_turn(conn, player_list, 0)


def game_turn(conn, player_list, turn_count):  # Also needs to receive map.
    while True:
        turn_count += 1
        print("\t\tTURN", turn_count)
        conn.sendall(str.encode("\t\tTURN " + str(turn_count) + "!\n"))

        """Make list contain all resolve effects (offer cards etc).
        Loop through, and when one action is done, delete (pop) from list
        Loop is broken if interrupted but will not replay events it should already have done"""

        """
        resolve_order = [offer_cards(player_list), draw_card, offer_cards(player_list), "maintenance",
                         offer_cards(player_list), "gain resources", offer_cards(player_list), "movement+attacks",
                         offer_cards(player_list), "resolve cards"]
        """

        for player in player_list:
            resolve_order = [draw_card, "maintenance", "generate_resources", "movementattacks", "resolve cards"]
            print("I have entered the turn order. Resolve order is:", resolve_order)
            conn.send(str.encode(player.name + ", it is your turn.\n"))
            conn.send(str.encode(player.name + ", you have " +
                                 str(player.hero.current_energy) + " " +
                                 player.hero.energy_type+".\n"))

            while len(resolve_order) > 0:
                print("It should be time for", player.name, "to", str(resolve_order[0]) + ".")
                if resolve_order[0] == draw_card:
                    player.draw_card()
                    print(player.name, "has drawn a card.")
                    conn.sendall(str.encode(player.name + " has drawn a card.\n"))

                elif resolve_order[0] == "generate_resources":
                    player.hero.generate_resources(conn, player)
                    print(player.name, "has generated resources.")
                    conn.sendall(str.encode(player.name + " has generated resources.\n"))

                elif type(resolve_order[0]) == str:
                    print("This is when", resolve_order[0], "should occur.")
                    conn.sendall(str.encode("This is when " + str(resolve_order[0]) + " should occur\n"))
                else:
                    print("I have entered the ELSE. Resolve order 0 is", resolve_order[0])

                time.sleep(1.3)
                resolve_order.pop(0)

            time.sleep(1.2)
            print("End of turn.")
            conn.sendall(str.encode("End of " + player.name + "'s turn.\n"))
            print(player.name, "currently has", player.hero.current_energy, player.hero.energy_type+".")
            print("")

        if turn_count != 1:
            print("It is not the first turn")

        if turn_count > 1:
            print("end of turn 2")
            break


def offer_cards(conn, player_list):
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
                inp = handle_input(conn)
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

"""
def handle_client(client):  # Takes client socket as argument.
    # Handles a single client connection.
    name = "billy"
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    client.sendall(str.encode(msg))
    clients[client] = name
    while True:
        msg = client.recv(2048)
        if msg != bytes("{quit}", "utf8"):
            client.sendall(str.encode(name + ": " + msg))
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            client.sendall(str.encode("%s has left the game." % name))
            break
"""


class Connector(Thread):
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, PORT))
            server.listen(1)
            print("Waiting for connection...")
            client, client_address = server.accept()
            print(client_address, "has joined.")
            with client:
                while True:
                    print("Player conn list:", clients)
                    main_menu(client)

    def add_player(self):
        print("I managed to enter additional player.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, 55554))
            print("I have bound myself.")
            server.listen(1)
            print("Waiting for connection...")
            client, client_address = server.accept()
            addresses[client] = client_address
            # clients.append(conn2)
            print(client_address, "has joined.")
            server.sendall(str.encode("Welcome," + client_address))
            # Thread(target=handle_client, args=(client,)).start()


clients = {}
addresses = {}
connecter = Connector()

connecter.start()


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
