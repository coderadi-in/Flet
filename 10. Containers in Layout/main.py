'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Day 10. Containers in Layouts"

    page.add(
        ft.Container(
            ft.Text("Inside Padding"),
            padding=ft.padding.symmetric(10, 20),
            margin=10,
            border=ft.border.all(2, 'white'),
            border_radius=10,
            bgcolor=ft.Colors.BLUE_400,
            alignment=ft.alignment.top_center,
            width=300, height=200,
            ink=True, ink_color=ft.Colors.BLUE_100,
            on_click=lambda e: print("Clicked!")
        )
    )

# ! Run the app
ft.app(main)