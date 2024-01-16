


class Universidad():
    def __init__ (self,nombre_f,pais,idioma):
      self.nombre_f = nombre_f
      self.pais = pais
      self.idioma = idioma

class Carrera():
   def carrera(self,especialidad,duracion,dificultad):
      self.especialidad = especialidad
      self.duracion = duracion
      self.dificultad = dificultad

class Estudiante(Universidad,Carrera):
   def datos(self,nombre,edad):
      self.nombre=nombre
      self.edad=edad
      print(f"Mi nombre es {self.nombre}, tengo {self.edad} anhos, mi especialidad es {self.especialidad} estudie en {self.nombre_f} de {self.pais} por {self.duracion} anhos ") 
      print("Mi nombre es {}, tengo {} anhos, mi especialidad es {} estudie en {} de {} por {} anhos ".format(self.nombre,self.edad,self.especialidad,self.nombre_f,self.pais,self.duracion)) 

persona = Estudiante ("Politecnica","Paraguay","Espanish")
persona.carrera ("Analisis de sistemas","5","H")
persona.datos("Mathias", 27)

