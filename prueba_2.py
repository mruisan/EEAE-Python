# Ejercicio 

# Crea una clase Concurso que calcule el problema de Monty Hall para un número determinado
# de veces.
# El programa hará de jugador y presentador de manera automática, eligiendo una puerta al azar
# descartando el presentador una puerta vacia no elegida y decidiendo de manera aleatoria el
# jugador si cambiar o no de elección.
# Al final se imprimirá un informe(print) de:
# - El porcentaje de veces que ganó manteniendo la elección
# - El porcentaje de veces que ganó cambiando la elección

from random import choice

class Concurso:
    def __init__(self,iteraciones):
        self.iteraciones = iteraciones
        self.puertas = [1, 2, 3]

    def concursar(self):
        ganador_cambio=0
        ganador_sincambio=0
        for i in range (self.iteraciones):
            premio=choice(self.puertas)
            jugador=choice(self.puertas)
            cambio=choice([True,False])
            porcentaje_cambio=round(ganador_cambio/self.iteraciones*100,1)
            porcentaje_sincambio=round(ganador_sincambio/self.iteraciones*100,1)
            if premio == jugador and cambio == False:
                ganador_sincambio+=1
            elif premio != jugador and cambio == True:
                ganador_cambio+=1
        print(f'\nTotal de partidas: {self.iteraciones}')
        print(f'\nESTADISTICAS: \n- Porcentaje de partidas ganadas sin cambio: {porcentaje_sincambio}%\n- Porcentaje de partidas ganadas con cambio: {porcentaje_cambio}%\n')
        
juego= Concurso(1000)

juego.concursar()