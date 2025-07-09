# Day 4: Container and styling basics

## 🎯 Learning objectives
- Learn how to use `Container` to wrap and style elements
- Understand alignment, padding, margin, border radius, background color
- Practice creating styled UI blocks

## 🧱 1. What is `Container`?
A `Container` in Flet is a wrapper that allows you to sytle and layout child elements.

### Basic Syntax:
```python
flet.Container(
    content=Text("Hello, styled world!"),
    bgcolor="blue",
    padding=10,
    border_radius=5
)
```

Think of it as a `div` in HTML + CSS — it doesn't do anything functionally but controls layout, spacing, appearance.

## 🧩 2. Important Container Properties

### 📌 `content`
The child control placed inside the container.
```python
content=Text("Hello")
```

### 📐 `alignment`
Aligns content inside the container.
```python
alignment=flet.alignment.center
alignment=flet.alignment.top_left
```

### 🧻 `padding` & `margin`
You can use an integer (uniform) or `padding` object for fine-tuning.

```python
padding=20  # uniform
padding=padding.only(left=10, top=5)
```
```python
margin=10
```

### 🎨 `bgcolor` and `gradient`
Set background color or gradient.
```python
bgcolor="red"
gradient=LinearGradient(colors=["red", "blue"])
```

### 🔳 `border_radius` & `border`
Gives border design and radius.
```python
border_radius=10
border=flet.border.all(1, "black")
```

### ⚙️ `width` and `height`
Set fixed size or use `expand` to fill space.
```python
width=200
height=100
expand=True
```

### 🧊 `shape`, `blur`, `shadow`, `opacity`
For advanced visual effects:
```python
blur=5
shadow=flet.BoxShadow(...)
opacity=0.8
```

## 🛠️ 3. Layouting With Containers
You can use `Row`, `Column`, or nested `Containers` to design beautiful UIs. Here's a card-style layout:

```python
Container(
    content=Column([
        Text("Card Title", weight="bold"),
        Text("Card content goes here")
    ]),
    padding=20,
    bgcolor="#f0f0f0",
    border_radius=10,
    width=300
)
```

## 💡 Tip:
Use nested Containers to create layers, like:
- Outer container with margin
- Inner with padding + background

## 🧠 Practce Set - Day 04

### ✅ Task 1:
Create 3 containers:
- Red box 200x100 with center-aligned text
- Blue box with padding and rounded corners
- Green box with gradient background

### ✅ Task 2:
Design a "Profile Card":
- Avatar (use `Image` or placeholder `CirclrAvatar`)
- Name (bold text)
- Bio (description text)
- All wrapped in a styled container

## 🎯 Challenge (Optional Mini-project)
### 💡 "Login Card" UI Clone
Create a card-based login form with:
- Username and Password fields
- Login button
- Card-style layout with padding, background, rounded borders
- Centered in the page

## 🔚 Summary
Topic | Description
-|-
`Container` | Wrapper for lyout and styling
`alignment` | Controls child alignment
`padding`/`margin` | Space inside/outside
`bgcolor`/`border_radius` | Visual design
`width`/`height`/`expand` | Sizing