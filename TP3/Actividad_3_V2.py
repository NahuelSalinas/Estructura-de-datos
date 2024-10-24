import tkinter as tk
from collections import deque
from tkinter import messagebox

cola = deque()

# Agregar clientes
def agregar_cliente():
    nombre = entrada_cliente.get()
    if nombre:
        cola.append(nombre)
        actualizar_lista()
        entrada_cliente.delete(0, tk.END)
        messagebox.showinfo("Cliente agregado", f"{nombre} ha sido agregado a la cola.")
    else:
        messagebox.showwarning("Error", "Debe ingresar el nombre del cliente.")

# Atender al primer cliente
def atender_cliente():
    if cola:
        cliente_atendido = cola.popleft()
        actualizar_lista()
        messagebox.showinfo("Atención", f"{cliente_atendido} ha sido atendido.")
    else:
        messagebox.showwarning("Cola vacía", "No hay clientes para atender.")

# Función para actualizar la lista de clientes en espera
def actualizar_lista():
    lista_clientes.delete(0, tk.END)
    for cliente in cola:
        lista_clientes.insert(tk.END, cliente)

ventana = tk.Tk()
ventana.title("Gestión de Cola de Clientes")

# Etiqueta y entrada para agregar clientes
tk.Label(ventana, text="Nombre del Cliente:").grid(row=0, column=0, padx=10, pady=10)
entrada_cliente = tk.Entry(ventana)
entrada_cliente.grid(row=0, column=1, padx=10, pady=10)

# Botón para agregar clientes
btn_agregar = tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente)
btn_agregar.grid(row=0, column=2, padx=10, pady=10)

# Lista para mostrar los clientes en espera
tk.Label(ventana, text="Clientes en Espera:").grid(row=1, column=0, padx=10, pady=10)
lista_clientes = tk.Listbox(ventana, height=10, width=40)
lista_clientes.grid(row=1, column=1, padx=10, pady=10)

# Botón para atender clientes
btn_atender = tk.Button(ventana, text="Atender Cliente", command=atender_cliente)
btn_atender.grid(row=2, column=1, padx=10, pady=10)

ventana.mainloop()
