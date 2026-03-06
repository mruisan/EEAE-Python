
# Crea una clase Calculadora que reciba 2 números.
# Haz los siguientes métodos:
# - Un método para sumar los dos números.
# - Un método para restar los dos números.
# - Al hacer print de un objeto Calculadora se imprimiran los dos números

'''
class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2

    def __str__(self):
        return str([self.num_1,self.num_2])
    
    def sumar(self):
        return (self.num_1+self.num_2)
    
    def restar(self):
        return (self.num_1-self.num_2)
    
    def multiplicar(self):
        return (self.num_1*self.num_2)
    
    def dividir(self):
        return (self.num_1/self.num_2)

calculadora_1=Calculadora (2,1)
calculadora_2=Calculadora(20,5)

print(calculadora_1.sumar())
print(calculadora_1.restar())
print(calculadora_2.multiplicar())
print(calculadora_2.dividir())
print(calculadora_1)
'''


'''
print(calculadora_2.sumar())
print(calculadora_2.restar())
print(calculadora_2)
'''
'''
class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2
        
    def __str__(self):
        return (f'Los números son {self.num_1} y {self.num_2}.')
    
    def sumar(self):
        return (self.num_1+self.num_2)
    
    def restar(self):
        return (self.num_1-self.num_2)
    
    def multiplicar(self):
        return (self.num_1*self.num_2)
    
    def dividir(self):
        return (self.num_1/self.num_2)

calculadora_1=Calculadora (2,1)
calculadora_2=Calculadora(20,5)

print(calculadora_1.sumar())
print(calculadora_1.restar())
print(calculadora_2.multiplicar())
print(calculadora_2.dividir())
print(calculadora_1)
'''

'''
class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2
        
    def __str__(self):
        return (f'Los números son {self.num_1} y {self.num_2}.')
    
    def sumar(self):
        try:
            x= self.num_1+self.num_2
            print(x)
        except:
            print(f'Los números no son correctos')       
        finally:
            print(f'Esto se ejecuta siempre')
        
        #else:
            #return (f'Hola')
    
    def restar(self):
        return (self.num_1-self.num_2)
    
    def multiplicar(self):
        return (self.num_1*self.num_2)
    
    def dividir(self):
        return (self.num_1/self.num_2)

calculadora_1=Calculadora (2,1)
calculadora_2=Calculadora('20',5)

calculadora_1.sumar()
calculadora_2.sumar()
#print(calculadora_1.restar())
#print(calculadora_2.multiplicar())
#print(calculadora_2.dividir())
#print(calculadora_1)

'''

# este no está terminado

class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1=num_1
        self.num_2=num_2
        
    def __str__(self):
        return (f'Los números son {self.num_1} y {self.num_2}.')
    
    def sumar(self):
        if int(self.num_1) >= 100 or int(self.num_2) >=100:
        try:
            x= self.num_1+self.num_2
            print(x)
        except:
            print(f'Los números no son correctos')       
        finally:
            print(f'Esto se ejecuta siempre')
        
        #else:
            #return (f'Hola')
    
    def restar(self):
        return (self.num_1-self.num_2)
    
    def multiplicar(self):
        return (self.num_1*self.num_2)
    
    def dividir(self):
        return (self.num_1/self.num_2)

calculadora_1=Calculadora (500,1)
calculadora_2=Calculadora('20',5)

calculadora_1.sumar()
calculadora_2.sumar()



