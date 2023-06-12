#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

contador_mujeres = 0
contador_varones = 0
contador_mayores = 0
contador_menores = 0

for i in range(15):
    edad = int(input(f"Ingrese su edad {i+1}: "))
    sexo = input(f"Ingrese su sexo (M/F) {i+1}: ")

    if sexo == "M" or sexo == "m":
        contador_varones += 1
    elif sexo == "F" or sexo == "f":
        contador_mujeres += 1

    if edad >= 18:
        contador_mayores += 1
    elif edad < 18:
        contador_menores += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de mayores de edad:", contador_mayores)
print("Cantidad de menores de edad:", contador_menores)
print("Fin del programa")
