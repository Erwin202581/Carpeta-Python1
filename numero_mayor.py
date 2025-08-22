"""Mayor de dos números: Encontrar e imprimir el mayor de dos números"""

print("Escriba un número")
Num1 = int(input())
print("Escriba un segundo número")
Num2 = int(input())
if Num1 > Num2:
    print("El primer número es mayor que el segundo.", Num1)
elif Num1 < Num2:
    print("El segundo número es mayor que el primero.", Num2)
else:
    print("Los dos números son iguales.")
