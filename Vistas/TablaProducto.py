import tkinter as tk
from tkinter import ttk
from Modelos.Productos import Producto
from Vistas.FormEditarProducto import abrir_formulario_edicion

import tkinter as tk
from tkinter import ttk


def mostrar_tabla(ventana):
    contenedor = tk.Frame(ventana)
    contenedor.pack(fill="both", expand=True)
    contenedorBusqueda = tk.Frame(contenedor)
    contenedorBusqueda.pack(fill="x", pady=5)

    tk.Label(contenedorBusqueda, text="Código de Barra:").pack(side="left", padx=5)
    entryBusqueda = tk.Entry(contenedorBusqueda)
    entryBusqueda.pack(side="left", padx=5)

    def buscar_producto():
        codigo = entryBusqueda.get().strip()
        for item in tabla.get_children():
            tabla.delete(item)
        for p in Producto.productos:
            if codigo == "" or str(p.getCodigoBarra()) == codigo:
                tabla.insert("", "end", iid=p.getId(), values=(p.getNombre(), p.getPrecio(), p.getStock(), p.getCategoria(), p.getCodigoBarra()))

    tk.Button(contenedorBusqueda, text="Buscar", command=buscar_producto).pack(side="left", padx=5)
    entryBusqueda.bind("<Return>", lambda event: buscar_producto())
    tabla = ttk.Treeview(
        contenedor,
        columns=("Nombre", "Precio", "Stock", "Categoria", "Codigo de Barra"),
        show="headings"
    )

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Precio", text="Precio")
    tabla.heading("Stock", text="Stock")
    tabla.heading("Categoria", text="Categoria")
    tabla.heading("Codigo de Barra", text="Codigo de Barra")

    scrollbar = ttk.Scrollbar(
        contenedor,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(yscrollcommand=scrollbar.set)

    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    contenedorBotones = tk.Frame(ventana)
    contenedorBotones.pack()

    def editar_producto():
        idProductoSeleccionado= tabla.selection()[0]
        print(idProductoSeleccionado)
        if idProductoSeleccionado != "":
            abrir_formulario_edicion(idProductoSeleccionado, tabla)                  
        else: print ('no hay producto seleccionado')


    def eliminar_producto():
        idProductoSeleccionado= tabla.selection()[0]
        if idProductoSeleccionado != "":
         for producto in Producto.productos:
            if producto.id_producto==idProductoSeleccionado:
               Producto.productos.remove(producto)
               break
         
         tabla.delete(idProductoSeleccionado)

         
        print(len(Producto.productos)) 

    botonEditar = tk.Button(
        contenedorBotones,
        text="Editar",
        command=editar_producto
    )

    botonEliminar = tk.Button(
        contenedorBotones,
        text="Eliminar",
        command=eliminar_producto
    )

    botonEditar.pack(side="left")
    botonEliminar.pack(side="left")


    return tabla
