'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Challenge day - 11"
    page.theme_mode = ft.ThemeMode.SYSTEM

    footer = ft.Row([
        ft.Row([
            ft.Image('logo.png', width=50, height=50, border_radius=50),
            ft.Text("$CODERADI>", size=36)
        ], spacing=10, alignment=ft.alignment.center),

        ft.Row([
            ft.Text("Home", size=16),
            ft.Text("Store", size=16),
            ft.Text("About", size=16),
            ft.Text("Contact", size=16)
        ], spacing=10),

        ft.Text("Copyright © | All rights reserved by coderadi.in")
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(
        ft.Divider(height=1, color=ft.Colors.BLUE_200), 
        footer
    )

# ! Run the app
ft.app(main)