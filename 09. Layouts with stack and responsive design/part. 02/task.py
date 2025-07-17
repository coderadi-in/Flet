'''coderadi'''

'''
✅ Task 1: Three Cards Layout
- Use ResponsiveRow
- Each card: Container with Text, 200px height
- Use col to show 1, 2, or 3 cards depending on screen size

✅ Task 2: Profile Layout
- Left: Avatar + name
- Right: Bio + edit button
- Collapse into a column layout on mobile screens using ResponsiveRow
'''

# ? Importing libraries
import flet as ft

# * task 1
def task1(page: ft.Page):
    page.title = "Task 1"

    row = ft.ResponsiveRow([
        ft.Container(ft.Text("Card 1", size=200), col={
            "xs": 12,
            "sm": 6,
            "md": 4
        }),
        ft.Container(ft.Text("Card 1", size=200), col={
            "xs": 12,
            "sm": 6,
            "md": 4
        }),
        ft.Container(ft.Text("Card 1", size=200), col={
            "xs": 12,
            "sm": 6,
            "md": 4
        })
    ], expand=True)

    page.add(row)

# * task 2
def task2(page: ft.Page):
    page.title = "Task 2"

    

# ! Run the app
ft.app(task1)