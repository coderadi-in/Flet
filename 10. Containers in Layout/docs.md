# ✅ Day 10: Containers in Layouts

---

## 🎯 Goals

- Understand Container as the fundamental layout wrapper in Flet
- Use it for spacing, background, borders, radius, alignment
- Combine with layout widgets like Row, Column, Stack
- Create reusable UI card structures

---

## 📦 What is Container?

A `Container` in Flet wraps any widget to style or position it using:
- Padding & margin
- Background color / image
- Borders & radius
- Alignment
- Width & height
- Ink effects & tap handlers

---

## 🔧 Container Syntax

```python
ft.Container(
    child,
    width=200,
    height=100,
    padding=10,
    bgcolor="blue",
    border_radius=8
)
```

---

## 🔹 Common Container Properties

| Property         | Description                                |
|------------------|--------------------------------------------|
| `content` / `child` | Inner element (Text, Column, etc.)       |
| `width` / `height` | Fixed dimensions                          |
| `padding`         | Inner spacing                             |
| `margin`          | Outer spacing                             |
| `bgcolor`         | Background color                          |
| `image_src`       | Background image                          |
| `border`          | Borders using `ft.border.all()`           |
| `border_radius`   | Rounded corners                           |
| `alignment`       | Align child inside container              |
| `expand`          | Fill parent area                          |
| `ink`             | Enable ripple effect on tap               |
| `on_click`        | Tap action                                |

---

## 🧪 Examples

### ✅ 1. Padding & Margin

```python
ft.Container(
    ft.Text("Padded Box"),
    padding=20,
    margin=10,
    bgcolor="green"
)
```

### ✅ 2. Border and Radius

```python
ft.Container(
    ft.Text("With Border"),
    border=ft.border.all(2, "white"),
    border_radius=10
)
```

### ✅ 3. Alignment Inside Container

```python
ft.Container(
    ft.Text("Bottom Center"),
    alignment=ft.alignment.bottom_center,
    width=300,
    height=200,
    bgcolor="black"
)
```

### ✅ 4. Background Image

```python
ft.Container(
    ft.Text("Over image", color="white"),
    image_src="https://picsum.photos/400",
    alignment=ft.alignment.bottom_left,
    padding=20
)
```

### ✅ 5. Clickable Ink Effect

```python
ft.Container(
    ft.Text("Tap Me"),
    ink=True,
    on_click=lambda e: print("Clicked!"),
    bgcolor="purple",
    padding=15
)
```

---

## 🧠 Practice Tasks

### 🟡 Task 1: Basic Card
- Create a container with text
- Padding: 20
- Background: #1e1e2f
- Border radius: 10

### 🟡 Task 2: Image Card
- Use `image_src`
- Overlay text aligned bottom-left
- Add border

### 🟡 Task 3: Profile Card
- Use Column inside Container
- Image avatar (circle), name, short bio
- Padding + centered alignment

---

## 💡 Mini Project: Feature Grid

Build a 6-card feature section using:

- `ResponsiveRow`
- Each card as a styled `Container`
- Icon + title + description inside each card
- Background + padding + rounded corners
- Responsive layout (col = {"xs": 12, "sm": 6, "md": 4})

---

## 🔚 Summary

- Containers = core of layout building
- Combine with Row, Column, Stack
- Style every control with margin, padding, background, radius
- Useful for cards, sections, panels, buttons, overlays
