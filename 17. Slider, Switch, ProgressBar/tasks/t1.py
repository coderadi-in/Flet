'''coderadi'''

# ? Importing libraries
import flet as ft

# * Task 1
def task1(page: ft.Page):
    page.title = "Practice - Day 17"

    txt = ft.Text(
        value="Hello, world!",
        color="#FFFDD0",
        size=16
    )

    def set_size(e):
        txt.size = e.control.value
        txt.update()

    bar = ft.Slider(
        value=16, min=10, max=110,
        thumb_color="#4c8eff",
        active_color="#86b2ff",
        overlay_color="#7794c7",
        inactive_color="#3469c5",
        on_change=set_size
    )

    page.add(txt, bar)


# ! Run the app
ft.app(task1)