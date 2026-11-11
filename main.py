import tkinter as tk
from Vistas.FormProducto import mostrar_formulario
from Vistas.TablaProducto import mostrar_tabla

ventana = tk.Tk()
ventana.title("Gestor de productos")
ventana.geometry("900x600")

contenedorFormulario = tk.Frame(ventana)
contenedorFormulario.pack(side="left", fill="y")

contenedorTabla = tk.Frame(ventana)
contenedorTabla.pack(side="right", fill="both", expand=True)

tabla = mostrar_tabla(contenedorTabla)
mostrar_formulario(contenedorFormulario, tabla)

ventana.mainloop()