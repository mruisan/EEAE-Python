


#   ----------------------------------------------     23-02-26       -------------------------------------------------------------

''' Escribe una función llamada calcular_imc que reciba el peso (kg)
y la altura (m). La función devolverá el índice de masa corporal (imc)
e indicar si el resultado es menor a 18.5 'Bajo peso' si está entre 18.5 y 25 'Normal'
si es 25 o mayor y menor a 30 'Sobrepeso' y si es mayor a 30 'Obesidad'''


'''def calcular_imc():
    peso=float(input('Indica el peso en KG: '))
    altura=float(input('Indica la altura en M: '))
    imc= round(peso/altura**2,2)
    return (imc)
    if imc < 18.5:
        return ('Bajo peso')
    elif imc >= 18.5 and imc < 25:
        return ('Normal')
    elif imc >= 25 and imc < 30:
        return ('Sobrepeso')
    else:
        return ('Obesidad')
print (calcular_imc()) '''



'''def calcular_imc(kg, m):
    IMC=round(kg/m**2,2)

    if IMC < 18.5:
        return (IMC, ' Bajo peso')
    elif IMC >= 18.5 and IMC < 25:
        return (IMC, ' Normal') # return por defecto da una tupla
    elif IMC >= 25 and IMC < 30:
        return (IMC, ' Sobrepeso')
    else:
        return (IMC, ' Obesidad')
print(calcular_imc(85,1.75))'''


'''def calcular_imc(kg, m):
    IMC=round(kg/m**2,2)

    if IMC < 18.5:
        return (IMC, ' Bajo peso')
    elif IMC >= 18.5 and IMC < 25:
        return (IMC, ' Normal') # return por defecto da una tupla
    elif IMC >= 25 and IMC < 30:
        return (IMC, ' Sobrepeso')
    else:
        return (IMC, ' Obesidad')   
tipo,valor=calcular_imc(85,1.75)
print(f'Tiene un IMC {tipo} con un valor de {valor}')'''


'''# Crea una funcion llamada generar_lista que reciba un numero y haga una lista de 
# los numeros impares hasta ese número.
# Al final imprimirá por pantalla los números en una sola linea separados por el caracter '|' (altGr+1)

def generar_lista(num):
    lista=[]
    for i in range(1,num+1,2):
        lista.append(i)
    return lista
for i in generar_lista(10):
    print(i, end='|')'''


#   ----------------------------------------------     24-02-26       -------------------------------------------------------------


'''La empresa "YoParaSerFelizQuieroUnCamion" paga un extra a sus conductores
a final de año.
Los accidentes son clasificados en base al porcentaje de responsabilidad
que tenga el conductor en el mismo (p.ej. saltarse un STOP es culpa
del conductor, un choque culpa de otro no lo es)
El extra se recibirá integro si el conductor no ha tenido ningún
accidente con una responsabilidad mayor al 20% del accidente.
Si la responsabilidad es superior se le considera responsable del
accidente y por tanto: 
- Si tuvo un accidente responsable su extra será de la mitad
- Dos accidentes responsables su extra será de un tercio
- Tres accidentes responsables su extra será de un cuarto
- Más de tres accidentes responsables y no recibirá extra
- El extra se calcula sumando la prima de antigüedad y la prima de kilómetros.
- La prima de antigüedad se empieza a cobrar al 4º año en la empresa, es de
200€ y aumenta 20€ cada año después del 4º·
La prima de kilómetros es de 1 céntimo por km recorrido hasta un
máximo de 400€
Escriba un programa que permita introducir los datos necesarios para
calcular la prima de un conductor dado y nos entregue el importe.'''

'''accidentes_res= int(input("Indica nº accidentes responsables: "))
anos= int(input('Introduce años de antiguedad: '))
km= int(input('km este año: '))


if anos < 4 :
    prima_anos=0
else:
    prima_anos= int(200+(anos-4)*20)

prima_km= km * 0.01
if prima_km > 400:
    prima_km=400

extra= prima_anos + prima_km
if accidentes_res == 1:
    extra /= 2
elif accidentes_res == 2:
    extra /=3
elif accidentes_res == 3:
    extra /=4
elif accidentes_res > 3:
    extra=0

print(round(extra,2))'''

'''Este metodo es mas eficiente, más rapido

import math
print(math.sqrt(100))'''

'''Este es vlaido, solo importa el módulo sqrt, se puede llamar sin hacer referencia a al modulo math

from math import sqrt
print(sqrt(100))'''

''' Se puede crear un modulo (una funcion en un archivo concreto, despues importarla y llamarla igual)'''

''' crea un generador de contraseñas seguras usando los modulos:
- random
- string

import random
import string

contrasena=''
for i in range(10):
    caracteres=string.ascii_letters+string.digits+string.punctuation
    contrasena += random.choice(caracteres)

print(contrasena)'''

