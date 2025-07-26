'''coderadi'''

# ? Importing libraries
import flet as ft

# * Task 2
def task2(page: ft.Page):
    page.title = "Practice - Day 17"
    page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_theme(e):
        if e.control.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    sw = ft.Switch(
        value=False,
        label="Change theme",
        on_change=toggle_theme
    )
    page.add(sw)

# ! Run the app
ft.app(task2)