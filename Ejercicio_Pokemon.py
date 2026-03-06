

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
    
    def pokeball_roja(self):
        exito= random.randint(1,100)
        if exito <= 20:
            self.capturado == True
            Pokemon.pokedex += 1
            return True
        else:
            return False
        
    def pokeball_blanca(self):
        exito= random.randint(1,100)
        if exito <= 40:
            self.capturado == True
            Pokemon.pokedex += 1
            return True
        else:
            return False
        
    def pokeball_dorada(self):
        exito= random.randint(1,100)
        if exito <= 60:
            self.capturado == True
            Pokemon.pokedex += 1
            return True
        else:
            return False


pokemon_1= Pokemon('Pikachu','electrico',5)
pokemon_2= Pokemon('Charmander','fuego',7)

print('MUNDO POKEMON\n')
print(f'Has visto a {Pokemon.vistos} Pokemon')
print(f'Marca 1 para capturar a {pokemon_1.nombre}.')
print(f'Marca 2 para capturar a {pokemon_2.nombre}.')
opcion= int(input('Indica tu opción: '))

if opcion == 1:
    print(f'Marca 1 para elegir la Pokeball Roja')
    print(f'Marca 2 para elegir la Pokeball Blanca')
    print(f'Marca 3 para elegir la Pokeball Dorada')
    opcion_2= int(input('Indica tu opción: '))

    if opcion_2 == 1:
        intentos_rojos=0
        while pokemon_1.pokeball_roja() != True:
            intentos_rojos +=1
            print(f'{pokemon_1.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_rojos +=1
            print(f'Enhorabuena, has capturado a {pokemon_1.nombre} en {intentos_rojos} intentos, tienes {Pokemon.pokedex} pokemon.')

    elif opcion_2 == 2:
        intentos_blancas=0
        while pokemon_1.pokeball_blanca() != True:
            intentos_blancas +=1
            print(f'{pokemon_1.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_blancas +=1
            print(f'Enhorabuena, has capturado a {pokemon_1.nombre} en {intentos_blancas} intentos, tienes {Pokemon.pokedex} pokemon.')

    elif opcion_2 == 3:
        intentos_doradas=0
        while pokemon_1.pokeball_dorada() != True:
            intentos_doradas +=1
            print(f'{pokemon_1.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_doradas +=1
            print(f'Enhorabuena, has capturado a {pokemon_1.nombre} en {intentos_doradas} intentos, tienes {Pokemon.pokedex} pokemon.')
    else:
        print('Opción no válida')
        opcion_2= int(input('Indica otra opción: '))

elif opcion == 2:
    print(f'Marca 1 para elegir la Pokeball Roja')
    print(f'Marca 2 para elegir la Pokeball Blanca')
    print(f'Marca 3 para elegir la Pokeball Dorada')
    opcion_2= int(input('Indica tu opción: '))

    if opcion_2 == 1:
        intentos_rojos=0
        while pokemon_2.pokeball_roja() != True:
            intentos_rojos +=1
            print(f'{pokemon_2.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_rojos +=1
            print(f'Enhorabuena, has capturado a {pokemon_2.nombre} en {intentos_rojos} intentos, tienes {Pokemon.pokedex} pokemon.')

    elif opcion_2 == 2:
        intentos_blancas=0
        while pokemon_2.pokeball_blanca() != True:
            intentos_blancas +=1
            print(f'{pokemon_2.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_blancas +=1
            print(f'Enhorabuena, has capturado a {pokemon_2.nombre} en {intentos_blancas} intentos, tienes {Pokemon.pokedex} pokemon.')

    elif opcion_2 == 3:
        intentos_doradas=0
        while pokemon_2.pokeball_dorada() != True:
            intentos_doradas +=1
            print(f'{pokemon_2.nombre}, se ha escapado. Vuelve a intentarlo')
        else:
            intentos_doradas +=1
            print(f'Enhorabuena, has capturado a {pokemon_2.nombre} en {intentos_doradas} intentos, tienes {Pokemon.pokedex} pokemon.')
    else:
        print('Opción no válida')
        opcion_2= int(input('Indica otra opción: '))   
else:
    print('Opción no válida')
    opcion= int(input('Indica otra opción: '))

