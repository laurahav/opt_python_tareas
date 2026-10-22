# Número mayor de tres valores: Pide tres números y muestra cuál es el mayor.

num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))
num3 = int(input("Introduce el tercer número:"))


numeros = [num1, num2, num3]
numeros.sort()

print(numeros.pop())