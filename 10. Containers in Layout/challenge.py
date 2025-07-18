'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Challenge - day 10"

    feature_card = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.CircleAvatar(content=ft.Image('pic.png', height=50, width=50, border_radius=50), width=50),
                ft.Text(value="BMW M4", size=32, color="#FFFFFF")
            ]),
            ft.Text("The New M4 Competition M xDrive combines aesthetics and the sportiness you expect from BMW M. A wealth of technologies from the motorsports sector enhance the driving dynamics of the M4, thus delivering on the racetrack as well as in everyday driving. The power output sees an upgrade, the iconic S58 inline-6 engine now pushes out a mighty 390 kW (530 hp) in the BMW M4 Competition Coupé with M xDrive. Discover the New BMW M4 Competition M xDrive with exciting equipment options, technical data, and a wide range of financing options.", color="#FFFFFF")
        ], spacing=10),
        padding=10, border_radius=10, bgcolor="#212122", border=ft.border.all(2, "#FFFFFF"),
        col={
            "xs": 12,
            "md": 6,
            "xl": 4
        }
    )

    feature_row = ft.ResponsiveRow([feature_card for _ in range(6)])

    page.add(feature_row)

# ! Run the app
ft.app(main)