'''Un programa que genere un numero aleatorio del uno al cien, le pida al usuario que introduzca numeros y la deiga si el numero es más alto o mas bajo

import random

secreto=random.randint(0,100)
numero=int(input('Indica un numero: '))
contador=9

while contador !=0:
    if numero == secreto:
        print('Has ganado')
        break
    elif numero > secreto:
        print('Tu numero es mayor al numero secreto')
        contador-=1
        numero=int(input('Indica otro numero: '))
    else:
        print('Tu numero es menor al numero secreto')
        contador-=1
        numero=int(input('Indica otro numero: '))
if contador == 0:
    print ('Has agotado tus 10 intentos')'''


'''import random
secreto=random.randint(1,100)
numero=int(input('Indica un número del 1 al 100: '))
contador=10

for i in range (100):
    if contador == 1:
        print('Agotaste tus intentos')
        break
    elif numero==secreto:
        print('Ganaste!!!')
        break
    elif numero>secreto:
        print('Tu numero es mayor que el secreto.')
        contador-=1
        numero=int(input('Indica otro numero: '))
    elif numero<secreto:
        print('Tu número es menor al numero secreto')
        contador-=1
        numero=int(input('Indica otro numero: '))'''


'''import random

secreto=random.randint(0,100)
numero=int(input('Indica un numero: '))
contador=9

while contador !=0:
    if numero == secreto:
        print('Has ganado')
        break
    elif numero > secreto:
        print('Tu numero es mayor al numero secreto')
        numero=int(input('Indica otro numero: '))
        contador-=1
    else:
        print('Tu numero es menor al numero secreto')
        numero=int(input('Indica otro numero: '))
        contador-=1
else:
    print ('Has agotado tus 10 intentos')'''


'''import random
secreto=random.randint(1,100)
numero=int(input('Indica un número del 1 al 100: '))

for i in range (9):
    if numero==secreto:
        print('Ganaste!!!')
        break
    elif numero>secreto:
        print('Tu numero es mayor que el secreto.')
        numero=int(input('Indica otro numero: '))
    elif numero<secreto:
        print('Tu número es menor al numero secreto')
        numero=int(input('Indica otro numero: '))
else: print('Agotaste tus 10 intentos.')'''


'''import random
secreto=random.randint(1,100)

for i in range (9):
    numero=int(input('Indica un número del 1 al 100: '))
    if numero==secreto:
        print('Ganaste!!!')
        break
    elif numero>secreto: print('Tu numero es mayor que el secreto.')
    elif numero<secreto: print('Tu número es menor al numero secreto')
else: print('Agotaste tus 10 intentos.')'''



#   ----------------------------------------------     25-02-26       -------------------------------------------------------------


''' Haz una calculadora de edad exacta (años, meses, dias)

import datetime

hoy=datetime.date.today()
ano=int(input('Indica tu año de nacimiento: '))
mes=int(input('Indica tu mes de nacimiento: '))
dia=int(input('Indica tu día de nacimiento: '))
cumple=datetime.date(ano,mes,dia)
dias_totales=(hoy-cumple).days
# print (dias_totales)
sol_ano=dias_totales//365
# print(sol_ano)
sol_mes=(dias_totales-(365*sol_ano))//30
# print(sol_mes)
sol_dia=dias_totales-((365*sol_ano)+(30*sol_mes))
print(f'Con los datos indicados tienes {sol_ano} años, {sol_mes} meses y {sol_dia} días de vida.')'''




#   ----------------------------------------------     26-02-26       -------------------------------------------------------------


'''Crea una clase para hacer cuentas bancarias
el constructor tendrá en cuenta el nombre de usuario y el saldo inicial.
Añade metodos para:
- Retirar dinero
- Ingresar dinero '''


'''import random
cantidad= random.randint(1,50)
class Cuentas:
    def __init__(self,name,balance):
        self.nombre=name
        self.saldo=balance
    def retirar(self,cantidad):
        if self.saldo < cantidad:
            return('No tienes saldo suficiente')
        else:
            self.saldo -= cantidad
            return self.saldo
    def ingresar(self,cantidad):
          self.saldo += cantidad
          return self.saldo
    
cuenta=Cuentas('Manuel',100)

print(cuenta.ingresar(cantidad))'''



#   ----------------------------------------------     27-02-26       -------------------------------------------------------------

# OK

'''import random
import string
cantidad= random.randint(1,50)
class Cuentas:
    def __init__(self,name,balance):
        self.nombre=name
        self.saldo=balance
        self.iban=self.numero_cuenta()

    def retirar(self,cantidad):
        self.saldo -= cantidad

    def ingresar(self,cantidad):
        self.saldo += cantidad

    def numero_cuenta(self):
        x=''
        for i in range (20):
            x += str(random.randint(0,9))
        return x
    
cuenta_prueba=Cuentas('Ruiz',1200)
print(f'La cuenta de {cuenta_prueba.nombre} tiene {cuenta_prueba.saldo}€\nEl IBAN es {cuenta_prueba.iban}')


while True:
    print('\nBANCO BBVA\n')
    print('Elija una opción\n')
    print('1. Consultar Datos')
    print('2. Retirar dinero')
    print('3. Ingresar dinero')
    print('4. Salir\n')
    opcion=int(input('Introduce una opción: '))

    if opcion == 1:
        print(f'Titular {cuenta_prueba.nombre}\nSaldo {cuenta_prueba.saldo}\nIBAN: {cuenta_prueba.iban}')
    elif opcion == 2:
        x= int(input('Dinero a retirar: '))
        cuenta_prueba.retirar(x)
    elif opcion == 3:
        x= int(input('Dinero a ingresar: '))
        cuenta_prueba.ingresar(x)
    elif opcion == 4:
        break
    else:
        print('Opción no válida')'''


