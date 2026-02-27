import os

def limpiar():
    os.system("cls")

def menu():
    while True:
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir\n")

        opcion = int(input("Digite una opcion: "))
        match opcion:
            case 1:
                limpiar()
                print("Hola, ¿cómo estás?")
                input("Presiona Enter para continuar...")
            case 2:
                limpiar()
                print("Hasta luego, ¡vuelve pronto!")
                input("Presiona Enter para continuar...")
            case 3:
                limpiar()
                print("Saliendo del programa...")
                input("Presiona Enter para continuar...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                limpiar()

menu()
print("Programa finalizado.")