'''coderadi'''

# ? Importing libraries
import flet as ft
import time

# * Task 3
def task3(page: ft.Page):
    page.title = "Practice - Day 17"

    bar = ft.ProgressBar(
        value=0.0, width=400
    )

    def increase(e):
        bar.value += 0.1
        bar.update()
        time.sleep(0.5)
        
        if bar.value < 1:
            increase(None)

    btn = ft.ElevatedButton(
        text="Start",
        on_click=increase
    )

    page.add(bar, btn)

# ! Run the app
ft.app(task3)