'''coderadi'''

'''
✅ Task 1: Overlapping Boxes
- Red background 300x300
- Blue box 150x150 over it, placed at left=50, top=50
- Green circle (use Container + shape) on bottom-right

✅ Task 2: Floating Button UI
- Image background
- Button with FloatingActionButton on top-right (using Stack)
'''

# ? Importing libraries
import flet as ft

# * Task 1
def task1(page: ft.Page):
    page.title = "Task 1"

    st = ft.Stack(
        controls=[
            ft.Container(bgcolor='red', expand=True),
            ft.Container(bgcolor='blue', width=150, height=150, left=50, top=50),
            ft.Container(bgcolor='green', width=100, height=100, shape=ft.BoxShape.CIRCLE, bottom=0, right=0)
        ], width=300, height=300,
    )

    page.add(st)

# * Task 2
def task2(page: ft.Page):
    page.title = "Task 2"

    st = ft.Stack(
        controls=[
            ft.Image(src='part. 01/bg.png', expand=True, border_radius=10),
            ft.FloatingActionButton(text="Buy", top=10, right=10)
        ]
    )

    page.add(st)

# ! Run the app
ft.app(task2)