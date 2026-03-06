
''' Haz un videojuego usando clases
- Está la clase Personaje que tiene nombre, vida y una funcion de ataque
- El jugador y el enemigo son Personajes y atacan por turnos
- Gana quien deje la vida del otro a cero'''

'''import random

class Personaje:
    def __init__(self,name, life):
        self.nombre= name
        self.vida=life
    def atacar(self):
        return(random.randint(1,5))


jugador= Personaje('spiderman',30)
enemigo= Personaje('duende verde',30)


while jugador.vida >0 and enemigo.vida > 0:
    jugador.vida -= enemigo.atacar()
    if jugador.vida>0: print(f'El {jugador.nombre} continua con {jugador.vida} puntos de vida')
    else: break
    enemigo.vida -= jugador.atacar()
    if enemigo.vida>0: print(f'El {enemigo.nombre} continua con {enemigo.vida} puntos de vida')
    else: break
if jugador.vida > 0:
    print(f'{jugador.nombre} gana, tiene una vida de {jugador.vida}')
else:
    print(f'{enemigo.nombre} gana, tiene una vida de {enemigo.vida}')'''




'''import random

class Personaje:
    def __init__(self,name, life):
        self.nombre= name
        self.vida=life
    def atacar(self):
        return(random.randint(1,5))

jugador= Personaje('spiderman',30)
enemigo= Personaje('duende verde',30)
turno=random.choice([jugador,enemigo])

while jugador.vida >0 and enemigo.vida > 0:
    if turno == enemigo:
        jugador.vida -= enemigo.atacar()
        if jugador.vida>0: print(f'El {jugador.nombre} continua con {"#"*(jugador.vida)} puntos de vida')
        else: break
        turno=jugador
    else:
        enemigo.vida -= jugador.atacar()
        if enemigo.vida>0: print(f'El {enemigo.nombre} continua con {'#'*(enemigo.vida)} puntos de vida')
        else: break
        turno=enemigo
if jugador.vida > 0:
    print(f'{jugador.nombre} gana, tiene una vida de {jugador.vida}')
else:
    print(f'{enemigo.nombre} gana, tiene una vida de {enemigo.vida}')'''







































'''jugador.vida -= enemigo.atacar

        if enemigo.vida != 0:
            print('El enemigo está muerto')
        else: atacar.enemigo
        if jugador.vida !=0: print('El jugador está muerto')
        else: atacar.jugador'''