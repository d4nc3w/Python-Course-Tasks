# Managing music band

class Musician:
    def __init__(self, firstName, lastName, instrument, role):
        self.firstName = firstName
        self.lastName = lastName
        self.instrument = instrument
        self.role = role

    def play(self):
        print(f"{self.firstName} {self.lastName} plays {self.instrument}.")

class Band:
    band = []
    def __init__(self, name):
        self.name = name

    def add_musician(self, musician):
        self.band.append(musician)

    def remove_musician(self, musician):
        self.band.remove(musician)

    def list_musicians(self):
        for musician in self.band:
            print(f"{musician.firstName} {musician.lastName}: {musician.instrument}")

    def play_music(self):
        for musician in self.band:
            musician.play()

piotr = Musician("Piotr", "Dancewicz", "Drums", "Drummer")
marta = Musician("Marta", "Kowalczyk", "Piano", "Pianist")
jakub = Musician("Jakub", "Czechanowski", "Guitar", "Guitarist")
andrzej = Musician("Andrzej", "Duda", "Violin", "Violinist")

piotr.play()
marta.play()
jakub.play()
andrzej.play()

duneGroup = Band("Kwizath")
duneGroup.add_musician(piotr)
duneGroup.add_musician(marta)
duneGroup.add_musician(jakub)
duneGroup.add_musician(andrzej)

duneGroup.remove_musician(andrzej)
duneGroup.list_musicians()

duneGroup.play_music()
