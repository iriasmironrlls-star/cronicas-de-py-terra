# ═══════════════════════════════════════════════════════════════
# 📚 GUÍA DE EXPANSIÓN - CRÓNICAS DE PY-TERRA
# Cómo agregar 100, 1000 o más items/enemigos al juego
# ═══════════════════════════════════════════════════════════════

## 🎯 ARQUITECTURA DEL SISTEMA

Tu juego está construido con **arquitectura modular**:
- `base_datos.py`: Toda la información (items, enemigos, habilidades)
- `personajes.py`: Sistema de personaje y mecánicas
- `logica.py`: Lógica del juego y eventos
- `index.html`: Interfaz de usuario

✅ **VENTAJA**: Puedes agregar 1000 items sin tocar la lógica del juego.

---

## 📦 CÓMO AGREGAR UN NUEVO ITEM

### Plantilla Base (Copia y Pega):

```python
"Nombre del Item": {
    "id": "XXX",                    # Código único (W001, A001, C001, etc.)
    "tipo": "equipamiento",         # consumible, equipamiento, material
    "subtipo": "arma",              # arma, armadura, accesorio, curación, etc.
    "slot": "mano_derecha",         # Para equipamiento: mano_derecha, torso, etc.
    "rareza": "raro",               # comun, raro, ultra_raro, legendario
    
    # TEXTO INMERSIVO
    "descripcion": "Descripción técnica del item",
    "lore": "Historia épica que hace al item memorable",
    
    # MECÁNICAS
    "stats": {"ataque": 10, "critico": 5},  # Solo para equipamiento
    "valor_curacion": 50,                    # Solo para consumibles
    "efecto_secundario": "5% de náuseas",   # Opcional
    "efecto_especial": "Texto del efecto",  # Opcional
    
    # SISTEMA DE ECONOMÍA
    "precio_compra": 100,
    "precio_venta": 50,             # Típicamente 50% del precio de compra
    "is_stackable": True,           # ¿Se pueden apilar?
    "level_requirement": 5,         # Nivel mínimo para usar
    
    # EXTRAS
    "peso": 5,                      # Para sistema de carga (futuro)
    "durabilidad": 100,             # Para items que se desgastan
    "icono": "⚔️"
}
```

### Ejemplo Real - Espada Legendary:

```python
"Espada del Rey Caído": {
    "id": "W010",
    "tipo": "equipamiento",
    "subtipo": "arma",
    "slot": "mano_derecha",
    "rareza": "legendario",
    "descripcion": "La espada del último rey. Pesa como el remordimiento, corta como la verdad.",
    "lore": "Forjada en lágrimas de súbditos traicionados. Quien la empuña siente el peso de un reino perdido. Dicen que la espada busca redención.",
    "stats": {"ataque": 100, "critico": 40, "fuerza": 15},
    "efecto_especial": "Cada enemigo derrotado aumenta ATK +1 (máximo +50)",
    "durabilidad": 999,
    "peso": 10,
    "precio_compra": 50000,
    "precio_venta": 25000,
    "is_stackable": False,
    "level_requirement": 20,
    "icono": "👑"
}
```

---

## 👹 CÓMO AGREGAR UN NUEVO ENEMIGO

### Plantilla Base:

```python
"Nombre del Enemigo": {
    "id": "E999",
    "nivel_base": 5,
    "categoria": "Bestia / No-muerto / Dragón / etc.",
    
    # INMERSIÓN VISUAL
    "estado_visual": "Descripción de cómo se ve el enemigo",
    "descripcion": "Descripción de combate",
    "lore": "Historia épica del enemigo",
    
    # STATS
    "stats": {
        "hp": 100,
        "mp": 20,
        "ataque": 15,
        "defensa": 10,
        "velocidad": 8
    },
    
    # EQUIPO VISUAL
    "equipo_visual": {
        "arma": "Nombre del arma",
        "arma_stats": "ATK +5",
        "armadura": "Nombre de armadura",
        "arma_natural": "Para bestias: Colmillos, Garras, etc."
    },
    
    # SISTEMA DE DEBILIDADES
    "resistencias": {
        "fuego": 50,      # 50% de resistencia
        "veneno": 100     # Inmune (100%)
    },
    "debilidades": {
        "hielo": 200,     # 200% de daño (el doble)
        "sagrado": 300    # 300% de daño (el triple)
    },
    
    # HABILIDADES
    "habilidades": [
        {
            "nombre": "Nombre de la Habilidad",
            "descripcion": "Qué hace la habilidad",
            "efecto": "Mecánica exacta",
            "cooldown": 3,
            "costo_mp": 10
        }
    ],
    
    # RECOMPENSAS
    "drops": ["Item 1", "Item 2", "Item 3"],
    "oro_min": 50,
    "oro_max": 100,
    "exp": 80,
    "icono": "👹"
}
```

### Ejemplo Real - Jefe Final:

