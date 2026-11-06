import tkinter as tk
from Vistas.FormProducto import mostrar_formulario

ventana = tk.Tk()
ventana.title("Gestor de productos")
ventana.geometry("600x500")

mostrar_formulario(ventana)

ventana.mainloop()