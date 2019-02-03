import random

class Player:
    def __init__(self, name, hero=""):
        self.name = name
        self.hero = hero
        self.deck = []
        self.hand = []
        self.discard = []

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        self.hand.append(self.deck.pop(0))

    def print_cards_in_deck(self):
        for card in self.deck:
            print(card.name)

    def print_cards_in_hand(self):
        for card in self.hand:
            print("Cost:", str(card.cost), "\t", card.name)

    def look_at_deck(self, card_num):
        print(self.name, "is looking at the top", card_num, "card(s) of a deck.")
        to_look_at = []
        for i in range(0, card_num):
            to_look_at.append(self.deck[i])
        for card in to_look_at:
            print(card.name)

    def card_effect_quick(self):
        while True:
            choice = 0
            print("Do you want the card to take place:"
                  "\n1. Before active player card draw?"
                  "\n2. After active player card draw?"

                  "\n3. Before active player's maintainance phase?"
                  "\n4. After active player's maintainance phase?"

                  "\n5. Before active player's resource phase?"
                  "\n6. After active player's resource phase?"

                  "\n7. Before active player's action phase?"
                  "\n8. Before active player's action phase?")
            try:
                choice = int(input())
            except ValueError:
                print("I could not understand that.")
            if choice > 0:
                if choice < 9:
                    return choice
                else:
                    print("Select a valid number.")
            else:
                print("Select a valid number.")

    def choose_card(self):
        # while True:
        hand_dict = {}
        hand_dict.clear()
        hand_dict = {
            "no card": [1, "Do not play any cards"]
        }
        x = 1
        for card in self.hand:
            x += 1
            hand_dict[card] = x, card.name

        for thing in hand_dict:
            if thing == "no card":
                print(str(hand_dict[thing][0])+".", hand_dict[thing][1])
            else:
                print(str(hand_dict[thing][0])+".", thing.name)

        try:
            usr_choice = int(input())

            for val in hand_dict:
                if usr_choice == hand_dict[val][0]:
                    if val == "no card":
                        print("no")
                    else:
                        print("You have chosen to play", val.name+".")
                        return val

        except ValueError:
            print("Please enter a number.")

        """
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

            # Clear screen needed
            for val in menu_dict:
                # print(menu_dict[val])
                if menu_dict[val][0] < 100:  # Doesn't show 'hidden' options (with arbitrarily high values)
                    print(str(menu_dict[val][0]) + ".", menu_dict[val][1])
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
            """

player1 = Player("Alice")
player2 = Player("Bob")
player3 = Player("Charlie")
player4 = Player("Devon")
