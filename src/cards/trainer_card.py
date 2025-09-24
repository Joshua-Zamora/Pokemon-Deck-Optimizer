from src.cards.card import Card


class TrainerCard(Card):
    def __init__(self, name: str, card_id: str, regulation_mark: str, trainer_type: str, effect_description: str):
        super().__init__(name, card_id, regulation_mark)
        self.trainer_type = trainer_type
        self.effect_description = effect_description
