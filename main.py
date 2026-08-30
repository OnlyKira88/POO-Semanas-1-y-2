from semana2 import Universidad, EstudianteUniversitario

nombre = input("Nombre: ")
universidad = input("Universidad: ")

nota1 = float(input("Nota 1 (0-10): "))
while nota1 < 0 or nota1 > 10:
    print("La nota debe estar entre 0 y 10.")
    nota1 = float(input("Nota 1 (0-10): "))

nota2 = float(input("Nota 2 (0-10): "))
while nota2 < 0 or nota2 > 10:
    print("La nota debe estar entre 0 y 10.")
    nota2 = float(input("Nota 2 (0-10): "))

nota3 = float(input("Nota 3 (0-10): "))
while nota3 < 0 or nota3 > 10:
    print("La nota debe estar entre 0 y 10.")
    nota3 = float(input("Nota 3 (0-10): "))

universidad1 = Universidad(universidad)

estudiante1 = EstudianteUniversitario(
    nombre,
    nota1,
    nota2,
    nota3,
    universidad1
)
estudiante1.mostrar_informacion()
