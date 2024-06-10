# APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
# Descripcion:
El proyecto es una aplicación de consola. Permite a veterinarios controlar integralmente
el estado de salud/bienestar de animales domesticos a traves de parametrizaciones de distintos
items a evaluar.


# OBJETIVO
El objetivo es facilitar la tarea del veterinario en cada consulta, pudiendo ingresar nuevos datos, consultar y modificar existentes, eliminar, buscar y listar segun necesidad, proporcionando asi la persistencia de datos mediante el uso de archivos de texto. Un menu principal deriva a realizar estas tareas en el area correpondiente.


# PUBLICO OBJETIVO
Dirigido a profesionales del area Veterinaria en sus puestos de trabajo.


# REQUERIMIENTO FUNCIONAL (VER)
1. Funcionalidades Básicas
    - buscar ficha del paciente: permite busqueda x identificacion de la mascota
    - agregar: permite agregar datos sobre la evaluacion del paciente
    - Modificar: permite modificar datos ya cargados
    - Eliminar: permite quitar datos (hay que ver cuales)
    - Listar:permite mostrar opciones de tratamientos (VER) 
    - calcular: permite que el profesional calcular peso, altura, cant.de comida sugerida, cant de hs de movilidad, etc


2. Persistencia de Datos
    - Almacenamiento en Archivos de Texto: Utilizar archivos de texto para guardar y recuperar todo dato ingresado
   
3. Interfaz de Usuario
    Los datos obtenidos se cargan al programa, pudiendo luego buscar, modificar,
    agregar, eliminar y listar segun necesidad, proporcionando persistencia de datos mediante el uso
    de archivos de texto.


4.  - Un menu principal deriva a realizar estas tareas en el area correpondiente.
    - Interfaz de Consola: el usuario puede interactuar introduciendo o eligiendo informacion
5.  - Menú Principal: desde el cual el usuario pueda seleccionar las diferentes funcionalidades (Agregar,   Buscar, Modificar, Eliminar, Listar, calcular).


4.  Validaciones de Datos
    - Entrada de Usuario: validar ingreso del usuario
    - Gestión de Errores:


5.  Estructura del Código
    - Modularidad: Organizar el código en funciones y, si es necesario, en clases, para mejorar la legibilidad y mantenibilidad.
    - Funciones Principales: Crear funciones específicas para agregar, buscar, modificar, eliminar y listar términos.
    - Manejo de Archivos: Crear funciones para leer y escribir en los archivos de texto.
6.  Documentación
    - Comentarios en el Código: Incluir comentarios en el código para explicar el propósito y funcionamiento de las diferentes partes.
    - Archivo README: Proporcionar un archivo README que describa el propósito del proyecto, cómo ejecutarlo y cómo utilizar las diferentes funcionalidades.