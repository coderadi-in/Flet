'''coderadi'''

# ? Importing libraries
import flet as ft

# * task 3
def task3(page: ft.Page):
    page.title = "Practice - Day 16"

    def alert(e):
        page.add(ft.AlertDialog(
            title=ft.Text("Alert"),
            content=ft.Text("This is an alert."),
            title_padding=10,
            content_padding=10,
        ))
        page.update()

    fab = ft.FloatingActionButton(
        text="Click",
        icon=ft.Icons.ADS_CLICK,
        on_click=alert
    )

    page.add(fab)

# ! Run the app
ft.app(task3)