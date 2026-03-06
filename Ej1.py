# Escribe una función llamada calcular_imc que reciba el peso (kg)
# y la altura (m). La función devolverá el Índice de Masa Corporal 
# (IMC = peso / altura²).
# - Si el IMC es menor que 18.5, “Bajo peso”
# - Entre 18.5 y menor que 25, “Normal”
# - Entre 25 y menor que 30, “Sobrepeso”
# - 30 o más, “Obesidad”.

def calcular_imc (kg, m):
    IMC = round(kg / (m**2),2)

    if IMC < 18.5:
        return ("Bajo peso",IMC)
    elif IMC >= 18.5 and IMC < 25:
        return "Normal",IMC
    elif IMC >= 25 and IMC < 30:
        return "Sobrepeso",IMC
    else:
        return "Obesidad",IMC
    
tipo , valor = calcular_imc(80,1.80)
print(f"Tiene un IMC {tipo} con un valor de {round(valor,2)}")