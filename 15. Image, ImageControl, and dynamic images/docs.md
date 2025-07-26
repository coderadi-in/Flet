
# 📸 Day 15 – Image, ImageControl, and Dynamic Images in Flet

## 🎯 Goals
- Learn how to display static and dynamic images
- Use `Image` control for both local and network assets
- Understand layout sizing and behavior for images
- Handle image updates dynamically

---

## 📦 1. Image Basics

Flet uses the `Image` control to display images.

### ✅ Import:
```python
import flet as ft
```

### ✅ Basic Usage:
```python
img = ft.Image(src="https://picsum.photos/300", width=300, height=200)
```

| Parameter | Description |
|----------|-------------|
| `src`    | URL or local path to the image |
| `width`  | Width of the image |
| `height` | Height of the image |
| `fit`    | Controls image fitting (`BoxFit.CONTAIN`, `BoxFit.COVER`, etc.) |

---

## 🌐 2. Remote Image Example (Network)

```python
ft.Image(src="https://placekitten.com/400/300", fit=ft.ImageFit.COVER)
```

### 🔁 Image Fit Options:
- `ImageFit.CONTAIN`
- `ImageFit.COVER`
- `ImageFit.FILL`
- `ImageFit.NONE`
- `ImageFit.SCALE_DOWN`

---

## 🖼️ 3. Local Image Usage

```python
ft.Image(src="assets/images/sample.png")
```

⚠️ Make sure the image is inside your `assets/` folder and added in your app’s `pubspec.yaml` or properly referenced in the Flet `build` if configured.

---

## 🧠 4. Dynamically Change Image on Click

```python
def main(page: ft.Page):
    current_img = ft.Image(src="https://placekitten.com/200/300", width=200)

    def change_image(e):
        current_img.src = "https://placebear.com/200/300"
        current_img.update()

    btn = ft.ElevatedButton("Change Image", on_click=change_image)

    page.add(ft.Column([current_img, btn]))

ft.app(target=main)
```

---

## 📦 5. More `Image` Properties

| Property         | Use |
|------------------|-----|
| `repeat`         | Repeat behavior |
| `border_radius`  | Rounded corners |
| `tooltip`        | Hover tooltip text |
| `semantic_label` | Accessibility label |
| `gapless_playback` | Prevents flicker on update |

---

## 🧪 Practice Set

1. Display 3 images in a horizontal `Row`.
2. Create a button that cycles through 3 random image URLs.
3. Load a user-inputted image URL in a `TextField` and show the image.
4. Use `border_radius` to make circular profile-like images.
5. Build an image grid using `ResponsiveRow`.

---

## 🛠️ Mini Challenge (Optional)

Create a “Random Image Generator”:
- Button to fetch a random image from [picsum.photos](https://picsum.photos)
- Display with dynamic size
- Responsive layout on small/large screen
