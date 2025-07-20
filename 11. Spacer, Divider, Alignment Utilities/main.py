'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Day 11. Spacer, Divider, Alignment Utilities"

    spacer = ft.Row([
        ft.Text("Left"),
        ft.Container(expand=True),
        ft.Text("Right")
    ])

    vertical_divider = ft.Row([
        ft.Text("Item 1"),
        ft.VerticalDivider(width=1),
        ft.Text("Item 2")
    ])
    

    page.add(
        spacer,
        ft.Divider(height=1, color="#585858"),
        spacer,
        vertical_divider
    )

    

# ! Run the app
ft.app(main)