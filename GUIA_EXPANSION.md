# ═══════════════════════════════════════════════════════════════
# 📚 GUÍA DE EXPANSIÓN - CRÓNICAS DE PY-TERRA v2.0
# Cómo agregar 100, 1000 o más items/enemigos/mecánicas al juego
# ═══════════════════════════════════════════════════════════════

## 📖 TABLA DE CONTENIDOS

1. [Arquitectura del Sistema](#arquitectura-del-sistema)
2. [Cómo Agregar Items](#cómo-agregar-items)
3. [Cómo Agregar Enemigos](#cómo-agregar-enemigos)
4. [Cómo Agregar Habilidades](#cómo-agregar-habilidades)
5. [Sistema de Drops y Jefes](#sistema-de-drops-y-jefes)
6. [Sistema de Crafteo](#sistema-de-crafteo)
7. [Balance de Stats](#balance-de-stats)
8. [Consejos de Lore Épico](#consejos-de-lore-épico)

---

## 🎯 ARQUITECTURA DEL SISTEMA

Tu juego está construido con **arquitectura modular profesional**:

```
📁 Tu Proyecto
├── 📄 base_datos.py    ← Toda la información (items, enemigos, habilidades)
├── 📄 personajes.py    ← Sistema de personaje y mecánicas
├── 📄 logica.py        ← Lógica del juego y eventos
└── 📄 index.html       ← Interfaz de usuario
```

✅ **VENTAJA**: Puedes agregar 1000 items sin tocar la lógica del juego.

### 🔗 Flujo de Datos

```
base_datos.py → logica.py → index.html → Usuario
     ↑              ↓           ↓
     └── personajes.py ←────────┘
```

---

## 📦 CÓMO AGREGAR ITEMS

### 📝 Plantilla Completa

Para agregar un item, abre `base_datos.py` y agrega una nueva entrada en `ITEMS_DB`:

```python
"Nombre del Item": {
    # ═══ IDENTIFICACIÓN ═══
    "id": "XXX",                    # Código único (W001, A001, C001, M001, ACC001)
    "tipo": "equipamiento",         # consumible, equipamiento, material
    "subtipo": "arma",              # arma, armadura, accesorio, curación, mineral, etc.
    "slot": "mano_derecha",         # Para equipamiento: mano_derecha, torso, anillo, etc.
    "rareza": "raro",               # comun, raro, ultra_raro, legendario
    
    # ═══ TEXTO INMERSIVO ═══
    "descripcion": "Descripción técnica del item. Qué hace, cómo se ve.",
    "lore": "Historia épica que hace al item memorable. Quién lo creó, dónde, por qué.",
    
    # ═══ MECÁNICAS ═══
    "stats": {"ataque": 10, "critico": 5},  # Solo equipamiento
    "valor_curacion": 50,                    # Solo consumibles
    "efecto_secundario": "5% de náuseas",   # Opcional
    "efecto_especial": "Texto del efecto",  # Habilidades únicas
    
    # ═══ ECONOMÍA ═══
    "precio_compra": 100,
    "precio_venta": 50,             # Típicamente 50% del precio de compra
    "is_stackable": True,           # ¿Se pueden apilar? (consumibles=True, equipamiento=False)
    "level_requirement": 5,         # Nivel mínimo para usar
    
    # ═══ SISTEMA AVANZADO ═══
    "peso": 5,                      # Para sistema de carga (futuro)
    "durabilidad": 100,             # Para items que se desgastan
    "receta_crafteo": {             # 🔥 NUEVO: Sistema de crafteo
        "materiales": [
            {"item": "Item Base", "cantidad": 1},
            {"item": "Material", "cantidad": 5}
        ],
        "oro_requerido": 500
    },
    "icono": "⚔️"
}
```

### 🎯 Ejemplo Real - Espada Legendary

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
    "receta_crafteo": {
        "materiales": [
            {"item": "Colmillo de Dragón", "cantidad": 1},
            {"item": "Corona del Emperador", "cantidad": 1},
            {"item": "Cristal de Alma", "cantidad": 10}
        ],
        "oro_requerido": 10000
    },
    "icono": "👑"
}
```

---

## 👹 CÓMO AGREGAR ENEMIGOS

### 📝 Plantilla Completa

Para agregar un enemigo, abre `base_datos.py` y agrega una nueva entrada en `ENEMIGOS_DB`:

```python
"Nombre del Enemigo": {
    # ═══ IDENTIFICACIÓN ═══
    "id": "E999",
    "nivel_base": 5,
    "categoria": "Bestia / No-muerto / Dragón / Constructo / Demonio",
    "es_jefe": False,               # True para jefes con drops especiales
    
    # ═══ INMERSIÓN VISUAL ═══
    "estado_visual": "Cómo se ve el enemigo (ropa, armas, heridas, etc.)",
    "descripcion": "Descripción de combate y comportamiento",
    "lore": "Historia épica del enemigo. Origen, motivación, tragedia.",
    
    # ═══ STATS DE COMBATE ═══
    "stats": {
        "hp": 100,
        "mp": 20,
        "ataque": 15,
        "defensa": 10,
        "velocidad": 8
    },
    
    # ═══ EQUIPO VISUAL ═══
    "equipo_visual": {
        "arma": "Nombre del arma",
        "arma_stats": "ATK +5",
        "escudo": "Nombre escudo",
        "escudo_stats": "DEF +2",
        "armadura": "Nombre de armadura",
        "arma_natural": "Para bestias: Colmillos, Garras, Cuernos"
    },
    
    # ═══ PARA SLIMES Y CRIATURAS ═══
    "objeto_engullido": "Empuñadura de Bronce (Visible en el núcleo)",
    "drop_fijo": "Empuñadura de Bronce",  # Drop 100% garantizado
    
    # ═══ RESISTENCIAS Y DEBILIDADES ═══
    "resistencias": {
        "fuego": 50,      # 50% de resistencia
        "veneno": 100     # 100% = Inmune
    },
    "debilidades": {
        "hielo": 200,     # 200% = el doble de daño
        "sagrado": 300    # 300% = el triple de daño
    },
    
    # ═══ HABILIDADES ═══
    "habilidades": [
        {
            "nombre": "Nombre de la Habilidad",
            "descripcion": "Qué hace visualmente",
            "efecto": "Mecánica exacta (daño, buffs, debuffs)",
            "cooldown": 3,
            "costo_mp": 10
        }
    ],
    
    # ═══ RECOMPENSAS ═══
    "drops": ["Item 1", "Item 2", "Item 3"],           # Drops normales (40% prob)
    "drops_legendarios": ["Item Legendario"],          # 🔥 Para jefes (100% prob)
    "oro_min": 50,
    "oro_max": 100,
    "exp": 80,
    "icono": "👹"
}
```

---

## 🔥 SISTEMA DE DROPS Y JEFES

### 👑 Cómo Crear un Jefe

**Paso 1**: Marca el enemigo como jefe en `base_datos.py`:

```python
"Dragón Corrupto": {
    "id": "E005",
    "nivel_base": 10,
    "categoria": "Dragón / Jefe",
    "es_jefe": True,  # 🔥 Esto activa el sistema especial de drops
    # ... resto del código ...
    
    "drops": ["Escama de Dragón", "Colmillo de Dragón"],  # Drops normales (70% prob)
    "drops_legendarios": ["Cristal del Dragón", "Corazón Corrupto"],  # ¡GARANTIZADOS!
}
```

**Paso 2**: El juego automáticamente mostrará:

```
🏆 ¡INCREÍBLE! El 🐲 Dragón Corrupto soltó:
🔥 Escama de Dragón
💠 Cristal del Dragón ¡LEGENDARIO!
🫀 Corazón Corrupto ¡LEGENDARIO!
```

### 🟢 Drops Especiales para Slimes

```python
"Slime de Hierro": {
    "objeto_engullido": "Empuñadura de Bronce (Visible en el núcleo)",
    "drop_fijo": "Empuñadura de Bronce",  # Drop 100% garantizado
}
```

El jugador verá:
```
📦 Drops: 🔩 Empuñadura de Bronce (¡Objeto engullido!)
```

---

## 🔨 SISTEMA DE CRAFTEO

Para que un item sea crafteable, agrega `receta_crafteo`:

```python
"Espada Flamígera": {
    # ... stats normales ...
    "receta_crafteo": {
        "materiales": [
            {"item": "Espada de Hierro", "cantidad": 1},
            {"item": "Cristal de Fuego", "cantidad": 5},
            {"item": "Mineral de Hierro", "cantidad": 10}
        ],
        "oro_requerido": 500
    }
}
```

Cuando el jugador haga click en el item, verá:

```
🔨 CRAFTEO
Materiales necesarios:
• Espada de Hierro x1
• Cristal de Fuego x5
• Mineral de Hierro x10

Oro requerido: 500💰
```

---

## ⚡ CÓMO AGREGAR HABILIDADES

```python
"Nombre de Habilidad": {
    "id": "S999",
    "tipo": "activa",           # activa o pasiva
    "nombre": "Nombre completo",
    "descripcion": "Qué hace en combate",
    "lore": "Historia o filosofía detrás de la técnica",
    "efecto": "Mecánica exacta",
    "costo_mp": 20,
    "cooldown": 3,
    "nivel_desbloqueo": 10,
    "icono": "⚡"
}
```

---

## 📊 BALANCE DE STATS

### ⚔️ Armas por Nivel

| Nivel | ATK Base | Precio | Rareza |
|-------|----------|--------|--------|
| 1-5 | 5-15 | 50-200 | Común |
| 6-10 | 15-40 | 200-1000 | Raro |
| 11-15 | 40-80 | 1000-5000 | Ultra Raro |
| 16-20 | 80-150 | 5000-20000 | Legendario |

### 🛡️ Armaduras por Nivel

| Nivel | DEF Base | Precio | Rareza |
|-------|----------|--------|--------|
| 1-5 | 2-10 | 50-400 | Común |
| 6-10 | 10-25 | 400-2000 | Raro |
| 11-15 | 25-50 | 2000-10000 | Ultra Raro |
| 16-20 | 50-100 | 10000-40000 | Legendario |

### 👹 Enemigos por Nivel

| Stat | Fórmula |
|------|---------|
| HP | Nivel × 50 |
| ATK | Nivel × 5 + 5 |
| DEF | Nivel × 3 |
| EXP | Nivel × 20 + 20 |
| ORO | Nivel × 20 + 10 |

---

## 🎨 CONSEJOS DE LORE ÉPICO

### ✅ BUENO (Específico y Evocador)

```
"Forjada en el Monte Ignis por el herrero legendario Vulkan. 
Las llamas nunca se apagan, ni siquiera bajo el agua. Quien 
la empuña siente el calor de mil volcanes en su mano."
```

### ❌ MALO (Genérico y Aburrido)

```
"Una espada mágica muy poderosa que hace mucho daño."
```

### 📝 Fórmula del Lore Épico

1. **¿Dónde/Quién lo creó?** → "Forjada en X por Y"
2. **¿Qué lo hace único?** → "Las llamas nunca se apagan"
3. **¿Qué siente quien lo usa?** → "Quien la empuña siente..."

---

## 📈 SISTEMA DE RAREZA

| Rareza | Color | Precio Base | Drop Rate | Uso |
|--------|-------|-------------|-----------|-----|
| **Común** | 🟢 Verde | 10-200 | 60% | Items de inicio, materiales básicos |
| **Raro** | 🔵 Azul | 200-1000 | 25% | Equipo estándar, pociones buenas |
| **Ultra Raro** | 🟣 Morado | 1000-10000 | 10% | Equipo épico, jefes menores |
| **Legendario** | 🔴 Rojo | 10000+ | 5% | Únicas, drops de jefes finales |

---

## 🚀 EXPANSIÓN RÁPIDA

### Crear Familias de Items

```python
# FAMILIA DE ESPADAS (copia, pega, cambia números)
"Espada de Bronce": {"id": "W020", "ataque": 8, "level_requirement": 1, "precio_compra": 80}
"Espada de Hierro": {"id": "W021", "ataque": 15, "level_requirement": 3, "precio_compra": 200}
"Espada de Acero": {"id": "W022", "ataque": 25, "level_requirement": 5, "precio_compra": 600}
"Espada de Mithril": {"id": "W023", "ataque": 40, "level_requirement": 8, "precio_compra": 1500}
"Espada de Adamantita": {"id": "W024", "ataque": 60, "level_requirement": 12, "precio_compra": 4000}

# FAMILIA DE POCIONES
"Poción Menor": {"valor_curacion": 20, "precio_compra": 20}
"Poción": {"valor_curacion": 50, "precio_compra": 100}
"Poción Mayor": {"valor_curacion": 100, "precio_compra": 300}
"Super Poción": {"valor_curacion": 200, "precio_compra": 800}
"Hiper Poción": {"valor_curacion": 500, "precio_compra": 2000}
```

---

## 💡 CHECKLIST DE ITEM PERFECTO

Antes de agregar un item, verifica:

- [ ] Tiene ID único
- [ ] Tiene precio de compra Y venta
- [ ] Tiene level_requirement apropiado
- [ ] El lore es específico y memorable
- [ ] Los stats están balanceados para su nivel
- [ ] Is_stackable está configurado correctamente
- [ ] Si es legendary, tiene receta de crafteo
- [ ] Si es equipamiento, tiene slot definido

---

## 🎯 CHECKLIST DE ENEMIGO PERFECTO

- [ ] Tiene ID único
- [ ] Stats escalados al nivel
- [ ] Tiene al menos 2 habilidades
- [ ] Lore explica su origen
- [ ] Resistencias/debilidades lógicas
- [ ] Drops apropiados para su rareza
- [ ] Si es jefe, tiene drops_legendarios
- [ ] Estado visual es descriptivo

---

## 🔗 ENLACES RÁPIDOS

- **Agregar Item**: Abre `base_datos.py` → busca `ITEMS_DB` → copia plantilla
- **Agregar Enemigo**: Abre `base_datos.py` → busca `ENEMIGOS_DB` → copia plantilla
- **Agregar Habilidad**: Abre `base_datos.py` → busca `HABILIDADES_DB` → copia plantilla
- **Marcar Jefe**: Agrega `"es_jefe": True` y `"drops_legendarios": [...]`
- **Hacer Crafteable**: Agrega campo `"receta_crafteo": {...}`

---

**¡AHORA TIENES UN MOTOR DE RPG PROFESIONAL DE NIVEL AAA!** 🔥👑

Solo abre `base_datos.py`, copia una plantilla, personaliza y expande tu mundo.
Tu juego puede tener fácilmente:
- ✅ 100+ items
- ✅ 50+ enemigos
- ✅ 20+ jefes
- ✅ Sistema de crafteo completo
- ✅ Lore inmersivo

**Todo sin tocar el código de `logica.py` o `index.html`** 🚀
