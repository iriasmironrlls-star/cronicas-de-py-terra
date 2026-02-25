from pyscript import document
from personajes import Heroe
from base_datos import ITEMS_DB, ENEMIGOS_DB, HABILIDADES_DB, get_color_rareza, get_item, get_enemigo
import random

# ═══════════════════════════════════════════════════════════════
# 🎮 INICIALIZACIÓN DEL JUEGO
# ═══════════════════════════════════════════════════════════════

# Crear jugador
jugador = Heroe("Reencarnado", 100)

# Estado del enemigo actual
enemigo_actual = None
enemigo_vida = 0
enemigo_vida_max = 0

# Variables de combate
combate_activo = False

# ═══════════════════════════════════════════════════════════════
# 🖥️ ACTUALIZACIÓN DE INTERFAZ
# ═══════════════════════════════════════════════════════════════

def actualizar_pantalla(texto):
    """Actualiza todos los elementos de la interfaz"""
    document.getElementById("historia").innerHTML = texto
    document.getElementById("vida-jugador").innerHTML = f"{jugador.vida}/{jugador.vida_max}"
    document.getElementById("mp-jugador").innerHTML = f"{jugador.mp}/{jugador.mp_max}"
    document.getElementById("vida-enemigo").innerHTML = str(enemigo_vida) if combate_activo else "-"
    document.getElementById("nivel").innerHTML = str(jugador.nivel)
    document.getElementById("exp").innerHTML = f"{jugador.experiencia}/{jugador.exp_para_subir}"
    document.getElementById("oro").innerHTML = str(jugador.oro)
    document.getElementById("inventario-count").innerHTML = str(jugador.contar_items())
    
    # Actualizar stats del personaje
    document.getElementById("stat-str").innerHTML = str(jugador.fuerza)
    document.getElementById("stat-dex").innerHTML = str(jugador.destreza)
    document.getElementById("stat-end").innerHTML = str(jugador.aguante)
    document.getElementById("stat-atk").innerHTML = str(jugador.get_ataque_total())
    document.getElementById("stat-def").innerHTML = str(jugador.get_defensa_total())

# ═══════════════════════════════════════════════════════════════
# ⚔️ SISTEMA DE COMBATE
# ═══════════════════════════════════════════════════════════════

def generar_enemigo(nivel_sugerido=None):
    """Genera un enemigo aleatorio"""
    global enemigo_actual, enemigo_vida, enemigo_vida_max, combate_activo
    
    if nivel_sugerido is None:
        nivel_sugerido = jugador.nivel
    
    # Seleccionar enemigo aleatorio
    enemigos_disponibles = list(ENEMIGOS_DB.keys())
    nombre_enemigo = random.choice(enemigos_disponibles)
    enemigo_actual = ENEMIGOS_DB[nombre_enemigo].copy()
    enemigo_actual["nombre"] = nombre_enemigo
    
    # Ajustar nivel
    nivel_enemigo = max(1, nivel_sugerido + random.randint(-1, 2))
    enemigo_actual["nivel"] = nivel_enemigo
    
    # Escalar stats según nivel
    multiplicador = 1 + (nivel_enemigo - enemigo_actual["nivel_base"]) * 0.3
    enemigo_vida = int(enemigo_actual["stats"]["hp"] * multiplicador)
    enemigo_vida_max = enemigo_vida
    
    combate_activo = True
    
    return nombre_enemigo, nivel_enemigo

