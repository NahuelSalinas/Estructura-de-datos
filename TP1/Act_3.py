print('===========================')
print('Asignación de aulas')
print('===========================')

# Asignación de aulas
dia = int(input("Ingrese el número de día (1 a 6): "))

if dia % 2 == 0:
    print("Los alumnos cursan en el aula A-300.")
else:
    print("Los alumnos cursan en el aula A-315.")

# Descuento en la cuota
turno = input("Ingrese el turno (Mañana/Tarde): ").lower()
materias = int(input("Ingrese la cantidad de materias inscritas: "))
cuota = float(input("Ingrese el valor de la cuota: "))

if turno == "tarde" and materias > 3:
    descuento = cuota * 0.25
else:
    descuento = cuota * 0.05

cuota_con_descuento = cuota - descuento
print(f"El valor de la cuota con descuento es: ${cuota_con_descuento:.2f}")

# Costo de estacionamiento 
transporte = input("¿Viene en auto, moto o bicicleta?: ").lower()

if transporte in ["auto", "moto"]:
    costo_estacionamiento = 300
elif transporte == "bicicleta":
    costo_estacionamiento = 50
else:
    costo_estacionamiento = 0

print(f"El costo diario de estacionamiento es: ${costo_estacionamiento:.2f}")
