# Contador de letras: Pide una palabra y muestra cuántas letras tiene (sin usar funciones avanzadas).

palabra = input("Introduce una palabra: ")
cont = 0

for letra in palabra:
    cont += 1

print("La palabra", palabra, "tiene" ,cont, "letras.")