def turno_enemigo():
    """El enemigo ataca al jugador"""
    global combate_activo, enemigo_vida
    
    if enemigo_vida > 0 and jugador.vida > 0:
        ataque_base = enemigo_actual["stats"]["ataque"]
        nivel_enemigo = enemigo_actual["nivel"]
        daño_enemigo = random.randint(ataque_base - 2, ataque_base + 5) + (nivel_enemigo * 2)
        
        daño_real, defendio = jugador.recibir_daño(daño_enemigo)
        jugador.vida -= daño_real
        
        nombre_enemigo = enemigo_actual["nombre"]
        if defendio:
            mensaje = f"🛡️ ¡Bloqueaste! El {nombre_enemigo} causó {daño_real} de daño (reducido)."
        else:
            mensaje = f"👹 ¡El {nombre_enemigo} te golpea! Recibes {daño_real} de daño."
        
        if jugador.vida <= 0:
            jugador.vida = 0
            combate_activo = False
            actualizar_pantalla("💀 Has sido derrotado... GAME OVER<br><small>Presiona NUEVO COMBATE para reintentar</small>")
            return
        
        actualizar_pantalla(mensaje)

def dar_recompensas():
    """Da oro, experiencia e items al derrotar enemigo"""
    oro_min = enemigo_actual.get("oro_min", 10)
    oro_max = enemigo_actual.get("oro_max", 30)
    exp_ganada = enemigo_actual.get("exp", 20) * enemigo_actual["nivel"]
    
    oro_ganado = random.randint(oro_min, oro_max) + (enemigo_actual["nivel"] * 10)
    
    jugador.ganar_oro(oro_ganado)
    nivel_anterior = jugador.nivel
    jugador.ganar_experiencia(exp_ganada)
    jugador.combates_ganados += 1
    jugador.enemigos_derrotados += 1
    
    # Sistema de drops
    drops_posibles = enemigo_actual.get("drops", [])
    drops = []
    
    for item_nombre in drops_posibles:
        if random.random() < 0.4:  # 40% probabilidad por item
            if item_nombre in ITEMS_DB:
                item_data = ITEMS_DB[item_nombre]
                jugador.agregar_item(item_nombre)
                color = get_color_rareza(item_data.get("rareza", "comun"))
                icono = item_data.get("icono", "📦")
                drops.append(f'<span style="color:{color}">{icono} {item_nombre}</span>')
    
    if drops:
        items_msg = f"<br>📦 Drops: {', '.join(drops)}"
    else:
        items_msg = ""
    
    if jugador.nivel > nivel_anterior:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{items_msg}<br>⭐ ¡SUBISTE AL NIVEL {jugador.nivel}! Stats mejorados y vida restaurada."
    else:
        msg = f"🎉 ¡VICTORIA! +{oro_ganado}💰 +{exp_ganada}✨{items_msg}"
    
    return msg

def atacar(event):
    """Ataque básico del jugador"""
    global enemigo_vida, combate_activo
    
    if not combate_activo or enemigo_vida <= 0:
        actualizar_pantalla("No hay enemigos que enfrentar.")
        return
    
    # Calcular daño con stats
    ataque_total = jugador.get_ataque_total()
    critico_chance = jugador.get_critico_total()
    
    # Sistema de críticos mejorado
    dado = random.random() * 100
    
    if dado < 10:  # 10% fallo
        daño = 0
        mensaje = "❌ ¡Tu ataque falló!"
    elif dado > (100 - critico_chance):  # Basado en stat de crítico
        daño = ataque_total * 2
        mensaje = f"💥 ¡CRÍTICO! Causaste {daño} de daño."
        jugador.daño_total_causado += daño
    else:  # Ataque normal
        daño = random.randint(ataque_total - 3, ataque_total + 3)
        mensaje = f"⚔️ ¡Atacaste! Causaste {daño} de daño."
        jugador.daño_total_causado += daño
    
    enemigo_vida -= daño
    
    if enemigo_vida <= 0:
        enemigo_vida = 0
        combate_activo = False
        msg_victoria = dar_recompensas()
        actualizar_pantalla(msg_victoria)
    else:
        actualizar_pantalla(mensaje)
        turno_enemigo()

def defender(event):
    """Activa la defensa"""
    if not combate_activo or enemigo_vida <= 0:
        actualizar_pantalla("No hay necesidad de defenderte ahora.")
        return
    
    jugador.activar_defensa()
    actualizar_pantalla(f"🛡️ Adoptaste postura defensiva. DEF actual: {jugador.get_defensa_total() * 2}")
    turno_enemigo()

