from model.producto import Producto

class CRUDProductos:
    @staticmethod
    def agregar_producto(nombre, precio, dosis, tipo_animal):
        producto = Producto(nombre, precio, dosis, tipo_animal)
        producto.save()
        return producto

    @staticmethod
    def buscar_producto_por_nombre(nombre):
        return Producto.find_by_nombre(nombre)

    @staticmethod
    def actualizar_producto(producto, nueva_dosis, nuevo_tipo_animal, nuevo_valor):
        if producto:
            if nueva_dosis:
                producto.dosis = nueva_dosis
            if nuevo_tipo_animal:
                producto.tipo_animal = nuevo_tipo_animal
            if nuevo_valor:
                producto.valor = nuevo_valor
        return producto

    @staticmethod
    def eliminar_producto(producto):
        if producto:
            producto.delete()
        return producto
    
    @staticmethod
    def listar_productos():
        return Producto.lista_productos
