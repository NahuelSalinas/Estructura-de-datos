def calcular_descuento_o_incremento(moneda):
    # Tabla de descuentos por tipo de moneda
    descuentos = {
        "dolares": 0.05,
        "yenes": 0.15,
        "guaranies": 0.20,
        "pesos": 0.10
    }

    if moneda in descuentos:
        return -descuentos[moneda]
    else:
        return 0.1 

def emitir_recibo(nombre_comprador, moneda, cantidad):
    precio_por_unidad = 1000
    subtotal = precio_por_unidad * cantidad

    ajuste = calcular_descuento_o_incremento(moneda)
    total_ajuste = subtotal * ajuste
    total_final = subtotal + total_ajuste

    # Recibo de la compra
    print("\n----- Recibo de compra -----")
    print(f"Comprador: {nombre_comprador}")
    print(f"Producto: Zapallo")
    print(f"Cantidad: {cantidad}")
    print(f"Precio por unidad: {precio_por_unidad} pesos")
    print(f"Moneda: {moneda.capitalize()}")
    
    if ajuste < 0:
        print(f"Descuento aplicado: {abs(ajuste * 100)}%")
    else:
        print(f"Incremento aplicado: {ajuste * 100}%")
    
    print(f"Subtotal: {subtotal} pesos")
    print(f"Descuento: {total_ajuste} pesos")
    print(f"Total a pagar: {total_final} pesos")
    print("----------------------------")

def programa_principal():
    nombre_comprador = input("Ingrese el nombre del comprador: ")
    moneda = input("Ingrese la moneda de pago (dolares, yenes, guaranies, pesos u otra): ").lower()
    cantidad = int(input("Ingrese la cantidad de zapallos que desea comprar: "))

    emitir_recibo(nombre_comprador, moneda, cantidad)
programa_principal()