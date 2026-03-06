
# Crea una clase Calculadora que reciba 2 números.
# Haz los siguientes métodos:
# - Un método para sumar los dos números.
# - Un método para restar los dos números.
# - Al hacer print de un objeto Calculadora se imprimiran los dos números
# - Añade try/except para validar la entrada de datos.
'''
class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2
        
    def __str__(self):
        return (f'Los números son {self.num_1} y {self.num_2}.')
    
    def sumar(self):
        try:
            x= (self.num_1+self.num_2)
            print(x)
        except ValueError:
            print('Error de Valor')
        except SyntaxError:
            print('Error de Sintaxis')
        except NameError:
            print('Error de Nombre')
    
    def restar(self):
        return (self.num_1-self.num_2)

calculadora_1=Calculadora (2,1)
calculadora_2=Calculadora('20',5)

print(calculadora_1.sumar())
print(calculadora_2.sumar())

'''
class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2
        self.resultado=None
        
    def __str__(self):
        return (f'Los números son {self.num_1} y {self.num_2}.')
    
    def sumar(self):
        try:
            self.resultado= self.num_1+self.num_2
        except:
            try:
                self.resultado= int(self.num_1+self.num_2)
            except:
                self.resultado='No son números los datos introducidos'
        return self.resultado
        
    def restar(self):
        return (self.num_1-self.num_2)

calculadora_1=Calculadora (2,1)
calculadora_2=Calculadora('20',5)

print(calculadora_1.sumar())
print(calculadora_2.sumar())


