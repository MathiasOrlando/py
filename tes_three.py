
class Estudiante():
    def __init__(self,nombre,apellido,nota):
        self.nombre=nombre
        self.apellido=apellido
        self.nota=nota
        self.resul=None

    def imprimir(self):
        print(f"El Alumno {self.nombre.capitalize()} {self.apellido.capitalize()} con nota {self.nota} - {self.resul}")


    def Resultado(self):

        if self.nota > 7 :
            self.resul="Aprobado"
        else:
            self.resul="Reprobado"

        return self.resul

estudiante1= Estudiante("daniel","fernandez", 6)
estudiante1.Resultado()
estudiante1.imprimir()



