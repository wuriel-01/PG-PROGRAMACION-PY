
class Producto:
    productos = []

    def __init__(self, nombre, precio, stock, descripcion, categoria, id_producto, codigoBarra):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.categoria = categoria
        self.id_producto = id_producto
        self.codigoBarra = codigoBarra

        Producto.productos.append(self)

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getStock(self):
        return self.stock

    def getDescripcion(self):
        return self.descripcion

    def getCategoria(self):
        return self.categoria

    def getId(self):
        return self.id_producto

    def getCodigoBarra(self):
        return self.codigoBarra

    def getValorStock(self):
        return self.precio * self.stock

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def setStock(self, nuevoStock):
        self.stock = nuevoStock

    def setDescripcion(self, nuevaDescripcion):
        self.descripcion = nuevaDescripcion

    def setCategoria(self, nuevaCategoria):
        self.categoria = nuevaCategoria

    def setCodigoBarra(self, nuevoCodigoBarra):
        self.codigoBarra = nuevoCodigoBarra
