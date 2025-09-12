from src.Card import Card

class Player:
    prize_cards: list[Card] = []
    hand: list[Card] = []
    bench: list[Card] = []
    active_spot: Card | None = None
    discard_pile: list[Card] = []
    opponent = None


    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.__original_deck = deck[:]


    def reset_player_state(self):
        self.prize_cards = []
        self.hand = []
        self.bench = []
        self.active_spot = None
        self.discard_pile = []
        self.deck = self.__original_deck[:]


    def draw_card(self):
        self.hand.append(self.deck.pop(0))


    def attack(self, player):
        pass


    def prepare_for_sudden_death(self):
        self.prize_cards = [self.deck.pop(0)]


    def set_prize_cards(self):
        for i in range(6):
            self.prize_cards.append(self.deck.pop(0))