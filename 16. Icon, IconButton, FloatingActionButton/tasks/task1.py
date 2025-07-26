'''coderadi'''

# ? Importing libraries
import flet as ft

# * task 1
def task1(page: ft.Page):
    page.title = "Practice - Day 16"

    row = ft.Row([
        ft.Icon(
            name=ft.Icons.ABC,
            tooltip="Open keyboard",
            color=ft.Colors.BLUE_200
        ),
        ft.Icon(
            name=ft.Icons.OPEN_IN_BROWSER,
            tooltip="Open in browser",
            color=ft.Colors.RED_200
        ),
        ft.Icon(
            name=ft.Icons.ADD,
            tooltip="Add to page",
            color=ft.Colors.GREEN_200
        ),
        ft.Icon(
            name=ft.Icons.ACCESS_ALARM,
            tooltip="Add alarm",
            color=ft.Colors.GREY_200
        ),
        ft.Icon(
            name=ft.Icons.ACCOUNT_BALANCE,
            tooltip="Check balance",
            color=ft.Colors.YELLOW_200
        ),
    ], spacing=20)

    page.add(row)

# ! Run the app
ft.app(task1)