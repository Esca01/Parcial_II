
class ProductoControl:
    def __init__(self, ica_registro, nombre, frecuencia_aplicacion, valor):
        self.ica_registro = ica_registro
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor

class ControlPlagas(ProductoControl):
    def __init__(self, ica_registro, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(ica_registro, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia

class ControlFertilizantes(ProductoControl):
    def __init__(self, ica_registro, nombre, frecuencia_aplicacion, valor, ultima_aplicacion):
        super().__init__(ica_registro, nombre, frecuencia_aplicacion, valor)
        self.ultima_aplicacion = ultima_aplicacion
