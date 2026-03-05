import os
from saludo import saludo
from despedida import despedida
from trabajando import trabajando 

def limpiar():
    os.system("cls")

def menu():
    while True:
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Trabajar")
        print("4. Salir\n")

        opcion = int(input("Digite una opcion: "))
        match opcion:
            case 1:
                limpiar()
                saludo()
                input("Presiona Enter para continuar...")
            case 2:
                limpiar()
                despedida()
                input("Presiona Enter para continuar...")
            case 3:
                limpiar()
                trabajando()
                input("Presiona Enter para continuar...")
            case 4:
                limpiar()
                print("Saliendo del programa...")
                input("Presiona Enter para continuar...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                limpiar()

if __name__ == "__main__":
    menu()

# menu()
# print("Programa finalizado.")