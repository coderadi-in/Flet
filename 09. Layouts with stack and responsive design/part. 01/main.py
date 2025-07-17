'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Layouts with stack and responsive design"

    st = ft.Stack(
        controls=[
            ft.Container(width=200, height=200, bgcolor='red'),
            ft.Container(width=100, height=100, bgcolor='blue', left=50, top=50)
        ]
    )

    page.add(st)

# ! Run the app
ft.app(main)