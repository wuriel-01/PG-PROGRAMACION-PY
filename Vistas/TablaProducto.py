
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Modelos.Productos import Producto
from Vistas.FormEditarProducto import abrir_formulario_edicion


def mostrar_tabla(ventana):
    contenedor = tk.Frame(ventana)
    contenedor.pack(fill="both", expand=True)

    contenedorBusqueda = tk.Frame(contenedor)
    contenedorBusqueda.pack(fill="x", pady=5)

    tk.Label(
        contenedorBusqueda,
        text="Código de Barra:"
    ).pack(side="left", padx=5)


    estilo = ttk.Style()
    estilo.theme_use("clam")

   
    estilo.configure(
        "Treeview.Heading",
        background="#1F497D",
        foreground="white",
        font=("Segoe UI", 10, "bold"),
        padding=6
    )


    estilo.configure(
        "Treeview",
        background="#FFFFFF",
        foreground="#333333",
        rowheight=26,
        fieldbackground="#FFFFFF",
        font=("Segoe UI", 9)
    )

  
    estilo.map("Treeview", background=[("selected", "#0078D7")])
    entryBusqueda = tk.Entry(contenedorBusqueda)
    entryBusqueda.pack(side="left", padx=5)

    tabla = ttk.Treeview(
        contenedor,
        columns=("Nombre", "Precio", "Stock", "Categoria", "Codigo de Barra", "Estado"),
        show="headings"
    )

    def obtener_estado_stock(stock):
        if stock == 0:
            return "Sin stock"
        elif stock <= 5:
            return "Stock bajo"
        else:
            return "Disponible"

    def cargar_productos():
        for elemento in tabla.get_children():
            tabla.delete(elemento)

        for producto in Producto.productos:
            estado = obtener_estado_stock(producto.getStock())

            tabla.insert(
                "",
                tk.END,
                iid=producto.getId(),
                values=(
                    producto.getNombre(),
                    producto.getPrecio(),
                    producto.getStock(),
                    producto.getCategoria(),
                    producto.getCodigoBarra(),
                    estado
                )
            )

    def buscar_producto():
        codigo = entryBusqueda.get().strip()

        for item in tabla.get_children():
            tabla.delete(item)

        for p in Producto.productos:
            if codigo == "" or str(p.getCodigoBarra()).strip() == codigo:
                estado = obtener_estado_stock(p.getStock())

                tabla.insert(
                    "",
                    "end",
                    iid=p.getId(),
                    values=(
                        p.getNombre(),
                        p.getPrecio(),
                        p.getStock(),
                        p.getCategoria(),
                        p.getCodigoBarra(),
                        estado
                    )
                )

    def mostrar_todos():
        entryBusqueda.delete(0, tk.END)
        cargar_productos()

    tk.Button(
        contenedorBusqueda,
        text="Buscar",
        command=buscar_producto
    ).pack(side="left", padx=5)

    tk.Button(
        contenedorBusqueda,
        text="Mostrar todos",
        command=mostrar_todos
    ).pack(side="left", padx=5)

    entryBusqueda.bind(
        "<Return>",
        lambda event: buscar_producto()
    )

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Precio", text="Precio")
    tabla.heading("Stock", text="Stock")
    tabla.heading("Categoria", text="Categoria")
    tabla.heading("Codigo de Barra", text="Codigo de Barra")
    tabla.heading("Estado", text="Estado")
    
    tabla.column("Nombre", width=140, anchor="w")
    tabla.column("Precio", width=70, anchor="center")
    tabla.column("Stock", width=60, anchor="center")
    tabla.column("Categoria", width=110, anchor="center")
    tabla.column("Codigo de Barra", width=130, anchor="center")
    tabla.column("Estado", width=90, anchor="center")
    scrollbar = ttk.Scrollbar(
        contenedor,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(yscrollcommand=scrollbar.set)

    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    cargar_productos()

    contenedorBotones = tk.Frame(ventana)
    contenedorBotones.pack()

    def editar_producto():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showerror("Error", "Producto no seleccionado")
            return

        idProductoSeleccionado = seleccion[0]
        abrir_formulario_edicion(idProductoSeleccionado, tabla)

    def eliminar_producto():
        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showerror("Error", "Producto no seleccionado")
            return

        idProductoSeleccionado = seleccion[0]

        for producto in Producto.productos:
            if producto.id_producto == idProductoSeleccionado:
                Producto.productos.remove(producto)
                break

        tabla.delete(idProductoSeleccionado)
        messagebox.showinfo("", "Producto eliminado correctamente")
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
    contenedorBotones = tk.Frame(contenedor)
    contenedorBotones.pack(pady=10)

    tk.Button(contenedorBotones, text="Editar", command=editar_producto, bg="#1F497D", fg="white").pack(side="left", padx=5)
    tk.Button(contenedorBotones, text="Eliminar", command=eliminar_producto, bg="#C00000", fg="white").pack(side="left", padx=5)
    return tabla