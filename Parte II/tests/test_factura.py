import unittest
from model.factura import Factura
from crud.crud_facturas import CRUDFacturas
from model.cliente import Cliente
from model.producto import Producto

class TestFactura(unittest.TestCase):
    def test_crear_factura(self):
        # Prueba la creación de una factura
        cliente = Cliente("123456789", "Juan Pérez")
        producto = Producto("Producto de Prueba1", 15000,400.0,"bovino")
        factura = Factura(cliente, [{"producto": producto, "cantidad": 2}], 2000,"F001", "2023-10-07")
        self.assertEqual(factura.valor_total, 2000)

    def test_buscar_factura_por_numero(self):
        # Prueba la búsqueda de una factura por número
        cliente = "123456789", "Juan Pérez"
        producto = "Producto de Prueba1", 15000,400.0,"bovino"
        factura = Factura(cliente, [{"producto": producto, "cantidad": 2}], 2000, "F001","2023-10-07")
        CRUDFacturas.crear_factura(cliente, [{"producto": producto, "cantidad": 2}], 2000,"F001", "2023-10-07")

        factura_encontrada = CRUDFacturas.buscar_facturas_por_fecha("2023-10-07")
        self.assertEqual(factura_encontrada.valor_total, 2000)

if __name__ == '__main__':
    unittest.main()
