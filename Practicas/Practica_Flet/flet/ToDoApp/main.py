import flet as ft

class Task(ft.Row):

    def __init__(self,text):
        super().__init__()
        self.text_view=ft.Text(text)
        self.text_edit=ft.TextField(text,visible=False)
        self.edit_button=ft.IconButton(icon=ft.icons.EDIT,on_click=self.edit)
        self.save_button=ft.IconButton(visible=False,icon=ft.icons.SAVE,on_click=self.save)

        self.controls=[
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button
            
            
        ]
    def edit(self,e):
        self.edit_button.visible=False
        self.save_button.visible=True
        self.text_view.visible=False
        self.text_edit.visible=True
        self.update()
        
    def save(self,e):
        self.edit_button.visible=True
        self.save_button.visible=False
        self.text_view.visible=True
        self.text_edit.visible=False
        self.text_view.value=self.text_edit.value
        self.update()
        
      
def main(page: ft.Page):
    page.window_center()
    page.window_resizable=False
    page.window_width=700
    page.window_height=700
    page.padding=50
    page.theme_mode=ft.ThemeMode.LIGHT
    
    tarea=ft.TextField(label="Task",width=400)
    def Agg(e):
        
        page.add(ft.Row([Task(text=tarea.value)],alignment=ft.MainAxisAlignment.CENTER))
        tarea.value=""
        page.update()
    
    agregar=ft.ElevatedButton(text="Add",icon=ft.icons.ADD_TASK,on_click=Agg)
    
    
    
    page.add(ft.Row([tarea,agregar],alignment=ft.MainAxisAlignment.CENTER))
        
    
    
ft.app(target=main)