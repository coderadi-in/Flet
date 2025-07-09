'''
🎯 Challenge (Optional Mini-Project)
💡 "Login Card" UI Clone
Create a card-based login form with:
    - Username and Password fields
    - Login button
    - Card-style layout with padding, background, rounded borders
    - Centered in the page
'''

# ? Importing Libraires
import flet as ft

# ! The main function
def main(page: ft.Page):
    # & Page design
    page.title = "Login card UI clone"
    page.vertical_alignment = ft.alignment.center
    page.horizontal_alignment = ft.alignment.center

    # | Login controls

    # & username
    username = ft.TextField(
        label="Your name", hint_text="coderadi",
        border_radius=5, width=300, height=50, border=2,
        border_color="#212122"
    )

    # & password
    password = ft.TextField(
        label="Password",
        border_radius=5, width=300, height=50, border=2,
        border_color="#212122", password=True
    )

    # & login button
    login_btn = ft.FilledButton(
        text="Login", width=300, height=50
    )

    # & form container
    login_form = ft.Container(
        content=ft.Column([
            ft.Text("Login", size=32, color="#212122"),
            username, password, login_btn
        ], spacing=10),
        width=340, border_radius=20, padding=20,
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient([
            ft.Colors.BLUE_500,
            ft.Colors.GREEN_500
        ], rotation=135)
    )

    # * Adding controls to page
    page.add(login_form)

# ! Run the app
ft.app(main)