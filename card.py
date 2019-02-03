import random


class Card:
    def __init__(self, name, cost, card_type, effects=[]):
        self.name = name
        self.cost = cost
        self.card_type = card_type
        self.effects = effects


def shuffle_deck(deck):
    print("I have now shuffled the deck.")
    random.shuffle(deck)


def draw_card(hand, deck):
    print("I have now drawn a card.")
    hand.append(deck[0])
    print("i have drawn \"" + deck[0].name + "\"")
    deck.pop(0)


"""
Jarax
"""

card_jarax_blood_god = Card("Blood for the Blood God", 6, "Ability")
card_jarax_cleave = Card("Cleave", 0, "Ability")
card_jarax_fist = Card("I CAST FIST!", 0, "Ability")
card_jarax_juggernaut = Card("Juggernaut", 3, "Ability")
card_jarax_magic_weak = Card("Magic is for the Weak!", 2, "Ability")
card_jarax_sear_soul = Card("Sear the Soul", 2, "Ability")
card_jarax_severing_blow = Card("Severing Blow", 0, "Ability")
card_jarax_legion_moves = Card("The Legion Moves", 3, "Ability")
card_jarax_skull_don_throne = Card("Your skull will don the throne!", 0, "Ability")

card_jarax_fusion = Card("A fusion of Brass and Bones", 5, "Constant Hero")
card_jarax_hand_of_the_warmaster = Card("Hand of the Warmaster", 4, "Constant Hero")

card_jarax_blood_rain = Card("Blood Rain", 2, "Constant World")

card_jarax_lord_of_blood = Card("Lord of Blood", 0, "Constant Equipment")

card_jarax_forsworn = Card("Call upon the Forsworn", 0, "Summon")
card_jarax_chosen = Card("Chosen of Chaos", 5, "Summon")
card_jarax_dark_cabal = Card("Dark Cabal", 2, "Summon")
card_jarax_dark_machinery = Card("Dark Machinery", 3, "Summon")
card_jarax_dreadnought = Card("Deathwish Dreadnought", 4, "Summon")
card_jarax_fire_from_sky = Card("Fire from the Sky", 4, "Summon")
card_jarax_harvesters = Card("Harvesters", 2, "Summon")
card_jarax_rampagers = Card("Rampagers", 3, "Summon")
card_jarax_ritual_of_eight = Card("Ritual of Eight", 4, "Summon")
card_jarax_to_the_hunt = Card("To the hunt!", 4, "Summon")
card_jarax_unholy_engineering = Card("Unholy Engineering", 4, "Summon")
card_jarax_hounds = Card("Unleash the Hounds", 3, "Summon")

card_jarax_araghast = Card("Araghast", 0, "Equipment")
card_jarax_bloodforged_armor = Card("Bloodforged Armor", 0, "Equipment")
card_jarax_bloodthirster_helmet = Card("Bloodthirster Helmet", 0, "Equipment")
card_jarax_champions_greaves = Card("Champion's Greaves", 0, "Equipment")
card_jarax_soulstealer_hammer = Card("Soulstealer Hammer", 0, "Equipment")

jarax_deck = [card_jarax_araghast, card_jarax_blood_god, card_jarax_blood_rain, card_jarax_bloodforged_armor,
              card_jarax_bloodthirster_helmet, card_jarax_champions_greaves, card_jarax_chosen, card_jarax_cleave,
              card_jarax_dark_cabal, card_jarax_dark_machinery, card_jarax_dreadnought, card_jarax_fire_from_sky,
              card_jarax_fist, card_jarax_forsworn, card_jarax_fusion, card_jarax_harvesters, card_jarax_hounds,
              card_jarax_juggernaut, card_jarax_hand_of_the_warmaster, card_jarax_legion_moves,
              card_jarax_lord_of_blood, card_jarax_magic_weak, card_jarax_rampagers, card_jarax_ritual_of_eight,
              card_jarax_sear_soul, card_jarax_severing_blow, card_jarax_skull_don_throne,
              card_jarax_soulstealer_hammer, card_jarax_to_the_hunt, card_jarax_unholy_engineering]


"""
Stalin
"""

card_stalin_absolute_zero = Card("Absolute Zero", 5, "Ability", ["exceptional"])  # destroy all creatures, exceptional
card_stalin_bear_arms = Card("Bear Arms",  3, "Ability")
card_stalin_cold_embrace = Card("Cold Embrace", 2, "Ability")
card_stalin_consume_heat = Card("Consume Heat", 4, "Ability")
card_stalin_double_strike = Card("Double Strike", 2, "Ability")
card_stalin_frictionless = Card("Frictionless", 2, "Ability")
card_stalin_frigid_transfixion = Card("Frigid Transfixion", 3, "Ability")
card_stalin_harsh_winds = Card("Harsh Winds", 1, "Ability")
card_stalin_ice_shards = Card("Ice Shards", 2, "Ability")
card_stalin_northern_light = Card("Northern Light", 1, "Ability")
card_stalin_nuclear_winter = Card("Nuclear Winter", 6, "Ability")
card_stalin_primal_roar = Card("Primal Roar", 1, "Ability", ["quick"])
card_stalin_purging_cold = Card("Purging Cold", 2, "Ability")
card_stalin_quick_assault = Card("Quick Assault", 2, "Ability")
card_stalin_savage_rend = Card("Savage Rend", 2, "Ability")
card_stalin_shatter = Card("Shatter", 1, "Ability")
card_stalin_sweep_combo = Card("Sweep Strike Combo", 2, "Ability")
card_stalin_whiteout = Card("Whiteout", 4, "Ability")

