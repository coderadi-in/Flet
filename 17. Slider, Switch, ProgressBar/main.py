'''coderadi'''

# ? Importing libraries
import flet as ft
import time

# * Slider
def main(page: ft.Page):
    page.title = "Day 17 Slider, Switch, ProgressBar"

    def slider_change(e):
        txt.value = f"Value: {e.control.value}"
        txt.update()

    txt = ft.Text()
    slider = ft.Slider(
        min=0, max=100,
        divisions=10,
        on_change=slider_change,
        label="Slide"
    )

    page.add(txt, slider)

# * Switch
def switch(page: ft.Page):
    page.title = "Day 17 Slider, Switch, ProgressBar"

    def on_switch_change(e):
        txt.value = "ON" if e.control.value else "OFF"
        txt.update()

    txt = ft.Text("OFF")
    sw = ft.Switch(value=False, on_change=on_switch_change)

    page.add(txt, sw)

# * Progressbar
def progressbar(page: ft.Page):
    page.title = "Day 17 Slider, Switch, ProgressBar"

    progress = ft.ProgressBar(
        color="blue", width=400
    )

    page.add(progress)

    for i in range(0, 101, 10):
        progress.value = i / 100
        progress.update()
        time.sleep(0.1)

# ! Run the app
ft.app(progressbar)