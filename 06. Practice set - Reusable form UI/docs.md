# 📝 Day 06: Reusable Form UI Practice

---

## 🎯 Goals
- Build a styled user input form
- Add validation logic
- Learn to update UI dynamically
- Structure form in a reusable card layout

---

## 🧩 Components Used
- TextField – Full Name, Email
- Dropdown – Gender
- Checkbox – Terms acceptance
- ElevatedButton – Submit
- Text / SnackBar / Dialog – Feedback

---

## 💡 Reusable Component Function

```python
def user_form_card():
    return Container(
        content=Column([...]),
        padding=20,
        bgcolor="#f8f8f8",
        border_radius=12,
        width=400
    )
```

---

## ✅ Practice Set

### Task 1:
Build a form card with:
- Name
- Email
- Gender (dropdown)
- Terms (checkbox)
- Submit button

### Task 2:
Add validation:
- Required fields
- Valid email (`@` check)
- Checkbox must be checked

### Task 3:
Bonus: Add Reset Button

---

## 🧾 Summary

Feature           | Method
------------------|-----------------------------
Input collection  | .value of fields
Validation        | if not input.value: ...
Feedback          | Text, SnackBar, or Dialog
Reset             | input.value = "" + update()
