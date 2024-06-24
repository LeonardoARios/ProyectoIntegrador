""" APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
AUTORES: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 """
import json
import os
import colorama
from colorama import Back,Fore,Style #dejo agregado esto x si usamos los estilos
def cargar_Pacientes(): # lo que hace es leer el archivo y ponerlo en el dicc.
    """
    Función que lee un archivo y lo coloca en el diccionario base,
    no recibe argumento, retorna un diccionario vacío en caso de haber
    un error, seria la solucion a la continuidad del programa
    AUTOR:
    COLABORADORES:
    """
    try:
        with open("pacientes.json","r") as archivo:
            return json.load(archivo)
    except:
        return {}


def guardar_Pacientes(): #esto deberia guardar lo que se incorporó al dicc
    """
    Función que guarda datos recolectados en la funcion agregar, no recibe argumentos,
    no retorna valor
    AUTOR:
    COLABORADORES:
    """
    with open("pacientes.jason","w") as archivo:
        json.dump(pacientes,archivo,ident=4) #dump es volcar
        return


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

def listar(lista):
    """
    La Función da como retorno una un listado de los datos que se guardaron.
    Parametros: 
    Un dato en forma de lista y diccionarios.
    Retorna: 
    Muestra en pantalla. 
    AUTOR: Leonardo Rios
    COLABORADORES: Marina Toledo, Ale Ante, Brenda Sztryk
    """
    carti = 1
    print(colorama.Fore.BLUE)
    print(f'{"-"*35}{carti}{"-"*35}'.center(100))
    for paciente in lista:
        for dato, info in paciente.items():
            if dato == "Mascotas":
                continue
            print(f'\t\t{dato}: {info}')
        for dato in paciente:
            if dato == "Mascotas":
                print("\t\tMascotas: ", end="")
                for info in info:
                    print(f' {info}', end="")
                print()
        if carti < len(lista):
            carti = carti +1
            print(f'{"-"*35}{carti}{"-"*35}'.center(100))
    print(("-"*70).center(100))
    input("\t\tPresione Enter para continuar")
    limpiar_Pantalla()
    return lista

def modificarD(lista):
    '''
    Función que muestra la cantidad de datos guardados, enumera las cartillas y da la opción de 
    que items se quiere cambiar. 
    Parametros: 
    Espera una lista e itera diccionario
    Retorna: 
    Lista modificada para la opcion "Listar"
    Autor: Leonardo RIos
    colaboradores: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    '''
    bucaDNI = int(input("\t\tIngrese el número de de DNI a buscar:  "))
    if bucaDNI in lista: 
        for idDueño, datosDueño in lista.items():
            nombreDueño = datosDueño['Dueño']['Nombre']
            apellDueño = datosDueño['Dueño']['Apellido']
            print()
            print("\t\tDatos del dueño".upper())
            print(("="*70).center(100))
            print(f'\t\tNombre: {nombreDueño}\n\t\tApellido: {apellDueño} ')
            print()
            print("\t\tDatos de la Mascotas:".upper())
            for nombreMascota, datosMascota in datosDueño['Mascotas'].items():
                nombreMascota = datosMascota['Nombre']
                print(("="*70).center(100))
                tipoMascota = datosMascota['Tipo']
                razaMascota = datosMascota['Raza']
                sexoMascota = datosMascota['Sexo']
                edadMascota = datosMascota['Edad']
                pesoMascota = datosMascota['Peso']
                print(f'\t\t{nombreMascota}:')
                print(f'\t\tTipo: {tipoMascota}')
                print(f'\t\tRaza: {razaMascota}')
                print(f'\t\tSexo: {sexoMascota}')
                print(f'\t\tSexo: {edadMascota}años')
                print(f'\t\tPeso: {pesoMascota}kg')
    else: 
        print("\t\tEL DNI no se encuentra en la lista")
    return lista

