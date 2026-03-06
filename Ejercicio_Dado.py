
# Haz una clase Dado que simule el lanzamiento de un dado de 2 caras (moneda)

'''from random import choice

class Moneda:
    def __init__(self):
        pass
    def lanzamiento(self):
        resultado=choice(['Cara','Cruz']) # de esta manera hay que hacer la lista, si es muy grande es un inconveniente
        return resultado
moneda= Moneda()
print(moneda.lanzamiento())
'''

'''from random import randint

class Moneda:
    def __init__(self):
        self.caras=(2)
    def lanzamiento(self):
        resultado=randint(1,self.caras) #
        return resultado
moneda= Moneda()
print(d6) # Estoy imprimiendo un objeto
print(moneda.lanzamiento())

'''

from random import randint

class Moneda:
    def __init__(self,caras):
        self.caras=caras
    
    def __str__(self):
       return str(self.lanzamiento())
        
    def lanzamiento(self):
        resultado=randint(1,self.caras) #
        return resultado
    
moneda= Moneda(2)
d6= Moneda(6)
d8= Moneda(8)
d10= Moneda(10)
d12= Moneda(12)
d20= Moneda(20)

dadoRaro=randint(1,6)

# print(d20)  # con el metodo __str__ ya podemos llamar directamente al metodo lanzar que llama a la clase Moneda.

# print(d20.lanzamiento())

print(f'El dado raro tiene {}') # terminar...