
import tkinter as tk
from Modelos.Productos import Producto


def abrir_formulario_edicion(idProducto, tabla):
    ProductoSelecionado = None

    for producto in Producto.productos:
        if producto.id_producto == idProducto:
            ProductoSelecionado = producto
            break
        
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
        precio = float(inputPrecio.get())
        stock = int(inputStock.get())
        categoria = inputCategoria.get()
        codigoBarra = inputCodigoBarra.get()

        ProductoSelecionado.setNombre(nombre)
        ProductoSelecionado.setPrecio(precio)
        ProductoSelecionado.setStock(stock)
        ProductoSelecionado.setCategoria(categoria)
        ProductoSelecionado.setCodigoBarra(codigoBarra)

        tabla.item(
            idProducto,
            values=(
                nombre,
                precio,
                stock,
                categoria,
                codigoBarra
            )
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
