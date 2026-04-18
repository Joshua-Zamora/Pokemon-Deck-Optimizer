from cards.abilities.passives.board import OpponentCantGetCardsFromDiscardPilePassiveAbility, \
    PokemonMayUseAttackTwicePassiveAbility, OpponentCantPlayAceSpecCardsIfToolAttachedPassiveAbility
from cards.abilities.passives.evolution import PokemonCanUseAttacksFromPastEvolutionsPassiveAbility
from abilities.triggers.affliction import FlipExtraCoinIfAsleepTriggerAbility
from abilities.triggers.board import TakeOneFewerPrizeCardOnKnockoutTriggerAbility, \
    DiscardFromHandOnKnockoutTriggerAbility, SearchDeckForCardTriggerAbility, SearchDeckForCardOnKnockoutTriggerAbility
from abilities.triggers.damage import HealDuringPokemonCheckupTriggerAbility, \
    ApplyDamageDuringPokemonCheckupTriggerAbility, ApplyDamageToBasicPokemonDuringPokemonCheckupTriggerAbility, \
    ApplyDamageToPokemonWithAbilityDuringPokemonCheckupTriggerAbility, \
    ApplyDamageToBurnedPokemonDuringPokemonCheckupTriggerAbility, PreventDamageOnAttackedTriggerAbility, \
    PreventDamageIfSameEnergyAsOpponentTriggerAbility, DamageAttackingPokemonOnAttackedTriggerAbility
from abilities.triggers.energy import MaySwitchOnEnergyAttachedTriggerAbility
from abilities.triggers.health import PreventKnockOutTriggerAbility
from cards.abilities.actives.damage import *
from cards.abilities.actives.energy import *
from cards.abilities.passives.ability import BasicPokemonInPlayHaveNoAbilities, \
    PokemonWIthRuleBoxHaveNoAbilitiesExceptFuture, OpponentsActivePokemonHaveNoAbilitiesPassiveAbility, \
    PokemonWithDamageHaveNoAbilitiesPassiveAbility, BenchedStageTwoPokemonHaveNoAbilitiesPassiveAbility
from cards.abilities.passives.board import LimitNumberOfOpponentBenchedPokemonPassiveAbility, \
    OpponentCantPlayItemCardsPassiveAbility, OpponentCantPlayItemCardsOrToolsPassiveAbility, \
    CantPlayPokemonWithAbilityExceptForPassiveAbility, OpponentCantPlayStadiumCardsPassiveAbility
from cards.abilities.passives.damage import *
from cards.abilities.passives.damage import IncreasePokemonAttackDamageForPokemonPassiveAbility
from cards.abilities.passives.energy import *
from cards.abilities.passives.evolution import PokemonCanEvolveImmediatelyPassiveAbility
from cards.abilities.passives.health import *
from cards.abilities.passives.affliction import *
from src.abilities.triggers.affliction import AddDamageToPoisonedPokemonTriggerAbility, \
    PreventAllEffectsOnSupportCardPlayedTriggerAbility
from src.abilities.triggers.damage import HealWhenAttachingEnergyTriggerAbility

