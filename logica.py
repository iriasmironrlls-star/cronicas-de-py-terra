from pyscript import document  # 🔥 CAMBIO: Usar document en lugar de display
from personajes import Heroe # Importamos del otro archivo .py
import random  # 🔥 NUEVO: Para elementos aleatorios

# Creamos al jugador usando la clase del otro archivo
jugador = Heroe("Guerrero", 100)
enemigo_vida = 50
enemigo_max = 50  # 🔥 NUEVO: Para tracking
enemigo_turno = False  # 🔥 NUEVO: Para turnos del enemigo

# 🔥 NUEVO: Variables de combate
combate_activo = True
mensaje_extra = ""

def actualizar_pantalla(texto):
    """Actualiza todos los elementos de la interfaz"""
    # 🐛 FIX DEFINITIVO: Usar innerHTML directamente
    document.getElementById("historia").innerHTML = texto
    document.getElementById("vida-jugador").innerHTML = str(jugador.vida)
    document.getElementById("vida-enemigo").innerHTML = str(enemigo_vida)
    document.getElementById("nivel").innerHTML = str(jugador.nivel)
    document.getElementById("exp").innerHTML = f"{jugador.experiencia}/{jugador.exp_para_subir}"
    document.getElementById("oro").innerHTML = str(jugador.oro)
    document.getElementById("inventario").innerHTML = f"{len(jugador.inventario)} items"

def turno_enemigo():
    """🔥 NUEVO: El enemigo ataca al jugador"""
    global combate_activo, mensaje_extra
    
    if enemigo_vida > 0 and jugador.vida > 0:
        # Daño del enemigo (aleatorio)
        daño_enemigo = random.randint(5, 15)
        daño_real, defendio = jugador.recibir_daño(daño_enemigo)
        jugador.vida -= daño_real
        
        if defendio:
            mensaje_extra = f"🛡️ ¡Bloqueaste! Solo recibiste {daño_real} de daño (reducido de {daño_enemigo})."
        else:
            mensaje_extra = f"👹 ¡El ogro te golpea! Recibes {daño_real} de daño."
        
        # Verificar si el jugador murió
        if jugador.vida <= 0:
            jugador.vida = 0
            combate_activo = False
            actualizar_pantalla("💀 Has sido derrotado... GAME OVER")
            return
        
        actualizar_pantalla(mensaje_extra)

def dar_recompensas():
    """🔥 NUEVO: Da oro y experiencia al derrotar enemigo"""
    oro_ganado = random.randint(20, 50)
    exp_ganada = random.randint(30, 60)
    
    jugador.ganar_oro(oro_ganado)
    jugador.ganar_experiencia(exp_ganada)
    
    # Chance de conseguir poción
    if random.random() < 0.3:  # 30% de probabilidad
        jugador.agregar_item("Poción")
        item_msg = " ¡Conseguiste una Poción!"
    else:
        item_msg = ""
    
    nivel_subio = jugador.nivel > 1 and jugador.experiencia == 0  # Si acaba de subir
    
    if nivel_subio:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{item_msg}<br>⭐ ¡SUBISTE AL NIVEL {jugador.nivel}! Vida restaurada."
    else:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{item_msg}"
    
    return msg

def atacar(event):
    """Sistema de ataque mejorado con críticos y fallos"""
    global enemigo_vida, combate_activo, mensaje_extra
    
    if not combate_activo or enemigo_vida <= 0:
        actualizar_pantalla("No hay enemigos que enfrentar.")
        return
    
    # 🔥 NUEVO: Sistema de críticos y fallos
    dado = random.random()
    daño_base = 10 + (jugador.nivel * 2)  # Aumenta con nivel
    
    if dado < 0.1:  # 10% de fallo
        mensaje_extra = "❌ ¡Tu ataque falló!"
        daño = 0
    elif dado > 0.85:  # 15% de crítico
        daño = daño_base * 2
        mensaje_extra = f"💥 ¡CRÍTICO! Causaste {daño} de daño."
    else:  # Ataque normal
        daño = daño_base
        mensaje_extra = f"⚔️ ¡Atacaste! El enemigo perdió {daño} de vida."
    
    enemigo_vida -= daño
    
    if enemigo_vida <= 0:
        enemigo_vida = 0
        combate_activo = False
        msg_victoria = dar_recompensas()
        actualizar_pantalla(msg_victoria)
    else:
        actualizar_pantalla(mensaje_extra)
        turno_enemigo()  # 🔥 NUEVO: El enemigo contraataca

def defender(event):
    """🔥 NUEVO: Activa la defensa para reducir daño"""
    global combate_activo
    
    if not combate_activo or enemigo_vida <= 0:
        actualizar_pantalla("No hay necesidad de defenderte ahora.")
        return
    
    jugador.activar_defensa()
    actualizar_pantalla("🛡️ Adoptaste postura defensiva. El próximo ataque hará la mitad de daño.")
    turno_enemigo()

def curar(event):
    """Sistema de curación mejorado"""
    global combate_activo
    
    if len(jugador.inventario) > 0 and "Poción" in jugador.inventario:
        # Usar poción del inventario
        jugador.inventario.remove("Poción")
        curacion = 25
        jugador.curar(curacion)
        actualizar_pantalla(f"🧪 Usaste una Poción del inventario. +{curacion} de vida.")
    else:
        # Curación básica (gratis pero menos efectiva)
        curacion = 15
        jugador.curar(curacion)
        actualizar_pantalla(f"💚 Te curaste un poco. +{curacion} de vida.")
    
    if combate_activo and enemigo_vida > 0:
        turno_enemigo()

def nuevo_combate(event):
    """🔥 NUEVO: Inicia un nuevo combate"""
    global enemigo_vida, enemigo_max, combate_activo
    
    enemigo_vida = 50 + (jugador.nivel * 10)  # Enemigos más fuertes en niveles altos
    enemigo_max = enemigo_vida
    combate_activo = True
    
    tipos_enemigo = ["Ogro", "Goblin", "Troll", "Orco", "Lobo Salvaje"]
    enemigo_nombre = random.choice(tipos_enemigo)
    
    actualizar_pantalla(f"⚠️ ¡Un {enemigo_nombre} salvaje apareció! ({enemigo_vida} HP)")

# Mensaje inicial
actualizar_pantalla("Te encuentras frente a un ogro gruñón. ¿Qué harás?")
