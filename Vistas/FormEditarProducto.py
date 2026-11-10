
import tkinter as tk
from tkinter import messagebox
from Modelos.Productos import Producto
from Validaciones.ValidacionProducto import (
    validar_nombre,
    validar_precio,
    validar_stock,
    validar_categoria,
    validar_codigoBarra
)


def abrir_formulario_edicion(idProducto, tabla):

    ProductoSelecionado = None

    for producto in Producto.productos:
        if producto.id_producto == idProducto:
            ProductoSelecionado = producto
            break

    if ProductoSelecionado is None:
        return

    ventanaEditar = tk.Toplevel()
    ventanaEditar.title("Editar producto")
    ventanaEditar.geometry("400x400")

    contenedorFormulario = tk.Frame(ventanaEditar)
    contenedorFormulario.pack()

    labelNombre = tk.Label(contenedorFormulario, text="Nombre")
    inputNombre = tk.Entry(contenedorFormulario)
    inputNombre.insert(0, ProductoSelecionado.nombre)
    labelNombre.grid(row=0, column=0)
    inputNombre.grid(row=0, column=1)

    labelPrecio = tk.Label(contenedorFormulario, text="Precio")
    inputPrecio = tk.Entry(contenedorFormulario)
    inputPrecio.insert(0, str(ProductoSelecionado.precio))
    labelPrecio.grid(row=1, column=0)
    inputPrecio.grid(row=1, column=1)

    labelStock = tk.Label(contenedorFormulario, text="Stock")
    inputStock = tk.Entry(contenedorFormulario)
    inputStock.insert(0, str(ProductoSelecionado.stock))
    labelStock.grid(row=2, column=0)
    inputStock.grid(row=2, column=1)

    labelCategoria = tk.Label(contenedorFormulario, text="Categoria")
    inputCategoria = tk.Entry(contenedorFormulario)
    inputCategoria.insert(0, ProductoSelecionado.categoria)
    labelCategoria.grid(row=3, column=0)
    inputCategoria.grid(row=3, column=1)

    labelCodigoBarra = tk.Label(contenedorFormulario, text="Codigo de Barra")
    inputCodigoBarra = tk.Entry(contenedorFormulario)
    inputCodigoBarra.insert(0, ProductoSelecionado.codigoBarra)
    labelCodigoBarra.grid(row=4, column=0)
    inputCodigoBarra.grid(row=4, column=1)

    contenedorBotones = tk.Frame(ventanaEditar)
    contenedorBotones.pack()

    def aceptar_edicion():
        nombre = inputNombre.get()
        precio = inputPrecio.get()
        stock = inputStock.get()
        categoria = inputCategoria.get()
        codigoBarra = inputCodigoBarra.get()

        if not validar_nombre(nombre):
            return

        if not validar_precio(precio):
            return

        if not validar_stock(stock):
            return

        if not validar_categoria(categoria):
            return

        if not validar_codigoBarra(codigoBarra):
            return

        for p in Producto.productos:
            if p != ProductoSelecionado and p.getCodigoBarra().strip() == codigoBarra.strip():
                messagebox.showerror(
                    "Código duplicado",
                    f"El código '{codigoBarra}' ya pertenece al producto: {p.getNombre()}",
                    parent=ventanaEditar
                )
                return

        precio = float(precio)
        stock = int(stock)

        ProductoSelecionado.setNombre(nombre)
        ProductoSelecionado.setPrecio(precio)
        ProductoSelecionado.setStock(stock)
        ProductoSelecionado.setCategoria(categoria)
        ProductoSelecionado.setCodigoBarra(codigoBarra)

        if stock == 0:
            estado = "Sin stock"
        elif stock <= 5:
            estado = "Stock bajo"
        else:
            estado = "Disponible"

        tabla.item(
            idProducto,
            values=(
                nombre,
                precio,
                stock,
                categoria,
                codigoBarra,
                estado
            )
        )

        messagebox.showinfo(
            "Éxito",
            "Producto editado correctamente",
            parent=ventanaEditar
        )

        ventanaEditar.destroy()

    botonEditar = tk.Button(
        contenedorBotones,
        text="Aceptar",
        command=aceptar_edicion
    )

    botonCancelar = tk.Button(
        contenedorBotones,
        text="Cancelar",
        command=ventanaEditar.destroy
    )

    botonEditar.pack(side="left")
    botonCancelar.pack(side="left")
