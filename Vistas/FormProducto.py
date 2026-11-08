
import tkinter as tk
import uuid
from Modelos.Productos import Producto


def mostrar_formulario(ventana, tabla):
    formulario = tk.Frame(ventana)
    formulario.pack()

    labelNombre = tk.Label(formulario, text="Nombre")
    inputNombre = tk.Entry(formulario)
    labelNombre.grid(row=0, column=0)
    inputNombre.grid(row=0, column=1)

    labelPrecio = tk.Label(formulario, text="Precio")
    inputPrecio = tk.Entry(formulario)
    labelPrecio.grid(row=1, column=0)
    inputPrecio.grid(row=1, column=1)

    labelStock = tk.Label(formulario, text="Stock")
    inputStock = tk.Entry(formulario)
    labelStock.grid(row=2, column=0)
    inputStock.grid(row=2, column=1)

    labelCategoria = tk.Label(formulario, text="Categoria")
    inputCategoria = tk.Entry(formulario)
    labelCategoria.grid(row=3, column=0)
    inputCategoria.grid(row=3, column=1)

    labelCodigoBarra = tk.Label(formulario, text="Codigo de Barra")
    inputCodigoBarra = tk.Entry(formulario)
    labelCodigoBarra.grid(row=4, column=0)
    inputCodigoBarra.grid(row=4, column=1)



    def generar_id():
        return str(uuid.uuid4())

    def crear_producto():
        nombre = inputNombre.get()
        precio = float(inputPrecio.get())
        stock = int(inputStock.get())
        categoria = inputCategoria.get()
        codigoBarra = inputCodigoBarra.get()
        descripcion = ""
    
        for p in Producto.productos:
            if str(p.getCodigoBarra()).strip() == codigoBarra.strip():
                from tkinter import messagebox
                messagebox.showerror("Código duplicado", f"El código '{codigoBarra}' ya pertenece al producto: {p.getNombre()}")
                return
        id_producto = generar_id()
        
        Producto(nombre,precio,stock,descripcion,categoria,id_producto,codigoBarra)
        print(len(Producto.productos))
        

        tabla.insert(
            "",
            tk.END,
            iid=id_producto,
            values=(
                nombre,
                precio,
                stock,
                categoria,
                codigoBarra
            )
        )


        
    

    botonCrear = tk.Button(
        formulario,
        text="Crear producto",
        command=crear_producto
    )
    botonCrear.grid(row=6, column=0, columnspan=2)