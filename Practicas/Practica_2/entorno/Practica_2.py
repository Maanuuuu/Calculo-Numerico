
"""
    Calculo Numerico - Practica 2 - 23/04/24
    
    Manuel Nava
    30.822.007
    Seccion: 305C1
    
    Integrando la Practica 1 al entorno virtual
"""

class Persona():
    def __init__(self):
        self.nombre=""
        self.edad=0
        self.cedula=""
    
        
    def getnombre(self):
        return self.nombre
    
    def getedad(self):
        return self.cedula

    def getcedula(self):
        return self.cedula
    
    def setnombre(self,nombre):
        self.nombre=nombre
    
    def setedad(self,edad):
        self.edad=edad
    
    def setcedula(self,cedula):
        self.cedula=cedula
    
    def datos(self):
        print(self.nombre,self.edad,self.cedula+"\n")
        

    def mayoredad(self):
        if (self.edad>=18):
            return True
        else: 
            return False
    


grupo=[["Manuel",18,"30829292"],["Rodrigo",17,"30191919"],["Juan",19,"29101010"],["Jesus",15,"31554405"]]

print("Mostrando a las personas del grupo mayores de edad: \n")

for i in range(len(grupo)):
    persona=Persona()
    persona.setnombre(grupo[i][0])
    persona.setedad(grupo[i][1])
    persona.setcedula(grupo[i][2])
    if persona.mayoredad():
        persona.datos()