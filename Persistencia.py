import json
from semana5 import Producto


class ProductoRepository:

    def __init__(self, archivo="productos.json"):
        self.archivo = archivo

    def guardar(self, catalogo):

        datos = []

        for producto in catalogo.productos:
            datos.append({
                "id": producto.get_id(),
                "nombre": producto.get_nombre(),
                "precio": producto.get_precio(),
                "categoria": producto.get_categoria()
            })

        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar(self, catalogo):

        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            for dato in datos:
                producto = Producto(
                    dato["id"],
                    dato["nombre"],
                    dato["precio"],
                    dato["categoria"]
                )

                catalogo.agregar(producto)

        except FileNotFoundError:
            print("No existe un archivo de productos todavía.")

        except json.JSONDecodeError:
            print("El archivo de productos tiene un formato incorrecto.")
