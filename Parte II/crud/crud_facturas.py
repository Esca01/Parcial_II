from model.factura import Factura

class CRUDFacturas:
    @staticmethod
    def crear_factura(cliente, productos, valor_total, numero_factura, fecha):
        factura = Factura(cliente, productos, valor_total, numero_factura, fecha)
        factura.save()
        return factura

    @staticmethod
    def buscar_facturas_por_cliente(cliente):
        return Factura.find_by_cliente(cliente)

    @staticmethod
    def buscar_facturas_por_fecha(fecha):
        return Factura.find_by_fecha(fecha)

    @staticmethod
    def buscar_factura_por_numero(numero_factura):
        for factura in Factura.facturas:  # Suponiendo que tienes una lista de facturas en la clase Factura
            if factura.numero == numero_factura:
                return factura  # Devuelve la factura si se encuentra
        return None 


    @staticmethod
    def actualizar_factura(factura):
        factura.save()

    @staticmethod
    def eliminar_factura(factura):
        factura.delete()
