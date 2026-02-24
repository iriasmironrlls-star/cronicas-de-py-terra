# ═══════════════════════════════════════════════════════════════
# 🔥 BASE DE DATOS MAESTRA - CRÓNICAS DE PY-TERRA 
# ═══════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════
# 📦 SISTEMA DE ITEMS
# ═══════════════════════════════════════════════════════════════

ITEMS_DB = {
    # ─────────────────────────────────────────────────────────────
    # 🧪 CONSUMIBLES - POCIONES
    # ─────────────────────────────────────────────────────────────
    "Poción de Moho Azul": {
        "id": "C001",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "comun",
        "descripcion": "Un brebaje viscoso hecho con hongos de cueva. Sabe a tierra húmeda, pero cierra las heridas.",
        "lore": "Los aventureros novatos aprenden rápido: si brilla azul en la oscuridad, probablemente te salve la vida... o te haga vomitar.",
        "efecto": "Recupera 20 HP",
        "efecto_secundario": "5% probabilidad de Náuseas (baja precisión 1 turno)",
        "valor_curacion": 20,
        "precio": 15,
        "icono": "🧪"
    },
    
    "Poción": {
        "id": "C002",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "raro",
        "descripcion": "Una poción estándar de curación hecha por alquimistas profesionales.",
        "lore": "Elaborada siguiendo recetas de siglos. El secreto está en la miel de abeja lunar y las lágrimas de sauce llorón.",
        "efecto": "Recupera 50 HP",
        "valor_curacion": 50,
        "precio": 50,
        "icono": "⚗️"
    },
    
    "Gran Poción": {
        "id": "C003",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "ultra_raro",
        "descripcion": "Una poción magistral que brilla con luz dorada. Se siente cálida al tacto.",
        "lore": "Solo los maestros alquimistas pueden destilar la esencia de vida pura. Dicen que una sola gota puede revivir flores marchitas.",
        "efecto": "Recupera 100 HP",
        "valor_curacion": 100,
        "precio": 150,
        "icono": "🌟"
    },
    
    "Elixir Legendario": {
        "id": "C004",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "legendario",
        "descripcion": "Un elixir mítico que late como un corazón. Restaura completamente la vida y rompe maldiciones.",
        "lore": "Forjado en las Fuentes de Aeterna. Solo 7 existen en todo Py-Terra. Los dioses lo beben en sus festivales.",
        "efecto": "Restaura HP y MP completos + Cura estados negativos",
        "valor_curacion": 9999,
        "precio": 1000,
        "icono": "💎"
    },
    
    # ─────────────────────────────────────────────────────────────
    # ⚔️ EQUIPAMIENTO - ARMAS
    # ─────────────────────────────────────────────────────────────
    "Espada Oxidada": {
        "id": "W001",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "comun",
        "descripcion": "Un pedazo de hierro viejo que apenas conserva su filo. Huele a óxido y abandono.",
        "lore": "Encontrada en el cadáver de un soldado olvidado. Su último dueño la soltó hace 50 años... y nunca volvió.",
        "stats": {"ataque": 5, "critico": 2},
        "durabilidad": 10,
        "precio": 20,
        "icono": "🗡️"
    },
    
    "Espada de Hierro": {
        "id": "W002",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "comun",
        "descripcion": "Una espada básica pero funcional. Forjada con hierro de mina.",
        "lore": "El arma estándar de cualquier soldado. Simple, efectiva, confiable. Como debe ser.",
        "stats": {"ataque": 12, "critico": 5},
        "durabilidad": 50,
        "precio": 100,
        "icono": "⚔️"
    },
    
    "Espada Flamígera": {
        "id": "W003",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "ultra_raro",
        "descripcion": "Una espada que arde con fuego eterno. El calor no quema a su portador.",
        "lore": "Forjada en el corazón de un volcán por el herrero Ignis. Las llamas nunca se apagan, ni siquiera bajo el agua.",
        "stats": {"ataque": 35, "critico": 15, "elemento": "fuego"},
        "durabilidad": 200,
        "precio": 800,
        "icono": "🔥"
    },
    
    "Colmillo de Dragón": {
        "id": "W004",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "legendario",
        "descripcion": "Un colmillo arrancado de la mandíbula del Dragón Anciano. Resuena con poder primordial.",
        "lore": "Solo un dragón muerto suelta sus colmillos. Quien porta esto ha matado lo imposible.",
        "stats": {"ataque": 80, "critico": 30, "fuerza": 10},
        "durabilidad": 999,
        "precio": 5000,
        "icono": "🐉"
    },
    
    # ─────────────────────────────────────────────────────────────
    # 🛡️ EQUIPAMIENTO - ARMADURAS
    # ─────────────────────────────────────────────────────────────
    "Túnica de Novato": {
        "id": "A001",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "comun",
        "descripcion": "Tela barata de algodón. Apenas protege del frío, menos de las espadas.",
        "lore": "Todo aventurero empieza con una de estas. Los que sobreviven, la queman como ritual de paso.",
        "stats": {"defensa": 2, "evasion": 2},
        "precio": 25,
        "icono": "👕"
    },
    
    "Armadura de Cuero": {
        "id": "A002",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "raro",
        "descripcion": "Cuero curtido de jabalí. Flexible pero resistente.",
        "lore": "El cuero de los jabalíes de Bosque Negro es conocido por su dureza. Detuvo más flechas que escudos de madera.",
        "stats": {"defensa": 8, "evasion": 5},
        "precio": 200,
        "icono": "🦺"
    },
    
    "Armadura Divina": {
        "id": "A003",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "legendario",
        "descripcion": "Armadura bendecida por los dioses. Brilla con luz sagrada y repele la oscuridad.",
        "lore": "Dicen que fue vestida por el primer Paladín. Las marcas de garras demoníacas se desvanecen al tocarla.",
        "stats": {"defensa": 50, "resistencia_oscuridad": 80, "regeneracion": 5},
        "precio": 4500,
        "icono": "✨"
    },
    
    # ─────────────────────────────────────────────────────────────
    # 💍 EQUIPAMIENTO - ACCESORIOS
    # ─────────────────────────────────────────────────────────────
    "Anillo de Fuerza": {
        "id": "ACC001",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "anillo",
        "rareza": "raro",
        "descripcion": "Un anillo grabado con runas de poder. Se siente pesado pero da fuerza.",
        "lore": "Usado por guerreros de la Orden del Puño de Hierro. Cada runa es un voto de fuerza inquebrantable.",
        "stats": {"fuerza": 5, "ataque": 3},
        "precio": 300,
        "icono": "💍"
    },
    
    "Amuleto de Vitalidad": {
        "id": "ACC002",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "cuello",
        "rareza": "ultra_raro",
        "descripcion": "Un amuleto que late suavemente. Aumenta tu capacidad vital.",
        "lore": "Tallado del corazón cristalizado de un Treant milenario. La vida fluye eternamente en su interior.",
        "stats": {"vida_max": 50, "regeneracion": 3},
        "precio": 600,
        "icono": "📿"
    },
    
    # ─────────────────────────────────────────────────────────────
    # 🔧 MATERIALES
    # ─────────────────────────────────────────────────────────────
    "Mineral de Hierro": {
        "id": "M001",
        "tipo": "material",
        "rareza": "comun",
        "descripcion": "Mineral básico para herrería. Denso y oscuro.",
        "lore": "La base de toda civilización. Sin hierro, no hay espadas. Sin espadas, no hay héroes.",
        "precio": 10,
        "icono": "⛏️"
    },
    
    "Cristal del Dragón": {
        "id": "M002",
        "tipo": "material",
        "rareza": "legendario",
        "descripcion": "Un cristal que contiene la esencia de un dragón. Pulsa con energía mágica.",
        "lore": "Cuando un dragón muere, su alma se condensa en un cristal. Este es el material más codiciado del reino.",
        "precio": 10000,
        "icono": "💠"
    }
}

