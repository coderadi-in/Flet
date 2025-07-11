# Day 5: Buttons & Event Handling in Flet

---

## 🧩 Types of Buttons

### ✅ ElevatedButton
```python
ElevatedButton(text="Submit", on_click=handle_submit)
```

### ✅ TextButton
```python
TextButton(text="Cancel", on_click=handle_cancel)
```

### ✅ OutlinedButton
```python
OutlinedButton(text="View", on_click=handle_view)
```

### ✅ IconButton
```python
IconButton(icon=icons.EDIT, on_click=handle_edit)
```

### ✅ FloatingActionButton
```python
FloatingActionButton(icon=icons.ADD, on_click=handle_add)
```

---

## ⚡ Event Handling in Flet

```python
def handle_click(e):
    print("Button clicked")
    page.controls.append(Text("You clicked!"))
    page.update()
```

- `e.control` – button that triggered
- `e.data` – custom data
- `e.page` – page reference

---

## 🔁 Updating the UI

- Use `control.update()` for individual updates
- Use `page.update()` for global UI refresh

---

## 🧠 Practice Tasks

### ✅ Task 1: Click Counter
- Button "+"
- Label with counter value
- Increments on each click

### ✅ Task 2: Show/Hide Password
- Password `TextField`
- Show/Hide toggle using `TextButton`

---

## 💡 Mini Project: Mood Logger

- Emoji buttons: 😄 😐 😢
- Append selected mood to a visible log
- Show date-time with each entry
- Use `Column` to display the log

---

## 🧾 Summary Table

| Button Type         | Purpose                          |
|---------------------|----------------------------------|
| `ElevatedButton`    | Primary action, raised style     |
| `TextButton`        | Minimal, flat action             |
| `OutlinedButton`    | Secondary neutral action         |
| `IconButton`        | Action with icon only            |
| `FloatingActionButton` | Floating action (mobile-like) |
