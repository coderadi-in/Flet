'''coderadi'''

# ? Importing libraries
import flet as ft
import math

# ! The main function
def main(page: ft.Page):
    page.title = "Volume controller"

    vol = ft.Text()

    def toggle_mute(e):
        if e.control.value:
            vol.value = "Muted"
        else:
            vol.value = ""
        vol.update()

    def set_volume(e):
        value = str(math.floor(e.control.value))
        e.control.label = value
        if vol.value != "Muted":
            vol.value = value
            
        e.control.update()
        vol.update()

    volume = ft.Row([
        ft.Row([
            ft.Switch(
                value=False,
                on_change=toggle_mute
            ),

            ft.Slider(
                value=50,
                min=0, max=100,
                width=200,
                label="50",
                on_change=set_volume
            )
        ]),
        vol
    ])

    page.add(volume)

# ! Run the app
ft.app(main)