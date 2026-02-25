import flet as ft


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
        on_click=None
    )
    play_button = ft.Button(
        ft.Text("Play", size=20),
        width=100,
        height=50,
        disabled=True,
        on_click=None
    )
    statistics_button = ft.Button(
        ft.Text("Statistics", size=20),
        width=150,
        height=50,
        on_click=None
    )

    page.add(main_icon, spacing, deck_builder_button, play_button, statistics_button)

ft.run(main)
