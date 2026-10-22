# Contar números pares en un rango: Pide dos números y muestra
# cuántos números pares hay entre ellos.

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if(num1 > num2):
    temp = num2
    num2 = num1
    num1 = temp

contador = 0
for i in range(num1 + 1, num2):
    if i % 2 == 0:
        contador += 1

print("Entre", num1, "y", num2, "hay", contador, "números pares.")
