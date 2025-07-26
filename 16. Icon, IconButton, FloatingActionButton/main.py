'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Day 16 Icon, IconButton, FloatingActionButton"

    icon = ft.Icon(
        name=ft.Icons.HOME,
        size=32,
        color="#4C8EFF"
    )

    liked = False

    def toggle(e):
        nonlocal liked
        liked = not liked
        icon_btn.icon = ft.Icons.FAVORITE if liked else ft.Icons.FAVORITE_BORDER
        icon_btn.icon_color = "#FFCCCC" if liked else "#212122"
        icon_btn.update()

    icon_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER,
        icon_color="#212122",
        on_click=toggle
    )

    page.add(icon, icon_btn)

# ! Run the app
ft.app(main)