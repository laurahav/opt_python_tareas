# Conversor de segundos: Pide una cantidad de segundos y conviértela a horas, minutos y segundos

segundos = int(input("Introduce la cantidad de segundos que quieres convertir: "))

if segundos > 60:
    minutos = int(segundos / 60)
    segundos = segundos % 60
    if minutos > 60:
        horas = int(minutos / 60)
        minutos = minutos % 60

print("Son", horas, "horas,", minutos, "minutos y", segundos, "segundos.")