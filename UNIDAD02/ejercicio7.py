# Detectar número negativo: Pide números al usuario hasta que introduzca uno negativo.
# Muestra cuántos números positivos ha introducido.
num = int(input("Introduce un número: "))
cont = 1
while num > 0:
    num = int(input("Introduce un número: "))
    if(num > 0):
        cont += 1

print("Ha introducido", cont, "números pares.")

