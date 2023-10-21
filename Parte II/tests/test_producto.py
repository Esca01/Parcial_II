import unittest
from model.producto import Producto
from crud.crud_productos import CRUDProductos

class TestProducto(unittest.TestCase):
    def test_crear_producto(self):
        # Prueba la creación de un producto
        nuevo_producto = Producto("Producto de Prueba", 15000,400.0,"bovino")
        self.assertEqual(nuevo_producto.nombre, "Producto de Prueba")
        self.assertEqual(nuevo_producto.precio, 15000)
        self.assertEqual(nuevo_producto.dosis, 400.0)
        self.assertEqual(nuevo_producto.tipo_animal, "bovino")
        

    def test_listar_productos(self):
        CRUDProductos.agregar_producto("Producto de Prueba1", 15000,400.0,"bovino")
        CRUDProductos.agregar_producto("Producto de Prueba2", 25000,600.0,"caprinos")

        productos = CRUDProductos.listar_productos()
        self.assertEqual(len(productos), 2)

if __name__ == '__main__':
    unittest.main()
