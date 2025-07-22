
# 💡 Day 14 – Mini Project: BMI Calculator

## 🎯 Goals
- Build a real-world calculator app UI
- Practice input handling, state updates, layout organization
- Use `TextField`, `ElevatedButton`, `Text`, and styling

---

## 📱 What You’ll Build

A clean and interactive BMI calculator that:

- Takes **height (cm)** and **weight (kg)** from user input
- Calculates BMI on button press
- Displays result + BMI category (Underweight, Normal, Overweight, Obese)
- Looks polished with a card layout

---

## ✏️ UI Layout Plan

```
-----------------------------
|        BMI Calculator     |
-----------------------------
| [ Height (cm) ]           |
| [ Weight (kg) ]           |
|                           |
|   [  Calculate BMI  ]     |
|                           |
| BMI: 23.5                 |
| Status: Normal            |
-----------------------------
```

---

## 🧠 Step-by-Step: Code Explanation

```python
import flet as ft

def main(page: ft.Page):
    page.title = "BMI Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    height_field = ft.TextField(label="Height (cm)", width=300, keyboard_type=ft.KeyboardType.NUMBER)
    weight_field = ft.TextField(label="Weight (kg)", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("", size=20, weight="bold")
    status_text = ft.Text("", size=16)

    def calculate_bmi(e):
        try:
            height = float(height_field.value) / 100
            weight = float(weight_field.value)
            bmi = round(weight / (height ** 2), 2)

            result_text.value = f"BMI: {bmi}"

            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"

            status_text.value = f"Status: {status}"

        except:
            result_text.value = "Invalid input"
            status_text.value = ""

        result_text.update()
        status_text.update()

    calc_button = ft.ElevatedButton("Calculate BMI", on_click=calculate_bmi)

    page.add(
        ft.Column([
            ft.Text("BMI Calculator", size=30, weight="bold"),
            height_field,
            weight_field,
            ft.Container(height=10),
            calc_button,
            result_text,
            status_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
```

---

## ✅ Features to Try

| Feature | Description |
|--------|-------------|
| 🎨 Theming | Use `page.bgcolor`, card-like containers |
| 💡 Status color | Change `status_text.color` based on result |
| 🧮 Reset Button | Add a button to clear the fields |
| 📱 Responsive | Wrap inputs inside a `ResponsiveRow` or limit width |
| 📐 Result Card | Show BMI & category inside a bordered `Container` |

---

## 🧪 Practice Set

1. Add BMI range info below result.
2. Validate inputs (no negative numbers).
3. Add a dropdown for gender (optional).
4. Save past BMI results in a list.
