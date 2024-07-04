# APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
# Descripcion:
Aplicación de consola. Permite a veterinarios controlar integralmente
el estado de salud/bienestar de animales domesticos a traves de parametrizaciones de distintos
items a evaluar.


# OBJETIVO
Facilitar la tarea del veterinario en cada consulta, pudiendo ingresar nuevos pacientes, sus datos, consultar y modificar existentes, eliminar, buscar y listar segun necesidad, y adicionalmente presupuestar servicios ofreecidos. Se proporciona persistencia de datos mediante el uso de archivos de texto.


# PUBLICO OBJETIVO
Dirigido a profesionales del area Veterinaria en sus puestos de trabajo.


# REQUERIMIENTO FUNCIONAL
1. Funcionalidades Básicas
    - Buscar datos de la mascota (paciente) asociados a al DNI de su dueño.
    - Agregar: permite agregar mascotas a la base de datos.
    - Modificar: permite modificar datos ya cargados relacionados a la mascota o su dueño
    - Eliminar: permite dar de baja una mascota o el dueño y sus mascotas.
    - Listar: muestra un listado de mascotas de la base de datos
    - Presupuestar: permite que el profesional obtener un presupuesto de los servicios que ofrece la veterinaria


2. Persistencia de Datos
    - Almacenamiento en Archivos de Texto: Utilizar archivos de texto para guardar y recuperar todo dato ingresado
   
3. Interfaz de Usuario
    Los datos obtenidos se cargan al programa, pudiendo luego buscar, modificar,
    agregar, eliminar y listar segun necesidad, proporcionando persistencia de datos mediante el uso
    de archivos de texto.


4.  - Un menu principal permite seleccionar que tarea relizar.
    - Interfaz de Consola: el usuario puede interactuar introduciendo o eligiendo informacion a la cual acceder
5.  - Menú Principal: desde el cual el usuario pueda seleccionar las diferentes funcionalidades (Agregar,   Buscar, Modificar, Eliminar,       Listar, presupuestar).


4.  Validaciones de Datos
    - Entrada de Usuario: Se valida el ingreso de usuario con password
    - Gestión de Errores: tratamiento de gestion de errores posibles en el funcionamiento del programa


5.  Estructura del Código
    - Modularidad: Organiza el código en funciones y, si es necesario, en clases, para mejorar la legibilidad y mantenibilidad.
    - Funciones Principales: Crear funciones específicas para agregar, buscar, modificar, eliminar y listar términos.
    - Manejo de Archivos: Crear funciones para leer y escribir en los archivos de texto.
6.  Documentación
    - Comentarios en el Código: Incluir comentarios en el código para explicar el propósito y funcionamiento de las diferentes partes.
    - Archivo README: Proporcionar un archivo README que describa el propósito del proyecto, cómo ejecutarlo y cómo utilizar las               diferentes funcionalidades.
