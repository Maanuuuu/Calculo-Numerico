import flet as ft
import random as rd

def main(page: ft.Page):
    page.window_center()
    page.window_resizable=False
    page.window_width=1000
    page.window_height=600
    page.padding=20
    page.theme_mode=ft.ThemeMode.LIGHT
    
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
        tf1.read_only=False
        bs1=str(dp1.value)
        if bs1==("Decimal"):
            tf1.input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
        elif bs1==("Binario"):
            tf1.input_filter=ft.InputFilter(allow=True, regex_string=r"[0-1]", replacement_string="")
        elif bs1==("Octal"):
            tf1.input_filter=ft.InputFilter(allow=True, regex_string=r"[0-7]", replacement_string="")
        elif bs1==("Hexadecimal"):
            tf1.input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9ABCDEF]", replacement_string="")
        
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
    
    
        
     
    base1=base2=0
    def dp2bases(e):
        global base1
        global base2
        base1=determinar_base(str(dp1.value))
        base2=determinar_base(str(dp2.value))
        tf2.value=None
        page.update()


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
        try:
            deci=base_a_decimal(str(tf1.value),base1)
            decimal_a_base(deci,base2)
            tf1.focus()
            
        except Exception:
            print("Operacion Invalida")

    def cambio_pag(e):
        if rail.selected_index==0:
            General_Row.controls.clear()
            General_Row.controls.append(rail)
            General_Row.controls.append(ft.VerticalDivider(width=1,color=ft.colors.BLACK45))
            General_Row.controls.append(pagina1)
            dp1.value=dp2.value=tf1.value=tf2.value=None
            
            
        elif rail.selected_index==1:
            General_Row.controls.clear()
            General_Row.controls.append(rail)
            General_Row.controls.append(ft.VerticalDivider(width=1,color=ft.colors.BLACK45))
            General_Row.controls.append(pagina2)
            dp1.value=dp2.value=tf1.value=tf2.value=None
        page.update()
    
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
   
        
    dp2=ft.Dropdown(
        text_size=16,
        height=50,
        width=130,
        disabled=True,
        on_change=dp2bases
            
        )
    
    tf1=ft.TextField(input_filter=ft.InputFilter(allow=True,regex_string=r"[0-9]"),
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
                     border_color=ft.colors.BLACK,
                     
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
    
    img = ft.Image(
        src=f"codificacion.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    rail=ft.NavigationRail(
        selected_index=0,
        label_type=None,
        min_width=40,
        height=800,
        extended=True,
        min_extended_width=40,
        leading=img,
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label_content=ft.Text("Conversion",size=16),padding=15
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Gauss-Jordan",size=16),padding=15
                
            ),
        ],
        on_change=cambio_pag,
    )
    

        
        
    
    pagina1=        ft.Column(controls=[
            ft.Row(controls=[texto,dp1,texto2,dp2],spacing=10),
            ft.Container(height=1),
            ft.Row(controls=[tf1,tf2],alignment=ft.MainAxisAlignment.CENTER,spacing=50),
            ft.Row(controls=[ft.Container(width=176),ejecutar],alignment=ft.MainAxisAlignment.CENTER,spacing=50)
            ],spacing=20,horizontal_alignment=ft.MainAxisAlignment.CENTER)

    def generar_matriz(e):
        
        size=int(tam.value)
        x=[]
        col=[]
        filas=ft.Row(spacing=10,expand=True)
        x=ft.Column()
        
        for i in range(size):
            columna=ft.Column()
            for j in range(size):
                    columna.controls.append(ft.TextField(height=30,width=70,text_size=15,text_vertical_align=-0.5,input_filter=ft.NumbersOnlyInputFilter()))
                    
            x.controls.append(ft.TextField(height=30,width=70,text_size=15,text_vertical_align=-0.5,input_filter=ft.NumbersOnlyInputFilter()))     
            filas.controls.append(columna)
             
        filas.controls.append(ft.VerticalDivider(width=5,color=ft.colors.BLACK45,trailing_indent=160,leading_indent=30))   
        filas.controls.append(x)
        pagina2.controls.append(filas)
        btnrandom=ft.ElevatedButton(text="Llenado Random",on_click=llenadorandom) 
        pagina2.controls.append(btnrandom) 
        page.update()  
        pagina2.controls.remove(filas)
        pagina2.controls.remove(btnrandom)
    
    def llenadorandom(e):
        size=int(tam.value)
        x=[]
        col=[]
        filas=ft.Row(spacing=10,expand=True)
        x=ft.Column()
        
        for i in range(size):
            columna=ft.Column()
            for j in range(size):
                    columna.controls.append(ft.TextField(value=rd.randint(0,100),height=30,width=70,text_size=15,text_vertical_align=-0.5,input_filter=ft.NumbersOnlyInputFilter()))
                    
            x.controls.append(ft.TextField(value=rd.randint(0,100),height=30,width=70,text_size=15,text_vertical_align=-0.5,input_filter=ft.NumbersOnlyInputFilter()))     
            filas.controls.append(columna)
             
        filas.controls.append(ft.VerticalDivider(width=5,color=ft.colors.BLACK45,trailing_indent=160,leading_indent=30))   
        filas.controls.append(x)
        pagina2.controls.append(filas)
        btnrandom=ft.ElevatedButton(text="Llenado Random",on_click=llenadorandom) 
        pagina2.controls.append(btnrandom) 
        page.update()  
        pagina2.controls.remove(filas)
        pagina2.controls.remove(btnrandom)
        
    
            
    tam=ft.TextField(text_size=16,width=80,text_vertical_align=-0.5,height=40,input_filter=ft.NumbersOnlyInputFilter())
    generar=ft.ElevatedButton(text="Generar Matriz",icon=ft.icons.ADD_CIRCLE_OUTLINE,on_click=generar_matriz)
    pagina2=ft.Column(controls=[
        
        ft.Row(controls=[ft.Text("Ingrese el tamaño de la matriz NxN: ",size=18),tam,generar],spacing=20),
        
        
        
    ],horizontal_alignment=ft.MainAxisAlignment.CENTER,spacing=30)
    
    General_Row=ft.Row(controls=[
                rail,
                ft.VerticalDivider(width=1,color=ft.colors.BLACK45),
                pagina1],expand=True,spacing=30,alignment=ft.MainAxisAlignment.START)

    
    page.add(
        General_Row
    )
    
    page.update()
    

ft.app(target=main)
