


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

accidentes_res= int(input("Indica nº accidentes responsables: "))
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

print(round(extra,2))







    
