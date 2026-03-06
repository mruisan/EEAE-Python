
# Crea una clase Kart.
# Cada kart tendrá un piloto, una velocidad inicial, una velocidad máxima y una aceleración
# Haz metodos para:
# - Acelerar, que subirá la velocidad el valor de la aceleración.
# - Frenar, que reducirá la velocidad el valor de la aceleración.
# - Mostrar datos, que devolverá que el piloto X va a velocidad Y.
# - Añade manejo de excepciones para evitar pasar de las velocidades máximas.

class Kart:
    def __init__(self, piloto, vel_ini, vel_max, acel):
        self.piloto=piloto
        self.vel_ini=vel_ini
        self.vel_max=vel_max
        self.acel=acel
        self.vel_act=None

    def acelerar(self):
        try:
            if self.vel_ini + self.acel <= self.vel_max:
                self.vel_act= self.vel_ini + self.acel
                return (f'El piloto {self.piloto}, va a una velocidad de {self.vel_ini} y tras la aceleración llega a {self.vel_act}.')
            else:
                return (f'No puedes acelerar, superas la velocidad máxima')
        except:
            return (f'Los datos no son correctos')

    def frenar(self):
        try:
            if self.vel_act==None:
                return(f'Estas parado')
        
            elif self.vel_act-self.acel <= 0:
                return (f'No puedes frenar')
        
            else:
                self.vel_act -= self.acel
                return self.vel_act
        except:
            return (f'Los datos no son correctos')
        
    def datos(self):
        return(f'El piloto {self.piloto}, va a una velocidad {self.vel_act}')

kart_1= Kart('Manuel',5,100,'5')
kart_2= Kart('Pepe',50,90,50)
kart_3= Kart('José',50,150,20)

print(kart_1.acelerar())
print(kart_2.acelerar())
print(kart_1.frenar())
print(kart_2.frenar())
print(kart_3.acelerar())
print(kart_3.frenar())
print(kart_3.datos())




'''
    def acelerar(self):
        if self.vel_ini <= 0 and self.vel_max <= (self.vel_max-self.self.acel):
            self.vel_act=self.vel_ini+self.acel
            return self.vel_act
    def frenar(self):
        if self.vel_ini <= 0:
            return(f'Estas parado')
        elif self.vel_act >= self.acel
'''


'''
       try:
            if self.vel_ini + self.acel <= self.vel_max:
                self.vel_act= self.vel_ini + self.acel
                return self.vel_act
        except:
            if self.vel_ini + self.acel <= self.vel_max:
                return(f'No puedes acelerar, superas la velocidad máxima')   
'''


