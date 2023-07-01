#A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.

def saludar(nombre):
    mensaje = "Hola " + nombre + ", ¿Qué tal?"
    print(mensaje)

nombres = ["Ana", "Juan", "María", "Pedro", "Lucía", "Carlos", "Sofía", "Jorge", "Marta",]

for i in range(len(nombres)):
    if i == 3 or i == 6:
        print("")
    saludar(nombres[i])

print("Fin del programa")