card_stalin_blessing_of_ice = Card("Blessing of Ice", 2, "Constant Hero", ["exceptional"])
card_stalin_cold_iron = Card("Cold Iron Weapons", 3, "Constant Hero")
card_stalin_dire_form = Card("Dire Form", 1, "Constant Hero")
card_stalin_sharpened_claws = Card("Sharpened Bear Claws", 2, "Constant Hero")

card_stalin_frozen_field = Card("Frigid Field", 3, "Constant World")

card_stalin_aurora_chargeblade = Card("Aurora Chargeblade", 0, "Equipment")
card_stalin_crown_of_ice = Card("Crown of Ice", 0, "Equipment")
card_stalin_heart_of_winter = Card("Heart of Winter", 0, "Equipment")
card_stalin_ice_armor = Card("Ice Armor", 0, "Equipment")
card_stalin_leggings = Card("Leggings of the Northern Winds", 0, "Equipment")
card_stalin_motherlands_protection = Card("Motherland's Protection", 0, "Equipment")
card_stalin_pernach = Card("Pernach of the Motherland", 0, "Equipment")


stalin_deck = [card_stalin_absolute_zero, card_stalin_bear_arms, card_stalin_blessing_of_ice,
               card_stalin_cold_embrace, card_stalin_cold_iron, card_stalin_consume_heat, card_stalin_dire_form,
               card_stalin_double_strike, card_stalin_frictionless, card_stalin_frigid_transfixion,
               card_stalin_frozen_field, card_stalin_harsh_winds, card_stalin_ice_shards,
               card_stalin_northern_light, card_stalin_nuclear_winter, card_stalin_primal_roar,
               card_stalin_purging_cold, card_stalin_quick_assault, card_stalin_savage_rend,
               card_stalin_sharpened_claws, card_stalin_shatter, card_stalin_sweep_combo, card_stalin_whiteout,
               card_stalin_aurora_chargeblade, card_stalin_crown_of_ice, card_stalin_heart_of_winter,
               card_stalin_ice_armor, card_stalin_leggings, card_stalin_motherlands_protection, card_stalin_pernach]


"""
Hitler
poor Hitler has no cards of his own :(
"""

hitler_deck = [card_jarax_araghast, card_jarax_blood_god, card_jarax_blood_rain, card_jarax_bloodforged_armor,
               card_jarax_bloodthirster_helmet, card_jarax_champions_greaves, card_jarax_chosen, card_jarax_cleave,
               card_jarax_dark_cabal, card_jarax_dark_machinery, card_jarax_dreadnought, card_jarax_fire_from_sky,
               card_jarax_fist, card_jarax_forsworn, card_jarax_fusion, card_jarax_harvesters, card_jarax_hounds,
               card_jarax_juggernaut, card_jarax_hand_of_the_warmaster, card_jarax_legion_moves,
               card_jarax_lord_of_blood, card_jarax_magic_weak, card_jarax_rampagers, card_jarax_ritual_of_eight,
               card_jarax_sear_soul, card_jarax_severing_blow, card_jarax_skull_don_throne,
               card_jarax_soulstealer_hammer, card_jarax_to_the_hunt, card_jarax_unholy_engineering]


"""
Neutral
"""

card_neutral_cosmic_reshaping = Card("Cosmic Reshaping", 0, "Ability")
card_neutral_dark_summons = Card("Dark Summons", 0, "Summon")
card_neutral_deja_vu = Card("Deja Vu", 0, "Ability")
card_neutral_how_quickly = Card("How Quickly The Tide Turns!", 0, "Ability")

card_neutral_boots_of_speed = Card("Botos of Speed", 0, "Equipment")
card_neutral_chargecoil_boots = Card("Chargecoil Boots", 0, "Equipment")
card_neutral_crown_of_alternate_realities = Card("Crown of Alternate Realities", 0, "Equipment")
card_neutral_discharge_vest = Card("Discharge Vest", 0, "Equipment")
card_neutral_dwarven_sabatons = Card("Dwarven Sabatons", 0, "Equipment")
card_neutral_hatemail = Card("Hatemail", 0, "Equipment")
card_neutral_lifereaver = Card("Lifereaver", 0, "Equipment")

neutral_deck = [card_neutral_cosmic_reshaping, card_neutral_dark_summons, card_neutral_deja_vu,
                card_neutral_how_quickly, card_neutral_boots_of_speed, card_neutral_chargecoil_boots,
                card_neutral_crown_of_alternate_realities, card_neutral_discharge_vest, card_neutral_dwarven_sabatons,
                card_neutral_hatemail, card_neutral_lifereaver]


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
