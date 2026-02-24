class Heroe:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.inventario = []
        # 🔥 NUEVAS PROPIEDADES AGREGADAS
        self.vida_max = vida
        self.nivel = 1
        self.experiencia = 0
        self.exp_para_subir = 100
        self.oro = 0
        self.defensa_activa = False
    
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
    
    def agregar_item(self, item):
        """Agrega un item al inventario"""
        self.inventario.append(item)
    
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
