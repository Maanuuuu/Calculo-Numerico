import flet as ft


def main(page: ft.Page):
    page.window_center()
    page.window_resizable=False
    page.window_width=800
    page.window_height=500
    page.padding=50
    page.theme_mode=ft.ThemeMode.LIGHT
    page.bottom_appbar
    
    def dropclicked(e):
        dp2.options.clear()
        dp2.value=None
        tf1.value=None
        tf2.value=None
        options=["Decimal","Binario","Octal","Hexadecimal"]
        if dp1.value in options:
            options.remove(dp1.value)
            for i in range(len(options)):
                dp2.options.append(ft.dropdown.Option(options[i]))
        dp2.disabled=False
        page.update()
    
    def determinar_base(value):
        if value=="Decimal":
            base=10
        elif value=="Binario":
            base=2
        elif value=="Octal":
            base=8
        elif value=="Hexadecimal":
            base=16
    
        return base
    
    
        
    dp1=ft.Dropdown(
        width=130,
        height=50,
        text_size=16,
        on_change=dropclicked,
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
            
            
        ])
    
    base1=base2=0
    def dp2bases(e):
        global base1
        global base2
        base1=determinar_base(str(dp1.value))
        base2=determinar_base(str(dp2.value))
        
    def base_a_decimal(numero, base):
        decimal = 0
        for i in range(len(numero)):
            digito = int(numero[len(numero) - 1 - i], base)
            decimal += digito * (base ** i)
        return decimal

    def decimal_a_base(decimal, base):
        if decimal == 0:
            return "0"

        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while decimal > 0:
            resultado = caracteres[decimal % base] + resultado
            decimal //= base

        tf2.value=resultado
        page.update()
        
    def proceso(e):
        global base2
        global base1
        deci=base_a_decimal(str(tf1.value),base1)
        decimal_a_base(deci,base2)
        
        
    dp2=ft.Dropdown(
        text_size=16,
        height=50,
        width=130,
        disabled=True,
        on_change=dp2bases
            
        )
    
    tf1=ft.TextField(
                     
                     border=True,
                     border_radius=10,
                     width=300,
                     height=200,
                     text_size=20,
                     multiline=True,
                     min_lines=5,
                     max_lines=5,
                     fill_color=ft.colors.WHITE,
                     filled=True,
                     label_style=ft.TextStyle(size=15,color=ft.colors.BLACK),
                     border_width=2,
                     border_color=ft.colors.BLACK
                     )
    
    tf2=ft.TextField(
                     read_only=True,
                     border=True,
                     border_radius=10,
                     width=300,
                     height=200,
                     text_size=20,
                     multiline=True,
                     min_lines=5,
                     max_lines=5,
                     fill_color=ft.colors.WHITE,
                     filled=True,
                     label_style=ft.TextStyle(size=15,color=ft.colors.BLACK),
                     border_width=2,
                     border_color=ft.colors.BLACK
                     )
    

              
    
    
    ejecutar=ft.FilledButton(text="Ejecutar",width=200,height=45,on_click=proceso)
    texto=ft.Text("Convertir numero de: ",size=20)
    texto2=ft.Text(" a: ",size=20)
    
    
    
    page.add(ft.Column(controls=[
        ft.Row(controls=[texto,dp1,texto2,dp2]),
        ft.Container(height=0),
        ft.Row(controls=[tf1,tf2],alignment=ft.MainAxisAlignment.CENTER,spacing=50),
        ft.Row(controls=[ejecutar],alignment=ft.MainAxisAlignment.CENTER,spacing=50)
        ],spacing=20))
    page.update()
    

ft.app(target=main)
