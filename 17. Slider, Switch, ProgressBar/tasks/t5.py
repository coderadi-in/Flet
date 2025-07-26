'''coderadi'''

# ? Importing libraries
import flet as ft
import time, math

# * Task 3
def task3(page: ft.Page):
    page.title = "Practice - Day 17"

    value = ft.Text("OFF")

    def toggle(e):
        v = sw.value
        value.value = "ON" if v else "OFF"
        value.update()

    sw = ft.Switch(
        label="Switch",
        value=False,
        on_change=toggle
    )

    page.add(
        ft.Row(
            [sw, value],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    
# ! Run the app
ft.app(task3)