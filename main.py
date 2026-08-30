from semana2 import Universidad, EstudianteUniversitario
from semana3 import ClienteMayorista, ClienteMinorista

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

estudiante1 = EstudianteUniversitari(
    nombre,
    nota1,
    nota2,
    nota3,
    universidad1
)

promedio = estudiante1.calcular_promedio()

if promedio > 7:
    cliente = ClienteMayorista()
    estado = "Aprobaste"
else:
    cliente = ClienteMinorista()
    estado = "Reprobaste"


precio = 172

descuento = cliente.calcularDescuento(precio)
precio_final = precio - descuento

print("Resultado")
print("Nombre:", estudiante1.get_nombre())
print("Universidad:", universidad1.get_nombre())
print("Nota 1:", estudiante1.get_nota1())
print("Nota 2:", estudiante1.get_nota2())
print("Nota 3:", estudiante1.get_nota3())
print("Promedio:", promedio)
print("Estado:", estado)
print("Precio universidad: $", precio)
print("Descuento: $", descuento)
print("Precio final: $", precio_final)
