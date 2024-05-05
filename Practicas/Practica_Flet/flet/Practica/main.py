import flet as ft


def main(page: ft.Page):
    page.window_center()
    page.window_resizable=False
    page.window_width=800
    page.window_height=500
    page.padding=50
    page.theme_mode=ft.ThemeMode.LIGHT

    page.add(ft.Row([ft.ElevatedButton(text="ALO")]))
    
    
ft.app(target=main)
