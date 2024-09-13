print('Función de número mayor')

def max_estricto(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return None 

# Ejecución del ejercicio
def programa_principal():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))

    resultado = max_estricto(a, b, c)

    if resultado is None:
        print("No existe un mayor estricto.")
    else:
        print(f"El mayor estricto es: {resultado}")

programa_principal()