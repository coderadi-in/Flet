'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Layouts: Stack and Responsive Design"

    row = ft.ResponsiveRow([
        ft.Container(ft.Text("A"), col={
            "xs": 12,
            "sm": 6,
            "md": 4
        })
    ])

    page.add(row)

# ! Run the app
ft.app(main)