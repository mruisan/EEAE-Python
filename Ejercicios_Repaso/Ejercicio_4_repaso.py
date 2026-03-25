
# Ejercicio 4: Conversor de temperaturas
# Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
# Usa un constructor para inicializar una temperatura base.

class ConversorTemperatura:

    def __init__(self,temperatura,base):
        self.temperatura=temperatura
        self.base=base
    
    def conversor(self):
        if self.base.lower() == "celsius":
            fahrenheit= round((self.temperatura * 1.8) + 32,2)
            print (f"La temperatura {self.temperatura}º Celsius es de {fahrenheit}º Fahrenheit.")
        else:
            celsius= round((self.temperatura - 32) / 1.8,2)
            print (f"La temperatura {self.temperatura}º Fahrenheit es de {celsius}º Celsius.")

temperatura_1=ConversorTemperatura(45,"Fahrenheit")
temperatura_2=ConversorTemperatura(23,"Celsius")

temperatura_1.conversor()
temperatura_2.conversor()




