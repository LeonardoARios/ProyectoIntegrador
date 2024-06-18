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
    return

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
    carti = 1
    print(colorama.Fore.YELLOW)
    print(f'\t\tNumero de datos cargados: {len(lista)}')
    print(colorama.Fore.RESET)
    print(f'{"-"*35}{carti}{"-"*35}'.center(100))
    for deDic in lista:
        for dato,infos in deDic.items():
            if dato == "Mascotas":
                continue
            else:
                print(f'\t\t{dato}: {infos}')
        for dato in deDic:
            if dato == "Mascotas":
                print("\t\tMascotas:  ", end="")
                for info in infos: 
                    print(f'{info}, ', end="")
                print()
        if carti < len(lista):
            carti = carti +1
            print(f'{"-"*35}{carti}{"-"*35}'.center(100))

    respo1 = int(input(colorama.Fore.YELLOW + "\t\tQue cartilla desea cambiar?:  ".upper() + colorama.Fore.RESET))
    respo1 = respo1 - 1 
    bande = True
    while bande:
        if respo1 >= 0 and respo1 <= len(lista):
                if lista[respo1] in lista:
                    respo2 = input(colorama.Fore.YELLOW + "\t\tQue item desea cambiar?:  ".upper() + colorama.Fore.RESET) 
                    while bande:
                        if respo2 in lista[respo1]:
                            if respo2 == "Mascotas":
                                for dato in deDic:
                                    if dato == "Mascotas":
                                        print("\t\tMascotas:  ", end="")
                                        num = 0
                                        for info in infos:
                                            num = num +1
                                            print(f'{num}:{info}, ', end="")
                                        print()
                                nuModifico = int(input(colorama.Fore.YELLOW + "\t\tIngrese el número que desea modificar:  " + colorama.Fore.RESET))
                                nuModifico = nuModifico - 1
                                nueMascota = input(colorama.Fore.YELLOW + "\t\tIngrese la nueva mascota:  ".upper() + colorama.Fore.RESET)
                                deDic[dato][nuModifico]=nueMascota
                                bande = False
                            else:    
                                respo3 = input(colorama.Fore.YELLOW + "\t\tEscriba el nuevo valor:  ".upper() + colorama.Fore.RESET)
                                lista[respo1][respo2]=respo3
                                bande = False
                        else:
                            print(colorama.Fore.RED + "\t\tItem ingresado no valido".upper() + colorama.Fore.RESET)
                            respo2 = input(colorama.Fore.YELLOW + "\t\tQue item desea cambiar?:  ".upper() + colorama.Fore.RESET)
        else: 
            print(colorama.Fore.RED + "\t\tNumero ingresado fuera de rango".upper() + colorama.Fore.RESET)
            respo1 = int(input(colorama.Fore.YELLOW + "\t\tQue cartilla desea cambiar?:  ".upper()) + colorama.Fore.RESET)
    return lista
            
def agregar(paci):
    """
    Función agregar 
    La función agrega datos en seguidos imput's organizados los datos del paciente. 
    Parametros: 
    Datos ingresados de caracteres string y entero
    Retorna: 
    Dato en forma de lista empaquetada, que incluye por cada usuario un diccionario. 
    Autor: Leonardo Ríos
    Colaboradores: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    """
    masco = []
    print(("-"*70).center(100))
    nomPaci = input(colorama.Fore.GREEN + "\t\tIngrese el nombre:  " + colorama.Fore.RESET)
    apellPaci = input(colorama.Fore.GREEN + "\t\tIngrese el apellido:  " + colorama.Fore.RESET)
    dniPaci = input(colorama.Fore.GREEN + "\t\tIngrese el DNI:  " + colorama.Fore.RESET)
    direPaci = input(colorama.Fore.GREEN + "\t\tIngrese la dirección:  " + colorama.Fore.RESET)
    respuesta = input(colorama.Fore.GREEN + "\t\tIngrese el nombre de la mascota:  " + colorama.Fore.RESET)
    masco.append(respuesta)
    respo = input(colorama.Fore.GREEN + "\t\tQuiere ingresar otra mascota? s/n:  " + colorama.Fore.RESET)
    while respo == "s":
        respuesta = input(colorama.Fore.GREEN + "\t\tIngrese la otra mascota:  " + colorama.Fore.RESET)
        masco.append(respuesta)
        respo = input(colorama.Fore.GREEN + "\t\tQuiere ingresar otra mascota? s/n:  " + colorama.Fore.RESET)
    
    paci = {
        "Nombre": nomPaci,
        "Apellido": apellPaci,
        "DNI": dniPaci,
        "Direccion": direPaci,
        "Mascotas": masco
        }
    nombre.append(paci)
    return paci, masco

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
nombre = []
pacientes = {}
bande = True
op = menu()
while bande == True:
    match op:
        case "a": #Nuevo Paciente
            print(colorama.Fore.GREEN + "\t\tUsted seleccionó Agregar" + colorama.Fore.RESET)
            agregar(pacientes)
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
            modificarD(nombre)
            print(("-"*70).center(100))
            print(colorama.Fore.RESET)
            input("\t\tPresione enter para continuar")

        case "e": #Listar Paciente
            print(colorama.Fore.BLUE + "\t\tUsted seleccionó Listar" + colorama.Fore.RESET)
            listar(nombre)
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