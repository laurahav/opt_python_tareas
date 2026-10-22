# Contador de vocales: Pide una frase y cuenta cuántas vocales contiene.
print("CONTADOR DE VOCALES")
print("-------------------")

s = input("Introduce una frase: ")
vocales = 0
for i in s.lower():
    if i in ("a", "e", "i", "o", "u"):
        vocales += 1

print("En la frase \"", s, "\", hay", vocales, "vocales.")