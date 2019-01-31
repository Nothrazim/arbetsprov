import random


class Card:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


def shuffle_deck(deck):
    print("I have now shuffled the deck.")
    random.shuffle(deck)


def print_cards_in_deck(deck):
    print("\nList of cards in deck:")
    for card in deck:
        print(card.name)


def draw_card(hand, deck):
    randomized_card = random.randrange(0, len(deck)-1)
    hand.append(deck[randomized_card])
    print("i have drawn \"" + deck[randomized_card].name + "\"")
    deck.pop(randomized_card)


card_stalin_absolute_zero = Card("Absolute Zero", 5)  # destroy all creatures, exceptional
card_stalin_bear_arms = Card("Bear Arms",  3)
card_stalin_blessing_of_ice = Card("Blessing of Ice", 2)
card_stalin_cold_embrace = Card("Cold Embrace", 2)
card_stalin_cold_iron = Card("Cold Iron Weapons", 3)
card_stalin_consume_heat = Card("Consume Heat", 4)
card_stalin_dire_form = Card("Dire Form", 1)
card_stalin_double_strike = Card("Double Strike", 2)
card_stalin_frictionless = Card("Frictionless", 2)
card_stalin_frigid_transfixion = Card("Frigid Transfixion", 3)
card_stalin_frozen_field = Card("Frigid Field", 3)
card_stalin_harsh_winds = Card("Harsh Winds", 1)
card_stalin_ice_shards = Card("Ice Shards", 2)
card_stalin_northern_light = Card("Northern Light", 1)
card_stalin_nuclear_winter = Card("Nuclear Winter", 6)
card_stalin_primal_roar = Card("Primal Roar", 1)
card_stalin_purging_cold = Card("Purging Cold", 2)
card_stalin_quick_assault = Card("Quick Assault", 2)
card_stalin_savage_rend = Card("Savage Rend", 2)
card_stalin_sharpened_claws = Card("Sharpened Bear Claws", 2)
card_stalin_shatter = Card("Shatter", 1)
card_stalin_sweep_combo = Card("Sweep Strike Combo", 2)
card_stalin_whiteout = Card("Whiteout", 4)

card_stalin_aurora_chargeblade = Card("Aurora Chargeblade", 0)
card_stalin_crown_of_ice = Card("Crown of Ice", 0)
card_stalin_heart_of_winter = Card("Heart of Winter", 0)
card_stalin_ice_armor = Card("Ice Armor", 0)
card_stalin_leggings = Card("Leggings of the Northern Winds", 0)
card_stalin_motherlands_protection = Card("Motherland's Protection", 0)
card_stalin_pernach = Card("Pernach of the Motherland", 0)

card_jarax_fusion = Card("A fusion of Brass and Bones", 5)
card_jarax_blood_god = Card("Blood for the Blood God", 6)
card_jarax_blood_rain = Card("Blood Rain", 2)
card_jarax_forsworn = Card("Call upon the Forsworn", 0)
card_jarax_chosen = Card("Chosen of Chaos", 5)
card_jarax_cleave = Card("Cleave", 0)
card_jarax_dark_cabal = Card("Dark Cabal", 2)
card_jarax_dark_machinery = Card("Dark Machinery", 3)
card_jarax_dreadnought = Card("Deathwish Dreadnought", 4)
card_jarax_fire_from_sky = Card("Fire from the Sky", 4)
card_jarax_kyras = Card("Hand of the Warmaster", 4)
card_jarax_harvesters = Card("Harvesters", 2)
card_jarax_fist = Card("I CAST FIST!", 0)
card_jarax_juggernaut = Card("Juggernaut", 3)
card_jarax_lord_of_blood = Card("Lord of Blood", 0)
card_jarax_magic_weak = Card("Magic is for the Weak!", 2)
card_jarax_rampagers = Card("Rampagers", 3)
card_jarax_ritual_of_eight = Card("Ritual of Eight", 4)
card_jarax_sear_soul = Card("Sear the Soul", 2)
card_jarax_severing_blow = Card("Severing Blow", 0)
card_jarax_legion_moves = Card("The Legion Moves", 3)
card_jarax_to_the_hunt = Card("To the hunt!", 4)
card_jarax_unholy_engineering = Card("Unholy Engineering", 4)
card_jarax_hounds = Card("Unleash the Hounds", 3)
card_jarax_skull_don_throne = Card("Your skull will don the throne!", 0)

card_jarax_araghast = Card("Araghast", 0)
card_jarax_bloodforged_armor = Card("Bloodforged Armor", 0)
card_jarax_bloodthirster_helmet = Card("Bloodthirster Helmet", 0)
card_jarax_champions_greaves = Card("Champion's Greaves", 0)
card_jarax_soulstealer_hammer = Card("Soulstealer Hammer", 0)


jarax_deck = [card_jarax_araghast, card_jarax_blood_god, card_jarax_blood_rain, card_jarax_bloodforged_armor,
              card_jarax_bloodthirster_helmet, card_jarax_champions_greaves, card_jarax_chosen, card_jarax_cleave,
              card_jarax_dark_cabal, card_jarax_dark_machinery, card_jarax_dreadnought, card_jarax_fire_from_sky,
              card_jarax_fist, card_jarax_forsworn, card_jarax_fusion, card_jarax_harvesters, card_jarax_hounds,
              card_jarax_juggernaut, card_jarax_kyras, card_jarax_legion_moves, card_jarax_lord_of_blood,
              card_jarax_magic_weak, card_jarax_rampagers, card_jarax_ritual_of_eight, card_jarax_sear_soul,
              card_jarax_severing_blow, card_jarax_skull_don_throne, card_jarax_soulstealer_hammer,
              card_jarax_to_the_hunt, card_jarax_unholy_engineering]
stalin_deck = []
hitler_deck = []
neutral_deck = []


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
