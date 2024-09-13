def calcular_cambio(total_compra, dinero_recibido):
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    
    if dinero_recibido < total_compra:
        print("Error: El dinero recibido es insuficiente.")
        return
    
    cambio = dinero_recibido - total_compra
    print(f"El cambio a devolver es: ${cambio}")

    resultado = {}
    
    for billete in denominaciones:
        cantidad_billetes = cambio // billete
        if cantidad_billetes > 0:
            resultado[billete] = cantidad_billetes
            cambio -= cantidad_billetes * billete
    
    for billete, cantidad in resultado.items():
        print(f"{cantidad} billete(s) de ${billete}")

# Ingreso de valores
def programa_principal():
    total_compra = int(input("Ingresa el total de la compra: "))
    dinero_recibido = int(input("Ingresa el dinero recibido: "))
    
    calcular_cambio(total_compra, dinero_recibido)
programa_principal()