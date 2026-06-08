# Sistema de Registro Escolar en Python

Proyecto desarrollado en Python utilizando Programación Orientada a Objetos (POO) para registrar, buscar y analizar información de estudiantes.

## Descripción
Este sistema permite:

- Registrar más de un estudiante.
- Guardar nombre completo, curso, notas, apoderado, contacto, faltas y anotaciones.
- Buscar estudiantes por nombre completo y curso.
- Mostrar toda la información registrada.
- Calcular el promedio de notas.
- Evaluar riesgo académico y riesgo por faltas/anotaciones negativas.

## Funcionalidades
### 1. Registro de estudiantes
Se puede registrar:
- Nombre completo
- Curso
- Notas
- Nombre del apoderado
- Contacto del apoderado (teléfono, correo o ambos)
- Número de faltas
- Anotaciones positivas
- Anotaciones negativas

### 2. Búsqueda precisa
La búsqueda se realiza usando:
- Nombre completo
- Curso

El sistema muestra todos los datos del estudiante encontrado.

### 3. Evaluación de riesgo
Se consideran los siguientes criterios:

- **Riesgo académico:** promedio de notas menor a 4.0
- **Riesgo por faltas/anotaciones negativas:**  
  - 8 o más faltas, o
  - 3 o más anotaciones negativas

### Mensajes de riesgo
- **Riesgo académico.**
- **Riesgo por faltas/anotaciones negativas.**
- **Riesgo académico y riesgo por faltas/anotaciones negativas.**
- **No presenta riesgo.**

## Conceptos de POO utilizados
- **Encapsulamiento:** atributos protegidos con propiedades.
- **Herencia:** la clase `Estudiante` hereda de `Persona`.
- **Abstracción:** `Persona` es una clase abstracta.
- **Polimorfismo:** el método `mostrar_informacion()` se implementa en la clase hija.

## Estructura del proyecto
```bash
📁 proyecto-registro-escolar
 ┣ 📄 main.py
 ┣ 📄 README.md
