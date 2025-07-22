'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Day 14 Mini Project #2"

    height = ft.TextField(label="Height", hint_text="m", keyboard_type=ft.KeyboardType.NUMBER)
    weight = ft.TextField(label="Weight", hint_text="kg", keyboard_type=ft.KeyboardType.NUMBER)
    bmi = ft.Text()
    status = ft.Text()

    def calculate_bmi(e):
        height_value = float(height.value)
        weight_value = float(weight.value)
        bmi_value = round(weight_value / (height_value ** 2), 2)
        bmi.value = f"BMI: {bmi_value}"

        if bmi_value < 18.5:
            status.value = "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            status.value = "Normal"
        elif 25 <= bmi_value < 29.9:
            status.value = "Overweight"
        else:
            status.value = "Obese"

        page.update()

    btn = ft.FilledTonalButton("Calculate BMI", icon=ft.Icons.CALCULATE, on_click=calculate_bmi)

    app_content = ft.Container(
        ft.Column([
            ft.Text("BMI Calculator", size=36),
            ft.Divider(height=1, color="#FFFFFF"),
            height,
            weight,
            btn,
            bmi,
            status
        ]),
        padding=20, border_radius=10, bgcolor="#1A1A1D"
    )

    page.add(app_content)

# ! Run the app
ft.app(main)