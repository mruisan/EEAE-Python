
# Ejercicio 

# Crea una clase Concurso que calcule el problema de Monty Hall para un número determinado
# de veces.
# El programa hará de jugador y presentador de manera automática, eligiendo una puerta al azar
# descartando el presentador una puerta vacia no elegida y decidiendo de manera aleatoria el
# jugador si cambiar o no de elección.
# Al final se imprimirá un informe(print) de:
# - El porcentaje de veces que ganó manteniendo la elección
# - El porcentaje de veces que ganó cambiando la elección

import random

class Concurso:
    def __init__(self,iteraciones):
        self.iteraciones = iteraciones
        self.puertas = [1, 2, 3]

    def concursar(self):
        #presentador=random.choice(self.puertas)    # No es necesario, se puede obviar.
        #while presentador == premio or presentador == jugador:     # No es necesario, se puede obviar.
            #presentador = random.choice(self.puertas)      # No es necesario, se puede obviar.
        ganador_cambio=0
        ganador_sincambio=0
        contador=0
        for i in range (self.iteraciones):
            premio=random.choice(self.puertas)
            jugador=random.choice(self.puertas)
            cambio=random.choice([True,False])
            porcentaje_cambio=round((ganador_cambio/self.iteraciones)*100,2)
            porcentaje_sincambio=round((ganador_sincambio/self.iteraciones)*100,2)
            if premio == jugador and cambio == True:
                print(f'Tu elección fue la puerta {jugador}.\nEl premio estaba en la puerta {premio}.\nPierdes el concurso por cambiar de puerta\n')
                contador+=1
                continue
            elif premio == jugador and cambio == False:
                print(f'Tu elección fue la puerta {jugador}.\nEl premio estaba en la puerta {premio}.\nGanas el concurso sin cambiar de puerta!!!\n')
                ganador_sincambio+=1
                contador+=1
                continue
            elif premio != jugador and cambio == True:
                print(f'Tu elección fue la puerta {jugador}.\nEl premio estaba en la puerta {premio}.\nGanas el concurso por cambiar de puerta!!!\n')
                ganador_cambio+=1
                contador+=1
                continue
            elif premio != jugador and cambio == False:
                print(f'Tu elección fue la puerta {jugador}.\nEl premio estaba en la puerta {premio}.\nPierdes el concurso por no cambiar de puerta\n')
                contador+=1
                continue
        print(f'Total de partidas: {contador}')
        print(f'Ganadas cambiando de puerta: {ganador_cambio}')
        print(f'Ganadas sin cambiar de puerta: {ganador_sincambio}')
        print(f'\nESTADISTICAS: \n- Porcentaje de partidas ganadas sin cambio: {porcentaje_sincambio}%\n- Porcentaje de partidas ganadas con cambio: {porcentaje_cambio}%\n')
        
juego= Concurso(100)

juego.concursar()

