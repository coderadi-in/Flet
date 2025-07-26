'''coderadi'''

# ? Importing libraries
import flet as ft
import time, math

# * Task 3
def task3(page: ft.Page):
    page.title = "Practice - Day 17"

    bar = ft.ProgressBar(
        value=0, width=720
    )

    timer_value = ft.Text("10")

    def start_timer(e):
        if bar.value < 1.0:
            bar.value += 1 / slider.value
            bar.update()

            current_time = int(timer_value.value)
            timer_value.value = str(current_time - 1) if current_time >= 1 else "Done."
            timer_value.update()

            time.sleep(1)

        else:
            bar.value = 0
            bar.update()
            return

        start_timer(e)

    def on_change(e):
        timer_value.value = str(math.floor(slider.value))
        timer_value.update()

    slider = ft.Slider(
        min=1, max=1440, value=10,
        width=720,
        on_change=on_change
    )

    btn = ft.FloatingActionButton(
        icon=ft.Icons.TIMER,
        on_click=start_timer
    )

    page.add(ft.Column([
        ft.Row([
            slider, timer_value, btn
        ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.CENTER),

        bar
    ], spacing=10, alignment=ft.MainAxisAlignment.SPACE_EVENLY, height=300))

# ! Run the app
ft.app(task3)