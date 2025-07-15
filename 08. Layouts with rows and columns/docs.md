# ✅ Day 08: Layouts with Row and Column in Flet

---

## 🎯 Goals

- Understand layout containers in Flet: `Row` and `Column`
- Learn alignment, spacing, and nesting
- Practice responsive UI layouts
- Build practical structures using these containers

---

## 🧩 What are `Row` and `Column`?

### Row
Arranges child elements horizontally.

Example:
```python
Row([
    Text("Left"),
    Text("Right")
])
```

### Column
Arranges child elements vertically.

Example:
```python
Column([
    Text("Top"),
    Text("Bottom")
])
```

---

## ⚙️ Common Properties

- alignment: aligns children inside the container
- vertical_alignment (Row): top, center, bottom
- horizontal_alignment (Column): start, center, end
- spacing: space between children
- wrap (Row): wraps items to next line if needed
- expand: fills remaining space

---

## 🧱 Layout Examples

### Horizontal Button Group
```python
Row([
    ElevatedButton("Yes"),
    ElevatedButton("No")
], spacing=10)
```

### Profile Card Layout
```python
Row([
    Image(src="avatar.png", width=50),
    Column([
        Text("John Doe"),
        Text("Developer")
    ])
])
```

---

## 🧠 Practice Set – Day 08

### ✅ Task 1: Horizontal Navigation Bar

- Use Row
- Add 3 TextButtons: Home, About, Contact
- Center align them

### ✅ Task 2: Two-Column Layout

- Left Column: Name and Email TextFields
- Right Column: Live preview of input
- Use Row with two Columns inside

---

## 💡 Bonus Challenge: Dashboard Header

Layout:
[Logo]     [Dashboard Title]                [User Avatar]

- Use Row with alignment = "spaceBetween"
- Add margins and spacing
- Try wrapping it in a Container

---

## 🧾 Summary Table

Feature                 | Description
------------------------|---------------------------------
Row                     | Horizontal layout
Column                  | Vertical layout
spacing                 | Space between child controls
alignment               | Aligns children inside container
expand                  | Makes child fill extra space
nesting                 | Layout inside layout
