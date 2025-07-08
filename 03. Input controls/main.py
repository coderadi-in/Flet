'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Input controls"

    name = ft.TextField(label="Enter your name", hint_text="Adi", width=300)
    check = ft.Checkbox(label="I agree to the terms", value=False)
    
    dropdown = ft.Dropdown(width=300, options=[
        ft.dropdown.Option("Python"),
        ft.dropdown.Option("JavaScript"),
        ft.dropdown.Option("C/C++"),
    ], value="Python")

    radio = ft.RadioGroup(content=ft.Column(controls=[
        ft.Radio(label="Light", value="light"),
        ft.Radio(label="Dark", value="dark")
    ]))

    page.add(
        name, check, 
        dropdown, radio
    )

# ! Run the window
ft.app(main)