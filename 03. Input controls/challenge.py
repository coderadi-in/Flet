'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Challenge for day - 03"

    name = ft.TextField(label="Your name", hint_text="Adi", width=300)
    feedback = ft.TextField(label="Feedback", hint_text="X needs to be improved", width=300, multiline=True)

    recommend = ft.RadioGroup(ft.Column(controls=[
        ft.Radio(label="Yes", value='yes'),
        ft.Radio(label="No", value='no')
    ]))

    share_email = ft.Checkbox(label="Share email?")
    summary = ft.Text()

    def on_submit(e=None):
        summary.value = (
            f"Name: {name.value}\n"
            f"Feedback: {feedback.value}\n"
            f"Recommendation: {recommend.value}\n"
            f"Share Email: {share_email.value}"
        )
        page.update()

    submit_btn = ft.ElevatedButton("Submit", width=300, on_click=on_submit)


    page.add(ft.Column([
        name,
        feedback,
        ft.Column([
            ft.Text("Recommend Us?"),
            recommend
        ], spacing=10),
        share_email,
        submit_btn,
        summary
    ], spacing=20))

# ! Run the app
ft.app(main)