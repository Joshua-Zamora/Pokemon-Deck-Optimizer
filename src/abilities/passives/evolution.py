from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class PokemonCanEvolveImmediatelyPassiveAbility(PassiveAbility):
    names: list[str] = ["Boosted Evolution"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, it can evolve during your first turn or the turn you play it."]

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard):
        return {"can_evolve_immediately": True} if self.can_activate(player, ability_owner) else {}


class PokemonCanUseAttacksFromPastEvolutionsPassiveAbility(PassiveAbility):
    names: list[str] = ["Memory Dive"]
    descriptions: list[str] = [
        "Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)"]

    def can_activate(self) -> bool:
        return True

    def activate(self):
        return {"use_past_evolutions": True} if self.can_activate() else {}
