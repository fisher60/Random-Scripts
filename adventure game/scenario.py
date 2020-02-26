from functions import load_json, clear, print_choices
from random import choice


class Map:


    def __init__(self, name):
        map_data = load_json("static/maps.JSON", name)
        self.name = name
        self.npcs = load_json("static/npcs.JSON", self.name)
        self.special = None
        self.locations = map_data["locations"]
        self.passive = map_data["passive"]





class Encounter:

    def __init__(self, map_object):
        self.npc = None
        self.in_combat = False
        self.hp = None
        self.current_location = None
        self.map = map_object
        self.stage_count = 0

    def start_encounter(self):
        self.stage_count += 1
        location_choice = print_choices('Where would you like to go?', self.map.locations)
        clear()
        self.next_encounter(location_choice)

    def next_encounter(self, location_in_map=None):
        if self.map.passive is True:
            npcs = list(self.map.npcs.keys()) if location_in_map is None else [x for x in self.map.npcs.keys() if location_in_map in self.map.npcs[x]["locations"]]
            npc_choice = print_choices('Who would you like to talk to?', npcs)
            clear()

            options = []
            if self.map.npcs[npc_choice]["trade"] == True:
                options = self.map.npcs[npc_choice]["trade_options"]
            if self.map.npcs[npc_choice]["quest"] == True:
                options.append(choice(self.map.npcs[npc_choice]["quests"]))
            interaction_choice = print_choices(choice(self.map.npcs[npc_choice]["dialogue"]), options)


        else:
            pass

    def start_trade(self):
        pass

    def start_combat(self):
        pass


def start_scenario(player):


    map_data = load_json("static/maps.JSON")

    options = [x for x in map_data if map_data[x]["min_level"] <= player.level]
    print("player level: ", player.level)
    map_decision = print_choices('Where would you like to travel?', options)
    clear()
    this_map = Map(map_decision)
    this_encounter = Encounter(this_map)
    this_encounter.start_encounter()
