'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Container and styling basics"

    # & Creating a container
    container = ft.Container(
        content=ft.Text("Hello, world!", color="#212122"),
        # bgcolor=ft.Colors.BLUE_300,
        gradient=ft.LinearGradient(colors=[
            ft.Colors.BLUE_100,
            ft.Colors.RED_100
        ]),
        padding=10,
        border_radius=5,
        alignment=ft.alignment.center,
        border=ft.border.all(1, '#212122'),
        width=200,
        height=50,
        # expand=True,
        blur=5,
        shadow=ft.BoxShadow(5, 10, "#77DD77"),
        opacity=0.8
    )

    # & Adding controls to page
    page.add(container)

# ! Run the app
ft.app(main)