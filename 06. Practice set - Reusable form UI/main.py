'''coderadi'''

# ? Importing libraries
import flet as ft
import re

# ! The main function
def main(page: ft.Page):
    page.title = "Practice set - Reusable form UI"

    # * function to return a styled container
    def form_card(content: ft.Column):
        return ft.Container(
            content=content,
            padding=10,
            border_radius=10,
            bgcolor="#1A1A1D",
            width=400,
        )
    
    # & Creating form inputs
    name = ft.TextField(label="Your name", hint_text="Enter your name")
    email = ft.TextField(label="Your email", hint_text="Enter your email")
    gender = ft.Dropdown(
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
            ft.dropdown.Option("Other")
        ]
    )
    terms = ft.Checkbox(label="I agree to all terms and conditions.")

    # * function to handle form submission
    def submit_form(e):
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        valid = re.search(pattern, email.value)
        if not (terms.value):
            print("It's required to agree to terms"); return

        if (valid) and (email != ""):
            print("You're signed up!")

        else:   print("Invalid email.")

    form_content = ft.Column(controls=[
        name,
        email,
        gender,
        terms,
        ft.ElevatedButton("Submit", on_click=submit_form)
    ])

    form = form_card(form_content)

    page.add(form)

# ! Run the app
ft.app(main)