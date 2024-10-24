#Gestión de cola utilizando deque()
from collections import deque

cola = deque()

def agregar_cliente():
    cliente = input("Ingrese el nombre del cliente: ")
    cola.append(cliente)
    print(f"{cliente} ha sido agregado a la cola.")

def atender_cliente():
    if cola:
        cliente = cola.popleft()
        print(f"{cliente} ha sido atendido.")
    else:
        print("No hay clientes para atender.")

def clientes_en_espera():
    print(f"Clientes en espera: {len(cola)}")

def mostrar_menu():
    print("\n--- Menú de Gestión de Cola ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver clientes en espera")
    print("4. Salir")

def iniciar_gestion_cola():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            atender_cliente()
        elif opcion == "3":
            clientes_en_espera()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elija entre 1 y 4.")

iniciar_gestion_cola()
