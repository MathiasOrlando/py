


class Universidad():
    def __init__ (self,nombre_f):
      self.nombre_f = nombre_f

class Carrera():
   def carrera(self,especialidad):
      self.especialidad = especialidad

class Estudiante(Universidad,Carrera):
   def datos(self,nombre,edad):
      self.nombre=nombre
      self.edad=edad
      print("Mi nombre es {}, tengo {} anhos, mi especialidad es {} estudie en {} ".format(self.nombre,self.edad,self.especialidad,self.nombre_f)) 

persona = Estudiante ("Politecnica")
persona.carrera ("Analisis de sistemas")
persona.datos("Mathias",20)
      