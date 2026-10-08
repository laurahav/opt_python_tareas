# Elabora un algoritmo en pseudocódigo que calcule el promedio de tres notas y muestre si el estudiante aprueba.

n1 = float(input("Introduce la primera nota: "))
n2 = float(input("Introduce la segunda nota: "))
n3 = float(input("Introduce la tercera nota: "))

media = (n1 + n2 + n3)/3

if media >= 5:
    print("¡ENHORABUENA! Has aprobado la asignatura con una nota de ", round(media, 2), ".")
else:
    print("Has suspendido la asignatura con una nota de ", round(media, 2), ". ¡Debes estudiar más!")