# Proyecto de Programación Orientada a Objetos

## Nombre del estudiante

Fernando Ramirez Almeida

## Descripción

Este proyecto fue desarrollado en Python con el objetivo de aplicar los principales conceptos de la Programación Orientada a Objetos (POO) aprendidos durante las semanas 1, 2 y 3.

El programa permite ingresar los datos de un estudiante, su universidad y tres notas. Luego calcula el promedio, determina si el estudiante aprobó o reprobó y aplica un descuento dependiendo del tipo de cliente.

## Objetivo

Aplicar los conceptos de Programación Orientada a Objetos mediante un programa desarrollado en Python, utilizando clases, objetos, encapsulación, herencia, composición, abstracción y polimorfismo.

## Organización del proyecto

El proyecto está dividido en los siguientes archivos:

- `main.py`: Archivo principal que ejecuta el programa.
- `semana1.py`: Contiene la clase `Estudiante` y aplica encapsulación.
- `semana2.py`: Contiene las clases `Universidad` y `EstudianteUniversitario`, aplicando herencia y composición.
- `semana3.py`: Contiene la clase abstracta `Cliente` y las clases `ClienteMayorista` y `ClienteMinorista`, aplicando abstracción y polimorfismo.

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

## Lenguaje utilizado

Python

## Librerías utilizadas

El proyecto utiliza la librería estándar `abc` de Python para implementar la clase abstracta.

No se utilizan librerías externas.

## Conclusión

Este proyecto permitió aplicar los principales conceptos de Programación Orientada a Objetos mediante un programa funcional desarrollado en Python.

Se utilizaron clases, objetos, encapsulación, herencia, composición, abstracción y polimorfismo.
