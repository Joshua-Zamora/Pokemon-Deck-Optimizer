import flet as ft
from core.deck_builder import DeckBuilder


def on_deck_builder_click():
    print("on_deck_builder_click() clicked")
    card_regulations_allowed = ["G", "H", "I"]

    deck_builder = DeckBuilder(card_regulations_allowed,
                               games_per_evaluation=20,
                               population_size=50,
                               generations=30,
                               mutation_rate=0.1,
                               crossover_rate=0.7,
                               deck_size=60
                               )

    best_deck = deck_builder.optimize()

    print(best_deck)

def on_play_click():
    print("on_play_click() clicked")
    pass

def on_statistics_click():
    print("on_statistics_click() clicked")
    pass

def main(page: ft.Page):
    page.title = "Pokemon Deck Builder"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    main_icon = ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PRIMARY, size=40)
    spacing = ft.Container(height=40)
    deck_builder_button = ft.Button(
        ft.Text("Deck Builder", size=20),
        width=180,
        height=50,
        on_click=on_deck_builder_click
    )
    play_button = ft.Button(
        ft.Text("Play", size=20),
        width=100,
        height=50,
        disabled=True,
        on_click=on_play_click
    )
    statistics_button = ft.Button(
        ft.Text("Statistics", size=20),
        width=150,
        height=50,
        on_click=on_statistics_click
    )

    page.add(main_icon, spacing, deck_builder_button, play_button, statistics_button)

ft.run(main)
