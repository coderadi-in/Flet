'''
✅ Task 1: Click Counter App
Create an app with:
    - A button labeled "+"
    - A Text label showing how many times it was clicked
    - Each click updates the counter

✅ Task 2: Show/Hide Password
Create:
    - A password TextField
    - A TextButton labeled “Show/Hide”
    - Toggle between password=True/False on click
'''

# ? Importing Libraries
import flet as ft

# ! task1 function
def task1(page: ft.Page):
    page.title = "Task 1"
    page.vertical_alignment = ft.alignment.center
    page.horizontal_alignment = ft.alignment.center

    count = ft.TextField(value="0")

    def increase_val(e):
        count.value = int(count.value) + 1
        page.update()

    def decrease_val(e):
        count.value = int(count.value) - 1
        page.update()

    add_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=increase_val)
    minus_btn = ft.IconButton(icon=ft.Icons.REMOVE, on_click=decrease_val)

    page.add(
        ft.Row(
            controls=[
                minus_btn, count, add_btn
            ], spacing=10, vertical_alignment=ft.alignment.center
        )
    )

# ! task2 function
def task2(page: ft.Page):
    page.title = "Task 2"
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center

    def toggle_password_visibility(e):
        password.password = False if password.password == True else True
        page.update()

    password = ft.TextField(label="Password", hint_text="Enter your password", password=True)
    show_btn = ft.IconButton(ft.Icons.PASSWORD, on_click=toggle_password_visibility)

    page.add(
        ft.Row(
            controls=[
                password, show_btn
            ], spacing=10, vertical_alignment=ft.alignment.center
        )
    )

ft.app(task2)