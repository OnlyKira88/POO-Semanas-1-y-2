# Proyecto POO - Semanas 1 y 2

## Descripción

Este proyecto integra los conocimientos desarrollados durante las semanas 1 y 2 de Programación Orientada a Objetos (POO). Se implementaron clases, objetos, encapsulación, herencia y composición utilizando Python.

## Organización del código

El proyecto está organizado en tres archivos:

- `semana1.py`: contiene la clase `Estudiante`, donde se aplica encapsulación mediante atributos privados, getters y setters, además del método para calcular el promedio.
- `semana2.py`: contiene las clases `Universidad` y `EstudianteUniversitario`. La clase `EstudianteUniversitario` hereda de `Estudiante` y utiliza composición con la clase `Universidad`.
- `main.py`: contiene la ejecución principal del programa. Solicita los datos al usuario, crea los objetos y muestra los resultados.

## Funcionamiento del programa

Al ejecutar `main.py`, el programa solicita al usuario su nombre, universidad y tres notas.

Con estos datos se crean los objetos correspondientes. Luego se calcula el promedio de las tres notas y se muestran el nombre del estudiante, la universidad, las notas, el promedio y el estado final.

Si el promedio es mayor a 7, el programa muestra "Aprobaste". En caso contrario, muestra "Reprobaste".

## Validación de datos

Actualmente el programa solicita las notas mediante valores numéricos utilizando `float`. Las notas se utilizan para calcular el promedio y determinar si el estudiante aprobó o reprobó.

## Programación Orientada a Objetos

En el proyecto se aplican los siguientes conceptos:

- Clases y objetos.
- Encapsulación mediante atributos privados.
- Getters y setters.
- Herencia.
- Composición.

## Librerías

El proyecto no utiliza librerías externas. Se utilizan únicamente las funcionalidades básicas de Python.

## Ejecución

Para ejecutar el proyecto se debe ejecutar el archivo:

`main.py`
