import random
from Enemigo import *

class Zombie(Enemigo):
    def _init_(self, puntos_energia=10, atque=1):
        super().__init__(tipo_enemigo="Zombie", puntos_energia=puntos_energia,)
    
    def habla(self):
        print("Hummm...")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando depropagar la enfermedad")

    def ataque_especial (self):
        print("Zombie ataque especial")
        funciona_ataque_especia = random.random() < 0.50
        if funciona_ataque_especia:
            self.puntos_energia += 2
            print("Zombie te ha regenerado su enetgia von 2HP!")

