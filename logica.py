from pyscript import window, document

# Estado inicial del juego
jugador_vida = 100
enemigo_vida = 50

def actualizar_interfaz(mensaje):
    # Actualiza el texto de la historia
    document.getElementById("historia").innerText = mensaje
    # Actualiza los números de vida en pantalla
    document.getElementById("vida-jugador").innerText = str(jugador_vida)
    document.getElementById("vida-enemigo").innerText = str(enemigo_vida)

def atacar(event):
    global enemigo_vida
    if enemigo_vida > 0:
        daño = 10
        enemigo_vida -= daño
        if enemigo_vida <= 0:
            enemigo_vida = 0
            actualizar_interfaz("¡Golpe crítico! Has derrotado al enemigo. El reino está a salvo... por ahora.")
        else:
            actualizar_interfaz(f"¡Atacaste con tu espada! El enemigo pierde {daño} de vida.")
    else:
        actualizar_interfaz("El enemigo ya ha caído. No hay necesidad de más violencia.")

def curar(event):
    global jugador_vida
    if jugador_vida < 100:
        curacion = 15
        jugador_vida += curacion
        if jugador_vida > 100: jugador_vida = 100
        actualizar_interfaz(f"Bebiste una poción mágica. Recuperas {curacion} de vida.")
    else:
        actualizar_interfaz("Tu salud ya está al máximo.")

# Mensaje de bienvenida una vez que Python carga
actualizar_interfaz("¡Bienvenido, viajero! Un Ogro bloquea tu camino hacia Py-Terra. ¿Qué harás?")
