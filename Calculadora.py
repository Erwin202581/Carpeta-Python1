"""CALCULADORA"""

print("Escriba el primer número")
num1 = float(input())
print("Escriba el segundo número")
num2 = float(input())
print("Escriba la operación deseada (+, -, *, /)")
operacion = input()

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    print("Operación no válida")

print("El resultado es:", resultado)
