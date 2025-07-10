# 01. Intro

## 1.1 What is Flet ?
Flet is a Python-based framework for building real-time, interactive frontend applications without needing HTML/CSS/JS. Think of it like Flutter for Python - it let's you create UI using Flutter widgets directly in Python.

### In simple terms:
> Flet = Python + Flutter-like UI = Web/Desktop/Mobile apps with one codebase.

## 1.2 Why use Flet ?
- **Write UI in Python**, not HTML/CSS/JS.
- Real-time state syncing and hot reload.
- Build for **Web**, **Desktop (Windows/macOS/Linux)**, and **Mobile** (PWA-style).
- Uses Flutter's rendering engine under the hood.
- Super productive for internal tools, dashboards, and UI-rich apps

## 1.3 Installation of Flet
> Lets set up Flet in your dev environment.

### Step 1: Set up a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On windows: .venv\Scripts\activate
```

### Step 2: Install Flet

```bash
pip install flet
```

### Step 3: Verify Installation
Create a file called `main.py`:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Hello, Flet!"
    page.add(ft.Text("Welcome to Flet"))

ft.app(target=main)
```

Run it:
```bash
python main.py
```

This will open a local window (desktop) and run your Flet app.

## 1.4 Flet Architecture (How it works internally)
Here's a simplified view of **Flet architecture**:

```less
[ Your Python Code]
         |
     [Flet SDK]
         |
  [ WebSocket Bridge ]
         |
[Flutter frontend engine (Browser or Desktop window)]
```

### Key Points:
- Your Python code runs a **server**.
- The frontend in rendered using **Flutter**, either in a browser or window.
- Python and Flutter communicate via **WebSocket** (like a live chat between frontend and backend).

## 1.5 Web, Desktop, and Mobile Support

Platform | Mode | How to Run
-|-|-
Web | Localhost/PWA | `flet.app(target=main, view=WEB_BROWSER)`
Desktop | Flutter-rendered window | Default: `flet.app(target=main)`
Mobile | Browser + Add to Home Screen | Host it on a server (Flet Cloud or custom)

> You write **one codebase**, and Flet makes it run on all platforms.

## 1.6 Recap for Day 1:
- Flet is a Python UI frameword built on top of Flutter.
- It supports Desktop, Web, and Mobile (via PWA).
- Installs easily via pip in runs with `flet.app(...)`.
- You build interfaces using Python objects (like `ft.Text`, `ft.Column`, etc.).
- It uses WebSocket to sync the Python backend and Flutter frontend.
