from src.abilities.actives.active_ability import ActiveAbility


class MoveEnergyActiveAbility(ActiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def activate(self, game_state, source: str, target: str = "", amount: int = 1):
        game_state.player_one.move_energy(source, target, "energy", amount)

class AttachEnergyActiveAbility(ActiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def activate(self, game_state):
        pass


