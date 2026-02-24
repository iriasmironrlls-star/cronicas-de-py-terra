from pyscript import document
from personajes import Heroe, Item
import random

# Creamos al jugador usando la clase del otro archivo
jugador = Heroe("Guerrero", 100)
enemigo_vida = 50
enemigo_max = 50
enemigo_nivel = 1  # 🔥 NUEVO: Nivel del enemigo
enemigo_nombre = "Ogro"  # 🔥 NUEVO: Nombre del enemigo

# Variables de combate
combate_activo = True
mensaje_extra = ""

# 🔥 NUEVO: Base de datos de items por rareza
ITEMS_DROPS = {
    "comun": ["Poción menor", "Hierba curativa", "Pan duro", "Agua"],
    "raro": ["Poción", "Elixir", "Antídoto", "Espada oxidada"],
    "ultra_raro": ["Gran poción", "Poción mágica", "Amuleto", "Gema azul"],
    "legendario": ["Elixir legendario", "Espada flamígera", "Armadura divina", "Cristal del dragón"]
}

def actualizar_pantalla(texto):
    """Actualiza todos los elementos de la interfaz"""
    document.getElementById("historia").innerHTML = texto
    document.getElementById("vida-jugador").innerHTML = str(jugador.vida)
    document.getElementById("vida-enemigo").innerHTML = str(enemigo_vida)
    document.getElementById("nivel").innerHTML = str(jugador.nivel)
    document.getElementById("exp").innerHTML = f"{jugador.experiencia}/{jugador.exp_para_subir}"
    document.getElementById("oro").innerHTML = str(jugador.oro)
    document.getElementById("inventario-count").innerHTML = str(jugador.contar_items())

def generar_drop():
    """🔥 NUEVO: Genera un item aleatorio según rareza del enemigo"""
    # Probabilidades según nivel del enemigo
    roll = random.random()
    
    if enemigo_nivel >= 5:
        # Enemigos nivel 5+ pueden dar legendarios
        if roll < 0.05:  # 5% legendario
            rareza = "legendario"
        elif roll < 0.20:  # 15% ultra raro
            rareza = "ultra_raro"
        elif roll < 0.50:  # 30% raro
            rareza = "raro"
        else:  # 50% común
            rareza = "comun"
    elif enemigo_nivel >= 3:
        # Enemigos nivel 3-4
        if roll < 0.15:  # 15% ultra raro
            rareza = "ultra_raro"
        elif roll < 0.40:  # 25% raro
            rareza = "raro"
        else:  # 60% común
            rareza = "comun"
    else:
        # Enemigos nivel 1-2
        if roll < 0.25:  # 25% raro
            rareza = "raro"
        else:  # 75% común
            rareza = "comun"
    
    item_nombre = random.choice(ITEMS_DROPS[rareza])
    return item_nombre, rareza

def turno_enemigo():
    """El enemigo ataca al jugador"""
    global combate_activo, mensaje_extra
    
    if enemigo_vida > 0 and jugador.vida > 0:
        daño_enemigo = random.randint(5, 15) + (enemigo_nivel * 2)
        daño_real, defendio = jugador.recibir_daño(daño_enemigo)
        jugador.vida -= daño_real
        
        if defendio:
            mensaje_extra = f"🛡️ ¡Bloqueaste! Solo recibiste {daño_real} de daño (reducido de {daño_enemigo})."
        else:
            mensaje_extra = f"👹 ¡El {enemigo_nombre} te golpea! Recibes {daño_real} de daño."
        
        if jugador.vida <= 0:
            jugador.vida = 0
            combate_activo = False
            actualizar_pantalla("💀 Has sido derrotado... GAME OVER")
            return
        
        actualizar_pantalla(mensaje_extra)

