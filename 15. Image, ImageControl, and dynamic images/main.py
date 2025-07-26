'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "15. Image, ImageControl, and dynamic images"

    img = ft.Image(
        src="car3.png",
        width=300,
        height=300
    )
    
    img2 = ft.Image(
        src="https://picsum.photos/seed/picsum/200/300",
        width=640,
        height=360
    )

    page.add(img, img2)

# ! Run the app
ft.app(main)