from semana2 import Universidad, EstudianteUniversitario


nombre = input("Nombre: ")
universidad = input("Universidad: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))


universidad1 = Universidad(universidad)

estudiante1 = EstudianteUniversitario(
    nombre,
    nota1,
    nota2,
    nota3,
    universidad1
)

estudiante1.mostrar_informacion()