def agregar_Pac(pacientes):
    dueñoMascota = {}

    #Datos del dueño.
    nomDueño = input("Ingrese el nombre del dueño:  ".capitalize())
    apellDueño = input("Ingrese su apellido:  ".capitalize())
    dniDueño = int(input("Ingrese el dni:  "))

    #Datos de las mascotas: 
    while True:
        nomMascota = input("Ingrese el nombre de la mascota:  ").upper()
        tipo = input("Ingrese el tipo de mascota:  ").upper()
        raza = input("Ingrese la raza de la macota:  ").upper()
        sexo = input("Ingrese el sexo de la mascota H/M:  ").upper()
        while sexo != "H" and sexo != "M":
            print("Error debe ingresar H o M")
            sexo = input("Ingrese el sexo de la mascota H/M:  ").upper()
        edad = int(input("Ingrese la edad de la mascota:  "))
        peso = float(input("Ingrese el peso de la mascota:  "))
        #Creo un diccionario que va guardar los datos. 
        mascota = {
            "Nombre": nomMascota, 
            "Tipo": tipo,
            "Raza": raza,
            "Sexo": sexo, 
            "Edad": edad,
            "Peso": peso,
        }
        #Guardo el diccionario pero que aparezca la variable nomMascota como clave del dict macotas
        dueñoMascota[nomMascota] = mascota
        #Creo una pregunta para salir del bucle: 
        pregunta = input("Quiere agregar otra mascota?S/N:  ").upper()
        if pregunta != "S":
            break
    pacientes[dniDueño] = {"Dueño":{"Nombre": nomDueño, "Apellido": apellDueño}, "Mascotas":dueñoMascota }
    guardar_Pacientes()

    return pacientes
    
def menu():
    """
    La funcion da opciones a seleccionar x el usuario
    no espera argumentos y retorna la opcion elegida x usuario.
    AUTOR: Brenda Sztryk
    COLABORADORES: Marina Toledo, Ale Ante, Leo Rios
    """
    print()
    print((Style.BRIGHT + "*" * 40).center(100) )
    print (" MENU ".center(20).center(100))
    print((Style.BRIGHT + "*" * 40).center(100) )
    print(Style.RESET_ALL) #RESETEA LOS EFECTOS VISUALES DE ACA HACIA ABAJO, HASTA VOLVER A APLICARLO
    print(("SELECCIONE LETRA PARA OPCION DESEADA").center(40).center(100))
    print()
    print((Fore.LIGHTMAGENTA_EX + "\t A" + Fore.RESET + " - Nuevo paciente").center(100))
    print((Fore.LIGHTMAGENTA_EX + "\t B" + Fore.RESET + " - Buscar paciente").center(100))
    print((Fore.LIGHTMAGENTA_EX + "\t C" + Fore.RESET + " - Eliminar paciente").center(100))
    print((Fore.LIGHTMAGENTA_EX + "\t D" + Fore.RESET + " - Modificar base datos").center(100))
    print((Fore.LIGHTMAGENTA_EX + "\t E" + Fore.RESET + " - Listar pacientes").center(100))
    print((Fore.LIGHTMAGENTA_EX + "\t F" + Fore.RESET + " - Presupuestar").center(100)) #aca un modelo de ticket o factura
    print((Fore.LIGHTMAGENTA_EX + "\t G" " - SALIR").center(90))
    print()
    print((Fore.RESET + "*" * 40).center(100))
    #print(Style.RESET_ALL)
    op_elegida = input("\t\t\t\tIngrese letra seleccionada: ").lower()
    limpiar_Pantalla()
    return op_elegida

#Programa Principal
pacientes = {}
bande = True
op = menu()
while bande:
    match op:
            case "a": #Nuevo Paciente
                print(colorama.Fore.GREEN + "\t\tUsted seleccionó Agregar" + colorama.Fore.RESET)
                agregar_Pac(pacientes)
                print(("-"*70).center(100))
                print(colorama.Fore.RESET)
                input("\t\tPresione enter para continuar")
                
            case "b": #Buscar Paciente
                print()
                print()
                print("\t\tUsted seleccionó Buscar Paciente")
                #En Espera
                input("\t\tPresione enter para continuar")

            case "c": #Eliminar Paciente
                print()
                print("\t\tUsted seleccionó Eliminar Paciente")
                #En Espera
                input("\t\tPresione enter para continuar")
            
            case "d": #Modificar Dato
                print(colorama.Fore.YELLOW + "\t\tUsted seleccionó Modificar" + colorama.Fore.RESET)
                modificarD(pacientes)
                print(("-"*70).center(100))
                print(colorama.Fore.RESET)
                input("\t\tPresione enter para continuar")

            case "e": #Listar Paciente
                print(colorama.Fore.BLUE + "\t\tUsted seleccionó Listar" + colorama.Fore.RESET)
                listar(pacientes)
                print(colorama.Fore.RESET)
            
            case "f":#Presupuestar
                print()
                print("\t\tUsted seleccionó Presupuestar")
                #En Espera
                input("\t\tPresione enter para continuar")

            case "g": #Salir
                print(("-"*70).center(100))
                print("\t\tUsted seleccionó Salir")
                break
            case _:
                print("\t\tValor invalido")
    op = menu()
print("\t\tHasta Luego! ")