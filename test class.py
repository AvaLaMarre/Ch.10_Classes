class Character:
    def __init__(self, name, planet):
        self.name = name
        self.home = planet

    def fight(self):
        print("Lightsaber on, says " + self.name)


class Jedi(Character):
    def force_hug(self):
        print("Feel the love force, says " + self.name)

    def fight(self):
        super().fight()
        print("Come to the Light Side, says " + self.name)


class Sith(Character):
    def __int__(self, name, planet, apprentice):
        super().__init__(name, planet)
        self.apprentice = apprentice

    def force_choke(self):
        print("Dont choke on your words, says " + self.name)

    def fight(self):
        super().fight()
        print("Come to the Dark Side, says" + self.name)


jedi = Jedi("Luke", "Tatoine")
sith = Sith("Darth Mal", "Dathomir", "Savage")

jedi.fight()
sith.fight()
jedi.force_hug()
sith.force_choke()
print()
print("This object that we just created was " + jedi.name + ". From the planet " + jedi.home)
print("This object that we just created was " + sith.name + ". From the planet " + sith.home)
print(sith.name + "Has an apprentice called " + sith.apprentice)
