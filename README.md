# Proyecto de Programación Orientada a Objetos

## Nombre del estudiante

Fernando Ramirez Almeida

## Descripción

Este proyecto fue desarrollado en Python con el objetivo de aplicar los principales conceptos de la Programación Orientada a Objetos (POO) aprendidos durante las semanas 1, 2, 3, 5, 6 y 7.

El proyecto contiene diferentes ejercicios en los que se aplican conceptos de POO, colecciones, interfaces gráficas, manejo de eventos, estructuras de datos abstractas, patrones de diseño y pruebas unitarias.

## Objetivo

Aplicar los conceptos de Programación Orientada a Objetos mediante programas desarrollados en Python, utilizando clases, objetos, encapsulación, herencia, composición, abstracción, polimorfismo, colecciones, interfaces gráficas, patrones de diseño y pruebas unitarias.

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
- Administración de productos mediante colecciones.
- Interfaz gráfica para el catálogo de productos.
- Manejo de eventos.
- Cola de atención al cliente.
- Patrón Repository.
- Pruebas unitarias con pytest.

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

Para ejecutar los programas se debe abrir el archivo correspondiente en Visual Studio Code y ejecutar el programa.

Para la semana 7 se debe ejecutar:

```bash
python semana7,py
