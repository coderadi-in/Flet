
# Day 3: Input Controls in Flet

## 🧩 Controls Covered:
- TextField
- Checkbox
- Dropdown
- RadioGroup

---

## 🔹 TextField

```python
ft.TextField(label="Your Name", hint_text="e.g. Adi", width=300)
```

- `value`: the text input
- Events: `on_change`, `on_submit`

---

## 🔹 Checkbox

```python
ft.Checkbox(label="Subscribe", value=False)
```

- `value`: True/False
- Event: `on_change`

---

## 🔹 Dropdown

```python
ft.Dropdown(
    width=300,
    options=[ft.dropdown.Option("Python"), ft.dropdown.Option("Flet")]
)
```

- `value`: selected option
- Event: `on_change`

---

## 🔹 RadioGroup

```python
ft.RadioGroup(
    content=ft.Column([
        ft.Radio(label="Light", value="light"),
        ft.Radio(label="Dark", value="dark")
    ]),
    value="light"
)
```

- Single-choice selector
- `value`: selected option
- Event: `on_change`

---

## 🛠️ Mini Form App (Code)

```python
import flet as ft

def main(page: ft.Page):
    name = ft.TextField(label="Name")
    lang = ft.Dropdown(
        options=[
            ft.dropdown.Option("Python"), 
            ft.dropdown.Option("Flet")
        ]
    )
    agree = ft.Checkbox(label="Accept Terms")
    mode = ft.RadioGroup(
        value="light",
        content=ft.Row([
            ft.Radio(label="Light", value="light"),
            ft.Radio(label="Dark", value="dark")
        ])
    )
    result = ft.Text()

    def submit(e):
        result.value = (
            f"Name: {name.value}\nLang: {lang.value}\n"
            f"Accepted: {agree.value}\nTheme: {mode.value}"
        )
        page.update()

    page.add(name, lang, agree, mode, ft.ElevatedButton("Submit", on_click=submit), result)

ft.app(main)
```

---

## ✅ Challenge:
Create a Feedback Form with:
- Name
- Feedback (multiline TextField)
- Recommend us? (Yes/No RadioGroup)
- Share email? (Checkbox)
- Summary on Submit

---

# End of Day 3
