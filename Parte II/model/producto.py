class Producto:
    lista_productos = []

    def __init__(self,nombre, precio, dosis, tipo_animal):
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    def save(self):
        Producto.lista_productos.append(self)

    @classmethod
    def find_by_nombre(cls, nombre):
        for producto in cls.lista_productos:
            if producto.nombre == nombre:
                return producto
        return None

    def delete(self):
        Producto.lista_productos.remove(self)
