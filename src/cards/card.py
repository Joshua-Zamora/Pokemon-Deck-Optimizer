from abc import ABC

class Card(ABC):
    def __init__(self, name: str, card_id: str, regulation_mark: str):
        self.name = name
        self.card_id = card_id
        self.regulation_mark = regulation_mark