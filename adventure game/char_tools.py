from functions import save_json, load_json

classnames = {"wizard": {"special": "magic"}, "warrior": {"special": "strength"}, "archer": {"special": "ranged"}}
class Character:

    def __init__(self, name=None, classrole=None):
        self.name = name
        self.classrole = classrole
        self.xp = 1

    def calc_level(self):
        self.level = self.xp//10 + 1

    def save(self):
        return save_json("saves/characters.JSON", {self.name: {"classrole": self.classrole, "xp": self.xp}})

    def load(self, name):
        this_char =  load_json("saves/characters.JSON", name)
        self.name = name
        self.classrole = this_char["classrole"]
        self.xp = this_char["xp"]
        self.calc_level()
        return self

class ClassRole:
    def __init__(self, name):
        self.name = name
        self.special = classnames[name]["special"]