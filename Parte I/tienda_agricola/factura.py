class Factura:
    def __init__(self, cliente, fecha, productos):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos
    
    def calcular_total(self):
        total = sum(producto.valor for producto in self.productos if hasattr(producto, 'valor'))
        return total
