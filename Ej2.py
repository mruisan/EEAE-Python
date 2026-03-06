# Crea una función llamada generar_lista que  reciba un número
# y haga una lista de  los números impares hasta ese número.
# Al final imprimirá por pantalla los números en una sola línea separados
# por el  caracter "|" (AltGr + 1)

def generar_lista (x):
    resultado = ""
    for n in range (1,x+1,2):
        print (resultado)
        resultado = resultado + str(n) + "|"


generar_lista(100)