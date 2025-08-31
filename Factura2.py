print("Ingrese su Nombre: ")
NOMBRE = input()
print("Ingrese su Dirección: ")
DIRECCION = input()
print("Ingrese su Nit: ")
NIT = input()

# Listas para almacenar datos
productos = []
cantidades = []
precios = []
ivas = []
totales = []


# Ingreso de 10 productos
for i in range(1, 11):
    print(f"\nProducto {i}:")
    nombre_prod = input("Ingrese nombre del producto: ")
    cantidad = int(input("Ingrese cantidad: "))
    precio = float(input("Ingrese precio unitario: "))

    iva = precio * cantidad * 0.19
    total = precio * cantidad + iva

    productos.append(nombre_prod)
    cantidades.append(cantidad)
    precios.append(precio)
    ivas.append(iva)
    totales.append(total)

    # Encabezado
print("*" * 90)
print("-------------------------Bienvenido a la Facturación Electrónica--------------------------")
print("*                                                                                        *")
print("-" * 90)
print("NOMBRE :", NOMBRE)
print("DIRECCIÓN :", DIRECCION)
print("NIT :", NIT)
print("-" * 90)
print("*" * 90)

# Mostrar tabla de productos
print("\n" + "-" * 90)
print(f"{'Producto':20} {'Cantidad':10} {'Precio':10} {'IVA(19%)':12} {'Total':12}")
print("-" * 90)


for i in range(10):
    print(
        f"{productos[i]:20} {cantidades[i]:10} {precios[i]:10.2f} {ivas[i]:12.2f} {totales[i]:12.2f}")

# Cálculos finales
subtotal = sum(precios[i] * cantidades[i] for i in range(10))
total_iva = sum(ivas)
total_factura = sum(totales)

print("-" * 90)
print(f"{'Subtotal:':>55} {subtotal:12.2f}")
print(f"{'IVA total:':>55} {total_iva:12.2f}")
print(f"{'TOTAL FACTURA:':>55} {total_factura:12.2f}")
print("-" * 90)
