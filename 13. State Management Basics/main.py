'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "13. State Management Basics"
    counter = ft.Text("0", size=32)

    def increase(e):
        counter.value = str(int(counter.value) + 1)
        counter.update()

    btn = ft.OutlinedButton(
        icon=ft.Icons.ADD,
        text="Increase",
        on_click=increase
    )

    page.add(counter, btn)

# ! Run the app
ft.app(main)