def curar(event):
    """Sistema de curación con diferentes pociones"""
    pociones = {
        "Elixir Legendario": 9999,
        "Gran Poción": 100,
        "Poción": 50,
        "Poción de Moho Azul": 20
    }
    
    usado = False
    for pocion, curacion in pociones.items():
        if jugador.tiene_item(pocion):
            jugador.usar_item(pocion)
            jugador.curar(curacion)
            item_data = get_item(pocion)
            icono = item_data.get("icono", "🧪")
            actualizar_pantalla(f"{icono} Usaste {pocion}. +{min(curacion, jugador.vida_max - jugador.vida)} de vida.")
            usado = True
            break
    
    if not usado:
        curacion = 15
        jugador.curar(curacion)
        actualizar_pantalla(f"💚 Vendaje básico. +{curacion} de vida.")
    
    if combate_activo and enemigo_vida > 0:
        turno_enemigo()

def nuevo_combate(event):
    """Inicia un nuevo combate"""
    nombre, nivel = generar_enemigo()
    icono = enemigo_actual.get("icono", "👹")
    actualizar_pantalla(f"⚠️ ¡Un {icono} {nombre} Nv.{nivel} apareció! ({enemigo_vida} HP)")

# ═══════════════════════════════════════════════════════════════
# 🔍 SISTEMA DE ANÁLISIS DE ENEMIGOS
# ═══════════════════════════════════════════════════════════════

