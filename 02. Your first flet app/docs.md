# 02. Your first flet app

## 2.1 Your first flet app (Basic UI)
```python
def first_app(page: ft.Page):
    page.title = "My first flet app"

    txt = ft.Text("Hello, Adi 👋!", size=24)

    # * on_click function
    def on_click(e):
        txt.value = "Button clicked!"
        page.update()

    btn = ft.ElevatedButton("Click Me!", on_click=on_click)
    page.add(txt, btn)

ft.app(first_app)
```

### 🔍What's happening here ?
Concept | Description
-|-
`page.title` | Sets the window/browser title
`Text(...)` | Adds a text widget
`ElevatedButton` | Creates a button
`on_click` | Event handler for the button
`page.add(...)` | Adds widgets to the page
`page.update()` | Refreshes the UI after the change

## 2.2 Step 2: Using `Column` to arrange vertically
```python
def app_with_columns(page: ft.Page):
    page.title = "Using Column"

    txt = ft.Text("Hi Adi, press the button 👇", size=20)

    def say_hello(e):
        txt.value = "You're doing awesome!"
        page.update()

    btn = ft.ElevatedButton("Say Hello", on_click=say_hello)

    layout = ft.Column(controls=[txt, btn], alignment=ft.MainAxisAlignment.CENTER)

    page.add(layout)

ft.app(app_with_columns)
```

### 🤔Why use `Column`?
- Makes vertical layout easier
- Allows you to align and space elements clearly
- Can nest more complex layous later (Rows inside Columns etc.)

## Step 3: Using `Rows` for horizontal layout
```python
def app_with_rows(page: ft.Page):
    page.title = "Using Row"

    btn1 = ft.ElevatedButton("Left")
    btn2 = ft.ElevatedButton("Right")

    row = ft.Row(controls=[btn1, btn2], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(row)

ft.app(app_with_rows)
```

> Combine `Row` and `Column` for grids, forms, navbars, etc.

## Pro Tips:
- Use `.alignment` to control layout (`START`, `CENTER`, `END`, `SPACE_BETWEEN`, etc.)
- `page.add(...)` can take multiple controls or a layout like `Column/Row`
- Always call `page.update()` if you're changing values dynamically (e.g., `Text.value`)

## 🧪 Challenge for Today
**Build a small app with this structure:**
```makefile
Title: Flet Counter
Text: Count = 0
[ + ]     [ Reset ]     [ - ]
```