from tkinter import messagebox
def validar_nombre(nombre):
    nombre=nombre.strip()

    if nombre == "":
        messagebox.showerror("Error", "El nombre no puede estar vacío")
        return False

    elif len(nombre) > 20:
        messagebox.showerror("Error", "El nombre no puede contener más de 20 caracteres")
        return False

    elif len(nombre) < 3:
        messagebox.showerror("Error", "El nombre debe tener al menos 3 caracteres")
        return False

    else:
        return True


def validar_precio (precio):
    try:
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "El precio debe ser numérico")
        return False

    if precio <= 0:
        messagebox.showerror("Error", "El precio debe ser mayor que cero")
        return False

    elif precio > 10000000:
        messagebox.showerror("Error", "El precio no puede superar los $10.000.000")
        return False
    
    else:
        return True


def validar_stock (stock):
    try:
        stock= int(stock)
    except ValueError:
            messagebox.showerror("Error", "El stock debe ser numérico")
            return False

    if stock < 0 :
        messagebox.showerror("Error", "El stock debe ser mayor/igual que cero")
        return False 

    elif stock > 100000:
        messagebox.showerror("Error", "El stock no puede superar las 100.000 unidades")
        return False

    else:
        return True


def validar_codigoBarra(codigoBarra):
    if codigoBarra == "":
        messagebox.showerror("Error", "El código de barras no puede estar vacío")
        return False

    elif not codigoBarra.isdigit():
        messagebox.showerror("Error", "El código de barras debe contener solamente números")
        return False

    elif len(codigoBarra) != 13:
        messagebox.showerror("Error", "El código de barras debe contener 13 dígitos")
        return False

    else:
        return True


def validar_categoria(categoria):
    if categoria=="":
        messagebox.showerror("Error", "La categoria no puede estar vacío")
        return False

    elif len(categoria) <3 or len(categoria)>20:
        messagebox.showerror("Error", "La categoria debe contener entre 3 y 20 caracteres")
        return False 

    else: 
        return True
