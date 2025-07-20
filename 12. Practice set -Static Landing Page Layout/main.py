'''coderadi'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Practice set - 02: Static Landing Page Layout"
    page.padding = ft.padding.symmetric(20, 50)

    # * function to create a feature card
    def feature_card(icon: str, title: str, desc: str) -> ft.Container:
        return ft.Container(
            ft.Column([
                ft.Row([
                    ft.Text(icon, size=50),
                    ft.Text(title, size=36)
                ], spacing=10, alignment=ft.alignment.center),
                ft.Text(desc)
            ], spacing=20),
            padding=20, border_radius=20,
            bgcolor="#212122"
        )

    # & Header
    header = ft.Row([
        # | Title
        ft.Row([
            ft.Image("logo.png", width=50, height=50, border_radius=50),
            ft.Text("$CODERADI>", size=36)
        ], spacing=ft.alignment.center),

        ft.Container(expand=True),

        # | Navbar (links)
        ft.Row([
            ft.Text("Home", size=16),
            ft.Text("About", size=16),
            ft.Text("Contact", size=16)
        ], spacing=10)
    ], alignment=ft.alignment.center)

    # & Hero section
    hero = ft.Column([
        ft.Text("Build better apps.", size=64, weight=ft.FontWeight.BOLD),
        ft.Row([
            ft.FilledButton("Get started", width=150),
            ft.OutlinedButton("Explore gallery", width=150)
        ], spacing=10)
    ], spacing=20, horizontal_alignment=ft.MainAxisAlignment.CENTER)

    # & Features section
    features = ft.ResponsiveRow([
        feature_card("⚡", "Fast UI", "Quickly prototype apps."),
        feature_card("🎨", "Modern Design", "Sleek & customizable."),
        feature_card("🔧", "Easy Code", "Powered by Python.")
    ], spacing=20, col={
        "xs": 12,
        "md": 4
    })
    
    # & Footer section
    footer = ft.Column([
        ft.Divider(height=1, color='white'),
        ft.Text("© 2025 Coderadi • Built with Flet", size=12, text_align=ft.TextAlign.CENTER)
    ], alignment=ft.alignment.center)

    # * Adding elements to the page
    page.add(
        ft.Column([
            header,
            hero,
            features,
            footer
        ], spacing=50)
    )

# ! Run the app
ft.app(main)