import flet as ft

def main(page: ft.Page):
    page.title = "Hello, Flet!"
    page.add(ft.Text("Welcome to Flet"))

ft.app(target=main)