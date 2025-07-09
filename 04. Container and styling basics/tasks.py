'''coderadi'''

'''
✅ Task 1:
Create 3 Containers:
    - Red box 200x100 with center-aligned text
    - Blue box with padding and rounded corners
    - Green box with a gradient background

✅ Task 2:
Design a "Profile Card":
    - Avatar (use Image or placeholder CircleAvatar)
    - Name (bold text)
    - Bio (description text)
    - All wrapped in a styled container
'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Tasks - day #04"

    # & Task 01

    # | Red box 200x100 with center-aligned text
    cont1 = ft.Container(
        content=ft.Text("Hello, Flet!", color="#212122"),
        width=200, height=100,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.RED_200
    )

    # | Blue box with padding and rounded corners
    cont2 = ft.Container(
        content=ft.Text("Hello, Flet!", color="#212122"),
        border_radius=5, padding=10,
        bgcolor=ft.Colors.BLUE_200
    )

    # | Green box with a gradient background
    cont3 = ft.Container(
        content=ft.Text("Hello, Flet!", color="#212122"),
        padding=ft.padding.symmetric(20, 50),
        border_radius=50,
        gradient=ft.LinearGradient(colors=[
            ft.Colors.GREEN_100,
            ft.Colors.GREY_300
        ])
    )

    # & Task 02
    profile = ft.Container(
        content=ft.Column(controls=[
            ft.CircleAvatar(bgcolor="#212122"),
            ft.Text("Adi", weight=ft.FontWeight.BOLD, size=32, text_align=ft.TextAlign.CENTER),
            ft.Text(
                "Python developer | Web developer | Full-stack developer | Cross platform app developer",
                size=16, text_align=ft.TextAlign.CENTER
            )
        ], spacing=10),
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.BLUE_300,
        alignment=ft.alignment.center,
        width=300
    )

    page.add(
        ft.Column(
            controls=[
                cont1, cont2, cont3
            ], spacing=20
        ),
        profile
    )

# ! Run the app
ft.app(main)