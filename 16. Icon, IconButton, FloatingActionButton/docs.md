
# 🔘 Day 16 – Icon, IconButton & FloatingActionButton in Flet

## 🎯 Goals
- Learn to use Icons in UI
- Add interaction using IconButton
- Use FloatingActionButton (FAB) for key actions

---

## 🔤 1. Icon Control

Flet provides a wide variety of icons using the `ft.Icons` module.

### ✅ Usage:
```python
import flet as ft

icon = ft.Icon(name=ft.Icons.HOME, size=30, color="blue")
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `name`    | Icon name from `ft.Icons` |
| `size`    | Icon size (int) |
| `color`   | Color name or hex code |

---

## 🖱️ 2. IconButton

Clickable icon with ripple effect, used like buttons with minimal UI.

### ✅ Example:
```python
ft.IconButton(
    icon=ft.Icons.ADD,
    icon_color="green",
    on_click=lambda e: print("Add clicked")
)
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `icon` | Icon name |
| `icon_color` | Color of icon |
| `selected_icon` | Optional icon for toggling |
| `tooltip` | Hover tooltip |
| `on_click` | Callback function |

---

## 💡 3. FloatingActionButton (FAB)

A floating circular button used for primary screen actions (like in mobile apps).

### ✅ Example:
```python
ft.FloatingActionButton(
    icon=ft.Icons.NAVIGATE_NEXT,
    bgcolor="blue",
    on_click=lambda e: print("Next clicked")
)
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `icon` | Main icon |
| `bgcolor` | Background color |
| `tooltip` | Description text |
| `mini` | Smaller FAB (bool) |

---

## 🔁 4. Toggle IconButton Example

```python
def main(page: ft.Page):
    liked = False

    def toggle(e):
        nonlocal liked
        liked = not liked
        icon_btn.icon = ft.Icons.FAVORITE if liked else ft.Icons.FAVORITE_BORDER
        icon_btn.icon_color = "red" if liked else "black"
        icon_btn.update()

    icon_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER,
        icon_color="black",
        on_click=toggle
    )

    page.add(icon_btn)

ft.app(target=main)
```

---

## 📚 Common Icons in `ft.Icons`

| Icon Name | Use Case |
|-----------|----------|
| `ADD` | Add item |
| `DELETE` | Delete item |
| `HOME` | Navigate to home |
| `FAVORITE` / `FAVORITE_BORDER` | Like / Unlike |
| `ARROW_FORWARD`, `ARROW_BACK` | Navigation |
| `SEARCH`, `MORE_VERT`, `MENU` | UI controls |

---

## 🧪 Practice Set

1. Display 5 icons in a `Row` with different colors and tooltips.
2. Create a toggleable like button (`IconButton`).
3. Add a FAB that shows an alert/snackbar on click.
4. Create a top bar with a few IconButtons aligned to the right.
5. Use an IconButton to toggle the visibility of a `TextField`.

---

## 🛠️ Mini Challenge

**🔧 Build a Quick Action Bar**  
- Use `Row` and `IconButtons` for actions: Add, Edit, Delete, Share  
- Highlight the selected icon  
- On click, show a `SnackBar` describing the action
