'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def first_app(page: ft.Page):
    page.title = "My first flet app"

    txt = ft.Text("Hello, Adi 👋!", size=24)

    # * on_click function
    def on_click(e):
        txt.value = "Button clicked!"
        page.update()

    btn = ft.ElevatedButton("Click Me!", on_click=on_click)
    page.add(txt, btn)

# ! app with columns
def app_with_columns(page: ft.Page):
    page.title = "Using Column"

    txt = ft.Text("Hi Adi, press the button 👇", size=20)

    def say_hello(e):
        txt.value = "You're doing awesome!"
        page.update()

    btn = ft.ElevatedButton("Say Hello", on_click=say_hello)

    layout = ft.Column(controls=[txt, btn], alignment=ft.MainAxisAlignment.CENTER)

    page.add(layout)

# ! app with rows
def app_with_rows(page: ft.Page):
    page.title = "Using Row"

    btn1 = ft.ElevatedButton("Left")
    btn2 = ft.ElevatedButton("Right")

    row = ft.Row(controls=[btn1, btn2], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(row)

ft.app(app_with_rows)