# Proyecto POO - Semanas 1, 2 y 3

## Descripción

Este proyecto integra los conocimientos desarrollados durante las semanas 1, 2 y 3 de Programación Orientada a Objetos (POO) utilizando Python.

Durante el proyecto se aplican los conceptos de clases, objetos, encapsulación, herencia, composición, clases abstractas, sobrescritura de métodos y polimorfismo.

## Organización del código

El proyecto está organizado en los siguientes archivos:

- `semana1.py`: contiene la clase `Estudiante`. Se aplican conceptos de clases, objetos y encapsulación mediante atributos privados y métodos getters y setters. También contiene el método para calcular el promedio.

- `semana2.py`: contiene las clases `Universidad` y `EstudianteUniversitario`. `EstudianteUniversitario` hereda de `Estudiante` y utiliza composición con la clase `Universidad`.

- `semana3.py`: contiene la clase abstracta `Cliente` y las clases `ClienteMayorista` y `ClienteMinorista`. Ambas clases heredan de `Cliente` y sobrescriben el método `calcularDescuento()` con diferentes porcentajes.

- `main.py`: contiene la ejecución principal del programa. Solicita los datos del estudiante, crea los objetos, calcula el promedio y determina el descuento correspondiente.

## Funcionamiento del programa

Al ejecutar `main.py`, el programa solicita el nombre del estudiante, la universidad y tres notas.

Con los datos ingresados se crea un objeto de tipo `EstudianteUniversitario`, que hereda de `Estudiante` y se relaciona mediante composición con un objeto de tipo `Universidad`.

El programa calcula el promedio de las tres notas.

Si el promedio es mayor a 7, el estudiante aprueba y se utiliza un objeto `ClienteMayorista`, que aplica un descuento del 15%.

Si el promedio es menor o igual a 7, el estudiante reprueba y se utiliza un objeto `ClienteMinorista`, que aplica un descuento del 5%.

El precio establecido para la universidad es de $172.

## Cálculo de descuentos

Para los estudiantes que aprueban:

- Precio: $172
- Descuento: 15%
- Descuento aplicado: $25.80
- Precio final: $146.20

Para los estudiantes que reprueban:

- Precio: $172
- Descuento: 5%
- Descuento aplicado: $8.60
- Precio final: $163.40

## Validación de datos

Las notas ingresadas por el usuario se validan para asegurar que estén dentro del rango de 0 a 10.

Si se ingresa una nota menor que 0 o mayor que 10, el programa muestra un mensaje y solicita nuevamente el valor.

Las notas se convierten a valores numéricos mediante `float` para poder realizar el cálculo del promedio.

## Polimorfismo

El polimorfismo se aplica mediante la clase abstracta `Cliente`.

Las clases `ClienteMayorista` y `ClienteMinorista` sobrescriben el método `calcularDescuento()` y utilizan una lógica diferente para calcular el descuento.

El programa puede trabajar con ambos tipos de cliente mediante la misma referencia `cliente`, sin necesitar diferentes instrucciones para calcular el descuento.

## Clase abstracta

La clase `Cliente` es una clase abstracta que establece el método `calcularDescuento()`.

Las clases `ClienteMayorista` y `ClienteMinorista` heredan de `Cliente` y proporcionan su propia implementación del método.

## Librerías

El proyecto no utiliza librerías externas. Se utiliza el módulo `abc`, que forma parte de la biblioteca estándar de Python, para implementar la clase abstracta.

## Ejecución

Para ejecutar el proyecto se debe ejecutar el archivo:

`main.py`
