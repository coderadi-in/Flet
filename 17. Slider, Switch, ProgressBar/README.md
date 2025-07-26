# 🎚️ Day 17 – Slider, Switch, and ProgressBar in Flet

## 🎯 Goals
- Learn to collect user input using sliders and switches
- Understand visual progress representation with ProgressBar
- Add interactivity and state handling to these controls

---

## 🎛️ 1. Slider

A slider allows users to select a value from a continuous range.

### ✅ Basic Usage:
```python
import flet as ft

def main(page: ft.Page):
    def slider_changed(e):
        txt.value = f"Value: {e.control.value}"
        txt.update()

    txt = ft.Text()
    slider = ft.Slider(min=0, max=100, divisions=10, on_change=slider_changed)

    page.add(txt, slider)

ft.app(target=main)
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `min` | Minimum value |
| `max` | Maximum value |
| `divisions` | Number of discrete steps |
| `value` | Default value |
| `on_change` | Callback on value change |
| `label` | Label to show current value |

---

## 🔘 2. Switch

Used for binary (on/off) toggling.

### ✅ Example:
```python
def main(page: ft.Page):
    def on_switch_change(e):
        txt.value = "ON" if e.control.value else "OFF"
        txt.update()

    txt = ft.Text("OFF")
    sw = ft.Switch(value=False, on_change=on_switch_change)

    page.add(txt, sw)

ft.app(target=main)
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `value` | Initial state (True/False) |
| `label` | Optional text label |
| `on_change` | Callback function |
| `active_color` | Color when ON |

---

## 📊 3. ProgressBar

Shows indeterminate or determinate loading status.

### ✅ Determinate ProgressBar:
```python
progress = ft.ProgressBar(value=0.5, color="blue")
```

### ✅ Indeterminate ProgressBar:
```python
progress = ft.ProgressBar(value=None, color="green")
```

### 🛠️ Parameters:
| Parameter | Description |
|-----------|-------------|
| `value` | Float (0 to 1), or `None` for indeterminate |
| `color` | Bar color |
| `bgcolor` | Background color |

---

## 🔁 Example: Simulate Progress

```python
import flet as ft
import time

def main(page: ft.Page):
    bar = ft.ProgressBar(width=400)
    page.add(bar)

    for i in range(0, 101, 10):
        bar.value = i / 100
        bar.update()
        time.sleep(0.1)

ft.app(target=main)
```

---

## 🧪 Practice Set

1. Create a slider that adjusts font size of a text dynamically.
2. Add a switch to toggle dark/light mode (background color).
3. Display a progress bar that increases when a button is clicked.
4. Build a timer using a slider + determinate progress bar.
5. Create a toggleable switch that shows ON/OFF status dynamically.

---

## 🧩 Mini Challenge

**Build a Volume Controller**
- Use a `Slider` to adjust volume (0–100)
- Add a `Switch` to toggle mute/unmute
- Use a `Text` label to show "Muted" or volume value
- Optional: show dynamic color based on volume range (low/medium/high)