abilities = {
    "All of your Pokémon in play get +40 HP. The effect of Vibrant Dance doesn't stack.":
        IncreaseAllPokemonHealthPassiveAbility(40),
    "All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).":
        DecreaseOpponentAttackDamagePassiveAbility(10),
    "All of your Pokémon that have any {M} Energy attached take 20 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).":
        DecreaseOpponentAttackDamageOnEnergiesAttachedPassiveAbility("metal", 20),
    "All of your Pokémon that have {M} Energy attached have no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("metal"),
    "All of your Pokémon that have {P} Energy attached have no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("psychic"),
    "Apply Weakness for your opponent's Active Pokémon as ×4 instead.":
        WeaknessStrengthModifierOnOpponentsActivePassiveAbility(4),
    "As long as this Pokémon has a Future Booster Energy Capsule attached, it is {F} and {M} type.":
        ChangePokemonEnergyTypeIfToolAttachedPassiveAbility(["fighting", "metal"], "Future Booster Energy Capsule"),
    "As long as this Pokémon is in play, it is {G} and {R} type.":
        ChangePokemonEnergyTypePassiveAbility(["grass", "fire"]),
    "As long as this Pokémon is in the Active Spot, Basic Pokémon in play (both yours and your opponent's) have no Abilities, except for Mischievous Lock.":
        BasicPokemonInPlayHaveNoAbilities(pokemon_exception="mischievous lock"),
    "As long as this Pokémon is in the Active Spot, Pokémon with a Rule Box in play (both yours and your opponent's) have no Abilities, except for Future Pokémon. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)":
        PokemonWIthRuleBoxHaveNoAbilitiesExceptFuture(),
    "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost {C} more.":
        IncreaseOpponentAttackCostPassiveAbility(["colorless", 1]),
    "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance).":
        DecreaseOpponentAttackDamageIfActivePassiveAbility(20),
    "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Basic Pokémon cost {C} more.":
        IncreaseOpponentAttackCostOfBasicPokemonPassiveAbility(["colorless", 1]),
    "As long as this Pokémon is in the Active Spot, it can evolve during your first turn or the turn you play it.":
        PokemonCanEvolveImmediatelyPassiveAbility(),
    "As long as this Pokémon is in the Active Spot, prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon.":
        MitigateAllBenchDamagePassiveAbility(),
    "As long as this Pokémon is in the Active Spot, put 5 more damage counters on your opponent's Poisoned Pokémon during Pokémon Checkup.":
        AddDamageToPoisonedPokemonTriggerAbility(5),
    "As long as this Pokémon is in the Active Spot, whenever you attach an Energy card from your hand to 1 of your Pokémon, heal 90 damage from that Pokémon.":
        HealWhenAttachingEnergyTriggerAbility(9),
    "As long as this Pokémon is in the Active Spot, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to all of your Pokémon.":
        PreventAllEffectsOnSupportCardPlayedTriggerAbility(),
    "As long as this Pokémon is in the Active Spot, your opponent can't have more than 3 Benched Pokémon. If they have 4 or more Benched Pokémon, they discard Benched Pokémon until they have 3 Pokémon on the Bench. If more than one effect changes the number of Benched Pokémon allowed, use the smaller number.": LimitNumberOfOpponentBenchedPokemonPassiveAbility(3),
    "As long as this Pokémon is in the Active Spot, your opponent can't play any Item cards from their hand.":
        OpponentCantPlayItemCardsPassiveAbility(),
    "As long as this Pokémon is in the Active Spot, your opponent can't play any Item cards or Pokémon Tool cards from their hand.":
        OpponentCantPlayItemCardsOrToolsPassiveAbility(),
    "As long as this Pokémon is in the Active Spot, your opponent can't play any Pokémon that has an Ability from their hand, except for Team Rocket's Pokémon.":
        CantPlayPokemonWithAbilityExceptForPassiveAbility("team rocket"),
    "As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand.":
        OpponentCantPlayStadiumCardsPassiveAbility(),
    "As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon can't retreat.":
        OpponentsActivePokemonCantRetreatPassiveAbility(),
    "As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon has no Abilities, except for Midnight Fluttering.":
        OpponentsActivePokemonHaveNoAbilitiesPassiveAbility("midnight fluttering"),
    "As long as this Pokémon is in the Active Spot, your opponent's Pokémon in play that have any damage counters on them have no Abilities, except for Pokémon ex.":
        PokemonWithDamageHaveNoAbilitiesPassiveAbility("ex"),
    "As long as this Pokémon is on your Bench, Benched Stage 2 Pokémon (both yours and your opponent's) have no Abilities.":
        BenchedStageTwoPokemonHaveNoAbilitiesPassiveAbility(),
    "As long as this Pokémon is on your Bench, all of your Steven's Pokémon take 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Stone Palace doesn't stack.":
        DecreaseOpponentAttackDamageIfOnBenchPassiveAbility(30, "steven"),
    "As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(30, pokemon_restriction="marowak"),
    "As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon.":
        MitigateAllDamageToPokemonPassiveAbility(),
    "As long as this Pokémon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon.":
        MitigateAllDamageAndEffectsToPokemonPassiveAbility(),
    "As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is {C}{C} less.":
        DecreaseRetreatCostIfOnBenchPassiveAbility(2, "colorless"),
    "As long as you have at least 1 other Bouffalant in play, all of your Basic {C} Pokémon take 60 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Curly Wall doesn't stack.":
        DecreaseOpponentAttackDamageOnBasicPokemonIfPokemonInPlayPassiveAbility(60, "bouffalant"),
    "As often as you like during your turn, you may attach a Basic {L} Energy card from your hand to 1 of your Iono's Pokémon.":
        AttachEnergyFromHandActiveAbility("lightning", 1, "iono"),
    "As often as you like during your turn, you may attach a Basic {P} Energy card from your discard pile to 1 of your {P} Pokémon. If you attached Energy to a Pokémon in this way, put 2 damage counters on that Pokémon. You can't use this Ability on a Pokémon that would be Knocked Out.":
        AttachEnergyFromDiscardPileWithDamageActiveAbility("psychic", 1, 2),
    "As often as you like during your turn, you may attach a Basic {R} Energy card from your hand to 1 of your Pokémon.":
        AttachEnergyFromHandActiveAbility("fire", 1),
    "As often as you like during your turn, you may attach a Basic {W} Energy card from your hand to 1 of your Pokémon.":
        AttachEnergyFromHandActiveAbility("water", 1),
    "As often as you like during your turn, you may move 1 damage counter from 1 of your Team Rocket's Pokémon to another of your Pokémon.":
        MoveDamageCounterToPokemonActiveAbility(1, "Team Rocket"),
    "As often as you like during your turn, you may move 1 damage counter from 1 of your other Pokémon to this Pokémon.":
        GetDamageCounterFromPokemonActiveAbility(1),
    "As often as you like during your turn, you may move a {R} Energy from 1 of your Benched Pokémon to your Active Pokémon.":
        MoveEnergyFromBenchToActiveActiveAbility("fire", 1),
    "Attacks used by this Pokémon cost {C} less for each Kofu card in your discard pile.":
        AttacksCostLessForCardInDiscardPilePassiveAbility("colorless", 1, "kofu"),
    "Attacks used by this Pokémon cost {C} less for each of your opponent's Benched Pokémon.":
        AttacksCostLessForEachOpponentBenchedPokemonPassiveAbility("colorless", 1),
    "Attacks used by this Pokémon do 50 more damage to your opponent's Active Pokémon that has an Ability (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageIfOpponentHasAbilityPassiveAbility(50),
    "Attacks used by your Cynthia's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(30, pokemon_restriction="cynthia"),
    "Attacks used by your Evolution {R} Pokémon do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(10, ["fire"]),
    "Attacks used by your Future Pokémon, except any Iron Crown ex, do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(20, pokemon_exception="iron crown"),
    "Attacks used by your Hop's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack.":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(30, pokemon_restriction="hop", doesnt_stack=True),
    "Attacks used by your Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(20),
    "Attacks used by your Pokémon do 30 more damage to your opponent's Active Evolution Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(30, against_evolved=True),
    "Attacks used by your {G} Pokémon and {R} Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreasePokemonAttackDamageForPokemonPassiveAbility(20, ["grass", "fire"]),
    "Basic Pokémon V in play (both yours and your opponent's) have no Abilities.":
        BasicPokemonInPlayHaveNoAbilities(pokemon_restriction="v"),
    "Blood Moon used by this Pokémon costs {C} less for each Prize card your opponent has taken.":
        AttackCostsLessForEachPrizeCardTakenPassiveAbility("colorless", 1, "blood-moon"),
    "Cards in your opponent's discard pile can't be put into their hand by an effect of your opponent's Abilities or Trainer cards.":
        OpponentCantGetCardsFromDiscardPilePassiveAbility(),
    "Damage from attacks used by this Pokémon isn't affected by any effects on your opponent's Active Pokémon.":
        OpponentEffectsNegatedFromAttackDamagePassiveAbility(),
    "During Pokémon Checkup, heal 20 damage from each of your Pokémon.":
        HealDuringPokemonCheckupTriggerAbility(2),
    "During Pokémon Checkup, if this Pokémon is in the Active Spot, put 1 damage counter on your opponent's Active Pokémon.":
        ApplyDamageDuringPokemonCheckupTriggerAbility(1),
    "During Pokémon Checkup, if this Pokémon is in the Active Spot, put 2 damage counters on each of your opponent's Basic Pokémon.":
        ApplyDamageToBasicPokemonDuringPokemonCheckupTriggerAbility(2),
    "During Pokémon Checkup, put 1 damage counter on each Pokémon that has an Ability (both yours and your opponent's), except any Froslass.":
        ApplyDamageToPokemonWithAbilityDuringPokemonCheckupTriggerAbility(1, "froslass"),
    "During Pokémon Checkup, put 3 more damage counters on your opponent's Burned Pokémon.":
        ApplyDamageToBurnedPokemonDuringPokemonCheckupTriggerAbility(3),
    "During your turn, if this Pokémon is on your Bench, whenever you attach an Energy card from your hand to this Pokémon, you may switch it with your Active Pokémon.":
        MaySwitchOnEnergyAttachedTriggerAbility(),
    "Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)":
        PokemonCanUseAttacksFromPastEvolutionsPassiveAbility(),
    "If Festival Grounds is in play, this Pokémon may use an attack it has twice. If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.":
        PokemonMayUseAttackTwicePassiveAbility(),
    "If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.":
        PreventDamageOnAttackedTriggerAbility(),
    "If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon.":
        PreventDamageIfSameEnergyAsOpponentTriggerAbility(),
    "If this Pokémon has 2 or more damage counters on it, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreaseDamageOnNumDamageCountersAttachedPassiveAbility(2, 120),
    "If this Pokémon has 3 or more {M} Energy attached, it gets +100 HP.":
        IncreaseHealthIfEnergyAttachedPassiveAbility("metal", 3, 100),
    "If this Pokémon has a Pokémon Tool attached, your opponent can't play any ACE SPEC cards from their hand.":
        OpponentCantPlayAceSpecCardsIfToolAttachedPassiveAbility(),
    "If this Pokémon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).":
        IncreaseDamageResistanceIfAnyEnergyAttachedPassiveAbility(30),
    "If this Pokémon has any Special Energy attached, it gets +100 HP.":
        IncreaseHealthIfEnergyAttachedPassiveAbility("special", 1, 100),
    "If this Pokémon has any {D} Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.":
        PreventDamageOnAttackedTriggerAbility("darkness"),
    "If this Pokémon has any {D} Energy attached, it gets +100 HP, and the attacks it uses do 100 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).":
        IncreaseHealthIfEnergyAttachedPassiveAbility("darkness", 1, 100, 100),
    "If this Pokémon has any {L} Energy attached, it has no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("lightning", True),
    "If this Pokémon has any {P} Energy attached, it has no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("psychic", True),
    "If this Pokémon has any {R} Energy attached, it has no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("fire", True),
    "If this Pokémon has any {W} Energy attached, it has no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("water", True),
    "If this Pokémon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10.":
        PreventKnockOutTriggerAbility(10),
    "If this Pokémon has full HP, it takes 80 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).":
        DecreaseOpponentAttackDamageIfFullHPPassiveAbility(80),
    "If this Pokémon has no Energy attached, it has no Retreat Cost.":
        NoRetreatCostForEnergyTypePokemonPassiveAbility("none", True),
    "If this Pokémon is Asleep, flip 2 coins instead of 1 during Pokémon Checkup. If either of them is tails, this Pokémon is still Asleep.":
        FlipExtraCoinIfAsleepTriggerAbility(),
    "If this Pokémon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage.":
        PreventDamageOnAttackedTriggerAbility(affliction="confused"),
    "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card.":
        TakeOneFewerPrizeCardOnKnockoutTriggerAbility("pecharunt ex"),
    "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, discard 2 random cards from your opponent's hand.":
        DiscardFromHandOnKnockoutTriggerAbility(2),
    "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck.":
        SearchDeckForCardOnKnockoutTriggerAbility(),
    "If this Pokémon is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon for each {M} Energy attached to this Pokémon.":
        DamageAttackingPokemonOnAttackedTriggerAbility(2, "metal"),
    "If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, flip a coin. If heads, the Attacking Pokémon is Knocked Out.": ["Let's Have a Blast"],
    "If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 2 {W} Energy cards from this Pokémon to 1 of your Benched Pokémon.": ['Fillet Memento'],
    "If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, put 6 damage counters on the Attacking Pokémon.": ['Exploding Needles'],
    "If this Pokémon is in the Active Spot and is Knocked Out, flip a coin. If heads, your opponent takes 1 fewer Prize card.": ['Evanescent'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), discard an Energy from the Attacking Pokémon.": ['Counterattacking Pincer'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon for each of your Tandemaus, Maushold, and Maushold ex in play.": ['Solidarity'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.": ['Counterattack Quills', 'Counterattack', 'Automated Combat'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), search your deck for up to 2 Pokémon that have \"Koffing\" in their name and put them onto your Bench. Then, shuffle your deck.": ['Smog Signals'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Burned.": ['Incandescent Body', 'Scorching Armor'],
    "If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.": ['Poison Point'],
    "If this Pokémon is in the Active Spot, has a Pokémon Tool attached, and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 5 damage counters on the Attacking Pokémon.": ['Custom Trap'],
    "If this Pokémon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pokémon is not Knocked Out, and its remaining HP becomes 10.": ['Guts'],
    "If you go first, this Pokémon can use attacks during your first turn.": ['Debut Performance'],
    "If you go second, this Pokémon can evolve during your first turn.": ['Evolutionary Advantage'],
    "If you have Karrablast in play, this Pokémon can evolve during your first turn or the turn you play it.": ['Stimulated Evolution'],
    "If you have Nidoqueen in play, ignore all Energy in the costs of attacks used by this Pokémon.": ['Enthusiastic King'],
    "If you have Plusle in play, whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon. The effect of Buddy Pulse doesn't stack.": ['Buddy Pulse'],
    "If you have Shelmet in play, this Pokémon can evolve during your first turn or the turn you play it.": ['Stimulated Evolution'],
    "If you have Simisage, Simisear, and Simipour in play, ignore all {C} Energy in the costs of attacks used by this Pokémon.": ['Monkey Trio'],
    "If you have Solrock in play, prevent all effects of any Stadium done to your Pokémon in play.": ['New Moon'],
    "If you have any Tera Pokémon in play, this Pokémon can use the Double-Edge attack for {P}.": ['Glistening Bubbles'],
    "If you have the same number of cards in your hand as your opponent, ignore all Energy in the cost of Frightening Howl used by this Pokémon.": ['Tuning Echo'],
    "If you took this Pokémon as a face-down Prize card during your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench. If you put this Pokémon onto your Bench in this way, flip a coin. If heads, take 1 more Prize card.": ['Lucky Bonus'],
    "If your opponent has any cards in their discard pile that have \"Colress\" in the name, this Pokémon can use the Trifrost attack for {C}.": ['Plasma Bane'],
    "If your opponent has no Pokémon ex or Pokémon V in play, this Pokémon can't attack.": ['Born to Slack'],
    "If your opponent's Basic Pokémon is Knocked Out by damage from an attack used by this Pokémon, take 1 more Prize card.": ['Greedy Eater'],
    "Once at the end of your turn (after your attack), if this Pokémon is in the Active Spot, you must discard the top 5 cards of your deck.": ['Quaking Demolition'],
    "Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 8 cards in your hand.": ['Precious Gift'],
    "Once during your first turn, if this Pokémon is in the Active Spot, you may search your deck and choose a Basic Pokémon you find there, except any Ditto. If you do, discard this Pokémon and all attached cards, and put the chosen Pokémon in its place. Then, shuffle your deck.": ['Transformative Start'],
    "Once during your first turn, you may discard your hand and draw 6 cards. You can't use more than 1 Squawk and Seize Ability during your turn.": ['Squawk and Seize'],
    "Once during your first turn, you may search your deck for up to 3 {C} Pokémon with 100 HP or less, reveal them, and put them into your hand. Then, shuffle your deck. You can't use more than 1 Fan Call Ability during your turn.": ['Fan Call'],
    "Once during your turn, if a Stadium is in play, you may make your opponent's Active Pokémon Poisoned.": ['Toxic Wetland'],
    "Once during your turn, if any of your Pokémon were Knocked Out during your opponent's last turn, you may draw 3 cards. You can't use more than 1 Flip the Script Ability each turn.": ['Flip the Script'],
    "Once during your turn, if this Pokémon has an Ancient Booster Energy Capsule attached, you may make both Active Pokémon Poisoned.": ['Toxic Powder'],
    "Once during your turn, if this Pokémon has any {D} Energy attached, you may move up to 3 damage counters from 1 of your Pokémon to 1 of your opponent's Pokémon.": ['Adrena-Brain'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may devolve 1 of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.": ['Ancient Wing'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may have your opponent reveal their hand.": ['Revealing Echo'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may have your opponent shuffle their hand into their deck and draw 3 cards.": ['Distorted Future'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may heal 60 damage from 1 of your Pokémon.": ['Tranquil Flower'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may look at the top 6 cards of your deck, reveal a Supporter card you find there, and put it into your hand. Shuffle the other cards back into your deck.": ['Attract Customers'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Asleep.": ['Calming Light'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may make your opponent's Active Pokémon Burned.": ['Scalding Steam'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may put a Basic Pokémon with 70 HP or less from your discard pile onto your Bench.": ['Gentle Fin'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may search your deck for up to 2 Basic {W} Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.": ['Shivery Chill'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may shuffle it and all attached cards into your deck.": ['Teleporter'],
    "Once during your turn, if this Pokémon is in the Active Spot, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)": ['Big Roar'],
    "Once during your turn, if this Pokémon is in your hand and you have more Prize cards remaining than your opponent, you may put this Pokémon onto your Bench.": ['Swelling Flash'],
    "Once during your turn, if this Pokémon is in your hand and your opponent has any Stage 2 Pokémon in play, you may put this Pokémon onto your Bench.": ['Emergency Rotation'],
    "Once during your turn, if this Pokémon is on your Bench, you may discard the bottom card of your deck. If you do, discard all cards from this Pokémon and put this Pokémon on top of your deck.": ['Flustered Leap'],
    "Once during your turn, if this Pokémon is on your Bench, you may switch it with your Active Pokémon.": ['Showtime'],
    "Once during your turn, if this Pokémon is on your Bench, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.) If you do, discard this Pokémon and all attached cards.": ['Hyper Blower'],
    "Once during your turn, if this Pokémon's remaining HP is 30 or less, you may search your deck for an Unfezant or Unfezant ex and put it onto this Pidove to evolve it. Then, shuffle your deck.": ['Emergency Evolution'],
    "Once during your turn, if you played Janine's Secret Art from your hand this turn, you may draw cards until you have 8 cards in your hand.": ['Shadowy Envoy'],
    "Once during your turn, if your Active Pokémon has the Festival Lead Ability, you may search your deck for a card and put it into your hand. Then, shuffle your deck.": ['Boom Boom Groove'],
    "Once during your turn, if your opponent has 4 or fewer Prize cards remaining, you may attach a Basic {F} Energy card from your discard pile to this Pokémon.": ['Magnetic Absorption'],
    "Once during your turn, when this Pokémon moves from the Active Spot to the Bench, you may search your deck for a Palafin ex and switch it with this Pokémon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pokémon. If you switched a Pokémon in this way, put this card into your deck. Then, shuffle your deck.": ['Zero to Hero'],
    "Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may move any amount of {R} Energy from your other Pokémon to it.": ['Thermal Reactor'],
    "Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may put 2 damage counters on 1 of your opponent's Pokémon.": ['Tachyon Bits'],
    "Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may search your deck for up to 3 Basic {G} Energy cards and attach them to this Pokémon. Then, shuffle your deck.": ['Buzzing Boost'],
    "Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may switch in 1 of your opponent's Benched Basic Pokémon to the Active Spot.": ['Assaulting Hunt'],
    "Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, if you have any Tera Pokémon in play, you may search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.": ['Jewel Seeker'],
    "Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Each player puts a Basic Pokémon from their discard pile onto their Bench. (Your opponent puts a Basic Pokémon onto their Bench first.)": ['Lifeboat'],
    "Once during your turn, you may attach a Basic Energy card from your discard pile to 1 of your Pokémon.": ['Seething Spirit'],
    "Once during your turn, you may attach a Basic Energy card from your discard pile to this Pokémon.": ['Charging Up'],
    "Once during your turn, you may attach a Basic Energy card from your hand to 1 of your Pokémon.": ['Energy Carnival'],
    "Once during your turn, you may attach a Basic {F} Energy card from your discard pile to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.": ['Energizing Rock Salt'],
    "Once during your turn, you may attach a Basic {G} Energy card from your hand to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.": ['Ripening Charge'],
    "Once during your turn, you may attach a Basic {G} Energy card from your hand to this Pokémon. If you attached Energy to a Pokémon in this way, draw a card.": ['Teal Dance'],
    "Once during your turn, you may attach a Basic {L} Energy card from your discard pile to 1 of your Benched Pokémon.": ['Dynamotor'],
    "Once during your turn, you may attach a Basic {P} Energy card from your hand to 1 of your Benched Pokémon. If you attached Energy to a Pokémon in this way, draw 2 cards.": ['Clairvoyant Sense'],
    "Once during your turn, you may attach a Basic {R} Energy card, a Basic {F} Energy card, or 1 of each from your hand to your Pokémon in any way you like.": ['Pyro Dance'],
    "Once during your turn, you may attach a Therapeutic Energy card from your hand to 1 of your Pokémon.": ['Balloon Therapy'],
    "Once during your turn, you may attach up to 2 Basic {F} Energy cards from your discard pile to your Basic {F} Pokémon in any way you like. If you use this Ability, your turn ends.": ['Dino Cry'],
    "Once during your turn, you may attach up to 2 Basic {R} Energy cards from your hand to 1 of your Benched Ethan's Pokémon.": ['Golden Flame'],
    "Once during your turn, you may attach up to 3 Basic Energy cards from your discard pile to your {L} Pokémon in any way you like. If you use this Ability, this Pokémon is Knocked Out.": ['Overvolt Discharge'],
    "Once during your turn, you may discard a Basic {R} Energy card from your hand in order to use this Ability. During this turn, attacks used by your Pokémon do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).": ['Incendiary Song'],
    "Once during your turn, you may draw 3 cards. If you drew any cards in this way, shuffle this Pokémon and all attached cards into your deck.": ['Run Away Draw'],
    "Once during your turn, you may draw a card.": ['Hurried Gait'],
    "Once during your turn, you may draw a card. If this Pokémon is in the Active Spot, draw 1 more card.": ['Coin Bonus'],
    "Once during your turn, you may draw cards until you have 3 cards in your hand.": ['Restart'],
    "Once during your turn, you may flip a coin. If heads, attach up to 4 Basic Energy cards from your discard pile to this Pokémon. If tails, discard an Energy from this Pokémon.": ['Buggy Turbo'],
    "Once during your turn, you may flip a coin. If heads, choose Burned, Confused, or Poisoned. Your opponent's Active Pokémon is now affected by that Special Condition.": ['Selective Slime'],
    "Once during your turn, you may flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot, and the new Active Pokémon is now Confused.": ['Captivating Invitation'],
    "Once during your turn, you may have each player draw a card.": ['Alluring Light'],
    "Once during your turn, you may heal 20 damage from each of your Pokémon.": ['Humming Heal'],
    "Once during your turn, you may heal 20 damage from your Active Evolution Pokémon.": ['Ardent Dancing'],
    "Once during your turn, you may heal 20 damage from your Active Pokémon.": ['Healing Leaves'],
    "Once during your turn, you may heal 30 damage from 1 of your Pokémon.": ['Confectionary Gift'],
    "Once during your turn, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card on the bottom of your deck.": ['Recon Directive'],
    "Once during your turn, you may look at the top 2 cards of your opponent's deck and put 1 of them back. Put the other card on the bottom of their deck.": ['Read the Stars'],
    "Once during your turn, you may look at the top 3 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Discard the other cards.": ['Tri Howl'],
    "Once during your turn, you may look at the top 4 cards of your deck and attach any number of Basic {M} Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards and put them on the bottom of your deck.": ['Metal Maker'],
    "Once during your turn, you may look at the top card of your deck. You may discard that card.": ['Snack Seek'],
    "Once during your turn, you may look at the top card of your opponent's deck. If you do, look at the top card of your deck.": ['Psychic Insight'],
    "Once during your turn, you may move a Basic Energy from 1 of your Pokémon to another of your Pokémon.": ['Happy Switch'],
    "Once during your turn, you may put 1 damage counter on this Pokémon. If you do, draw a card.": ['Zooming Draw'],
    "Once during your turn, you may put 13 damage counters on 1 of your opponent's Pokémon. If you use this Ability, this Pokémon is Knocked Out.": ['Cursed Blast'],
    "Once during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon. If you placed any damage counters in this way, discard this Pokémon and all attached cards.": ['Mysterious Comet'],
    "Once during your turn, you may put 5 damage counters on 1 of your opponent's Pokémon. If you use this Ability, this Pokémon is Knocked Out.": ['Cursed Blast'],
    "Once during your turn, you may put 5 damage counters on this Pokémon. If you do, during this turn, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).": ['Torrential Heart'],
    "Once during your turn, you may put up to 2 Leftovers cards from your discard pile into your hand.": ['Voraciousness'],
    "Once during your turn, you may search your deck for a Basic {L} Energy card and attach it to this Pokémon. Then, shuffle your deck.": ['Electrogenesis'],
    "Once during your turn, you may search your deck for a Basic {P} Energy card, a Basic {M} Energy card, or 1 of each and attach them to your {P} Pokémon and {M} Pokémon in any way you like. Then, shuffle your deck.": ['X-Boot'],
    "Once during your turn, you may search your deck for a Cynthia's Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.": ["Champion's Call"],
    "Once during your turn, you may search your deck for a Giovanni's Charisma card, reveal it, and put it into your hand. Then, shuffle your deck.": ['Rocket Call'],
    "Once during your turn, you may search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.": ['Mammoth Hauler'],
    "Once during your turn, you may search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.": ['Changing Seasons'],
    "Once during your turn, you may search your deck for a card and put it into your hand. Then, shuffle your deck. You can't use more than 1 Quick Search Ability each turn.": ['Quick Search'],
    "Once during your turn, you may search your deck for an Ethan's Adventure card, reveal it, and put it into your hand. Then, shuffle your deck.": ['Bonded by the Journey'],
    "Once during your turn, you may search your deck for up to 2 Basic {L} Pokémon and put them onto your Bench. Then, shuffle your deck.": ['Tandem Unit'],
    "Once during your turn, you may search your deck for up to 2 Evolution {M} Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.": ['Metallic Signal'],
    "Once during your turn, you may search your deck for up to 5 Basic {G} Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck. If you searched your deck in this way, this Pokémon is Knocked Out.": ['Exploding Energy'],
    "Once during your turn, you may shuffle your hand and put it on the bottom of your deck. If you put any cards on the bottom of your deck in this way, draw a card.": ['Nest Stash'],
    "Once during your turn, you may switch 1 of your Benched {D} Pokémon, except any Pecharunt ex, with your Active Pokémon. If you do, the new Active Pokémon is now Poisoned. You can't use more than 1 Subjugating Chains Ability each turn.": ['Subjugating Chains'],
    "Once during your turn, you may switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)": ['Intimidating Howl'],
    "Once during your turn, you may switch your Active Pokémon with 1 of your Benched Pokémon.": ['Night Gate'],
    "Once during your turn, you may switch your Active Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)": ['Torrential Whirlpool'],
    "Once during your turn, you may use this Ability. If this Pokémon is on the Bench, switch it with your Active Pokémon. Or, if this Pokémon is in the Active Spot, switch it with 1 of your Benched Pokémon.": ['Total Freedom'],
    "Once during your turn, you may use this Ability. Your Active Pokémon recovers from all Special Conditions.": ['Busybody Nurse'],
    "Once during your turn, you may use this Ability. Your opponent reveals their hand, and you put a Basic Pokémon with 70 HP or less that you find there onto your opponent's Bench.": ['Look for Prey'],
    "Pokémon (both yours and your opponent's) can't be healed.": ['Freezing Disaster'],
    "Prevent all damage counters from being placed on your Benched Pokémon by effects of attacks used by your opponent's Basic Pokémon.": ['Stellar Veil'],
    "Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon ex.": ['Armor Tail'],
    "Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex and Pokémon V.": ['Mysterious Shield', 'Safeguard'],
    "Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex.": ['Mysterious Rock Inn', 'Safeguard'],
    "Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon if that damage is 200 or more.": ['Impervious Shell'],
    "Prevent all damage done to this Pokémon by attacks from your opponent's {L} Pokémon.": ['Insulator'],
    "Prevent all damage done to your Benched Pokémon that don't have a Rule Box by attacks from your opponent's Pokémon. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)": ['Flower Curtain'],
    "Prevent all damage from and effects of attacks done to this Pokémon by your opponent's Pokémon that have any Special Energy attached.": ['Mighty Shell'],
    "Prevent all damage from and effects of attacks from your opponent's Pokémon done to your Benched Pokémon.": ['Spherical Shield'],
    "Prevent all damage from and effects of attacks from your opponent's Tera Pokémon done to this Pokémon.": ['Sparkling Scales'],
    "Prevent all damage from attacks done to this Pokémon by your opponent's Pokémon that have an Ability.": ['Cornerstone Stance'],
    "Prevent all effects of attacks used by your opponent's Pokémon done to all of your Pokémon that have Energy attached. (Existing effects are not removed. Damage is not an effect.)": ['Protective Mycelium'],
    "Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)": ['Protective Cover', 'Flare Veil', 'Cocoon Cover', 'Unaware'],
    "Prevent all effects of attacks used by your opponent's Pokémon done to your Basic Team Rocket's Pokémon. (Existing effects are not removed. Damage is not an effect.)": ['Repelling Veil'],
    "Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.": ['Amber Protection'],
    "Put this Pokémon into play only with the effect of Palafin's Zero to Hero Ability.": ["Hero's Spirit"],
    "The Weakness of each of your opponent's {N} Pokémon in play is now {P}. (Apply Weakness as ×2.)": ['Fairy Zone'],
    "This Pokémon can evolve during your first turn or the turn you play it.": ['Adaptive Evolution'],
    "This Pokémon can evolve into any Pokémon ex that evolves from Eevee if you play it from your hand onto this Pokémon. (This Pokémon can't evolve during your first turn or the turn you play it.)": ['Rainbow DNA'],
    "This Pokémon can't attack unless you have 4 or more Team Rocket's Pokémon in play.": ['Power Saver'],
    "This Pokémon can't be Asleep.": ['Insomnia'],
    "This Pokémon can't be Burned. Prevent all damage done to this Pokémon by attacks from your opponent's {R} Pokémon.": ['Well-Baked Body'],
    "This Pokémon can't be Paralyzed.": ['Electricity Pouches'],
    "This Pokémon can't be affected by any Special Conditions.": ['Salty Body'],
    "This Pokémon gets +40 HP for each {F} Energy attached to it.": ['Craftsmanship'],
    "This Pokémon gets +50 HP for each Prize card your opponent has taken.": ['Resilient Soul'],
    "This Pokémon may have up to 4 Pokémon Tools attached to it. If it loses this Ability, discard Pokémon Tools from it until only 1 remains.": ['Tune-Up'],
    "This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).": ['Bouffer', 'Exoskeleton', 'Fur Coat', 'Solid Shell'],
    "This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).": ['Solid Shell', 'Exoskeleton', 'Bronze Body', 'Bouffer', 'Soft Wool', 'Mud Coat', 'Thicket Body', 'Solid Body', 'Domed Armor'],
    "Trainer cards in your opponent's discard pile can't be put into their deck by an effect of your opponent's Item or Supporter cards.": ['Sand Screen'],
    "When 1 of your Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, you may move a {L} Energy from that Pokémon to this Pokémon.": ['Electrical Grounding'],
    "When 1 of your {W} Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, you may put all Basic {W} Energy attached to that Pokémon into your hand instead of the discard pile.": ["Diver's Catch"],
    "When this Pokémon is Knocked Out, flip a coin. If heads, your opponent can't take any Prize cards for it.": ['Shattering Crystal'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may attach up to 2 Basic {F} Energy cards from your hand to this Pokémon.": ['Battle-Hardened'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may choose 2 of your opponent's Benched Pokémon and put 1 damage counter on each of them.": ['Flying Entry'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Special Energy from your opponent's Active Pokémon.": ['Special Eater'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Stadium in play.": ['Snow Sink'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may discard the top card of your opponent's deck.": ['Sudden Shearing'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may heal 30 damage from your Active Pokémon and have it recover from a Special Condition.": ['Obliging Heal'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for a Pokémon Tool card and attach it to this Pokémon. Then, shuffle your deck.": ['Impromptu Carrier'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for up to 3 Basic {F} Energy cards and discard them. Then, shuffle your deck.": ['Dig Dig Dig'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for up to 3 Flamigo, reveal them, and put them into your hand. Then, shuffle your deck.": ['Insta-Flock'],
    "When you play this Pokémon from your hand onto your Bench during your turn, you may switch it with your Active Pokémon. If you do, you may move any amount of Energy from your other Pokémon to this Pokémon.": ['Rapid Vernier'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may attach up to 2 Basic {M} Energy cards from your discard pile to your {M} Pokémon in any way you like.": ['Assemble Alloy'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may attach up to 2 Spiky Energy cards from your discard pile to this Pokémon.": ['Spike-Clad'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may choose 1: put a Supporter card from your discard pile into your hand; or search your deck for a Supporter card, reveal it, put it into your hand, and then shuffle your deck.": ['Hearsay'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may choose 2 of your opponent's Pokémon and put 2 damage counters on each of them.": ['Biting Spree'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may draw 3 cards.": ['Suction Cup Draw'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may flip 2 coins. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.": ['Wicked Tail'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand and you put any number of Basic Pokémon you find there onto their Bench.": ['Inviting Wink'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand, and then you choose 2 Energy cards you find there and shuffle them into your opponent's deck.": ["Rob-'n'-Run"],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from 1 of your Pokémon.": ['Enriching Oil'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from each of your Evolution Pokémon. If you healed any damage in this way, discard all Energy from those Pokémon.": ['Time to Chow Down'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may heal all damage from your Active {G} Pokémon. If you healed any damage in this way, discard all Energy from that Pokémon.": ['Wafting Heal'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 3 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.": ['Semi-Blooming Energy'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may look at the top 8 cards of your deck and attach any number of Basic Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.": ['Fully Blooming Energy'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may make your opponent's Active Pokémon Asleep.": ['Here for Hypnosis'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.": ['Magical Flick'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon until the end of your opponent's next turn.": ['Stance'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon.": ['Sneaky Bite'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put a Supporter card from your opponent's discard pile into their hand.": ['Spirit Return'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put up to 2 Arven's Sandwich cards from your discard pile into your hand.": ['Greedy Order'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Basic {R} Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.": ['Infernal Reign'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.": ['Suddenly Select'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 5 Basic {D} Energy cards and attach them to your Marnie's Pokémon in any way you like. Then, shuffle your deck.": ['Punk Up'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch in 1 of your opponent's Benched Pokémon that has 90 HP or less remaining to the Active Spot.": ['Glittering Star Pattern'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch in 1 of your opponent's Benched Pokémon to the Active Spot.": ['Defiant Horn'],
    "When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you must discard the top 5 cards of your deck.": ['Untamed One'],
    "When your opponent's Active Pokémon is Knocked Out, flip a coin. If heads, take 1 more Prize card. The effect of Wonder Kiss doesn't stack.": ['Wonder Kiss'],
    "Whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon.": ['Gnawing Curse'],
    "Whenever your opponent plays a Pokémon from their hand to evolve 1 of their Pokémon, put 4 damage counters on that Pokémon. The effect of Darkest Impulse doesn't stack.": ['Darkest Impulse'],
    "Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.": ['Snow Camouflage', 'Unnerve'],
    "Whenever your opponent's Active Pokémon moves to the Bench during their turn, their new Active Pokémon is now Burned.": ['Lava Zone'],
    "You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may draw a card.": ['Reconstitute'],
    "You must discard a Basic {G} Energy card from your hand in order to use this Ability. Once during your turn, you may put 3 damage counters on 1 of your opponent's Benched Pokémon.": ['Bouquet Magic'],
    "You must discard a Basic {L} Energy from this Pokémon in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.": ['Flashing Draw'],
    "You must discard a Basic {R} Energy card from your hand in order to use this Ability. Once during your turn, you may make your opponent's Active Pokémon Burned.": ['Torrid Scales'],
    "You must discard a Chill Teaser Toy card from your hand in order to use this Ability. Once during your turn, you may switch in 1 of your opponent's Benched Pokémon to the Active Spot.": ['Beckoning Tail'],
    "You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.": ['Trade'],
    "You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.": ['Gather Materials'],
    "You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.": ['Rumbling Engine'],
    "You must put a card from your hand on the bottom of your deck in order to use this Ability. Once during your turn, you may draw cards until you have 5 cards in your hand.": ['Up-Tempo'],
    "Your Basic Pokémon in play have no Retreat Cost.": ['Skyliner'],
    "Your Basic Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).": ['Leadership'],
    "Your Pokémon in play have no Retreat Cost.": ['Jet Cruise'],
    "Your Pokémon in play have no Weakness.": ['Blooming Garden'],
    "Your opponent's Active Evolution Pokémon's Retreat Cost is {C} more.": ['Big Net'],
    "Your opponent's Active Pokémon's Retreat Cost is {C} more.": ['Trap Territory'],
    "Your opponent's Poisoned Pokémon don't recover from that Special Condition when they evolve or devolve.": ['Poison Sacs'],
    "Your opponent's Pokémon in play and all attached cards can't be put into your opponent's hand.": ['Mentally Calm'],
    "Your opponent's Pokémon that have 40 HP or less remaining can't attack.": ['Frigid Room'],
}

print(len(abilities))