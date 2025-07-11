'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Buttons & Events in Flet"

    # & Elevated Button
    eb = ft.ElevatedButton("Click")
    tb = ft.TextButton("Cancel")
    ob = ft.OutlinedButton("Details")
    ib = ft.IconButton(icon=ft.Icons.DELETE)
    fab = ft.FloatingActionButton(icon=ft.Icons.ADD)

    page.add(eb, tb, ob, ib, fab)

# ! Run the app
ft.app(main)