print('Actividad 4.a')
print('Aula según día')
print("Día   Aula")
for dia in range(1, 7):
    if dia % 2 == 0:
        aula = "A-300"
    else:
        aula = "A-315"
    print(f"{dia}     {aula}")


print('\nActividad 4.b')
errores = 0

while True:
    edad = int(input("Ingrese la edad (mayor de 18) o -1 para salir: "))
    
    if edad == -1:
        break

    if edad >= 18:
        print(f"Edad ingresada: {edad}")
    else:
        print("Edad no válida. Debe ser mayor de 18.")
        errores += 1

print(f"Cantidad de cargas erróneas: {errores}")

#///////////////////////////////////////
print('\nActividad 4.c')

suma_notas = 0

for i in range(5):
    nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / 5
print(f"El promedio de las notas es: {promedio:.2f}")

#///////////////////////////////////////
print('\nActividad 4.d')
cuota_diaria = 1250

print("Días  Costo total")
for dias in range(1, 7):
    costo_total = dias * cuota_diaria
    print(f"{dias}     ${costo_total}")
