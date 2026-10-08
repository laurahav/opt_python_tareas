# Implementa un programa que valide si una contraseña ingresada coincide con la almacenada.

contAlmacenada = "password"

contIntroducida = input("Para acceder al sitio debe introducir la contraseña: ")

if contAlmacenada == contIntroducida:
    print("Contraseña correcta, accediendo al sitio web...")
else:
    print("Contraseña incorrecta, sitio web bloqueado...")