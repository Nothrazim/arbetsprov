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

                  "\n3. Before active player's maintenance phase?"
                  "\n4. After active player's maintenance phase?"

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


player1 = Player("Alice")
player2 = Player("Bob")
player3 = Player("Charlie")
player4 = Player("Devon")
