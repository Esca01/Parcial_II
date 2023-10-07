import unittest
from tienda_agricola import Cliente
from tienda_agricola import Factura
from tienda_agricola import ProductoControl, ControlPlagas, ControlFertilizantes
from tienda_agricola import Antibiotico

class TestTiendaAgricola(unittest.TestCase):
    def test_factura_total(self):
        cliente = Cliente("Juan Perez", "1234567890")
        producto1 = ControlPlagas("ICA123", "Insecticida A", "15 días", 50.0, 30)
        producto2 = Antibiotico("Antibiótico B", 500, "Bovinos", 40.0, 40.0)
        factura = Factura(cliente, "2023-10-06", [producto1, producto2])
        total = factura.calcular_total()
        self.assertEqual(total, 90.0)
        print(total)
if __name__ == '__main__':
    unittest.main()
