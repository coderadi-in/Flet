'''coderadi'''

'''
🧪 Practice Tasks
🟡 Task 1: Evenly spaced Row
- Add 3 Text widgets
- Use Container() to place them evenly

🟡 Task 2: Vertical Card Divider
- Use Row
- Add two Containers
- Use VerticalDivider between them

🟡 Task 3: Centered Login Card
- Use Container with alignment.center
- Inside, put a login form (2 TextFields and a Button)
'''

# ? Importing libraries
import flet as ft

# * task 1
def task1(page: ft.Page):
    page.title = "Task 1"

    widgets = ft.Row([
        ft.Text("Item 1"),
        ft.Container(expand=True),
        ft.Text("Item 2"),
        ft.Container(expand=True),
        ft.Text("Item 3")
    ])

    page.add(widgets)

# * task 2
def task2(page: ft.Page):
    page.title = "Task 2"

    cards = ft.Row([
        ft.Container(
            ft.Text("Card 1"), bgcolor="#DD7777",
            border_radius=10, padding=ft.padding.symmetric(10, 20)
        ),
        ft.VerticalDivider(thickness=1, width=1, color="#FFFFFF"),
        ft.Container(
            ft.Text("Card 1"), bgcolor="#7777DD",
            border_radius=10, padding=ft.padding.symmetric(10, 20)
        )
    ])

    page.add(cards)

# * task 3
def task3(page: ft.Page):
    page.title = "Task 3"

    login_card = ft.Container(
        ft.Column([
            ft.TextField(label="Your email", hint_text="Enter your email", width=300),
            ft.TextField(label="Your password", hint_text="Enter your password", width=300, password=True),
            ft.ElevatedButton("Login", width=300),
        ], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center
    )

    page.add(login_card)

# ! Run the app
ft.app(task3)