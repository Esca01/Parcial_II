from crud.crud_clientes import CRUDClientes
from crud.crud_productos import CRUDProductos
from crud.crud_facturas import CRUDFacturas
from model.factura import Factura
from datetime import datetime


class MainMenu:
    def mostrar_menu(self):
        print("Menú Principal:")
        print("1. Clientes")
        print("2. Productos")
        print("3. Facturas")
        print("4. Salir")

    def menu_clientes(self):
        while True:
            print("\nMenú de Clientes:")
            print("1. Crear Cliente")
            print("2. Buscar Cliente por Cédula")
            print("3. Actualizar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.crear_cliente()
            elif opcion == "2":
                self.buscar_cliente_por_cedula()
            elif opcion == "3":
                self.actualizar_cliente()
            elif opcion == "4":
                self.eliminar_cliente()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def crear_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        CRUDClientes.agregar_cliente(nombre, cedula)
        print("Cliente creado con éxito.")

    def buscar_cliente_por_cedula(self):
        cedula = input("Ingrese la cédula del cliente a buscar: ")
        cliente = CRUDClientes.buscar_cliente_por_cedula(cedula)
        if cliente:
            print(f"Cliente encontrado: {cliente.nombre}")
        else:
            print("Cliente no encontrado.")

    def actualizar_cliente(self):
        cedula = input("Ingrese la cédula del cliente a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        cliente = CRUDClientes.actualizar_cliente(cedula, nuevo_nombre)
        if cliente:
            print("Cliente actualizado con éxito.")
        else:
            print("Cliente no encontrado.")

    def eliminar_cliente(self):
        cedula = input("Ingrese la cédula del cliente a eliminar: ")
        cliente = CRUDClientes.eliminar_cliente(cedula)
        if cliente:
            print("Cliente eliminado con éxito.")
        else:
            print("Cliente no encontrado.")

    def menu_productos(self):
        while True:
            print("\nMenú de Productos:")
            print("1. Crear Producto")
            print("2. Buscar Producto por Nombre")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Volver al Menú Principal")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.crear_producto()
            elif opcion == "2":
                self.buscar_producto_por_nombre()
            elif opcion == "3":
                self.actualizar_producto()
            elif opcion == "4":
                self.eliminar_producto()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def crear_producto(self):
        print("\nCreación de Producto:")
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        dosis = float(input("Ingrese la dosis del producto (entre 400Kg y 600Kg): "))
        tipo_animal = input("Ingrese el tipo de animal al que se aplica (Bovinos, caprinos o porcinos): ")
        

        if not (400 <= dosis <= 600):
            print("La dosis debe estar entre 400Kg y 600Kg.")
            return

        # Llama a la función del CRUD para agregar el producto
        nuevo_producto = CRUDProductos.agregar_producto(nombre, precio, dosis, tipo_animal)
        
        if nuevo_producto:
            print("Producto creado con éxito.")
        else:
            print("Error al crear el producto.")


    def buscar_producto_por_nombre(self):
        print("\nBúsqueda de Producto por Nombre:")
        nombre = input("Ingrese el nombre del producto a buscar: ")

        # Llama a la función del CRUD para buscar un producto por nombre
        producto_encontrado = CRUDProductos.buscar_producto_por_nombre(nombre)

        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado.nombre}")
            print(f"Precio: {producto_encontrado.precio}")
            print(f"Dosis: {producto_encontrado.dosis}")
            print(f"Tipo de Animal: {producto_encontrado.tipo_animal}")
            
        else:
            print("Producto no encontrado.")



    def actualizar_producto(self):
        print("\nActualización de Producto:")
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        # Llama a la función del CRUD para buscar el producto por nombre
        producto_existente = CRUDProductos.buscar_producto_por_nombre(nombre)

        if producto_existente:
            print(f"Producto encontrado: {producto_existente.nombre}")
            print(f"Precio actual: {producto_existente.precio}")

            nuevo_precio = input("Ingrese el nuevo precio (o deje en blanco para mantener el actual): ")

            # Actualizar el campo solo si se proporciona un nuevo precio
            if nuevo_precio:
                producto_existente.precio = nuevo_precio

            # Llama a la función del CRUD para actualizar el producto
            CRUDProductos.actualizar_producto(producto_existente)
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        print("\nEliminación de Producto:")
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        # Llama a la función del CRUD para buscar el producto por nombre
        producto_existente = CRUDProductos.buscar_producto_por_nombre(nombre)

        if producto_existente:
            print(f"Producto encontrado: {producto_existente.nombre}")
            confirmacion = input("¿Está seguro de que desea eliminar este producto? (S/N): ").strip().lower()

            if confirmacion == "s":
                # Llama a la función del CRUD para eliminar el producto
                CRUDProductos.eliminar_producto(producto_existente)
                print("Producto eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Producto no encontrado.")


    def menu_facturas(self):
        while True:
            print("\nMenú de Facturas:")
            print("1. Crear Factura")
            print("2. Buscar Facturas por Cliente")
            print("3. Buscar Facturas por Fecha")
            print("4. Actualizar Factura")
            print("5. Eliminar Factura")
            print("6. Volver al Menú Principal")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.crear_factura()
            elif opcion == "2":
                self.buscar_facturas_por_cliente()
            elif opcion == "3":
                self.buscar_facturas_por_fecha()
            elif opcion == "4":
                self.actualizar_factura()
            elif opcion == "5":
                self.eliminar_factura()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def crear_factura(self):
        print("\nCreación de Factura:")
        cedula_cliente = input("Ingrese la cédula del cliente: ")

        # Verificar si el cliente existe
        cliente_existente = CRUDClientes.buscar_cliente_por_cedula(cedula_cliente)

        if not cliente_existente:
            print("Cliente no encontrado.")
            return

        numero_factura = Factura.generar_numero_factura_unico()
        
        fecha_factura = input("Ingrese la fecha de la factura (en formato YYYY-MM-DD): ")

        # Listar productos disponibles
        productos_disponibles = CRUDProductos.listar_productos()
        if not productos_disponibles:
            print("No hay productos disponibles para agregar a la factura.")
            return

        # Mostrar productos disponibles y permitir al usuario seleccionar productos
        print("Productos Disponibles:")
        for i, producto in enumerate(productos_disponibles, start=1):
            print(f"{i}. {producto.nombre} (Precio: {producto.precio})")

        productos_seleccionados = []
        while True:
            seleccion = input("Seleccione un producto (0 para finalizar la selección): ")
            if seleccion == "0":
                break
            try:
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(productos_disponibles):
                    producto_seleccionado = productos_disponibles[seleccion - 1]
                    precio = float(producto_seleccionado.precio)  # Convertir el precio a float
                    cantidad = float(input("Ingrese la cantidad: "))  # Solicitar la cantidad
                    productos_seleccionados.append({"producto": producto_seleccionado, "cantidad": cantidad})
                    print(f"{producto_seleccionado.nombre} (Cantidad: {cantidad}) agregado a la factura.")
                else:
                    print("Opción no válida. Seleccione un número de producto válido.")
            except ValueError:
                print("Ingrese un número válido.")

        # Calcular el valor total de la factura
        valor_total = sum(float(producto["producto"].precio) * producto["cantidad"] for producto in productos_seleccionados)

        nueva_factura = CRUDFacturas.crear_factura(cliente_existente, productos_seleccionados, valor_total,numero_factura,fecha_factura)
        
        if nueva_factura:
            print("Factura creada con éxito.")
        else:
            print("Error al crear la factura.")


    def buscar_facturas_por_cliente(self):
        print("\nBúsqueda de Facturas por Cliente:")
        cedula_cliente = input("Ingrese la cédula del cliente: ")

        # Verificar si el cliente existe
        cliente_existente = CRUDClientes.buscar_cliente_por_cedula(cedula_cliente)

        if not cliente_existente:
            print(f"No se encontraron facturas para el cliente con cédula {cedula_cliente}.")
            return

        # Buscar facturas asociadas al cliente
        facturas_cliente = CRUDFacturas.buscar_facturas_por_cliente(cliente_existente)

        if facturas_cliente:
            print(f"Facturas para el cliente {cliente_existente.nombre} (Cédula: {cliente_existente.cedula}):")
            for factura in facturas_cliente:
                print(f"Número: {factura.numero}, Valor Total: {factura.valor_total}")
        else:
            print(f"No se encontraron facturas para el cliente {cliente_existente.nombre}.")



    def buscar_facturas_por_fecha(self):
        print("\nBúsqueda de Facturas por Fecha:")
        fecha_str = input("Ingrese la fecha (en formato YYYY-MM-DD): ")

        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            print("Formato de fecha no válido. Use el formato YYYY-MM-DD.")
            return

        # Buscar facturas por la fecha ingresada
        facturas_por_fecha = CRUDFacturas.buscar_facturas_por_fecha(fecha)

        if facturas_por_fecha:
            print(f"Facturas para la fecha {fecha}:")
            for factura in facturas_por_fecha:
                print(f"Número: {factura.numero}, Cliente: {factura.cliente.nombre}, Valor Total: {factura.valor_total}")
        else:
            print(f"No se encontraron facturas para la fecha {fecha}.")

    def actualizar_factura(self):
        print("\nActualización de Factura:")
        numero_factura = input("Ingrese el número de factura a actualizar: ")

        # Llama a la función para buscar la factura por su número
        factura_existente = CRUDFacturas.buscar_factura_por_numero(numero_factura)

        if factura_existente is None:
            print("Factura no encontrada.")
            return

        # Continúa con la lógica de actualización de la factura
        print(f"Factura encontrada - Número: {factura_existente.numero}, Cliente: {factura_existente.cliente.nombre}, Valor Total: {factura_existente.valor_total}")
        # ...

        nueva_fecha_str = input("Ingrese la nueva fecha (en formato YYYY-MM-DD) o deje en blanco para mantener la actual: ")
        nuevo_valor_total_str = input("Ingrese el nuevo valor total o deje en blanco para mantener el actual: ")

        # Actualizar los campos solo si se proporciona un nuevo valor
        if nueva_fecha_str:
            factura_existente.fecha = nueva_fecha_str

        if nuevo_valor_total_str:
            try:
                nuevo_valor_total = float(nuevo_valor_total_str)
                factura_existente.valor_total = nuevo_valor_total
            except ValueError:
                print("El valor total debe ser un número válido.")
                return

        # Llama a la función del CRUD para actualizar la factura
        CRUDFacturas.actualizar_factura(factura_existente)
        print("Factura actualizada con éxito.")

    def eliminar_factura(self):
        print("\nEliminación de Factura:")
        numero_factura = input("Ingrese el número de factura a eliminar: ")

        # Buscar la factura por número
        factura_existente = CRUDFacturas.buscar_factura_por_numero(numero_factura)

        if not factura_existente:
            print("Factura no encontrada.")
            return

        print(f"Factura encontrada - Número: {factura_existente.numero}, Cliente: {factura_existente.cliente.nombre}, Valor Total: {factura_existente.valor_total}")

        confirmacion = input("¿Está seguro de que desea eliminar esta factura? (S/N): ").strip().lower()

        if confirmacion == "s":
            # Llama a la función del CRUD para eliminar la factura
            CRUDFacturas.eliminar_factura(factura_existente)
            print("Factura eliminada con éxito.")
        else:
            print("Eliminación cancelada.")
