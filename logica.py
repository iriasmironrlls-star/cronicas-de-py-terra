from pyscript import display
from personajes import Heroe # Importamos del otro archivo .py

# Creamos al jugador usando la clase del otro archivo
jugador = Heroe("Guerrero", 100)
enemigo_vida = 50

def actualizar_pantalla(texto):
    display(texto, target="historia")
    display(str(jugador.vida), target="vida-jugador")
    display(str(enemigo_vida), target="vida-enemigo")

def atacar(event):
    global enemigo_vida
    daño = 10
    enemigo_vida -= daño
    actualizar_pantalla(f"¡Atacaste! El enemigo perdió {daño} de vida.")
    if enemigo_vida <= 0:
        actualizar_pantalla("¡Has derrotado al monstruo!")

def curar(event):
    jugador.vida += 15
    actualizar_pantalla("Bebiste una poción. +15 de vida.")

# Mensaje inicial
actualizar_pantalla("Te encuentras frente a un ogro gruñón. ¿Qué harás?")
