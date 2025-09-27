from src.abilities.base import TriggerAbility
from src.cards.pokemon_card import PokemonCard
from src.cards.trainer_card import TrainerCard
from src.core.game import Game
from src.core.player import Player


class AddDamageToPoisonedPokemonTriggerAbility(TriggerAbility):
    def __init__(self, name:str, description:str, damage_counters: int):
        super().__init__(name, description)
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game, player: Player) -> bool:
        return player.opponent.pokemon[0].afflictions["poisoned"] and game_state.in_pokemon_checkup

    def activate(self, game_state: Game, player: Player):
        if self.can_activate(game_state, player):
            player.opponent.pokemon[0].damage_counters_attached += self.damage_counters


class PreventAllEffectsOnSupportCardPlayedTriggerAbility(TriggerAbility):
    def __init__(self, name:str, description:str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(player, ability_owner):
            player.opponent.supporter_effects_mitigated = True