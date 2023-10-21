class Cliente:
    # Lista para almacenar todos los clientes en memoria
    clientes = []

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def save(self):
        # Agregar el cliente actual a la lista de clientes
        self.clientes.append(self)
        

    @classmethod
    def find_by_cedula(cls, cedula):
        # Buscar un cliente por cédula en la lista de clientes
        for cliente in cls.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    @classmethod
    def update_cliente(cls, cedula, nuevo_nombre):
        # Actualizar el nombre de un cliente por cédula
        for cliente in cls.clientes:
            if cliente.cedula == cedula:
                cliente.nombre = nuevo_nombre
                return True
        return False

   
    

