class Item:
    """🔥 NUEVO: Clase para items con rareza"""
    def __init__(self, nombre, rareza="comun", nivel=1, tipo="consumible"):
        self.nombre = nombre
        self.rareza = rareza  # comun, raro, ultra_raro, legendario
        self.nivel = nivel
        self.tipo = tipo
        
    def get_color(self):
        """Retorna el color según la rareza"""
        colores = {
            "comun": "#00ff00",      # Verde
            "raro": "#0080ff",       # Azul
            "ultra_raro": "#8000ff", # Morado
            "legendario": "#ff0000"  # Rojo
        }
        return colores.get(self.rareza, "#ffffff")

class Heroe:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.inventario = {}  # 🔥 CAMBIO: Diccionario para contar items
        # 🔥 NUEVAS PROPIEDADES AGREGADAS
        self.vida_max = vida
        self.nivel = 1
        self.experiencia = 0
        self.exp_para_subir = 100
        self.oro = 0
        self.defensa_activa = False
        self.combates_ganados = 0  # 🔥 NUEVO: Estadística
        self.enemigos_derrotados = 0  # 🔥 NUEVO: Estadística
        self.daño_total_causado = 0  # 🔥 NUEVO: Estadística
    
    # 🔥 MÉTODOS NUEVOS AGREGADOS
    def ganar_experiencia(self, exp):
        """Gana experiencia y sube de nivel si es necesario"""
        self.experiencia += exp
        if self.experiencia >= self.exp_para_subir:
            self.subir_nivel()
    
    def subir_nivel(self):
        """Sube de nivel y mejora stats"""
        self.nivel += 1
        self.experiencia = 0
        self.exp_para_subir = int(self.exp_para_subir * 1.5)  # Cada nivel necesita más exp
        self.vida_max += 20
        self.vida = self.vida_max  # Restaura vida completa al subir de nivel
        return True
    
    def ganar_oro(self, cantidad):
        """Agrega oro al inventario"""
        self.oro += cantidad
    
    def agregar_item(self, item_nombre, cantidad=1):
        """Agrega items al inventario contando cantidades"""
        if item_nombre in self.inventario:
            self.inventario[item_nombre] += cantidad
        else:
            self.inventario[item_nombre] = cantidad
    
    def usar_item(self, item_nombre):
        """Usa un item del inventario"""
        if item_nombre in self.inventario and self.inventario[item_nombre] > 0:
            self.inventario[item_nombre] -= 1
            if self.inventario[item_nombre] == 0:
                del self.inventario[item_nombre]
            return True
        return False
    
    def contar_items(self):
        """Cuenta el total de items en el inventario"""
        return sum(self.inventario.values())
    
    def activar_defensa(self):
        """Activa la defensa para el próximo turno"""
        self.defensa_activa = True
    
    def recibir_daño(self, daño):
        """Recibe daño, reducido si está defendiendo"""
        if self.defensa_activa:
            daño = daño // 2  # Reduce el daño a la mitad
            self.defensa_activa = False
            return daño, True  # Retorna daño recibido y si defendió
        return daño, False
    
    def curar(self, cantidad):
        """Cura al héroe sin exceder vida máxima"""
        self.vida = min(self.vida + cantidad, self.vida_max)
