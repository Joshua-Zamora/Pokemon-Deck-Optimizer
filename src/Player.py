class Player:
    def __init__(self, name, deck):
        self.name = name
        self.__deck = deck

    def get_deck(self):
        return self.__deck