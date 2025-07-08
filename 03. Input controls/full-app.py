'''coderadi'''

# ? Importing Libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Full Demo App"

    name = ft.TextField(label="Your name", hint_text="Adi", width=300)
    is_subscribed = ft.Checkbox(label="Subscribe to newsletter.")

    lang = ft.Dropdown(width=300, value="Python", label="Preferred language", options=[
        ft.dropdown.Option("Python"),
        ft.dropdown.Option("JavaScript"),
        ft.dropdown.Option("C/C++"),
        ft.dropdown.Option("Dart"),
        ft.dropdown.Option("Java")
    ])


    theme = ft.RadioGroup(ft.Column(controls=[
        ft.Radio(label="Light", value='light'),
        ft.Radio(label="Dark", value='dark')
    ]))

    result = ft.Text()

    def on_submit(e=None):
        result.value = (
            f"Name: {name.value}\n"
            f"Language: {lang.value}\n"
            f"Subscription: {is_subscribed.value}\n"
            f"Theme: {theme.value}"
        )
        page.update()

    submit_btn = ft.ElevatedButton("Submit", on_click=on_submit)

    page.add(
        ft.Column(controls=[
            name,
            lang, 
            is_subscribed,
            theme,
            submit_btn,
            result
        ], spacing=20)
    )

# ! Run the app
ft.app(main)