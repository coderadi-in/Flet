'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Challenge | Day 08",
    page.padding = 0

    header = ft.Container(
        ft.Row([
            ft.Image(src="logo.png", width=50, border_radius=50), # ! Add an image here
            ft.Text("Dashboard Title", size=32),
            ft.Image(src="avatar.png", width=20, border_radius=20) # ! Add an image here
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.Padding(20, 10, 20, 10)
    )

    page.add(header)

# ! Run the app
ft.app(main)