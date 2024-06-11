""" APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
AUTORES: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 """


import os
import colorama
from colorama import Back,Fore,Style #dejo agregado esto x si usamos los estilos




def limpiar_Pantalla():
    """ 
    La funcion limpia la pantalla 
    Realiza un limpiado de caracteres en la terminal al invocar
    Parametros: 
    No espera
    Retorna: 
    No tiene
    AUTOR: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    COLABORADORES:
    """

    if os =="nt":
       os.system("cls")
    else:
       os.system("clear")

    




def menu():
    """
    La funcion menú
    Muestra en pantalla las diferentes opciones que se muestran al usuario
    Parametros: 
    No recibe
    Retorna: 
    Un valor entero para seleccion en el Match
    AUTOR: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    COLABORADORES:
    """
    limpiar_Pantalla()
    print(colorama.Fore.CYAN)
    print("="*70)
    print("\t 1. Agregar Paciente")
    print("\t 2. Listar")
    print("\t 3. Salir")
    op = int(input("Ingresa la Opción:  "))
    limpiar_Pantalla()
    return op


def listar(lista):
    """
    La Función da como retorno una un listado de los datos que se guardaron.
    Parametros: 
    Un dato en forma de lista y diccionarios.
    Retorna: 
    Muestra en pantalla. 
    AUTOR: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    COLABORADORES:
    """
    print("-"*70)
    #como es una lista veo primero que tiene adentro
    for paciente in lista:
    #como veo que tiene diccionarios, itero a los diccionarios con paciente.items()
        for dato, info in paciente.items():
            #como no me gusta que se vea Mascotas: []entre corchetes uso continue
            if dato == "Mascotas":
                continue
            print(f'{dato}: {info}')
        #Luego itero solamente la lista que da como resultado "Mascotas" y lo itero con
        #end="" para que quede mas prolijo
        for dato in paciente:
            if dato == "Mascotas":
                print("Mascotas: ", end="")
                for info in info:
                    print(f' {info}', end="")
                print()
    return


def agregar(paci):
    """
    Función agregar 
    La función agrega datos en seguidos imput's organizados los datos del paciente. 
    Parametros: 
    Datos ingresados de caracteres string y entero
    Retorna: 
    Dato en forma de lista empaquetada, que incluye por cada usuario un diccionario. 
    """

    masco = []
    print("-"*70)
    nomPaci = input("Ingrese el nombre:  ")
    apellPaci = input("Ingrese el apellido:  ")
    dniPaci = input("Ingrese el DNI:  ")
    direPaci = input("Ingrese la dirección:  ")
    respuesta = input("Ingrese el nombre de la mascota:  ")
    masco.append(respuesta)
    respo = input("Quiere ingresar otra mascota? s/n:  ")
    while respo == "s":
        respuesta = input("Ingrese la otra mascota:  ")
        masco.append(respuesta)
        respo = input("Quiere ingresar otra mascota? s/n:  ")
    paci = {
        "Nombre": nomPaci,
        "Apellido": apellPaci,
        "DNI": dniPaci,
        "Direccion": direPaci,
        "Mascotas": masco
        }
    nombre.append(paci)

#Programa Principal
nombre = []
pacientes = {}
op = menu()
while op != 4:
    match op:
        case 1:
            print()
            print("Usted seleccionó Agregar")
            agregar(pacientes)
            input("Presione enter para continuar")
        case 2:
            print()
            print("Usted seleccionó Listar")
            listar(nombre)
            input("Presione enter para continuar")
        case 3:
            print()
            print("SALDRA DEL PROGRAMA")
            break
        case _:
            print("Valor invalido")
    op = menu()
print("Hasta Luego! ")