```python
"Lich Emperador": {
    "id": "E100",
    "nivel_base": 20,
    "categoria": "No-muerto / Jefe Final",
    "estado_visual": "Esqueleto vestido con túnicas negras. Corona de hierro oxidado. Ojos que arden con fuego verde.",
    "descripcion": "El emperador que conquistó la muerte pero perdió su humanidad. Comanda legiones de muertos vivientes.",
    "lore": "Hace 500 años, el Emperador Malachar eligió la inmortalidad sobre su pueblo. Ahora gobierna un reino de silencio y cenizas. Su único deseo: nunca estar solo en la muerte.",
    "stats": {
        "hp": 2000,
        "mp": 500,
        "ataque": 100,
        "defensa": 80,
        "velocidad": 15
    },
    "equipo_visual": {
        "arma": "Cetro de Almas Atrapadas",
        "arma_stats": "ATK +50, MAGIA +100",
        "armadura": "Túnicas de la Muerte Eterna"
    },
    "resistencias": {
        "veneno": 100,
        "oscuridad": 100,
        "hielo": 80,
        "fisico": 50
    },
    "debilidades": {
        "sagrado": 400,
        "fuego": 200
    },
    "habilidades": [
        {
            "nombre": "Marea de Muertos",
            "descripcion": "Invoca 3 esqueletos menores",
            "efecto": "Crea 3 aliados con 50 HP cada uno",
            "cooldown": 5,
            "costo_mp": 100
        },
        {
            "nombre": "Drenar Vida",
            "descripcion": "Absorbe la vida del enemigo",
            "efecto": "Daño 50 + recupera el 50% del daño causado",
            "cooldown": 3,
            "costo_mp": 80
        },
        {
            "nombre": "Último Aliento",
            "descripcion": "Al morir, revive con 30% HP (solo una vez)",
            "efecto": "Resurrección automática cuando HP llega a 0",
            "cooldown": 999,
            "costo_mp": 0
        }
    ],
    "drops": ["Corona del Emperador", "Cristal de Alma", "Espada del Rey Caído"],
    "oro_min": 5000,
    "oro_max": 10000,
    "exp": 5000,
    "icono": "💀"
}
```

---

## ⚡ CÓMO AGREGAR NUEVAS HABILIDADES

### Plantilla:

```python
"Nombre de Habilidad": {
    "id": "S999",
    "tipo": "activa",           # activa o pasiva
    "nombre": "Nombre completo",
    "descripcion": "Qué hace en combate",
    "lore": "Historia o filosofía detrás de la técnica",
    "efecto": "Mecánica exacta",
    "costo_mp": 20,
    "cooldown": 3,              # Solo para activas
    "nivel_desbloqueo": 10,
    "icono": "⚡"
}
```

---

## 🎨 CONSEJOS DE LORE ÉPICO

### ✅ BUENO:
- **Específico**: "Forjada en el Monte Ignis por el herrero Vulkan"
- **Evocador**: "El calor no quema a su portador, pero todo lo demás se consume"
- **Con historia**: "Las llamas nunca se apagan, ni siquiera bajo el agua"

### ❌ MALO:
- **Genérico**: "Una espada mágica muy poderosa"
- **Sin emoción**: "Hace +50 de daño"
- **Aburrido**: "Un arma normal"

---

## 📊 SISTEMA DE RAREZA - GUÍA

| Rareza | Color | Precio Base | Drop Rate | Uso |
|--------|-------|-------------|-----------|-----|
| **Común** | Verde | 10-200 | 60% | Items de inicio, materiales básicos |
| **Raro** | Azul | 200-1000 | 25% | Equipo estándar, pociones buenas |
| **Ultra Raro** | Morado | 1000-10000 | 10% | Equipo épico, jefes menores |
| **Legendario** | Rojo | 10000+ | 5% | Únicas, drops de jefes finales |

---

## 🔢 BALANCE DE STATS

### Armas por Nivel:
- **Nivel 1-5**: ATK 5-15
- **Nivel 6-10**: ATK 15-40
- **Nivel 11-15**: ATK 40-80
- **Nivel 16-20**: ATK 80-150

### Armaduras por Nivel:
- **Nivel 1-5**: DEF 2-10
- **Nivel 6-10**: DEF 10-25
- **Nivel 11-15**: DEF 25-50
- **Nivel 16-20**: DEF 50-100

### Enemigos por Nivel:
- **HP**: Nivel × 50 (aproximado)
- **ATK**: Nivel × 5 + 5
- **DEF**: Nivel × 3
- **EXP**: Nivel × 20 + 20
- **ORO**: Nivel × 20 + 10

---

## 🚀 PRÓXIMOS PASOS

1. **Agregar 10 armas nuevas** usando la plantilla
2. **Crear 5 enemigos únicos** con lore épico
3. **Diseñar 3 habilidades nuevas** para niveles 10, 15, 20
4. **Expandir materiales** para futuro sistema de crafteo

---

## ✨ EJEMPLO DE EXPANSIÓN RÁPIDA

Puedes crear variaciones fácilmente:

```python
# FAMILIA DE ESPADAS
"Espada de Bronce": {"id": "W020", "ataque": 8, "level_requirement": 1}
"Espada de Hierro": {"id": "W021", "ataque": 15, "level_requirement": 3}
"Espada de Acero": {"id": "W022", "ataque": 25, "level_requirement": 5}
"Espada de Mithril": {"id": "W023", "ataque": 40, "level_requirement": 8}
"Espada de Adamantita": {"id": "W024", "ataque": 60, "level_requirement": 12}

# FAMILIA DE POCIONES
"Poción Menor": {"valor_curacion": 20, "precio_compra": 20}
"Poción": {"valor_curacion": 50, "precio_compra": 100}
"Poción Mayor": {"valor_curacion": 100, "precio_compra": 300}
"Super Poción": {"valor_curacion": 200, "precio_compra": 800}
"Hiper Poción": {"valor_curacion": 500, "precio_compra": 2000}
```

---

**¡AHORA TIENES UN MOTOR DE RPG PROFESIONAL!** 🔥

Solo abre `base_datos.py`, copia una plantilla, y empieza a crear tu mundo.
