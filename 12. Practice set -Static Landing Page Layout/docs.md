
# Day 12: Practice Set 2 – Static Landing Page Layout

## 🎯 Goals
- Apply layout fundamentals to build a modern landing page UI
- Strengthen your command on Row, Column, Container, alignment, etc.
- Create clean static UI using real-world components

---

## 🧱 What You'll Build

A simple, clean layout like:

```
--------------------------------------------------
| Coderadi Logo        [Home] [About] [Contact] |
--------------------------------------------------

|          Hero Section                          |
|  "Build better apps" + CTA Button              |
|                                                |
--------------------------------------------------

|       Features Section (3 Cards)               |
|  Icon + Title + Description                    |
--------------------------------------------------

|              Footer                            |
|  © 2025 Coderadi | Built with Flet             |
--------------------------------------------------
```

---

## 🛠️ Widgets & Tools

- Row, Column, Container
- ResponsiveRow
- Text, ElevatedButton, Icon
- Divider
- CrossAxisAlignment, MainAxisAlignment
- Container(expand=True) for spacing

---

## 🧠 Step-by-Step Guide

### 1. Header / Navigation Bar

```python
ft.Row([
    ft.Text("coderadi.in", size=22, weight="bold"),
    ft.Container(expand=True),
    ft.Text("Home"),
    ft.Text("About"),
    ft.Text("Contact")
], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
```

---

### 2. Hero Section

```python
ft.Container(
    content=ft.Column([
        ft.Text("Build Better Apps with Flet", size=32, weight="bold"),
        ft.ElevatedButton("Get Started")
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
    height=300,
    bgcolor="#1e1e2f",
    padding=20
)
```

---

### 3. Features Section (Cards)

```python
ft.ResponsiveRow([
    feature_card("⚡", "Fast UI", "Quickly prototype apps."),
    feature_card("🎨", "Modern Design", "Sleek & customizable."),
    feature_card("🔧", "Easy Code", "Powered by Python.")
], col={"xs": 12, "md": 4}, spacing=15)

def feature_card(icon, title, desc):
    return ft.Container(
        content=ft.Column([
            ft.Text(icon, size=40),
            ft.Text(title, size=20, weight="bold"),
            ft.Text(desc)
        ],
        alignment=ft.MainAxisAlignment.START),
        padding=20,
        bgcolor="#2c2c31",
        border_radius=10
    )
```

---

### 4. Footer

```python
ft.Divider(),
ft.Container(
    ft.Text("© 2025 Coderadi • Built with Flet", size=12),
    alignment=ft.alignment.center,
    padding=15
)
```

---

## 💡 Challenge

Recreate the landing page using only layout widgets. No logic required. Structure should be responsive and modular.

---

## 🔁 Optional Stretch Goals

- Sticky header
- Hover effects
- Icons from `ft.icons` instead of emoji
