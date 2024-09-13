print('Verificar validez de fecha')

def es_fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False
    
    return True

# Validación de fecha
def probar_fecha():
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))

    if es_fecha_valida(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")

probar_fecha()