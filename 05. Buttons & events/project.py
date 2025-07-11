'''coderadi'''

# ? Importing libraries
import flet as ft
from datetime import datetime

# ! The main function
def main(page: ft.Page):
    page.title = "Mood logger - Mini Project"

    # * function to handle happy mood
    def handle_happy(e):
        logs.controls.append(
            ft.Text(f"Happy - {datetime.now().strftime("%H:%M:%S")}")
        )
        page.update()

    # * function to handle neutral mood
    def handle_neutral(e):
        logs.controls.append(
            ft.Text(f"Neutral - {datetime.now().strftime("%H:%M:%S")}")
        )
        page.update()

    # * function to handle sad mood
    def handle_sad(e):
        logs.controls.append(
            ft.Text(f"Sad - {datetime.now().strftime("%H:%M:S")}")
        )
        page.update()

    # & Mood buttons
    btn_rows = ft.Row([
        ft.TextButton("😃", on_click=handle_happy),
        ft.TextButton("😐", on_click=handle_neutral),
        ft.TextButton("😢", on_click=handle_sad)
    ])

    # & Mood log column
    logs = ft.Column([
        ft.Text("Mood history:", size=32)
    ])

    # & adding controls to page
    page.add(ft.Column([
        btn_rows,
        logs
    ], spacing=20))

# ! Run the app
ft.app(main)