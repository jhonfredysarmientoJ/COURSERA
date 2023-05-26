nombre_mayores = []
nombre_menores = []
 
edad_mayores = []
edad_menores = []
 
contador = 0
 
 
def agregar():
    global contador
    print("Ingrese los siguientes datos")
    nombre = input("Nombre > ")
    edad = int(input("Edad > "))
 
    contador += 1
 
    if edad >= 18:
        nombre_mayores.append(nombre)
        edad_mayores.append(edad)
    else:
        nombre_menores.append(nombre)
        edad_menores.append(edad)
 
def mostrar():
    print("1- Alumnos mayores")
    print("2- Alumnos menores")
 
    opcion = int(input("> "))
 
    if opcion == 1:
        print("Lista de alumnos mayores de edad")
        for a,b in zip(nombre_mayores, edad_mayores):
            print(f"Alumno: {a} de una edad de: {b}")
    elif opcion == 2:
        print("Lista de alumnos menores de edad")
        for a,b in zip(nombre_menores, edad_menores):
            print(f"Alumno: {a} de una edad de: {b}")
 
 
while True:
    print(
"""
Seleccione una opcion:
1- Agregar estudiante
2- Mostrar estudiantes
3- Mostrar el numero de registros realizados
0- salir
""")
 
    opcion = int(input("> "))
 
    if opcion == 1:
        agregar()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        print(f"Hoy se realizaron {contador} registros")
    elif opcion == 0:
        break