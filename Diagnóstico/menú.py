from Personaa import Persona
from Profesionn import Profesion, obtener_porcentaje

profesiones = {
        "Ingeniero": Profesion("Ingeniero"),
        "Abogado": Profesion("Abogado"),
        "Otra": Profesion("Otra")
}

continuar = True
while continuar:
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona (mayor a 0): "))
    while edad == 0:
        edad = int(input("Ingrese una edad válida (mayor a 0): "))
    sexo = input("Ingrese el sexo de la persona (Masculino/Femenino): ").capitalize()
    while sexo not in ["Masculino", "Femenino"]:
        sexo = input("Ingrese un sexo válido (Masculino/Femenino): ").capitalize()
    profesion = input("Ingrese la profesión de la persona (Ingeniero/Abogado/Otra): ").capitalize()
    while profesion not in ["Ingeniero", "Abogado", "Otra"]:
        profesion = input("Ingrese una profesión válida (Ingeniero/Abogado/Otra): ").capitalize()
    sueldo = float(input("Ingrese el sueldo de la persona: "))

    profesiones[profesion].agregar_persona(sueldo)

    continuar_respuesta = input("¿Desea continuar con otra persona? (Si/No): ").capitalize()
    continuar = continuar_respuesta == "Si"

total_personas = sum(profesion.cantidad_personas for profesion in profesiones.values())

print("\nResultados:")
for profesion in profesiones.values():
    porcentaje = obtener_porcentaje(total_personas, profesion.cantidad_personas)
    promedio_sueldo = profesion.sueldo_total / profesion.cantidad_personas if profesion.cantidad_personas > 0 else 0
    print(f"{profesion.nombre}: {porcentaje:.2f}% ({promedio_sueldo:.2f} sueldo promedio)")