def analizar_enemigo(event):
    """Muestra información detallada del enemigo con lore inmersivo"""
    if not combate_activo or not enemigo_actual:
        actualizar_pantalla("No hay enemigo para analizar.")
        return
    
    modal = document.getElementById("modal-analisis")
    
    # Información básica
    nombre = enemigo_actual["nombre"]
    nivel = enemigo_actual["nivel"]
    icono = enemigo_actual.get("icono", "👹")
    categoria = enemigo_actual.get("categoria", "Desconocido")
    
    document.getElementById("analisis-nombre").innerHTML = f"{icono} {nombre} Nv.{nivel}"
    document.getElementById("analisis-categoria").innerHTML = categoria
    
    # Estado visual del enemigo
    estado_visual = enemigo_actual.get("estado_visual", enemigo_actual.get("descripcion", ""))
    document.getElementById("analisis-estado").innerHTML = estado_visual
    
    # Descripción y lore
    document.getElementById("analisis-desc").innerHTML = enemigo_actual.get("descripcion", "")
    document.getElementById("analisis-lore").innerHTML = f'<em style="color:#888">"{enemigo_actual.get("lore", "")}"</em>'
    
    # Equipo visual del enemigo
    equipo_visual = enemigo_actual.get("equipo_visual", {})
    equipo_html = ""
    if equipo_visual:
        if "arma" in equipo_visual:
            equipo_html += f"⚔️ <strong>{equipo_visual['arma']}</strong>"
            if "arma_stats" in equipo_visual:
                equipo_html += f" <span style='color:#00ff41'>({equipo_visual['arma_stats']})</span>"
            equipo_html += "<br>"
        if "escudo" in equipo_visual:
            equipo_html += f"🛡️ <strong>{equipo_visual['escudo']}</strong>"
            if "escudo_stats" in equipo_visual:
                equipo_html += f" <span style='color:#00ff41'>({equipo_visual['escudo_stats']})</span>"
            equipo_html += "<br>"
        if "armadura" in equipo_visual:
            equipo_html += f"🦺 <strong>{equipo_visual['armadura']}</strong><br>"
        if "arma_natural" in equipo_visual:
            equipo_html += f"🦴 <strong>{equipo_visual['arma_natural']}</strong><br>"
    
    # Objeto engullido (para slimes)
    if "objeto_engullido" in enemigo_actual:
        equipo_html += f"<br>📦 <em style='color:#ffaa00'>Objeto visible: {enemigo_actual['objeto_engullido']}</em>"
    
    document.getElementById("analisis-equipo").innerHTML = equipo_html if equipo_html else "<span style='color:#888'>Sin equipo</span>"
    
    # Stats
    stats = enemigo_actual["stats"]
    document.getElementById("analisis-hp").innerHTML = f"{enemigo_vida}/{enemigo_vida_max}"
    document.getElementById("analisis-mp").innerHTML = str(stats.get("mp", 0))
    document.getElementById("analisis-atk").innerHTML = str(stats.get("ataque", 0))
    document.getElementById("analisis-def").innerHTML = str(stats.get("defensa", 0))
    document.getElementById("analisis-spd").innerHTML = str(stats.get("velocidad", 0))
    
    # Resistencias
    resistencias = enemigo_actual.get("resistencias", {})
    res_html = ""
    for elem, valor in resistencias.items():
        if valor >= 100:
            res_html += f"<span style='color:#00ff00; font-weight:bold'>{elem.upper()}: INMUNE ✓</span><br>"
        elif valor >= 50:
            res_html += f"<span style='color:#ffff00'>{elem.upper()}: {valor}% (Alta)</span><br>"
        elif valor > 0:
            res_html += f"<span style='color:#ffaa00'>{elem.upper()}: {valor}%</span><br>"
    document.getElementById("analisis-res").innerHTML = res_html if res_html else "<span style='color:#888'>Ninguna</span>"
    
    # Debilidades
    debilidades = enemigo_actual.get("debilidades", {})
    deb_html = ""
    for elem, valor in debilidades.items():
        if valor >= 250:
            color = "#ff0000"
            nivel = "CRÍTICA"
        elif valor >= 200:
            color = "#ff4444"
            nivel = "Severa"
        elif valor >= 150:
            color = "#ff8800"
            nivel = "Moderada"
        else:
            color = "#ffaa00"
            nivel = "Leve"
        deb_html += f"<span style='color:{color}; font-weight:bold'>{elem.upper()}: {valor}% ({nivel})</span><br>"
    document.getElementById("analisis-deb").innerHTML = deb_html if deb_html else "<span style='color:#888'>Ninguna</span>"
    
    # Habilidades
    habilidades = enemigo_actual.get("habilidades", [])
    hab_html = ""
    for hab in habilidades:
        hab_html += f"<div class='habilidad-enemigo'>"
        hab_html += f"<strong style='color:#ffd700; font-size:1.1rem'>{hab['nombre']}</strong><br>"
        hab_html += f"<small style='color:#ccc'>{hab['descripcion']}</small><br>"
        hab_html += f"<span style='color:#00ff41'>📊 Efecto: {hab['efecto']}</span><br>"
        hab_html += f"<small style='color:#888'>⏱️ Cooldown: {hab['cooldown']} turnos | 💙 Costo: {hab['costo_mp']} MP</small>"
        hab_html += f"</div>"
    document.getElementById("analisis-hab").innerHTML = hab_html
    
    modal.style.display = "flex"

def cerrar_analisis(event):
    """Cierra el modal de análisis"""
    document.getElementById("modal-analisis").style.display = "none"

# ═══════════════════════════════════════════════════════════════
# 🎒 GESTIÓN DE INVENTARIO Y EQUIPAMIENTO
# ═══════════════════════════════════════════════════════════════

def abrir_inventario(event):
    """Abre el modal del inventario"""
    modal = document.getElementById("modal-inventario")
    contenido = document.getElementById("lista-inventario")
    
    if jugador.contar_items() == 0:
        contenido.innerHTML = "<p style='text-align:center; color:#888;'>Inventario vacío</p>"
    else:
        html = ""
        for item_nombre, cantidad in jugador.inventario.items():
            item_data = get_item(item_nombre)
            if item_data:
                color = get_color_rareza(item_data.get("rareza", "comun"))
                icono = item_data.get("icono", "📦")
                tipo = item_data.get("tipo", "")
                
                html += f"<div class='item-inventario' onclick='mostrar_info_item(\"{item_nombre}\")'>"
                html += f"<span style='color:{color}'>{icono} {item_nombre} x{cantidad}</span>"
                html += f"<small style='color:#888'> [{tipo}]</small>"
                html += f"</div>"
        contenido.innerHTML = html
    
    modal.style.display = "flex"

