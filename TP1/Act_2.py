print("----- Registro de Notas de Exámenes -----")

nota1 = float(input("Ingrese la nota del primer examen: "))
nota2 = float(input("Ingrese la nota del segundo examen: "))

promedio = (nota1 + nota2) / 2
print(f"\nEl promedio de las dos notas es: {promedio:.2f}")

if nota2 >= 7:
    print("El alumno aprobó el segundo examen.")
else:
    print("El alumno desaprobó el segundo examen.")

if nota2 > nota1:
    print("Mejoró su desempeño.")
elif nota2 == nota1:
    print("Mantuvo la nota.")
else:
    print("Empeoró su desempeño.")

if promedio >= 7:
    print("El alumno promocionó la materia.")
elif promedio >= 4:
    print("El alumno debe rendir final.")
else:
    print("El alumno debe recursar la materia.")
