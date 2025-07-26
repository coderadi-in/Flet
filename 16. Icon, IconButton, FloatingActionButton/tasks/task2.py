'''coderadi'''

# ? Importing libraries
import flet as ft

# * task 2
def task2(page: ft.Page):
    page.title = "Practice - Day 16"
    liked = False

    def toggle(e):
        nonlocal liked
        if liked:
            icon_btn.icon = ft.Icons.FAVORITE_BORDER
            icon_btn.icon_color = "black"
            icon_btn.tooltip = "Like"

        else:
            icon_btn.icon = ft.Icons.FAVORITE
            icon_btn.icon_color = "red"
            icon_btn.tooltip = "Dislike"
        
        liked = not liked
        icon_btn.update()

    icon_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER,
        icon_color="black",
        tooltip="Like",
        on_click=toggle
    )

    page.add(icon_btn)

# ! Run the app
ft.app(task2)