# ═══════════════════════════════════════════════════════════════
# 👹 BESTIARIO - BASE DE DATOS DE ENEMIGOS
# ═══════════════════════════════════════════════════════════════

ENEMIGOS_DB = {
    "Escudero No-Muerto": {
        "id": "E001",
        "nivel_base": 1,
        "descripcion": "Un esqueleto que aún viste su armadura oxidada. Sus ojos vacíos brillan con odio.",
        "lore": "Soldados caídos que se niegan a descansar. Patrullan eternamente el campo de batalla donde murieron.",
        "stats": {
            "hp": 45,
            "mp": 10,
            "ataque": 8,
            "defensa": 6,
            "velocidad": 4
        },
        "equipo": {
            "arma": "Espada Rota (ATK +4)",
            "escudo": "Escudo de Madera Podrida (DEF +2)"
        },
        "resistencias": {
            "veneno": 100,  # Inmune
            "hielo": 50,
            "fisico": 0
        },
        "debilidades": {
            "fuego": 200,
            "sagrado": 300,
            "contundente": 150
        },
        "habilidades": [
            {
                "nombre": "Golpe de Pomo",
                "descripcion": "Golpea con el pomo de la espada, aturdiendo al enemigo",
                "efecto": "Aturde 1 turno",
                "cooldown": 3,
                "costo_mp": 5
            },
            {
                "nombre": "Guardia Oxidada",
                "descripcion": "Adopta postura defensiva, aumentando defensa pero perdiendo el siguiente ataque",
                "efecto": "DEF +30% por 1 turno, no puede atacar el siguiente turno",
                "cooldown": 4,
                "costo_mp": 8
            }
        ],
        "drops": ["Espada Oxidada", "Hueso Antiguo", "Mineral de Hierro"],
        "oro_min": 15,
        "oro_max": 30,
        "exp": 25,
        "icono": "💀"
    },
    
    "Slime de Hierro": {
        "id": "E002",
        "nivel_base": 2,
        "descripcion": "Un slime que consumió metal. Su cuerpo gelatinoso tiene trozos de hierro incrustados.",
        "lore": "Nacen en minas abandonadas. Se alimentan de minerales y se vuelven más densos con el tiempo.",
        "stats": {
            "hp": 60,
            "mp": 20,
            "ataque": 5,
            "defensa": 15,
            "velocidad": 2
        },
        "equipo": {},
        "resistencias": {
            "fisico": 60,
            "veneno": 100,
            "corte": 80
        },
        "debilidades": {
            "trueno": 250,
            "fuego": 150,
            "magia": 120
        },
        "habilidades": [
            {
                "nombre": "Lluvia Ácida",
                "descripcion": "Escupe ácido que reduce la defensa del enemigo",
                "efecto": "Daño moderado + DEF -20% por 2 turnos",
                "cooldown": 2,
                "costo_mp": 10
            },
            {
                "nombre": "División Celular",
                "descripcion": "Se divide en dos slimes más pequeños (solo si HP > 50%)",
                "efecto": "Crea un slime aliado con 30% HP",
                "cooldown": 999,  # Solo una vez por combate
                "costo_mp": 15
            }
        ],
        "drops": ["Gelatina de Slime", "Mineral de Hierro", "Núcleo de Slime"],
        "oro_min": 20,
        "oro_max": 45,
        "exp": 40,
        "icono": "🟢"
    },
    
    "Lobo Alfa": {
        "id": "E003",
        "nivel_base": 3,
        "descripcion": "El líder de la manada. Cicatrices cruzan su pelaje gris. Más grande y feroz que los lobos comunes.",
        "lore": "Ha sobrevivido 20 inviernos. Su aullido paraliza de miedo a los viajeros. La manada lo sigue hasta la muerte.",
        "stats": {
            "hp": 85,
            "mp": 15,
            "ataque": 18,
            "defensa": 8,
            "velocidad": 14
        },
        "equipo": {},
        "resistencias": {
            "hielo": 50,
            "oscuridad": 30
        },
        "debilidades": {
            "fuego": 180,
            "luz": 150
        },
        "habilidades": [
            {
                "nombre": "Mordida Salvaje",
                "descripcion": "Muerde ferozmente con probabilidad de sangrado",
                "efecto": "Daño alto + 40% prob. de Sangrado (5 HP/turno x 3 turnos)",
                "cooldown": 2,
                "costo_mp": 8
            },
            {
                "nombre": "Aullido de Guerra",
                "descripcion": "Aulla convocando refuerzos y aumentando su ataque",
                "efecto": "ATK +50% x 3 turnos + 30% prob. de invocar lobo menor",
                "cooldown": 5,
                "costo_mp": 12
            }
        ],
        "drops": ["Colmillo de Lobo", "Piel de Lobo", "Carne Fresca"],
        "oro_min": 40,
        "oro_max": 70,
        "exp": 65,
        "icono": "🐺"
    },
    
    "Gólem de Piedra": {
        "id": "E004",
        "nivel_base": 4,
        "descripcion": "Una construcción mágica de piedra antigua. Runas brillan en su pecho rocoso.",
        "lore": "Guardianes creados por magos hace siglos. Protegen ruinas olvidadas y tesoros enterrados. No sienten dolor ni miedo.",
        "stats": {
            "hp": 150,
            "mp": 30,
            "ataque": 25,
            "defensa": 30,
            "velocidad": 1
        },
        "equipo": {},
        "resistencias": {
            "fisico": 50,
            "veneno": 100,
            "tierra": 100
        },
        "debilidades": {
            "trueno": 200,
            "agua": 150,
            "perforante": 120
        },
        "habilidades": [
            {
                "nombre": "Puño Sísmico",
                "descripcion": "Golpea el suelo creando una onda de choque",
                "efecto": "Daño a todos los enemigos + 25% aturdir 1 turno",
                "cooldown": 3,
                "costo_mp": 15
            },
            {
                "nombre": "Muro de Piedra",
                "descripcion": "Se cubre de capas de roca adicionales",
                "efecto": "DEF +100% x 2 turnos, no puede moverse",
                "cooldown": 6,
                "costo_mp": 20
            }
        ],
        "drops": ["Fragmento de Gólem", "Runa Antigua", "Núcleo de Tierra"],
        "oro_min": 60,
        "oro_max": 100,
        "exp": 90,
        "icono": "🗿"
    },
    
    "Dragón Corrupto": {
        "id": "E005",
        "nivel_base": 10,
        "descripcion": "Un dragón caído en la oscuridad. Su aliento es veneno y sus escamas rezuman maldad.",
        "lore": "Antes era un dragón noble. La corrupción lo devoró desde dentro. Ahora solo busca destruir lo que una vez protegió.",
        "stats": {
            "hp": 500,
            "mp": 150,
            "ataque": 60,
            "defensa": 40,
            "velocidad": 12
        },
        "equipo": {},
        "resistencias": {
            "oscuridad": 100,
            "veneno": 80,
            "fuego": 50
        },
        "debilidades": {
            "sagrado": 300,
            "luz": 250,
            "dragon_slayer": 400
        },
        "habilidades": [
            {
                "nombre": "Aliento Corrupto",
                "descripcion": "Exhala un aliento tóxico que envenena y maldice",
                "efecto": "Daño masivo + Veneno (20 HP/turno) + Maldición (ATK -30%)",
                "cooldown": 4,
                "costo_mp": 40
            },
            {
                "nombre": "Vuelo Rasante",
                "descripcion": "Vuela alto y se lanza en picada",
                "efecto": "Daño brutal + Evasión +100% el turno anterior",
                "cooldown": 3,
                "costo_mp": 30
            },
            {
                "nombre": "Furia del Caído",
                "descripcion": "Se activa automáticamente cuando HP < 30%",
                "efecto": "ATK +200%, DEF -50%, Velocidad +100%",
                "cooldown": 999,  # Pasiva, solo una vez
                "costo_mp": 0
            }
        ],
        "drops": ["Escama de Dragón", "Colmillo de Dragón", "Cristal del Dragón", "Corazón Corrupto"],
        "oro_min": 500,
        "oro_max": 1000,
        "exp": 500,
        "icono": "🐲"
    }
}

