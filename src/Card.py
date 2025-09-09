
class Card:
    def __init__(self, name: str, card_type: str, hp: int, attacks: list, weaknesses: list, url: str):
        self.name = name
        self.card_type = card_type
        self.hp = hp
        self.attacks = attacks
        self.weaknesses = weaknesses
        self.url = url

