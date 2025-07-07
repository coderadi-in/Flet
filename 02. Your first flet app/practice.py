'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Counter app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    c = 0
    txt = ft.Text(f"Count: {c}", size=32)

    def minus(e):
        nonlocal c
        c -= 1
        txt.value = f"Count: {c}"
        page.update()

    def plus(e):
        nonlocal c
        c += 1
        txt.value = f"Count: {c}"
        page.update()

    def reset(e):
        nonlocal c
        c = 0
        txt.value = f"Count: {c}"
        page.update()

    minus_btn = ft.IconButton(icon=ft.Icons.REMOVE, on_click=minus)
    reset_btn = ft.ElevatedButton(icon=ft.Icons.RESTORE, text="Reset", on_click=reset)
    plus_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=plus)

    btnrow = ft.Row(controls=[minus_btn, reset_btn, plus_btn], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    main_column = ft.Column(controls=[txt, btnrow], alignment=ft.MainAxisAlignment.CENTER)

    page.add(main_column)

ft.app(main)