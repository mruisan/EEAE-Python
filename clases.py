
'''nombre='Manuel'
edad= 41
empleo='sgt1'

manuel=['manuel',41,'sgt1']'''

# Las clases se recomiendan empezar por mayusculas
# No se pueden crear vacias, minimo hay que ponerle pass
# la funcion init hay que ponerla obligatoriamente

class Persona:
    def __init__(self, name, age, rank):
        self.nombre= name
        self.edad= age
        self.empleo= rank

    def correr(self):
        print(f'{self.nombre} está corriendo')

    def saludar():
        print(f'Mano al botón')

    def cumpleaños(self):
        self.edad+=1
        print(f'{self.nombre} cumple {self.edad} felicidades')

antonio= Persona('Antonio',48,'Sgt1')
manuel= Persona('Manuel',45,'Sgt1')
javier= Persona('Javier',38,'Sgt1')

# Persona.saludar()

# manuel.correr()

# print(manuel.nombre)

# manuel.cumpleaños()


