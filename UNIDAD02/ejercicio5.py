# Simulador de cajero automático: Empieza con un saldo de 1000€.
# Permite al usuario retirar dinero hasta que decida salir o no tenga saldo suficiente.

def mostrar_menu():
    print("CAJERO AUTOMÁTICO")
    print("-----------------")
    print("1. Retirar dinero.")
    print("2. Consultar saldo disponible.")
    print("3. SALIR")
    opcion = int(input("Elige una opción: "))

    return opcion

saldo = 1000
opcion = mostrar_menu()

while opcion != 3:
    if opcion == 1:
        retirada = int(input("¿Cuánto dinero quieres retirar? "))
        if saldo >= retirada:
            saldo -= retirada
        else:
            print("No tienes saldo suficiente para hacer esa retirada.")
        print("El saldo restante es de ",saldo, "€")
    elif opcion == 2:
        print("Su saldo actual es de",saldo, "€")
    else:
        print("Elige una opción válida.")
    if saldo > 0:
        opcion = mostrar_menu()
    else:
        opcion = 3