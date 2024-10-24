# Turnero de cine
import tkinter as tk
from tkinter import messagebox, simpledialog

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Reservas - Cine")

letras_filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
filas = len(letras_filas)
columnas = 10

butacas = [[0 for _ in range(columnas)] for _ in range(filas)]

# Función para manejar la reserva de un asiento
def reservar_butaca(fila, columna):
    if butacas[fila][columna] == 0: 
        nombre = simpledialog.askstring("Reserva", "Ingrese su nombre:", parent=ventana)
        telefono = simpledialog.askstring("Reserva", "Ingrese su teléfono:", parent=ventana)
        if nombre and telefono:
            butacas[fila][columna] = (nombre, telefono)
            botones[fila][columna].config(text=f"{letras_filas[fila]}{columna + 1}\nReservado", bg="red")
            messagebox.showinfo("Reserva exitosa", f"Butaca {letras_filas[fila]}{columna + 1} reservada por {nombre}.")
        else:
            messagebox.showwarning("Datos incompletos", "Debe ingresar nombre y teléfono para completar la reserva.")
    else:
        reserva = butacas[fila][columna]
        messagebox.showinfo("Butaca ocupada", f"Butaca {letras_filas[fila]}{columna + 1} ya reservada por {reserva[0]} (Tel: {reserva[1]}).")

botones = []
for i in range(filas):
    fila_botones = []
    for j in range(columnas):
        boton = tk.Button(ventana, text=f"{letras_filas[i]}{j + 1}\nLibre", width=10, height=2, bg="green",
                          command=lambda i=i, j=j: reservar_butaca(i, j))
        boton.grid(row=i, column=j, padx=5, pady=5)
        fila_botones.append(boton)
    botones.append(fila_botones)

ventana.mainloop()
