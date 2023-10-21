## Diagrama de Componentes - Sistema de Facturación

### Componentes Principales
- **Aplicación de Facturación**
  - Clases:
    - `Cliente`
    - `Producto`
    - `Factura`
    - `CRUDClientes`
    - `CRUDProductos`
    - `CRUDFacturas`
  - Interacciones:
    - `Cliente` utiliza `CRUDClientes`
    - `Producto` utiliza `CRUDProductos`
    - `Factura` utiliza `CRUDFacturas`
    - `CRUDClientes` se relaciona con `Cliente`
    - `CRUDProductos` se relaciona con `Producto`
    - `CRUDFacturas` se relaciona con `Factura`

### Repositorios
- **Base de Datos (simulado)**
  - Clases:
    - `ClienteData`
    - `ProductoData`
    - `FacturaData`
  - Interacciones:
    - Las clases de datos se utilizan para almacenar y recuperar los objetos de las clases principales.

### Interfaces de Usuario
- **Interfaz de Usuario de Consola**
  - Funcionalidad:
    - Interacción con el usuario para realizar operaciones de facturación.
  - Clases:
    - `MainMenu`
  - Interacciones:
    - `MainMenu` interactúa con las clases de CRUD y las clases principales para realizar operaciones.

