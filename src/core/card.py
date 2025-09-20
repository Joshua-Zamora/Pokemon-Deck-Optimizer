class Card:
    def __init__(self, name: str, description: str, hp: int, evolves_from: str = None,
                 level: str = None, stage: str = None, abilities: list[str] = None, attacks: list[str] = None,
                 weaknesses: list[str] = None, resistances: list[str] = None, retreat: int = None,
                 effect: str = None, energyType: str = None,
                 regulationMark: str = None):