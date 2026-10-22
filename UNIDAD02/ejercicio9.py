# Juego de adivinanza: El programa “piensa” un número (por ejemplo 7) y
# el usuario tiene que adivinarlo. Indica si el número es mayor o menor hasta acertar.
import numpy as np

numero_secreto = np.random.randint(1,101)

numero_introducido = int(input('Introduce un número:'))

while numero_introducido != numero_secreto:
    if(numero_introducido < numero_secreto):
        numero_introducido = int(input("El número secreto es mayor. Vuelve a intentarlo: "))
    else:
        numero_introducido = int(input("El número secreto es menor. Vuelve a intentarlo: "))

print("Enhorabuena, has adivinado el número secreto.")