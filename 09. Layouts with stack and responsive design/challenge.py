'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Challenge - day 10"

    content = ft.ResponsiveRow([
        ft.Container(
            ft.Text("Card 1", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
        ft.Container(
            ft.Text("Card 2", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
        ft.Container(
            ft.Text("Card 3", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
        ft.Container(
            ft.Text("Card 4", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
        ft.Container(
            ft.Text("Card 5", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
        ft.Container(
            ft.Text("Card 6", size=32), bgcolor="#2c2c31", width=250, height=150, border_radius=5,
            col={
                'xs': 12,
                'md': 6,
                'xl': 4
            }
        ),
    ], spacing=10)

    page.add(content)

# ! Run the app
ft.app(main)