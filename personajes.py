# ═══════════════════════════════════════════════════════════════
# 🎮 SISTEMA DE PERSONAJES Y EQUIPAMIENTO
# ═══════════════════════════════════════════════════════════════

class Heroe:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida
        
        # 🔥 STATS BASE DEL PERSONAJE
        self.fuerza = 10      # STR - Aumenta daño físico
        self.destreza = 10    # DEX - Aumenta crítico y evasión
        self.aguante = 10     # END - Aumenta vida y defensa
        
        # Sistema de progresión
        self.nivel = 1
        self.experiencia = 0
        self.exp_para_subir = 100
        self.oro = 0
        
        # 🔥 INVENTARIO - Diccionario para contar items
        self.inventario = {}
        
        # 🔥 SISTEMA DE EQUIPAMIENTO
        self.equipo = {
            "mano_derecha": None,  # Arma
            "mano_izquierda": None,  # Escudo o arma secundaria
            "torso": None,         # Armadura
            "cabeza": None,        # Casco
            "piernas": None,       # Pantalones/Grevas
            "pies": None,          # Botas
            "anillo": None,        # Anillo
            "cuello": None,        # Amuleto/Collar
        }
        
        # Estados de combate
        self.defensa_activa = False
        self.mp = 50
        self.mp_max = 50
        
        # 🔥 ESTADÍSTICAS
        self.combates_ganados = 0
        self.enemigos_derrotados = 0
        self.daño_total_causado = 0
        self.items_equipados = 0
        self.oro_total_ganado = 0
        
        # 🔥 HABILIDADES PASIVAS
        self.habilidades_pasivas = ["Análisis de Otro Mundo"]
        self.habilidades_activas = []
    
    # ═══════════════════════════════════════════════════════════
    # 📊 CÁLCULO DE STATS FINALES (BASE + EQUIPO)
    # ═══════════════════════════════════════════════════════════
    
    def get_stat(self, stat_name):
        """Calcula stat total (base + equipamiento)"""
        stat_base = {
            "ataque": self.fuerza * 2,
            "defensa": self.aguante,
            "critico": self.destreza,
            "evasion": self.destreza // 2,
            "vida_max": self.vida_max,
            "fuerza": self.fuerza,
            "destreza": self.destreza,
            "aguante": self.aguante
        }
        
        total = stat_base.get(stat_name, 0)
        
        # Sumar bonos del equipamiento
        for slot, item_data in self.equipo.items():
            if item_data:
                stats_item = item_data.get("stats", {})
                total += stats_item.get(stat_name, 0)
        
        return total
    
    def get_ataque_total(self):
        """Calcula el ataque total"""
        return self.get_stat("ataque")
    
    def get_defensa_total(self):
        """Calcula la defensa total"""
        return self.get_stat("defensa")
    
    def get_critico_total(self):
        """Calcula la probabilidad de crítico"""
        return self.get_stat("critico")
    
    # ═══════════════════════════════════════════════════════════
    # 🎒 SISTEMA DE INVENTARIO
    # ═══════════════════════════════════════════════════════════
    
    def agregar_item(self, item_nombre, cantidad=1):
        """Agrega items al inventario contando cantidades"""
        if item_nombre in self.inventario:
            self.inventario[item_nombre] += cantidad
        else:
            self.inventario[item_nombre] = cantidad
    
    def usar_item(self, item_nombre):
        """Usa un item del inventario (reduce cantidad)"""
        if item_nombre in self.inventario and self.inventario[item_nombre] > 0:
            self.inventario[item_nombre] -= 1
            if self.inventario[item_nombre] == 0:
                del self.inventario[item_nombre]
            return True
        return False
    
    def tiene_item(self, item_nombre):
        """Verifica si tiene un item"""
        return item_nombre in self.inventario and self.inventario[item_nombre] > 0
    
    def contar_items(self):
        """Cuenta el total de items en el inventario"""
        return sum(self.inventario.values())
    
    # ═══════════════════════════════════════════════════════════
    # ⚔️ SISTEMA DE EQUIPAMIENTO
    # ═══════════════════════════════════════════════════════════
    
    def equipar_item(self, item_nombre, item_data):
        """Equipa un item del inventario"""
        if not self.tiene_item(item_nombre):
            return False, "No tienes este item en el inventario"
        
        slot = item_data.get("slot")
        if not slot:
            return False, "Este item no se puede equipar"
        
        # Si ya hay algo equipado, desequiparlo primero
        if self.equipo[slot]:
            self.desequipar_slot(slot)
        
        # Equipar el nuevo item
        self.equipo[slot] = item_data
        self.equipo[slot]["nombre"] = item_nombre
        self.usar_item(item_nombre)  # Quitar del inventario
        self.items_equipados += 1
        
        # Recalcular vida máxima si aumentó
        nueva_vida_max = 100 + (self.nivel - 1) * 20
        nueva_vida_max += self.get_stat("vida_max") - self.vida_max
        if nueva_vida_max > self.vida_max:
            diferencia = nueva_vida_max - self.vida_max
            self.vida_max = nueva_vida_max
            self.vida += diferencia  # Aumentar vida actual también
        
        return True, f"Equipaste {item_nombre}"
    
    def desequipar_slot(self, slot):
        """Desequipa un item de un slot específico"""
        if self.equipo[slot]:
            item_nombre = self.equipo[slot].get("nombre")
            self.agregar_item(item_nombre, 1)  # Devolver al inventario
            self.equipo[slot] = None
            return True, f"Desequipaste {item_nombre}"
        return False, "No hay nada equipado en ese slot"
    
    def get_items_equipados(self):
        """Retorna lista de items equipados"""
        equipados = []
        for slot, item_data in self.equipo.items():
            if item_data:
                equipados.append({
                    "slot": slot,
                    "nombre": item_data.get("nombre"),
                    "data": item_data
                })
        return equipados
    
    # ═══════════════════════════════════════════════════════════
    # 💪 SISTEMA DE PROGRESIÓN
    # ═══════════════════════════════════════════════════════════
    
    def ganar_experiencia(self, exp):
        """Gana experiencia y sube de nivel si es necesario"""
        self.experiencia += exp
        while self.experiencia >= self.exp_para_subir:
            self.subir_nivel()
    
    def subir_nivel(self):
        """Sube de nivel y mejora stats"""
        self.nivel += 1
        self.experiencia -= self.exp_para_subir
        self.exp_para_subir = int(self.exp_para_subir * 1.5)
        
        # Aumentar stats base
        self.fuerza += 2
        self.destreza += 2
        self.aguante += 2
        
        # Aumentar vida y MP máximos
        self.vida_max += 20
        self.mp_max += 10
        
        # Restaurar vida y MP completos
        self.vida = self.vida_max
        self.mp = self.mp_max
        
        # Desbloquear habilidades según nivel
        if self.nivel == 3 and "Corte Cruzado" not in self.habilidades_activas:
            self.habilidades_activas.append("Corte Cruzado")
        if self.nivel == 5 and "Golpe Poderoso" not in self.habilidades_activas:
            self.habilidades_activas.append("Golpe Poderoso")
        
        return True
    
    def ganar_oro(self, cantidad):
        """Agrega oro"""
        self.oro += cantidad
        self.oro_total_ganado += cantidad
    
    # ═══════════════════════════════════════════════════════════
    # ⚔️ SISTEMA DE COMBATE
    # ═══════════════════════════════════════════════════════════
    
    def activar_defensa(self):
        """Activa la defensa para el próximo turno"""
        self.defensa_activa = True
    
    def recibir_daño(self, daño):
        """Recibe daño, reducido por defensa"""
        defensa = self.get_defensa_total()
        reduccion = defensa // 2
        
        if self.defensa_activa:
            reduccion *= 2
            self.defensa_activa = False
            defendio = True
        else:
            defendio = False
        
        daño_real = max(1, daño - reduccion)
        return daño_real, defendio
    
    def curar(self, cantidad):
        """Cura al héroe sin exceder vida máxima"""
        self.vida = min(self.vida + cantidad, self.vida_max)
    
    def usar_mp(self, cantidad):
        """Usa MP para habilidades"""
        if self.mp >= cantidad:
            self.mp -= cantidad
            return True
        return False
