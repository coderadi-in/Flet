'''coderadi'''

'''
### ✅ Task 1: Horizontal Navigation Bar
    - Use Row
    - Add 3 TextButtons: Home, About, Contact
    - Center align them

### ✅ Task 2: Two-Column Layout

    - Left Column: Name and Email TextFields
    - Right Column: Live preview of input
    - Use Row with two Columns inside
'''

# ? Importing libraries
import flet as ft

# * Task 1
def task1(page: ft.Page):
    page.title = "Task 1"

    navbar = ft.Row([
        ft.TextButton('Home'),
        ft.TextButton('About'),
        ft.TextButton('Contact')
    ], spacing=10, alignment=ft.alignment.center)

    page.add(navbar)

# * Task 2
def task2(page: ft.Page):
    page.title = "Task 2"

    def show_preview(e, control: ft.TextField, output: ft.Text):
        output.value = control.value
        page.update()

    name = ft.TextField(
        label="Your Name", 
        on_change=lambda e: show_preview(e, name, name_preview)
    )

    email = ft.TextField(
        label="Your Email", 
        on_change=lambda e: show_preview(e, email, email_preview)
    )
    name_preview = ft.Text(value="")
    email_preview = ft.Text(value="")

    app_content = ft.Row([
        ft.Column([
            name, email
        ], spacing=10, alignment=ft.alignment.center),
        ft.Column([
            name_preview,
            email_preview
        ], spacing=10, alignment=ft.alignment.center)
    ], alignment=ft.alignment.center)

    page.add(app_content)

# ! Run the app
ft.app(task2)