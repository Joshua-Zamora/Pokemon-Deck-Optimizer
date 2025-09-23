from cards.card import Card


class EnergyCard(Card):
    def __init__(self, name: str, card_id: str, regulation_mark: str, energy_type: str):
        super().__init__(name, card_id, regulation_mark)
        self.energy_type = energy_type