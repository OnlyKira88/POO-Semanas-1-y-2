import flet as ft
from semana5 import Producto, Catalogo


def main(page: ft.Page):

    page.title = "Catálogo de Productos"
    page.scroll = "auto"

    catalogo = Catalogo()

    titulo = ft.Text("CATÁLOGO DE PRODUCTOS")

    campo_id = ft.TextField(label="ID del producto")
    campo_nombre = ft.TextField(label="Nombre")
    campo_precio = ft.TextField(label="Precio")
    campo_categoria = ft.TextField(label="Categoría")

    mensaje = ft.Text()
    lista_productos = ft.Column()

    def mostrar_productos():
        lista_productos.controls.clear()

        for producto in catalogo.productos:
            lista_productos.controls.append(
                ft.Text(
                    f"ID: {producto.get_id()} | "
                    f"Nombre: {producto.get_nombre()} | "
                    f"Precio: ${producto.get_precio()} | "
                    f"Categoría: {producto.get_categoria()}"
                )
            )

        page.update()

    def agregar_producto(e):

        try:
            id_producto = int(campo_id.value)
            nombre = campo_nombre.value.strip()
            precio = float(campo_precio.value)
            categoria = campo_categoria.value.strip()

            if nombre == "" or categoria == "":
                mensaje.value = "Complete todos los campos."
                page.update()
                return

            if id_producto in catalogo.ids:
                mensaje.value = f"Error: el ID {id_producto} ya existe."
                page.update()
                return

            producto = Producto(
                id_producto,
                nombre,
                precio,
                categoria
            )

            catalogo.agregar(producto)

            mensaje.value = "Producto agregado correctamente."

            limpiar_campos()
            mostrar_productos()

        except ValueError:
            mensaje.value = "ID y precio deben ser números."
            page.update()

    def buscar_producto(e):

        try:
            id_producto = int(campo_id.value)

            producto = catalogo.buscar(id_producto)

            if producto:
                campo_nombre.value = producto.get_nombre()
                campo_precio.value = str(producto.get_precio())
                campo_categoria.value = producto.get_categoria()

                mensaje.value = "Producto encontrado."
            else:
                mensaje.value = "Producto no encontrado."

            page.update()

        except ValueError:
            mensaje.value = "Ingrese un ID válido."
            page.update()

    def actualizar_producto(e):

        try:
            id_producto = int(campo_id.value)
            nombre = campo_nombre.value.strip()
            precio = float(campo_precio.value)
            categoria = campo_categoria.value.strip()

            if nombre == "" or categoria == "":
                mensaje.value = "Complete todos los campos."
                page.update()
                return

            producto = catalogo.buscar(id_producto)

            if producto is None:
                mensaje.value = "Producto no encontrado."
                page.update()
                return

            catalogo.actualizar(
                id_producto,
                nombre,
                precio,
                categoria
            )

            mensaje.value = "Producto actualizado correctamente."

            limpiar_campos()
            mostrar_productos()

        except ValueError:
            mensaje.value = "ID y precio deben ser números."
            page.update()

    def eliminar_producto(e):

        try:
            id_producto = int(campo_id.value)

            producto = catalogo.buscar(id_producto)

            if producto is None:
                mensaje.value = "Producto no encontrado."
                page.update()
                return

            catalogo.eliminar(id_producto)

            mensaje.value = "Producto eliminado correctamente."

            limpiar_campos()
            mostrar_productos()

        except ValueError:
            mensaje.value = "Ingrese un ID válido."
            page.update()

    def limpiar_campos():

        campo_id.value = ""
        campo_nombre.value = ""
        campo_precio.value = ""
        campo_categoria.value = ""

    boton_agregar = ft.ElevatedButton(
        text="Agregar producto",
        on_click=agregar_producto
    )

    boton_buscar = ft.ElevatedButton(
        text="Buscar producto",
        on_click=buscar_producto
    )

    boton_actualizar = ft.ElevatedButton(
        text="Actualizar producto",
        on_click=actualizar_producto
    )

    boton_eliminar = ft.ElevatedButton(
        text="Eliminar producto",
        on_click=eliminar_producto
    )

    page.add(
        titulo,
        campo_id,
        campo_nombre,
        campo_precio,
        campo_categoria,

        ft.Row(
            [
                boton_agregar,
                boton_buscar,
                boton_actualizar,
                boton_eliminar
            ]
        ),

        mensaje,

        ft.Divider(),

        ft.Text("Productos registrados:"),

        lista_productos
    )

ft.app(target=main)
