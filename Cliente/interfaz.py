import tkinter as tk
from tkinter import messagebox, ttk
import requests

# URL de la API de Django
API_URL = 'http://127.0.0.1:8000/api/clientes/'

# Función para guardar un cliente (Create)
def guardar_cliente():
    if (cedula.get() == '' or nombre.get() == '' or apellido.get() == '' or 
        telefono.get() == '' or direccion.get() == '' or correo.get() == ''):
        messagebox.showerror('Error', 'Todos los campos son obligatorios')
        return
    datos = {
        'cedula': cedula.get(),
        'nombre': nombre.get(),
        'apellido': apellido.get(),
        'telefono': telefono.get(),
        'direccion': direccion.get(),
        'correo': correo.get()
    }

    try:
        response = requests.post(API_URL, json=datos)
        if response.status_code == 201:
            messagebox.showinfo('Correcto', 'Cliente guardado correctamente')
            listar_clientes()  # Actualizar la lista después de guardar
        else:
            messagebox.showerror('Error', f'Error al guardar el cliente: {response.text}')
    except Exception as e:
        messagebox.showerror('Error', f'Error al conectar con la API: {str(e)}')

    borrar_campos()

# Función para listar clientes (Read)
def listar_clientes():
    try:
        response = requests.get(API_URL + 'listar/')
        if response.status_code == 200:
            clientes = response.json()
            tree.delete(*tree.get_children())  # Limpiar la tabla
            for cliente in clientes:
                tree.insert('', 'end', values=(
                    cliente['cedula'],
                    cliente['nombre'],
                    cliente['apellido'],
                    cliente['telefono'],
                    cliente['direccion']
                    # Si deseas mostrar el correo en la tabla, agrega: cliente['correo']
                ))
        else:
            messagebox.showerror('Error', f'Error al listar clientes: {response.text}')
    except Exception as e:
        messagebox.showerror('Error', f'Error al conectar con la API: {str(e)}')

# Función para actualizar un cliente (Update)
def actualizar_cliente():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showerror('Error', 'Seleccione un cliente para actualizar')
        return
    cliente_id = tree.item(seleccionado)['values'][0]  # Obtener la cédula del cliente seleccionado
    datos = {
        'cedula': cedula.get(),
        'nombre': nombre.get(),
        'apellido': apellido.get(),
        'telefono': telefono.get(),
        'direccion': direccion.get(),
        'correo': correo.get()
    }
    try:
        response = requests.put(f'{API_URL}{cliente_id}/actualizar/', json=datos)
        if response.status_code == 200:
            messagebox.showinfo('Correcto', 'Cliente actualizado correctamente')
            listar_clientes()  # Actualizar la lista después de actualizar
        else:
            messagebox.showerror('Error', f'Error al actualizar el cliente: {response.text}')
    except Exception as e:
        messagebox.showerror('Error', f'Error al conectar con la API: {str(e)}')
    borrar_campos()

# Función para eliminar un cliente (Delete)
def eliminar_cliente():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showerror('Error', 'Seleccione un cliente para eliminar')
        return

    cliente_id = tree.item(seleccionado)['values'][0]  # Obtener la cédula del cliente seleccionado

    try:
        response = requests.delete(f'{API_URL}{cliente_id}/eliminar/')
        if response.status_code == 204:
            messagebox.showinfo('Correcto', 'Cliente eliminado correctamente')
            listar_clientes()  # Actualizar la lista después de eliminar
        else:
            messagebox.showerror('Error', f'Error al eliminar el cliente: {response.text}')
    except Exception as e:
        messagebox.showerror('Error', f'Error al conectar con la API: {str(e)}')

# Función para borrar los campos de entrada
def borrar_campos():
    cedula.set('')
    nombre.set('')
    apellido.set('')
    telefono.set('')
    direccion.set('')
    correo.set('')

# Construcción de la ventana
ventana = tk.Tk()
ventana.title('Sistema de Registro de Clientes')
ventana.geometry('800x600')

# Variables
cedula = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
telefono = tk.StringVar()
direccion = tk.StringVar()
correo = tk.StringVar()

# Etiquetas y entradas
tk.Label(ventana, text='Cédula:').grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=cedula).grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text='Nombre:').grid(row=1, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=nombre).grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text='Apellido:').grid(row=2, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=apellido).grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text='Teléfono:').grid(row=3, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=telefono).grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text='Dirección:').grid(row=4, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=direccion).grid(row=4, column=1, padx=10, pady=5)

# Agregar el campo de correo
tk.Label(ventana, text='Correo:').grid(row=5, column=0, padx=10, pady=5, sticky='e')
tk.Entry(ventana, textvariable=correo).grid(row=5, column=1, padx=10, pady=5)

# Botones
tk.Button(ventana, text='Guardar', command=guardar_cliente).grid(row=6, column=0, pady=10)
tk.Button(ventana, text='Actualizar', command=actualizar_cliente).grid(row=6, column=1, pady=10)
tk.Button(ventana, text='Eliminar', command=eliminar_cliente).grid(row=6, column=2, pady=10)

# Tabla para listar clientes
columnas = ('Cédula', 'Nombre', 'Apellido', 'Teléfono', 'Dirección')
tree = ttk.Treeview(ventana, columns=columnas, show='headings')
for col in columnas:
    tree.heading(col, text=col)
tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Listar clientes al iniciar la aplicación
listar_clientes()

# Iniciar el loop de la ventana
ventana.mainloop()