# Comparar con ejercicio de Sauca y revisar para cuadrar menú

'''import random
import string
cantidad= random.randint(1,50)
class Cuentas:

    interes= 0.01
    comision= 1.5
    cantidad_clientes= 0

    def __init__(self,name,balance):
        self.nombre=name
        self.saldo=balance
        self.iban=self.numero_cuenta()
        Cuentas.cantidad_clientes += 1

    def retirar(self,cantidad):
        self.saldo -= (cantidad - Cuentas.comision)

    def ingresar(self,cantidad):
        self.saldo += cantidad

    def numero_cuenta(self):
        x=''
        for i in range (20):
            x += str(random.randint(0,9))
        return x
    
cuenta_prueba=Cuentas('Ruiz',1200)
cuenta_ruiz=Cuentas('Manuel'50)
print(f'La cuenta de {cuenta_prueba.nombre} tiene {cuenta_prueba.saldo}€\nEl IBAN es {cuenta_prueba.iban}')


while True:
    print('\nBANCO BBVA\n')
    print('Elija una opción\n')
    print('1. Consultar Datos')
    print('2. Retirar dinero')
    print('3. Ingresar dinero')
    print('4. Consular número de cuentas')
    print('5. ADMIN BANCO: Modificar comisión')
    print('6. Salir\n')
    opcion=int(input('Introduce una opción: '))

    if opcion == 1:
        print(f'Titular {cuenta_prueba.nombre}\nSaldo {cuenta_prueba.saldo}\nIBAN: {cuenta_prueba.iban}')
    elif opcion == 2:
        x= int(input('Dinero a retirar: '))
        cuenta_prueba.retirar(x)
    elif opcion == 3:
        x= int(input('Dinero a ingresar: '))
        cuenta_prueba.ingresar(x)
    elif opcion == 4:
        print(f"Hay {Cuentas.cantidad_clientes} cuentas")
    elif opcion == 5:
        x = float(input("Introduzcca la cantidad de interés de retirada: "))
        Cuenta.comision_retirada = x
    elif opcion == 6:
        break
    else:
        print('Opción no válida')'''


# Crea una clase Pokemon para llevar un registro de pokemon capturados
# Los pokemon tendrán nombre, tipo, nivel y si estan capturados o no
# Habrá un contador del número de pokemon capturados
# Crea un método para capturar un Pokemon, el método tendrá en cuenta la probabilidad
# de captura de un pokemon es del 40%

import random

class Pokemon:

    pokedex= 0
    vistos= 0

    def __init__(self,name,clase,level):
        self.nombre= name
        self.tipo= clase
        self.nivel= level
        self.capturado= False
        Pokemon.vistos +=1
    
    def pokeball(self):
        exito= random.randint(1,100)
        if exito <= 40:
            self.capturado == True
            Pokemon.pokedex += 1
            intentos += 1
            return True
        else:
            return False

pokemon_1= Pokemon('Pikachu','electrico',5)
pokemon_2= Pokemon('Charmander','fuego',7)

# print(f'has visto {Pokemon.vistos} pokemon')
# if pokemon_1.capturado():
#     print(f'Has capturado a {pokemon_1.nombre}, tienes {Pokemon.pokedex} pokemon')
# else:
#     print(f'Has capturado a {pokemon_1.nombre}, tienes {Pokemon.pokedex} pokemon')

print('MUNDO POKEMON\n')
print(f'Has visto a {Pokemon.vistos} Pokemon')
print(f'Marca 1 para capturar a {pokemon_1.nombre}.')
print(f'Marca 2 para capturar a {pokemon_2.nombre}.')
opcion=int(input('Indica tu opción: '))

if opcion == 1:
    intentos=0
    if pokemon_1.pokeball() == True:
        intentos +=1
        print(f'Enhorabuena, has capturado a {pokemon_1.nombre} en {intentos} intentos, tienes {Pokemon.pokedex} pokemon.')
    else:
        intentos +=1
        print(f'{pokemon_1.nombre}, se ha escapado. Vuelve a intentarlo')
        pokemon_1.pokeball()
elif opcion == 2:
    if pokemon_2.pokeball() == True:
        print(f'Enhorabuena, has capturado a {pokemon_2.nombre}, tienes {Pokemon.pokedex} pokemon.')
    else:
        print(f'{pokemon_1.nombre}, se ha escapado. Vuelve a intentarlo')
else:
    print('Opción incorrecta')
    opcion=int(input('Indica otra opción: '))










    
