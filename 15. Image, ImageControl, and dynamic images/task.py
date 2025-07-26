'''coderadi'''

# ? Importing libraries
import flet as ft
import random

# * Task 1
def task1(page: ft.Page):
    page.title = "Tasks - Day: 15"

    img_row = ft.Row([
        ft.Image("car3.png", width=300),
        ft.Image("car1.png", width=400),
        ft.Image("car2.png", width=400),
    ])

    page.add(img_row)

# * Task 2
def task2(page: ft.Page):
    page.title = "Tasks - Day: 15"

    img_url = ["car3.png", "car1.png", 'car2.png']

    frame = ft.Image(width=400)

    def get_img(e):
        url = random.choice(img_url)
        frame.src = url
        frame.update()
    
    btn = ft.ElevatedButton(
        text="Random",
        on_click=get_img
    )

    page.add(frame, btn)
    get_img(None)

# * Task 3
def task3(page: ft.Page):
    page.title = "Tasks - Day: 15"

    url = ft.TextField(
        label="Image URL",
        hint_text="Enter image url"
    )

    frame = ft.Image(
        src="img_src",
        width=400
    )

    def show_img(e):
        img_url = url.value
        frame.src = img_url
        frame.update()

    btn = ft.ElevatedButton(
        text="See image",
        on_click=show_img
    )

    page.add(url, btn, frame)

# * Task 4
def task4(page: ft.Page):
    page.title = "Tasks - Day: 15"

    profile_pic = ft.Image(
        src="car3.png",
        border_radius=200,
        width=400
    )

    page.add(profile_pic)

# * Task 5
def task5(page: ft.Page):
    page.title = "Tasks - Day: 15"

    grid = ft.ResponsiveRow([
        ft.Image("car1.png", expand=True, col={
            "xs": 12,
            "md": 6,
            "xl": 4
        }),
        ft.Image("car2.png", expand=True, col={
            "xs": 12,
            "md": 6,
            "xl": 4
        }),
        ft.Image("car3.png", expand=True, col={
            "xs": 12,
            "md": 6,
            "xl": 4
        })
    ])

    page.add(grid)

# ! Run the app
ft.app(task5)