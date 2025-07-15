'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Layouts with Row and Column"

    # & Horizontal Button Group
    btns = ft.Row([
            ft.ElevatedButton("Yes"),
            ft.TextButton("No")
    ], spacing=10)

    # & Profile Card Layout
    card = ft.Row([
        ft.Image(src="avatar.png", width=75, border_radius=50), # ! add an image here
        ft.Column([
            ft.Text("Alice", size=32),
            ft.Text("Developer", size=16)
        ], spacing=0)
    ], spacing=10, alignment=ft.alignment.center)

    # * adding elements to page
    page.add(btns, card)

# ! Run the app
ft.app(main)