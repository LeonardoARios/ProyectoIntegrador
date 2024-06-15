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
    print(" SYS PETS ".center(50,"*").center(100))
    print(("="*70).center(100))
    print("\t\t 1. Agregar Paciente")
    print("\t\t 2. Listar")
    print("\t\t 3. Salir")
    print(("="*70).center(100))
    op = int(input("\t\t Ingresa la Opción:  "))
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
    print(("-"*70).center(100))
    #como es una lista veo primero que tiene adentro
    for paciente in lista:
    #como veo que tiene diccionarios, itero a los diccionarios con paciente.items()
        for dato, info in paciente.items():
            #como no me gusta que se vea Mascotas: []entre corchetes uso continue
            if dato == "Mascotas":
                continue
            print(f'\t\t{dato}: {info}')
        #Luego itero solamente la lista que da como resultado "Mascotas" y lo itero con
        #end="" para que quede mas prolijo
        for dato in paciente:
            if dato == "Mascotas":
                print("\t\tMascotas: ", end="")
                for info in info:
                    print(f' {info}', end="")
                print()
        print(("-"*70).center(100))
    return

'''def presentar():
    """ funcion de bienvenida al programa
    no recibe parametro, retorna nombre del programa
    AUTOR: Brenda Sztryk
    COLABORADORES: """
    print (" SYS PETS ".center(50,"*").center(100)) # ESTA FRASE PENSE SE ESCRIBA CON ASTERISCOS O X LO MENOS "PETS" :)
    return'''

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
    print(("-"*70).center(100))
    nomPaci = input("\t\tIngrese el nombre:  ")
    apellPaci = input("\t\tIngrese el apellido:  ")
    dniPaci = input("\t\tIngrese el DNI:  ")
    direPaci = input("\t\tIngrese la dirección:  ")
    respuesta = input("\t\tIngrese el nombre de la mascota:  ")
    masco.append(respuesta)
    respo = input("\t\tQuiere ingresar otra mascota? s/n:  ")
    while respo == "s":
        respuesta = input("\t\tIngrese la otra mascota:  ")
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
            print("\t\tUsted seleccionó Agregar")
            agregar(pacientes)
            input("\t\tPresione enter para continuar")
        case 2:
            print()
            print("\t\tUsted seleccionó Listar")
            listar(nombre)
            input("\t\tPresione enter para continuar")
        case 3:
            print()
            print("\t\tSALDRA DEL PROGRAMA")
            break
        case _:
            print("\t\tValor invalido")
    op = menu()
print("\t\tHasta Luego! ")