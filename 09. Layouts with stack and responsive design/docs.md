# ✅ Day 09: Layout — Stack & Responsive Design in Flet

---

## 🎯 Goals

- Use `Stack` to layer UI elements
- Position controls absolutely within containers
- Build floating or overlapping components
- Use `ResponsiveRow` for adaptive layouts
- Build mobile-friendly responsive UIs

---

## 🔷 Part 1: Stack — Layered Layout

### ✅ What is Stack?

A container that **overlaps multiple controls**, useful for:

- Floating buttons
- Overlay banners
- Cards with badges
- Profile avatars over covers

### 🔧 Syntax Example:

Stack(
    controls=[
        Container(bgcolor="red", width=300, height=300),
        Container(bgcolor="blue", width=150, height=150, left=50, top=50),
        Container(bgcolor="green", width=60, height=60, bottom=10, right=10)
    ]
)

---

## ⚙️ Stack Properties

- controls: list of children
- expand: makes Stack fill its parent
- clip_behavior: controls overflow handling
- left / top / right / bottom: absolute positioning for children

---

## 🧠 Stack Practice

### ✅ Task 1: Overlapping Boxes
- Create red background box
- Place blue box over it (offset left=50, top=50)
- Add green circle on bottom-right corner

### ✅ Task 2: Floating Button UI
- Background image
- FloatingActionButton on top-right

---

## 🔷 Part 2: Responsive Layouts

### ✅ What is Responsive Design?
Build UIs that adapt to screen size (desktop/tablet/mobile)

---

## 🧰 Tools for Responsiveness in Flet

### 1. ResponsiveRow

ResponsiveRow([
    Container(Text("Card"), col={"xs": 12, "sm": 6, "md": 4})
])

- `col`: Controls width per screen size
- `xs`: Extra small (mobile)
- `sm`: Small (tablet)
- `md`: Medium (desktop)

### 2. expand=True

Use `expand=True` in `Row` or `Column` to auto-fill available space.

### 3. scroll="auto"

Use in parent container to enable scroll for small screen overflow.

---

## 🧠 Responsive Practice

### ✅ Task 1: Three Cards Grid
- Create 3 containers (cards)
- Use `ResponsiveRow`
- `col={"xs": 12, "sm": 6, "md": 4}`

### ✅ Task 2: Profile Section
- Left: Avatar + name
- Right: Bio + button
- Collapse into a column layout on mobile using `ResponsiveRow`

---

## 💡 Bonus Challenge

### Responsive Feature Grid (6 items)
- Use ResponsiveRow
- Add 6 items with icons + labels
- On mobile: stack vertically
- On desktop: show 3 in a row

---

## 🧾 Summary Table

| Feature          | Description                              |
|------------------|------------------------------------------|
| Stack            | Overlaps child widgets                   |
| left, top, etc.  | Position child inside Stack              |
| ResponsiveRow    | Responsive grid row                      |
| col              | Defines column span for breakpoints      |
| expand           | Makes control stretch to available width |
| scroll="auto"    | Enables scroll if overflow occurs        |
