# Proyecto de Programación Orientada a Objetos

## Nombre del estudiante

Fernando Ramirez Almeida

## Descripción

Este proyecto fue desarrollado en Python con el objetivo de aplicar los principales conceptos de la Programación Orientada a Objetos (POO) aprendidos durante las semanas 1, 2 3, 5, 6 y 7.

El programa permite ingresar los datos de un estudiante, su universidad y tres notas. Luego calcula el promedio, determina si el estudiante aprobó o reprobó y aplica un descuento dependiendo del tipo de cliente.

## Objetivo

Aplicar los conceptos de Programación Orientada a Objetos mediante un programa desarrollado en Python, utilizando clases, objetos, encapsulación, herencia, composición, abstracción y polimorfismo.

## Organización del proyecto

El proyecto está dividido en los siguientes archivos:

- `main.py`: Archivo principal que ejecuta el programa.
- `semana1.py`: Contiene la clase `Estudiante` y aplica encapsulación.
- `semana2.py`: Contiene las clases `Universidad` y `EstudianteUniversitario`, aplicando herencia y composición.
- `semana3.py`: Contiene la clase abstracta `Cliente` y las clases `ClienteMayorista` y `ClienteMinorista`, aplicando abstracción y polimorfismo.
- `semana5.py`: Contiene las clases `Producto` y `Catalogo`, utilizando List, Dict y Set para administrar los productos.
- `semana6.py`: Contiene la interfaz gráfica desarrollada con Flet y el manejo de eventos.
- `semana7.py`: Contiene una cola de atención al cliente, el patrón Repository y pruebas unitarias utilizando pytest.

## Principales funcionalidades

- Ingreso del nombre del estudiante.
- Ingreso de la universidad.
- Ingreso de tres notas.
- Validación de las notas entre 0 y 10.
- Cálculo del promedio.
- Determinación del estado del estudiante.
- Aplicación de descuentos según el tipo de cliente.
- Demostración de abstracción.
- Demostración de herencia.
- Demostración de composición.
- Demostración de polimorfismo.

## Conceptos de POO utilizados

### Encapsulación

La clase `Estudiante` utiliza atributos privados para proteger la información del estudiante. Para acceder y modificar estos atributos se utilizan métodos `get` y `set`.

### Herencia

La clase `EstudianteUniversitario` hereda de la clase `Estudiante`, permitiendo reutilizar sus atributos y métodos.

### Composición

La clase `EstudianteUniversitario` contiene un objeto de tipo `Universidad`, estableciendo una relación entre ambas clases.

### Abstracción

La clase `Cliente` es una clase abstracta que define el método `calcularDescuento`.

### Polimorfismo

Las clases `ClienteMayorista` y `ClienteMinorista` implementan el mismo método `calcularDescuento`, pero cada una tiene un comportamiento diferente.

El cliente mayorista obtiene un descuento del 15%, mientras que el cliente minorista obtiene un descuento del 5%.

## Cálculo de descuentos

El programa utiliza un precio de $172.

### Cliente mayorista

Descuento del 15%:

$172 × 0.15 = $25.80

Precio final:

$172 - $25.80 = $146.20

### Cliente minorista

Descuento del 5%:

$172 × 0.05 = $8.60

Precio final:

$172 - $8.60 = $163.40

## Validación

El programa valida que las notas ingresadas estén entre 0 y 10.

Si el usuario ingresa una nota fuera de este rango, el programa solicita nuevamente la nota.

## Ejecución

Para ejecutar el proyecto se debe abrir el archivo `main.py` y seleccionar:

**Run → Run Without Debugging**

El programa solicitará el nombre, universidad y las tres notas.

## Evidencias de pruebas

### Prueba 1: Estudiante aprobado

Datos utilizados:

- Nombre: Fernando
- Universidad: UEES
- Nota 1: 9
- Nota 2: 8
- Nota 3: 9

Promedio: 8.67

Resultado: Aprobaste

Tipo de cliente: Mayorista

Descuento: 15%

Precio final: $146.20

### Prueba 2: Estudiante reprobado

Datos utilizados:

