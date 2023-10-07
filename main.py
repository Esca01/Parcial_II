from tienda_agricola.cliente import Cliente
from tienda_agricola import ProductoControl, ControlPlagas, ControlFertilizantes
from tienda_agricola.antibiotico import Antibiotico
from tienda_agricola.factura import Factura

# Creación de objetos
cliente = Cliente("Juan Perez", "1234567890")
control_plagas = ControlPlagas("ICA123", "Insecticida A", "15 días", 50.0, 30)
control_fertilizantes = ControlFertilizantes("ICA456", "Fertilizante B", "30 días", 30.0, "2023-09-15")
antibiotico = Antibiotico("Antibiótico B", 500, "Bovinos", 40.0, 40.0)
factura = Factura(cliente, "2023-10-06", [control_plagas, control_fertilizantes, antibiotico])

# Prueba de cálculo de total
total = factura.calcular_total()
print(f"Cliente: {factura.cliente.nombre}")
print(f"Fecha: {factura.fecha}")
print(f"Total: ${total:.2f}")



