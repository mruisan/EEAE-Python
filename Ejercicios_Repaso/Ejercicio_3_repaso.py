
# Ejercicio 3: Lista de números pares
# Crea una clase Numeros con un atributo que sea una lista de enteros.
# Incluye un método que devuelva solo los números pares de esa lista.

class Numeros:
    def __init__(self,lista):
        self.enteros=lista
    def pares(self):
        lista=[]
        for i in self.enteros:
            if i % 2 == 0:
                lista.append(i)
        return lista

lista_1=Numeros([1,2,3,4,5,6,7,8,9])
lista_2=Numeros([23,54,86,97,36,24,12,66])


if __name__ == "__main__":
    print(lista_1.pares())
    print(lista_2.pares())

            