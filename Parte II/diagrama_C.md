## Diagrama de Clases - Sistema de Facturación

### Clases Principales
- **Cliente**
  - Atributos:
    - cedula: str
    - nombre: str
  - Métodos:
    - save()
- **Producto**
  - Atributos:
    - codigo: str
    - nombre: str
    - precio: float
  - Métodos:
    - save()
- **Factura**
  - Atributos:
    - numero: str
    - fecha: str
    - cliente: Cliente
    - productos: Lista de Productos
    - valor_total: float
  - Métodos:
    - save()
    
### CRUD para Clientes
- **CRUDClientes**
  - Métodos:
    - crear_cliente()
    - buscar_cliente_por_cedula(cedula: str)
    - listar_clientes()
    - actualizar_cliente(cliente: Cliente)
    - eliminar_cliente(cliente: Cliente)

### CRUD para Productos
- **CRUDProductos**
  - Métodos:
    - crear_producto()
    - buscar_producto_por_codigo(codigo: str)
    - listar_productos()
    - actualizar_producto(producto: Producto)
    - eliminar_producto(producto: Producto)

### CRUD para Facturas
- **CRUDFacturas**
  - Métodos:
    - crear_factura(cliente: Cliente, productos: Lista de Productos, valor_total: float, numero_factura: str, fecha: str)
    - buscar_factura_por_numero(numero_factura: str)
    - buscar_facturas_por_cliente(cliente: Cliente)
    - buscar_facturas_por_fecha(fecha: str)
    - actualizar_factura(factura: Factura)
    - eliminar_factura(factura: Factura)

