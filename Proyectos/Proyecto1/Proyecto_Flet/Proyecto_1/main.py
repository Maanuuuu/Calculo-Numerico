import flet as ft


def main(page: ft.Page):
    page.window_center()
    page.window_resizable=False
    page.window_width=800
    page.window_height=500
    page.padding=50
    page.theme_mode=ft.ThemeMode.LIGHT
    page.bottom_appbar
    
    
    switchi=ft.Dropdown(
        width=130,
        
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Hexadecimal"),
            
            
        ])
    
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
    
    def clicked(e):
        tf2.value=tf1.value
        page.update()
        
    def decimal(e):
        binario=float(tf1.value)
        decimal = 0
        i = 0
        while (binario>0):
            digito  = binario%10
            binario = int(binario//10)
            decimal = decimal+digito*(2**i)
            i = i+1
        
        tf2.value=int(decimal)
        
        tf1.focus()
        page.update()
    
    def hexadecimal(e):
        num_binario=str(tf1.value)
        num_decimal = int(num_binario, 2)
        tf2.value= hex(num_decimal)[2:]
        tf1.focus()
        page.update()

    def binario_to_octal(e):
        num_binario=tf1.value
        num_decimal = int(num_binario, 2)
        tf1.focus()
        tf2.value= oct(num_decimal)[2:]
        page.update()  
        
                  
    
    
    btn1=ft.FilledButton(text="Decimal",width=100,height=45,on_click=decimal)
    btn2=ft.FilledButton(text="Hexadecimal",width=140,height=45,on_click=hexadecimal)
    btn3=ft.FilledButton(text="Octal",width=100,height=45,on_click=binario_to_octal)
    texto=ft.Text("Conversion de Numero binario",size=20)
    
    page.add(ft.Column(controls=[
        ft.Row(controls=[texto,switchi],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=0),
        ft.Row(controls=[tf1,tf2],alignment=ft.MainAxisAlignment.CENTER,spacing=50),
        ft.Row(controls=[btn1,btn2,btn3],alignment=ft.MainAxisAlignment.CENTER,spacing=50)
        ],spacing=20))
    page.update()
    

ft.app(target=main)
