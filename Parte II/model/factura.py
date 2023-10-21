from datetime import datetime

class Factura:
    facturas = []

    def __init__(self, cliente, productos, valor_total, numero_factura, fecha):
        self.numero = numero_factura
        self.cliente = cliente
        self.productos = productos
        self.valor_total = valor_total
        self.fecha = datetime.now().strftime('%Y-%m-%d')
        Factura.facturas.append(self)

    @classmethod
    def generar_numero_factura_unico(cls):
        import random
        return random.randint(1000, 9999)

    @classmethod
    def find_by_cliente(cls, cliente):
        return [factura for factura in cls.facturas if factura.cliente == cliente]

    @classmethod
    def find_by_fecha(cls, fecha):
        return [factura for factura in cls.facturas if factura.fecha == fecha]

    @classmethod
    def find_by_numero(cls, numero):
        return [factura for factura in cls.facturas if factura.numero == numero]

    def save(self):
        self.fecha = datetime.strptime(self.fecha, '%Y-%m-%d').date()
        Factura.facturas.append(self)

    def delete(self):
        Factura.facturas.remove(self)