def dar_recompensas():
    """Da oro, experiencia e items al derrotar enemigo"""
    oro_ganado = random.randint(20, 50) + (enemigo_nivel * 10)
    exp_ganada = random.randint(30, 60) + (enemigo_nivel * 20)
    
    jugador.ganar_oro(oro_ganado)
    jugador.ganar_experiencia(exp_ganada)
    jugador.combates_ganados += 1
    jugador.enemigos_derrotados += 1
    
    # 🔥 NUEVO: Sistema de drops con rareza
    drops = []
    num_drops = random.randint(1, 3)  # 1-3 items
    
    for _ in range(num_drops):
        if random.random() < 0.7:  # 70% de probabilidad de drop
            item_nombre, rareza = generar_drop()
            jugador.agregar_item(item_nombre)
            
            # Colores para el mensaje
            color_map = {
                "comun": "#00ff00",
                "raro": "#0080ff",
                "ultra_raro": "#8000ff",
                "legendario": "#ff0000"
            }
            color = color_map[rareza]
            drops.append(f'<span style="color:{color}">{item_nombre}</span>')
    
    if drops:
        items_msg = f"<br>📦 Drops: {', '.join(drops)}"
    else:
        items_msg = ""
    
    nivel_subio = jugador.experiencia == 0 and jugador.nivel > 1
    
    if nivel_subio:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{items_msg}<br>⭐ ¡SUBISTE AL NIVEL {jugador.nivel}! Vida restaurada."
    else:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{items_msg}"
    
    return msg

def atacar(event):
    """Sistema de ataque mejorado con críticos y fallos"""
    global enemigo_vida, combate_activo, mensaje_extra
    
    if not combate_activo or enemigo_vida <= 0:
        actualizar_pantalla("No hay enemigos que enfrentar.")
        return
    
    dado = random.random()
    daño_base = 10 + (jugador.nivel * 2)
    
    if dado < 0.1:  # 10% de fallo
        mensaje_extra = "❌ ¡Tu ataque falló!"
        daño = 0
    elif dado > 0.85:  # 15% de crítico
        daño = daño_base * 2
        mensaje_extra = f"💥 ¡CRÍTICO! Causaste {daño} de daño."
        jugador.daño_total_causado += daño
    else:  # Ataque normal
        daño = daño_base
        mensaje_extra = f"⚔️ ¡Atacaste! El enemigo perdió {daño} de vida."
        jugador.daño_total_causado += daño
    
    enemigo_vida -= daño
    
    if enemigo_vida <= 0:
        enemigo_vida = 0
        combate_activo = False
        msg_victoria = dar_recompensas()
        actualizar_pantalla(msg_victoria)
    else:
        actualizar_pantalla(mensaje_extra)
        turno_enemigo()

def defender(event):
    """Activa la defensa para reducir daño"""
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
    
    # Intentar usar pociones en orden de poder
    pociones = ["Gran poción", "Poción mágica", "Poción", "Poción menor", "Hierba curativa"]
    curacion_map = {"Gran poción": 50, "Poción mágica": 40, "Poción": 25, "Poción menor": 15, "Hierba curativa": 10}
    
    usado = False
    for pocion in pociones:
        if pocion in jugador.inventario:
            jugador.usar_item(pocion)
            curacion = curacion_map[pocion]
            jugador.curar(curacion)
            actualizar_pantalla(f"🧪 Usaste {pocion}. +{curacion} de vida.")
            usado = True
            break
    
    if not usado:
        # Curación básica gratis
        curacion = 15
        jugador.curar(curacion)
        actualizar_pantalla(f"💚 Te curaste un poco. +{curacion} de vida.")
    
    if combate_activo and enemigo_vida > 0:
        turno_enemigo()

def nuevo_combate(event):
    """Inicia un nuevo combate"""
    global enemigo_vida, enemigo_max, combate_activo, enemigo_nivel, enemigo_nombre
    
    enemigo_nivel = max(1, jugador.nivel + random.randint(-1, 2))
    enemigo_vida = 50 + (enemigo_nivel * 15)
    enemigo_max = enemigo_vida
    combate_activo = True
    
    tipos_enemigo = ["Ogro", "Goblin", "Troll", "Orco", "Lobo Salvaje", "Esqueleto", "Bandido"]
    enemigo_nombre = random.choice(tipos_enemigo)
    
    actualizar_pantalla(f"⚠️ ¡Un {enemigo_nombre} Nv.{enemigo_nivel} apareció! ({enemigo_vida} HP)")

