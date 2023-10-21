from model.cliente import Cliente

class CRUDClientes:
    @staticmethod
    def agregar_cliente(nombre, cedula):
        cliente = Cliente(nombre, cedula)
        cliente.save()
        return cliente

    @staticmethod
    def buscar_cliente_por_cedula(cedula):
        for cliente in Cliente.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    @staticmethod
    def actualizar_cliente(cedula, nuevo_nombre):
        cliente = Cliente.find_by_cedula(cedula)
        if cliente:
            cliente.nombre = nuevo_nombre
            cliente.save()
        return cliente

    @staticmethod
    def eliminar_cliente(cedula):
        cliente = Cliente.find_by_cedula(cedula)
        if cliente:
            Cliente.clientes.remove(cliente)
            return True
        return False