- Nombre: Fernando
- Universidad: UEES
- Nota 1: 6
- Nota 2: 7
- Nota 3: 3

Promedio: 5.33

Resultado: Reprobaste

Tipo de cliente: Minorista

Descuento: 5%

Precio final: $163.40

### Demostración del polimorfismo

El polimorfismo se demuestra mediante el método `calcularDescuento`.

Cuando el objeto es de tipo `ClienteMayorista`, se aplica un descuento del 15%.

Cuando el objeto es de tipo `ClienteMinorista`, se aplica un descuento del 5%.

Aunque se utiliza el mismo método, el comportamiento cambia dependiendo del objeto.

## Semana 5: Colecciones y CRUD

En la semana 5 se desarrolló un catálogo de productos utilizando Python.

Cada producto contiene:

- ID
- Nombre
- Precio
- Categoría

La clase `Catalogo` permite realizar las siguientes operaciones:

- Agregar productos.
- Buscar productos.
- Listar productos.
- Actualizar productos.
- Eliminar productos.

### Colecciones utilizadas

Se utilizaron tres tipos de colecciones:

- **List:** se utiliza para almacenar los productos.
- **Dict:** se utiliza para buscar los productos mediante su ID.
- **Set:** se utiliza para almacenar los IDs y evitar productos duplicados.

### Validación

El programa verifica que no se pueda agregar más de un producto con el mismo ID.

## Semana 6: Interfaz gráfica y manejo de eventos

En la semana 6 se desarrolló una interfaz gráfica utilizando la librería Flet.

La interfaz permite ingresar:

- ID del producto.
- Nombre.
- Precio.
- Categoría.

También contiene un botón para agregar productos al catálogo.

### Manejo de eventos

El botón "Agregar producto" utiliza el evento `on_click` para ejecutar la función correspondiente cuando el usuario presiona el botón.

La función obtiene los datos ingresados, valida la información y agrega el producto al catálogo.

### Validación de datos

La interfaz verifica que:

- El ID sea un número.
- El precio sea un número.
- El nombre no esté vacío.
- La categoría no esté vacía.
- No exista otro producto con el mismo ID.

Si los datos son incorrectos, se muestra un mensaje de error.

Si el producto se agrega correctamente, se muestra un mensaje de confirmación.

## Semana 7: Cola, Repository y pruebas unitarias

En la semana 7 se desarrolló una aplicación de consola para administrar una cola de atención al cliente.

La cola utiliza el principio FIFO (First In, First Out), lo que significa que el primer cliente que ingresa es el primero en ser atendido.

### Clase Cliente

La clase `Cliente` representa a cada cliente que ingresa a la cola.

Cada cliente contiene:

- Nombre.

### Clase Cola

La clase `Cola` implementa manualmente la estructura de datos de una cola.

La clase permite realizar las siguientes operaciones:

- Agregar elementos.
- Eliminar elementos.
- Consultar el siguiente elemento.
- Verificar si la cola está vacía.
- Contar la cantidad de elementos.

La cola se implementa utilizando una lista de Python.

### Patrón Repository

Se implementó la clase `ClienteRepository` para separar la administración de los clientes de la lógica principal del programa.

El Repository permite realizar las siguientes operaciones:

- Agregar clientes.
- Obtener el siguiente cliente.
- Atender clientes.
- Consultar la cantidad de clientes.
- Verificar si la cola está vacía.

### Menú de la aplicación

El programa contiene las siguientes opciones:

1. Agregar cliente.
2. Ver siguiente cliente.
3. Atender cliente.
4. Ver cantidad de clientes.
5. Verificar si la cola está vacía.
6. Salir.

### Pruebas unitarias

Para comprobar el funcionamiento del programa se utilizó la librería `pytest`.

Se implementaron cinco pruebas unitarias:

- Prueba para agregar un cliente.
- Prueba para obtener el siguiente cliente.
- Prueba para atender un cliente.
- Prueba para verificar si la cola está vacía.
- Prueba para comprobar la cantidad de clientes.

Las pruebas se ejecutan mediante el siguiente comando:

```bash
pytest semana7.py