def explorar_mundo(event):
    """🔥 NUEVO: Explora el mundo y encuentra items/oro"""
    eventos = [
        {"tipo": "item", "prob": 0.4},
        {"tipo": "oro", "prob": 0.3},
        {"tipo": "nada", "prob": 0.2},
        {"tipo": "combate", "prob": 0.1}
    ]
    
    roll = random.random()
    acum = 0
    
    for evento in eventos:
        acum += evento["prob"]
        if roll < acum:
            tipo = evento["tipo"]
            break
    
    if tipo == "item":
        item_nombre, rareza = generar_drop()
        jugador.agregar_item(item_nombre)
        color_map = {
            "comun": "#00ff00",
            "raro": "#0080ff",
            "ultra_raro": "#8000ff",
            "legendario": "#ff0000"
        }
        color = color_map[rareza]
        actualizar_pantalla(f'🔍 ¡Exploraste y encontraste <span style="color:{color}">{item_nombre}</span>!')
        
    elif tipo == "oro":
        oro = random.randint(10, 50)
        jugador.ganar_oro(oro)
        actualizar_pantalla(f"💰 ¡Encontraste {oro} monedas de oro!")
        
    elif tipo == "combate":
        nuevo_combate(event)
        
    else:
        actualizar_pantalla("🌲 Exploraste la zona pero no encontraste nada interesante.")

# 🔥 NUEVO: Funciones para modales
def abrir_inventario(event):
    """Abre el modal del inventario"""
    modal = document.getElementById("modal-inventario")
    contenido = document.getElementById("lista-inventario")
    
    if jugador.contar_items() == 0:
        contenido.innerHTML = "<p style='text-align:center; color:#888;'>Inventario vacío</p>"
    else:
        html = ""
        for item, cantidad in jugador.inventario.items():
            html += f"<div class='item-inventario'>{item} <span style='color:#ffd700'>x{cantidad}</span></div>"
        contenido.innerHTML = html
    
    modal.style.display = "flex"

def cerrar_inventario(event):
    """Cierra el modal del inventario"""
    document.getElementById("modal-inventario").style.display = "none"

def abrir_stats(event):
    """Abre el modal de estadísticas"""
    modal = document.getElementById("modal-stats")
    
    document.getElementById("stat-nivel").innerHTML = str(jugador.nivel)
    document.getElementById("stat-vida").innerHTML = f"{jugador.vida}/{jugador.vida_max}"
    document.getElementById("stat-exp").innerHTML = f"{jugador.experiencia}/{jugador.exp_para_subir}"
    document.getElementById("stat-oro").innerHTML = str(jugador.oro)
    document.getElementById("stat-combates").innerHTML = str(jugador.combates_ganados)
    document.getElementById("stat-enemigos").innerHTML = str(jugador.enemigos_derrotados)
    document.getElementById("stat-dano").innerHTML = str(jugador.daño_total_causado)
    
    modal.style.display = "flex"

def cerrar_stats(event):
    """Cierra el modal de estadísticas"""
    document.getElementById("modal-stats").style.display = "none"

def toggle_opciones(event):
    """🔥 NUEVO: Muestra/oculta botones extras"""
    botones = document.getElementById("botones-extra")
    if botones.style.display == "none" or botones.style.display == "":
        botones.style.display = "grid"
    else:
        botones.style.display = "none"

def abrir_config(event):
    """🔥 NUEVO: Abre configuración"""
    actualizar_pantalla("⚙️ Configuración - Próximamente: Música, efectos de sonido, dificultad...")

# Mensaje inicial
actualizar_pantalla("Te encuentras frente a un ogro gruñón. ¿Qué harás?")