def cerrar_inventario(event):
    """Cierra el modal del inventario"""
    document.getElementById("modal-inventario").style.display = "none"

def abrir_equipamiento(event):
    """Abre el modal de equipamiento"""
    modal = document.getElementById("modal-equipo")
    actualizar_vista_equipamiento()
    modal.style.display = "flex"

def cerrar_equipamiento(event):
    """Cierra el modal de equipamiento"""
    document.getElementById("modal-equipo").style.display = "none"

def actualizar_vista_equipamiento():
    """Actualiza la visualización del equipamiento"""
    slots = ["mano_derecha", "mano_izquierda", "torso", "cabeza", "piernas", "pies", "anillo", "cuello"]
    nombres_slots = {
        "mano_derecha": "⚔️ Mano Derecha",
        "mano_izquierda": "🛡️ Mano Izquierda",
        "torso": "🦺 Torso",
        "cabeza": "👑 Cabeza",
        "piernas": "👖 Piernas",
        "pies": "👢 Pies",
        "anillo": "💍 Anillo",
        "cuello": "📿 Cuello"
    }
    
    html = ""
    for slot in slots:
        item_data = jugador.equipo[slot]
        html += f"<div class='slot-equipo'>"
        html += f"<div class='slot-nombre'>{nombres_slots[slot]}</div>"
        
        if item_data:
            nombre = item_data.get("nombre", "???")
            color = get_color_rareza(item_data.get("rareza", "comun"))
            icono = item_data.get("icono", "📦")
            html += f"<div class='slot-item' style='color:{color}'>{icono} {nombre}</div>"
            html += f"<button class='btn-desequipar' onclick='desequipar(\"{slot}\")'>Quitar</button>"
        else:
            html += f"<div class='slot-vacio'>Vacío</div>"
        
        html += f"</div>"
    
    document.getElementById("vista-equipo").innerHTML = html

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

def explorar_mundo(event):
    """Explora el mundo y encuentra items/oro"""
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
        items_posibles = list(ITEMS_DB.keys())
        item_nombre = random.choice(items_posibles)
        item_data = ITEMS_DB[item_nombre]
        jugador.agregar_item(item_nombre)
        color = get_color_rareza(item_data.get("rareza", "comun"))
        icono = item_data.get("icono", "📦")
        actualizar_pantalla(f'🔍 ¡Exploraste y encontraste <span style="color:{color}">{icono} {item_nombre}</span>!')
        
    elif tipo == "oro":
        oro = random.randint(10, 50)
        jugador.ganar_oro(oro)
        actualizar_pantalla(f"💰 ¡Encontraste {oro} monedas de oro!")
        
    elif tipo == "combate":
        nuevo_combate(event)
        
    else:
        actualizar_pantalla("🌲 Exploraste la zona pero no encontraste nada interesante.")

def toggle_opciones(event):
    """Muestra/oculta botones extras"""
    botones = document.getElementById("botones-extra")
    if botones.style.display == "none" or botones.style.display == "":
        botones.style.display = "grid"
    else:
        botones.style.display = "none"

def abrir_config(event):
    """Abre configuración"""
    actualizar_pantalla("⚙️ Configuración - Próximamente: Música, efectos de sonido, dificultad...")

# Mensaje inicial
actualizar_pantalla("🌟 Bienvenido, Reencarnado. Tu aventura en Py-Terra comienza ahora...<br><small>Presiona NUEVO COMBATE para empezar</small>")
