from ui.main_menu import MainMenu

def main():
    # Crear una instancia del menú principal
    menu = MainMenu()

    while True:
        menu.mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu.menu_clientes()

        elif opcion == "2":
            menu.menu_productos()
        
        elif opcion == "3":
            menu.menu_facturas()

        elif opcion == "4":
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
