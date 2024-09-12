print("========================================================")
print("----- Inscripción de Alumnos - Universidad Privada -----")
print("========================================================")

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

posee_titulo_secundario = True

monto_matricula = float(input("Ingrese el monto de la matricula: "))

cuota = monto_matricula + 1000

arancel_python = 12000 / 4

costo_mensual = cuota + arancel_python
print(f"\nEl costo mensual (incluyendo 'Python I') es: ${costo_mensual:.2f}")

pago_efectivo = input("¿Paga en efectivo? (si/no): ").lower()

if pago_efectivo == "si":
    descuento = costo_mensual * 0.75
    print(f"El costo con un 15% de descuento es: ${descuento:.2f}")
else:
    print("No se aplicará descuento.")

print("\n----- Resumen de la Inscripción -----")
print("=======================================")
print(f"Nombre del alumno: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de nacimiento: {fecha_nacimiento} ({edad})")
print(f"Posee título secundario: {posee_titulo_secundario}")
print(f"Monto de la matrícula: ${monto_matricula:.2f}")
print(f"Cuota mensual (sin descuento): ${costo_mensual:.2f}")

if pago_efectivo == "si":
    print(f"Cuota mensual (con descuento): ${descuento:.2f}")