# ═══════════════════════════════════════════════════════════════
# ⚡ HABILIDADES DEL JUGADOR
# ═══════════════════════════════════════════════════════════════

HABILIDADES_DB = {
    "Análisis de Otro Mundo": {
        "id": "S001",
        "tipo": "pasiva",
        "descripcion": "Tu conocimiento de otro mundo te permite ver información oculta de enemigos.",
        "lore": "Los reencarnados ven el mundo como datos. HP, debilidades, habilidades... todo es información.",
        "efecto": "Permite ver HP exacto, debilidades y habilidades de enemigos",
        "icono": "👁️"
    },
    
    "Corte Cruzado": {
        "id": "S002",
        "tipo": "activa",
        "descripcion": "Un ataque rápido en forma de X. Golpea dos veces.",
        "lore": "Técnica básica de espadachín. Simple pero letal si se ejecuta correctamente.",
        "efecto": "Daño Base × 1.5, 2 golpes",
        "costo_mp": 10,
        "cooldown": 2,
        "icono": "❌"
    },
    
    "Golpe Poderoso": {
        "id": "S003",
        "tipo": "activa",
        "descripcion": "Concentras toda tu fuerza en un solo golpe devastador.",
        "lore": "Sacrificas velocidad por poder. Un golpe bien dado puede cambiar la batalla.",
        "efecto": "Daño Base × 3.0, ignora 50% de defensa",
        "costo_mp": 25,
        "cooldown": 4,
        "icono": "💥"
    }
}

# ═══════════════════════════════════════════════════════════════
# 🎨 UTILIDADES
# ═══════════════════════════════════════════════════════════════

def get_color_rareza(rareza):
    """Retorna el color HTML según rareza"""
    colores = {
        "comun": "#00ff00",
        "raro": "#0080ff",
        "ultra_raro": "#8000ff",
        "legendario": "#ff0000"
    }
    return colores.get(rareza, "#ffffff")

def get_item(nombre):
    """Obtiene un item de la base de datos"""
    return ITEMS_DB.get(nombre, None)

def get_enemigo(nombre):
    """Obtiene un enemigo de la base de datos"""
    return ENEMIGOS_DB.get(nombre, None)

def get_habilidad(nombre):
    """Obtiene una habilidad de la base de datos"""
    return HABILIDADES_DB.get(nombre, None)
