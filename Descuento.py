print("Ingrese el valor de la compra")
valor_Compra = float(input())
descuento = valor_Compra*0.07
valorPagar = valor_Compra - descuento
if valor_Compra > 100:

    print("Tiene un descuento de; ", descuento)
else:
    print("No tiene descuento")
print("El valor a pagar es de: ", valor_Compra)
