import tkinter as tk
from tkinter import messagebox

contactos = []
Ruta_del_Logo = "celular.ico"

def mostrar_contactos():
    if contactos:
        texto = "Tus contactos:\n"
        for contacto in contactos:
            texto = texto + contacto + "\n"
    else:
        texto = "Aun no hay contactos guardados...\n¡Registra alguno!"
    etiqueta_derecha.config(text=texto)

def agregar_contacto():
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Contacto")
    ventana_agregar.geometry("300x200")
    
    tk.Label(ventana_agregar, text="Nombre:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_agregar, width=30)
    entrada_nombre.pack(pady=5)
    
    tk.Label(ventana_agregar, text="Telefono:").pack(pady=5)
    entrada_telefono = tk.Entry(ventana_agregar, width=30)
    entrada_telefono.pack(pady=5)
    
    def guardar():
        nombre = entrada_nombre.get()
        telefono = entrada_telefono.get()
        if nombre and telefono:
            contacto = nombre + " / " + telefono
            contactos.append(contacto)
            mostrar_contactos()
            messagebox.showinfo("Agregado", "Tu contacto '" + nombre + "' ha sido agregado.")
            ventana_agregar.destroy()
    
    tk.Button(ventana_agregar, text="Guardar", command=guardar).pack(pady=10)

def editar_contacto():
    if len(contactos) == 0:
        messagebox.showwarning("Error", "Aun no hay contactos para editar.")
        return
    
    ventana_editar = tk.Toplevel(ventana)
    ventana_editar.title("Editar Contacto")
    ventana_editar.geometry("300x200")
    
    tk.Label(ventana_editar, text="¿Que contacto quieres editar?\nSolo escribe el nombre").pack(pady=5)
    entrada_buscar = tk.Entry(ventana_editar, width=30)
    entrada_buscar.pack(pady=5)
    
    tk.Label(ventana_editar, text="Nuevo teléfono:").pack(pady=5)
    entrada_nuevo_tel = tk.Entry(ventana_editar, width=30)
    entrada_nuevo_tel.pack(pady=5)
    
    def actualizar():
        nombre_buscar = entrada_buscar.get()
        nuevo_tel = entrada_nuevo_tel.get()
        if nombre_buscar and nuevo_tel:
            encontrado = False
            for i in range(len(contactos)):
                contacto = contactos[i]
                if contacto.find(nombre_buscar) == 0:
                    contactos[i] = nombre_buscar + " - " + nuevo_tel
                    mostrar_contactos()
                    messagebox.showinfo("Agenda", "Telefono de '" + nombre_buscar + "' ha sido actualizado.")
                    ventana_editar.destroy()
                    encontrado = True
                    break
            if not encontrado:
                messagebox.showwarning("Error", "No se encontró el contacto " + nombre_buscar + ".")
    
    tk.Button(ventana_editar, text="Actualizar", command=actualizar).pack(pady=10)

def borrar_contacto():
    if len(contactos) == 0:
        messagebox.showwarning("Error", "Aun no hay contactos para borrar.")
        return
    
    ventana_borrar = tk.Toplevel(ventana)
    ventana_borrar.title("Borrar Contacto")
    ventana_borrar.geometry("300x120")
    
    tk.Label(ventana_borrar, text="¿Que contacto quieres borrar?\nSolo digita el nombre del contacto").pack(pady=5)
    entrada_buscar = tk.Entry(ventana_borrar, width=30)
    entrada_buscar.pack(pady=5)
    
    def eliminar():
        nombre_buscar = entrada_buscar.get()
        if nombre_buscar:
            encontrado = False
            for i in range(len(contactos)):
                contacto = contactos[i]
                if contacto.find(nombre_buscar) == 0:
                    contactos.pop(i)
                    mostrar_contactos()
                    messagebox.showinfo("Agenda", "Tu contacto '" + nombre_buscar + "' ha sido eliminado.")
                    encontrado = True
                    break
            if not encontrado:
                messagebox.showwarning("Error", "No se encontro el contacto " + nombre_buscar + ".\nIntenta con otro")
    
    tk.Button(ventana_borrar, text="Eliminar", command=eliminar).pack(pady=10)

def mostrar_tutorial():
    messagebox.showinfo("Tutorial", 
                        "Bienvenido a tu Agenda de Contactos.\n\n"
                        "- Puedes usar los botones para agregar, editar o borrar.\n"
                        "- Veras los contactos se mostrarán en el panel derecho.")

def salir():
    ventana.destroy()

def acerca_de():
    messagebox.showinfo("Acerca", "Creado por Victor Cordoba\nVersión 1.0\n17/09/2025")

ventana = tk.Tk()
ventana.title("Aplicacion de Contactos")
ventana.geometry("600x400")

try:
    ventana.iconbitmap(Ruta_del_Logo)
except tk.TclError:
    print("No se pudo cargar el icono desde la ruta: " + Ruta_del_Logo)

barra_menu = tk.Menu(ventana)

menu_inicio = tk.Menu(barra_menu, tearoff=0)
menu_inicio.add_command(label="Agregar Contacto", command=agregar_contacto)
menu_inicio.add_command(label="Editar Contacto", command=editar_contacto)
menu_inicio.add_command(label="Borrar Contacto", command=borrar_contacto)
menu_inicio.add_separator()
menu_inicio.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Tutorial de la aplicación", command=mostrar_tutorial)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

frame_izq = tk.Frame(ventana, width=200, height=400, bg="lightgray")
frame_izq.pack(side="left", fill="y")

frame_derecho = tk.Frame(ventana, width=400, height=400, bg="white")
frame_derecho.pack(side="right", expand=True, fill="both")

tk.Label(frame_izq, text="Opciones de la Agenda", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(frame_izq, text="Agregar Contacto", command=agregar_contacto).pack(pady=5, fill="x")
tk.Button(frame_izq, text="Editar Contacto", command=editar_contacto).pack(pady=5, fill="x")
tk.Button(frame_izq, text="Borrar Contacto", command=borrar_contacto).pack(pady=5, fill="x")

etiqueta_derecha = tk.Label(frame_derecho, text="Aun no hay contactos guardados...\n¡Registra alguno!", bg="white", font=("Arial", 14), justify="left")
etiqueta_derecha.pack(expand=True, anchor="nw", padx=10, pady=10)

ventana.mainloop()