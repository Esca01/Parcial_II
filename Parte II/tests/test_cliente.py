import unittest
from model.cliente import Cliente
from crud.crud_clientes import CRUDClientes

class TestCliente(unittest.TestCase):
    def test_crear_cliente(self):
        # Prueba la creación de un cliente
        nuevo_cliente = Cliente("Juan Pérez","123456789")
        self.assertEqual(nuevo_cliente.nombre, "Juan Pérez")
        self.assertEqual(nuevo_cliente.cedula, "123456789")
        

    def test_buscar_cliente_por_cedula(self):

        # Agrega el cliente a la base de datos o lista (usando el método apropiado)
        CRUDClientes.agregar_cliente("Juan Pérez","123456789")

        # Busca el cliente por cédula
        cliente_encontrado = CRUDClientes.buscar_cliente_por_cedula("123456789")

        # Verifica que el cliente se haya encontrado
        self.assertIsNotNone(cliente_encontrado)
        self.assertEqual(cliente_encontrado.cedula, "123456789")
