# ═══════════════════════════════════════════════════════════════
# 🔥 BASE DE DATOS MAESTRA - CRÓNICAS DE PY-TERRA 
# Sistema de Items, Enemigos y Habilidades de Rango SSS
# ═══════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════
# 📦 SISTEMA DE ITEMS
# ═══════════════════════════════════════════════════════════════

ITEMS_DB = {
    # ─────────────────────────────────────────────────────────────
    # 🧪 CONSUMIBLES - POCIONES Y ALIMENTOS
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
        "precio_compra": 20,
        "precio_venta": 10,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "🧪"
    },
    
    "Poción": {
        "id": "C002",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "raro",
        "descripcion": "Una poción estándar de curación hecha por alquimistas profesionales. Sin efectos secundarios.",
        "lore": "Elaborada siguiendo recetas de siglos. El secreto está en la miel de abeja lunar y las lágrimas de sauce llorón.",
        "efecto": "Recupera 50 HP",
        "valor_curacion": 50,
        "precio_compra": 100,
        "precio_venta": 50,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "⚗️"
    },
    
    "Gran Poción": {
        "id": "C003",
        "tipo": "consumible",
        "subtipo": "curación",
        "rareza": "ultra_raro",
        "descripcion": "Una poción magistral que brilla con luz dorada. Se siente cálida al tacto y huele a primavera eterna.",
        "lore": "Solo los maestros alquimistas pueden destilar la esencia de vida pura. Dicen que una sola gota puede revivir flores marchitas.",
        "efecto": "Recupera 100 HP",
        "valor_curacion": 100,
        "precio_compra": 300,
        "precio_venta": 150,
        "is_stackable": True,
        "level_requirement": 5,
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
        "precio_compra": 2000,
        "precio_venta": 1000,
        "is_stackable": True,
        "level_requirement": 10,
        "icono": "💎"
    },
    
    "Pan Duro": {
        "id": "C005",
        "tipo": "consumible",
        "subtipo": "alimento",
        "rareza": "comun",
        "descripcion": "Pan de hace tres días. Duro como piedra pero comestible... técnicamente.",
        "lore": "El sustento del aventurero pobre. Algunos lo usan como arma contundente.",
        "efecto": "Recupera 5 HP",
        "valor_curacion": 5,
        "precio_compra": 5,
        "precio_venta": 1,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "🍞"
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
        "peso": 3,
        "precio_compra": 40,
        "precio_venta": 20,
        "is_stackable": False,
        "level_requirement": 0,
        "icono": "🗡️"
    },
    
    "Espada de Hierro": {
        "id": "W002",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "comun",
        "descripcion": "Una espada básica pero funcional. Forjada con hierro de mina. El arma estándar del soldado.",
        "lore": "El arma estándar de cualquier soldado. Simple, efectiva, confiable. Como debe ser. Miles han caído portándola, miles más la seguirán usando.",
        "stats": {"ataque": 12, "critico": 5},
        "durabilidad": 50,
        "peso": 5,
        "precio_compra": 200,
        "precio_venta": 100,
        "is_stackable": False,
        "level_requirement": 2,
        "icono": "⚔️"
    },
    
    "Espada Flamígera": {
        "id": "W003",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "ultra_raro",
        "descripcion": "Una espada que arde con fuego eterno. El calor no quema a su portador, pero todo lo demás se consume.",
        "lore": "Forjada en el corazón del Monte Ignis por el herrero legendario Vulkan. Las llamas nunca se apagan, ni siquiera bajo el agua.",
        "stats": {"ataque": 35, "critico": 15, "elemento": "fuego"},
        "durabilidad": 200,
        "peso": 6,
        "precio_compra": 1600,
        "precio_venta": 800,
        "is_stackable": False,
        "level_requirement": 8,
        "receta_crafteo": {
            "materiales": [
                {"item": "Espada de Hierro", "cantidad": 1},
                {"item": "Cristal de Fuego", "cantidad": 5},
                {"item": "Mineral de Hierro", "cantidad": 10}
            ],
            "oro_requerido": 500
        },
        "icono": "🔥"
    },
    
    "Colmillo de Dragón": {
        "id": "W004",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "legendario",
        "descripcion": "Un colmillo arrancado de la mandíbula del Dragón Anciano. Resuena con poder primordial y sed de batalla.",
        "lore": "Solo un dragón muerto suelta sus colmillos. Quien porta esto ha matado lo imposible. El colmillo recuerda la furia de su dueño.",
        "stats": {"ataque": 80, "critico": 30, "fuerza": 10},
        "durabilidad": 999,
        "peso": 8,
        "precio_compra": 10000,
        "precio_venta": 5000,
        "is_stackable": False,
        "level_requirement": 15,
        "icono": "🐉"
    },
    
    "Daga de Hierro": {
        "id": "W005",
        "tipo": "equipamiento",
        "subtipo": "arma",
        "slot": "mano_derecha",
        "rareza": "comun",
        "descripcion": "Una daga simple pero letal. Ligera y rápida, perfecta para ataques críticos.",
        "lore": "El arma favorita de asesinos y ladrones. En manos expertas, es más mortal que cualquier espada.",
        "stats": {"ataque": 8, "critico": 15, "velocidad": 3},
        "durabilidad": 40,
        "peso": 1,
        "precio_compra": 150,
        "precio_venta": 75,
        "is_stackable": False,
        "level_requirement": 1,
        "icono": "🗡️"
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
        "lore": "Todo aventurero empieza con una de estas. Los que sobreviven, la queman como ritual de paso. Los que no... bueno, ya no les importa.",
        "stats": {"defensa": 2, "evasion": 2},
        "peso": 2,
        "precio_compra": 50,
        "precio_venta": 25,
        "is_stackable": False,
        "level_requirement": 0,
        "icono": "👕"
    },
    
    "Armadura de Cuero": {
        "id": "A002",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "raro",
        "descripcion": "Cuero curtido de jabalí del Bosque Negro. Flexible pero resistente. Huele a naturaleza salvaje.",
        "lore": "El cuero de los jabalíes de Bosque Negro es conocido por su dureza antinatural. Ha detenido más flechas que escudos de roble.",
        "stats": {"defensa": 8, "evasion": 5},
        "peso": 5,
        "precio_compra": 400,
        "precio_venta": 200,
        "is_stackable": False,
        "level_requirement": 3,
        "icono": "🦺"
    },
    
    "Cota de Mallas": {
        "id": "A003",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "raro",
        "descripcion": "Anillos de acero entrelazados. Pesada pero ofrece excelente protección contra cortes.",
        "lore": "Cada anillo fue forjado individualmente y enlazado a mano. Lleva meses de trabajo. El tintinear del metal es música para un guerrero.",
        "stats": {"defensa": 15, "resistencia_corte": 20},
        "peso": 15,
        "precio_compra": 800,
        "precio_venta": 400,
        "is_stackable": False,
        "level_requirement": 5,
        "icono": "🛡️"
    },
    
    "Armadura Divina": {
        "id": "A004",
        "tipo": "equipamiento",
        "subtipo": "armadura",
        "slot": "torso",
        "rareza": "legendario",
        "descripcion": "Armadura bendecida por los dioses. Brilla con luz sagrada y repele la oscuridad como el amanecer repele la noche.",
        "lore": "Dicen que fue vestida por el primer Paladín. Las marcas de garras demoníacas se desvanecen al tocarla. Quien la porta lleva la bendición celestial.",
        "stats": {"defensa": 50, "resistencia_oscuridad": 80, "regeneracion": 5},
        "peso": 20,
        "precio_compra": 9000,
        "precio_venta": 4500,
        "is_stackable": False,
        "level_requirement": 12,
        "icono": "✨"
    },
    
    # ─────────────────────────────────────────────────────────────
    # 💍 EQUIPAMIENTO - ACCESORIOS
    # ─────────────────────────────────────────────────────────────
    "Anillo de Ojo de Cuervo": {
        "id": "ACC001",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "anillo",
        "rareza": "raro",
        "descripcion": "Tallado en obsidiana con la forma de un ojo vigilante. Mejora tu percepción en combate.",
        "lore": "Se dice que los antiguos exploradores lo usaban para detectar emboscadas en la Niebla de los Lamentos. El ojo nunca parpadea.",
        "stats": {"critico": 5, "vision": 1},
        "efecto_especial": "Permite ver HP exacto de enemigos de nivel 1-10",
        "peso": 0,
        "precio_compra": 400,
        "precio_venta": 200,
        "is_stackable": False,
        "level_requirement": 3,
        "icono": "👁️"
    },
    
    "Anillo de Fuerza": {
        "id": "ACC002",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "anillo",
        "rareza": "raro",
        "descripcion": "Un anillo grabado con runas de poder. Se siente pesado pero da fuerza sobrehumana.",
        "lore": "Usado por guerreros de la Orden del Puño de Hierro. Cada runa es un voto de fuerza inquebrantable. Quien lo usa no puede retroceder.",
        "stats": {"fuerza": 5, "ataque": 3},
        "peso": 0,
        "precio_compra": 600,
        "precio_venta": 300,
        "is_stackable": False,
        "level_requirement": 4,
        "icono": "💍"
    },
    
    "Amuleto de Vitalidad": {
        "id": "ACC003",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "cuello",
        "rareza": "ultra_raro",
        "descripcion": "Un amuleto que late suavemente contra tu pecho. Aumenta tu capacidad vital y regeneración.",
        "lore": "Tallado del corazón cristalizado de un Treant milenario. La vida fluye eternamente en su interior. Quien lo porta siente el latido del bosque.",
        "stats": {"vida_max": 50, "regeneracion": 3},
        "peso": 0,
        "precio_compra": 1200,
        "precio_venta": 600,
        "is_stackable": False,
        "level_requirement": 6,
        "icono": "📿"
    },
    
    "Colgante del Sabio": {
        "id": "ACC004",
        "tipo": "equipamiento",
        "subtipo": "accesorio",
        "slot": "cuello",
        "rareza": "ultra_raro",
        "descripcion": "Un colgante de plata con una gema azul que brilla con luz propia. Aumenta tu reserva de maná.",
        "lore": "Pertenecía al Archimago Merithios. La gema es un fragmento de estrella caída. Aún contiene ecos de hechizos olvidados.",
        "stats": {"mp_max": 30, "magia": 5},
        "peso": 0,
        "precio_compra": 1500,
        "precio_venta": 750,
        "is_stackable": False,
        "level_requirement": 7,
        "icono": "💠"
    },
    
    # ─────────────────────────────────────────────────────────────
    # 🔧 MATERIALES
    # ─────────────────────────────────────────────────────────────
    "Mineral de Hierro": {
        "id": "M001",
        "tipo": "material",
        "subtipo": "mineral",
        "rareza": "comun",
        "descripcion": "Mineral básico para herrería. Denso y oscuro. El fundamento de toda civilización.",
        "lore": "La base de toda civilización. Sin hierro, no hay espadas. Sin espadas, no hay héroes. Sin héroes... solo monstruos.",
        "peso": 2,
        "precio_compra": 20,
        "precio_venta": 10,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "⛏️"
    },
    
    "Cuero Salvaje": {
        "id": "M002",
        "tipo": "material",
        "subtipo": "cuero",
        "rareza": "comun",
        "descripcion": "Cuero curtido de bestias salvajes. Flexible y resistente.",
        "lore": "De cada bestia caída, un cazador obtiene su tributo. Este cuero ha visto la libertad de los bosques.",
        "peso": 1,
        "precio_compra": 30,
        "precio_venta": 15,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "🦌"
    },
    
    "Cristal del Dragón": {
        "id": "M003",
        "tipo": "material",
        "subtipo": "gema",
        "rareza": "legendario",
        "descripcion": "Un cristal que contiene la esencia de un dragón. Pulsa con energía mágica primordial.",
        "lore": "Cuando un dragón muere, su alma se condensa en un cristal. Este es el material más codiciado del reino. Reyes matarían por poseerlo.",
        "peso": 0,
        "precio_compra": 20000,
        "precio_venta": 10000,
        "is_stackable": True,
        "level_requirement": 15,
        "icono": "💠"
    },
    
    "Empuñadura de Bronce": {
        "id": "M004",
        "tipo": "material",
        "subtipo": "metal",
        "rareza": "comun",
        "descripcion": "Una empuñadura de espada antigua hecha de bronce. Cubierta de óxido verde.",
        "lore": "Parte de un arma rota hace siglos. El slime que la tragó la protegió del tiempo.",
        "peso": 1,
        "precio_compra": 50,
        "precio_venta": 25,
        "is_stackable": True,
        "level_requirement": 0,
        "icono": "🔩"
    },
    
    "Cristal de Fuego": {
        "id": "M005",
        "tipo": "material",
        "subtipo": "cristal",
        "rareza": "raro",
        "descripcion": "Un cristal que arde con calor interno. Nunca se enfría.",
        "lore": "Formado en las profundidades de volcanes activos. Los herreros lo usan para forjar armas elementales.",
        "peso": 0,
        "precio_compra": 200,
        "precio_venta": 100,
        "is_stackable": True,
        "level_requirement": 5,
        "icono": "🔥"
    },
    
    "Corazón Corrupto": {
        "id": "M006",
        "tipo": "material",
        "subtipo": "órgano",
        "rareza": "legendario",
        "descripcion": "El corazón aún latiente de un dragón corrupto. Pulsa con oscuridad.",
        "lore": "Incluso muerto, el corazón late. La corrupción es eterna. Úsalo con cautela... o conviértete en lo que destruiste.",
        "peso": 2,
        "precio_compra": 15000,
        "precio_venta": 7500,
        "is_stackable": False,
        "level_requirement": 15,
        "icono": "🫀"
    },
    
    "Escama de Dragón": {
        "id": "M007",
        "tipo": "material",
        "subtipo": "escama",
        "rareza": "ultra_raro",
        "descripcion": "Una escama de dragón. Más dura que el acero, más ligera que el cuero.",
        "lore": "Armaduras forjadas con escamas de dragón protegieron a emperadores. Una sola vale más que una aldea.",
        "peso": 0,
        "precio_compra": 5000,
        "precio_venta": 2500,
        "is_stackable": True,
        "level_requirement": 10,
        "icono": "🐉"
    }
}

