'''coderadi'''

# ? Importing libraries
import flet as ft

# * task 1
def task1(page: ft.Page):
    page.title = "Task 1"

    cont = ft.Container(
        content=ft.Text("This is a text."),
        bgcolor='#1E1E2F',
        border_radius=10,
        padding=20
    )

    page.add(cont)

# * task 2
def task2(page: ft.Page):
    page.title = "Task 2"

    card = ft.Container(
        image_src="bg.png",
        image_fit=ft.ImageFit.COVER,
        expand=True,
        content=ft.Text("BMW M4"),
        alignment=ft.alignment.bottom_left,
        border=ft.border.all(2, 'white')
    )

    page.add(card)

def task2(page: ft.Page): # Assuming this is your function
    
    card = ft.Container(
        content=ft.Text("BMW M4", size=32, color='black'),
        alignment=ft.alignment.bottom_left,
        border=ft.border.all(2, 'white'),
        width=800, height=450,

        image=ft.DecorationImage(
            'bg.png',
            fit=ft.ImageFit.COVER,
        )
    )

    page.add(card)


# ! Run the app
ft.app(task2)