import random
from Enemigo import *

class Ogro (Enemigo):
    def __init__(self, tipo_enemigo, puntos_energia=20, ataque=1):
        super().__init__(tipo_enemigo, puntos_energia, ataque=ataque)
        
    def habla(self):
        print("Ogro aplastar todo!!!")

        def atque_especial(self):
            print("Ogro ataque especial")
            funcio_ataque_especial = random.random() < 0.20
            if funcio_ataque_especial:
                self.ataque += 4
                print("Ogro enojado y incremento")
