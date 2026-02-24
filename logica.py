from pyscript import document
import random # Para que el daño del ogro sea aleatorio

# Estado inicial
jugador_vida = 100
enemigo_vida = 50
juego_activo = True

def actualizar_interfaz(mensaje):
    document.getElementById("historia").innerText = mensaje
    document.getElementById("vida-jugador").innerText = str(jugador_vida)
    document.getElementById("vida-enemigo").innerText = str(enemigo_vida)

def atacar(event):
    global enemigo_vida, jugador_vida, juego_activo
    
    if not juego_activo: return

    # Tu turno
    daño_jugador = 10
    enemigo_vida -= daño_jugador
    
    if enemigo_vida <= 0:
        enemigo_vida = 0
        juego_activo = False
        actualizar_interfaz("¡Victoria! El Ogro ha caído. Has salvado el paso de montaña.")
        return

    # Turno del Ogro (Contraataque)
    daño_ogro = random.randint(5, 15) # Daño aleatorio entre 5 y 15
    jugador_vida -= daño_ogro
    
    if jugador_vida <= 0:
        jugador_vida = 0
        juego_activo = False
        actualizar_interfaz(f"¡Has sido derrotado! El Ogro te golpeó con {daño_ogro} de daño. Fin de la aventura.")
    else:
        actualizar_interfaz(f"Le quitas {daño_jugador} al Ogro, ¡pero él te devuelve un golpe de {daño_ogro}!")

def curar(event):
    global jugador_vida, juego_activo
    if not juego_activo: return

    if jugador_vida < 100:
        curacion = 20
        jugador_vida += curacion
        if jugador_vida > 100: jugador_vida = 100
        
        # El Ogro no te deja curar gratis, ¡te ataca mientras bebes!
        daño_ogro = random.randint(5, 10)
        jugador_vida -= daño_ogro
        actualizar_interfaz(f"Bebes la poción (+{curacion}), pero el Ogro aprovecha para golpearte (-{daño_ogro}).")
    else:
        actualizar_interfaz("Tu salud ya está al máximo, ¡concéntrate en la batalla!")
