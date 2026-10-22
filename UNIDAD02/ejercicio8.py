# Suma de dígitos: Pide un número entero y calcula la suma de sus dígitos (ej: 123 → 6).

num = int(input("Introduce un número entero: "))
suma = 0

for i in str(num):
    suma += int(i)

print("La suma de los dígitos de", num, "es", suma)