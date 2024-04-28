import flet as ft

def main(page):
    def Button_Clicked(e):
        page.add(ft.Text(f"\n{first_name.value} {last_name.value}",size=20))
    
    first_name = ft.TextField(text_size=20,height=60,width=300,label="Name")
    last_name = ft.TextField(text_size=20,height=60,width=300,label="Surname")
    c = ft.Column(controls=[
        first_name,
        last_name
        ])
    btn=ft.ElevatedButton("Agregar.",on_click=Button_Clicked)
    
    ft.Page.bgcolor=ft.colors.CYAN
    page.add(c,btn)
ft.app(target=main)