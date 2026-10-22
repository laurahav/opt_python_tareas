# Invertir un número: Pide un número entero y muestra su valor invertido (por ejemplo, 123 → 321).

numero = int(input("Introduce un número: "))
digitos = list(iter(str(numero)))
numero_invertido = ""

for i in digitos[::-1]:
    numero_invertido += str(i)

print("El número invertido es", numero_invertido)