# ═══════════════════════════════════════════════════════════════
# 👹 BESTIARIO - BASE DE DATOS DE ENEMIGOS
# ═══════════════════════════════════════════════════════════════

ENEMIGOS_DB = {
    "Escudero No-Muerto": {
        "id": "E001",
        "nivel_base": 1,
        "categoria": "No-muerto",
        "estado_visual": "Esqueleto animado vestido con armadura oxidada. Sus ojos vacíos brillan con odio eterno.",
        "descripcion": "Un soldado caído que se niega a descansar. Aún porta su equipo de batalla, oxidado por décadas de abandono.",
        "lore": "Soldados caídos que se niegan a descansar. Patrullan eternamente el campo de batalla donde murieron, repitiendo órdenes que nadie da.",
        "stats": {
            "hp": 45,
            "mp": 10,
            "ataque": 8,
            "defensa": 6,
            "velocidad": 4
        },
        "equipo_visual": {
            "arma": "Espada Rota",
            "arma_stats": "ATK +4",
            "escudo": "Escudo de Madera Podrida",
            "escudo_stats": "DEF +2",
            "armadura": "Cota de Mallas Oxidada"
        },
        "resistencias": {
            "veneno": 100,
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
        "drops": ["Espada Oxidada", "Mineral de Hierro", "Hueso Antiguo"],
        "oro_min": 15,
        "oro_max": 30,
        "exp": 25,
        "icono": "💀"
    },
    
    "Slime de Hierro": {
        "id": "E002",
        "nivel_base": 2,
        "categoria": "Bestia mágica",
        "estado_visual": "Recubierto de una capa metálica natural. Trozos de hierro flotan en su cuerpo gelatinoso.",
        "objeto_engullido": "Empuñadura de Bronce (Visible en el núcleo)",
        "drop_fijo": "Empuñadura de Bronce",  # 🔥 NUEVO: Drop garantizado 100%
        "descripcion": "Un slime que consumió metal en las minas profundas. Su cuerpo se ha vuelto denso y metálico.",
        "lore": "Nacen en minas abandonadas. Se alimentan de minerales y se vuelven más densos con el tiempo. Los mineros los temen más que a los derrumbes.",
        "stats": {
            "hp": 60,
            "mp": 20,
            "ataque": 5,
            "defensa": 15,
            "velocidad": 2
        },
        "equipo_visual": {
            "arma_natural": "Pseudópodo Pesado (Daño Contundente)"
        },
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
                "descripcion": "Escupe ácido corrosivo que reduce la defensa del enemigo",
                "efecto": "Daño moderado + DEF -20% por 2 turnos",
                "cooldown": 2,
                "costo_mp": 10
            },
            {
                "nombre": "División Celular",
                "descripcion": "Se divide en dos slimes más pequeños (solo si HP > 50%)",
                "efecto": "Crea un slime aliado con 30% HP",
                "cooldown": 999,
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
        "categoria": "Bestia",
        "estado_visual": "Pelaje gris plateado cubierto de cicatrices de batalla. Ojos amarillos que brillan con inteligencia salvaje.",
        "descripcion": "El líder de la manada. Más grande y feroz que los lobos comunes. Sus colmillos gotean saliva mientras gruñe.",
        "lore": "Ha sobrevivido 20 inviernos. Su aullido paraliza de miedo a los viajeros. La manada lo sigue hasta la muerte. Nunca caza solo.",
        "stats": {
            "hp": 85,
            "mp": 15,
            "ataque": 18,
            "defensa": 8,
            "velocidad": 14
        },
        "equipo_visual": {
            "arma_natural": "Colmillos Afilados + Garras"
        },
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
                "descripcion": "Muerde ferozmente con probabilidad de causar sangrado",
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
        "drops": ["Colmillo de Lobo", "Piel de Lobo", "Carne Fresca", "Cuero Salvaje"],
        "oro_min": 40,
        "oro_max": 70,
        "exp": 65,
        "icono": "🐺"
    },
    
    "Gólem de Piedra": {
        "id": "E004",
        "nivel_base": 4,
        "categoria": "Constructo",
        "estado_visual": "Construcción mágica de piedra antigua. Runas brillan en su pecho rocoso con pulsos de energía.",
        "descripcion": "Una construcción mágica creada para proteger. Sus movimientos son lentos pero devastadores.",
        "lore": "Guardianes creados por magos hace siglos. Protegen ruinas olvidadas y tesoros enterrados. No sienten dolor ni miedo. Solo obediencia eterna.",
        "stats": {
            "hp": 150,
            "mp": 30,
            "ataque": 25,
            "defensa": 30,
            "velocidad": 1
        },
        "equipo_visual": {
            "arma_natural": "Puños de Piedra Maciza"
        },
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
                "descripcion": "Golpea el suelo creando una onda de choque devastadora",
                "efecto": "Daño a todos los enemigos + 25% aturdir 1 turno",
                "cooldown": 3,
                "costo_mp": 15
            },
            {
                "nombre": "Muro de Piedra",
                "descripcion": "Se cubre de capas de roca adicionales, volviéndose casi impenetrable",
                "efecto": "DEF +100% x 2 turnos, no puede moverse",
                "cooldown": 6,
                "costo_mp": 20
            }
        ],
        "drops": ["Fragmento de Gólem", "Runa Antigua", "Núcleo de Tierra", "Mineral de Hierro"],
        "oro_min": 60,
        "oro_max": 100,
        "exp": 90,
        "icono": "🗿"
    },
    
    "Dragón Corrupto": {
        "id": "E005",
        "nivel_base": 10,
        "categoria": "Dragón / Jefe",
        "es_jefe": True,  # 🔥 NUEVO: Marca como jefe para drops especiales
        "estado_visual": "Escamas negras que rezuman corrupción. Sus ojos son pozos de oscuridad. Aliento tóxico gotea de sus fauces.",
        "descripcion": "Un dragón caído en la oscuridad. Su aliento es veneno y sus escamas rezuman maldad pura.",
        "lore": "Antes era un dragón noble, guardián de las montañas. La corrupción lo devoró desde dentro. Ahora solo busca destruir lo que una vez protegió. Su rugido hace temblar la tierra.",
        "stats": {
            "hp": 500,
            "mp": 150,
            "ataque": 60,
            "defensa": 40,
            "velocidad": 12
        },
        "equipo_visual": {
            "arma_natural": "Colmillos + Garras + Aliento Corrupto"
        },
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
                "descripcion": "Vuela alto y se lanza en picada con furia destructiva",
                "efecto": "Daño brutal + Evasión +100% el turno anterior",
                "cooldown": 3,
                "costo_mp": 30
            },
            {
                "nombre": "Furia del Caído",
                "descripcion": "Se activa automáticamente cuando HP < 30%. La desesperación lo vuelve letal.",
                "efecto": "ATK +200%, DEF -50%, Velocidad +100%",
                "cooldown": 999,
                "costo_mp": 0
            }
        ],
        "drops": ["Escama de Dragón", "Colmillo de Dragón"],  # Drops normales
        "drops_legendarios": ["Cristal del Dragón", "Corazón Corrupto"],  # 🔥 NUEVO: Drops garantizados de jefe
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
    "Percepción del Reencarnado": {
        "id": "S001",
        "tipo": "pasiva",
        "nombre": "Percepción del Reencarnado",
        "descripcion": "Al venir de otro mundo, tus ojos ven datos donde otros ven monstruos.",
        "lore": "Los reencarnados ven el mundo como datos. HP, debilidades, habilidades... todo es información. Esta es tu mayor ventaja.",
        "efecto": "Desbloquea el botón [ANALIZAR] en combate. Revela información completa del enemigo.",
        "costo_mp": 0,
        "nivel_desbloqueo": 1,
        "icono": "👁️"
    },
    
    "Corte Cruzado": {
        "id": "S002",
        "tipo": "activa",
        "nombre": "Corte Cruzado",
        "descripcion": "Un ataque rápido en forma de X. Golpea dos veces en sucesión.",
        "lore": "Técnica básica de espadachín. Simple pero letal si se ejecuta correctamente. La segunda estocada siempre sorprende.",
        "efecto": "Daño Base × 1.5, golpea 2 veces",
        "costo_mp": 10,
        "cooldown": 2,
        "nivel_desbloqueo": 3,
        "icono": "❌"
    },
    
    "Corte de Precisión": {
        "id": "S003",
        "tipo": "activa",
        "nombre": "Corte de Precisión",
        "descripcion": "Un ataque concentrado que busca las grietas en la armadura enemiga.",
        "lore": "No se trata de fuerza bruta, sino de conocer dónde golpear. Toda armadura tiene debilidades. Solo debes encontrarlas.",
        "efecto": "Ignora el 50% de la Defensa del enemigo",
        "costo_mp": 15,
        "cooldown": 3,
        "nivel_desbloqueo": 5,
        "icono": "🎯"
    },
    
    "Golpe Poderoso": {
        "id": "S004",
        "tipo": "activa",
        "nombre": "Golpe Poderoso",
        "descripcion": "Concentras toda tu fuerza en un solo golpe devastador.",
        "lore": "Sacrificas velocidad por poder puro. Un golpe bien dado puede cambiar el curso de cualquier batalla.",
        "efecto": "Daño Base × 3.0, ignora 50% de defensa",
        "costo_mp": 25,
        "cooldown": 4,
        "nivel_desbloqueo": 7,
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
