""" APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
AUTORES: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 """
import json
import os
import colorama
from colorama import Fore,Style #dejo agregado esto x si usamos los estilos

def validar():
    """ 
    funcion que permite el ingreso con usuario y pass
    com posibilidad de cambiarla y agregarla a una lista
    de accesos validos
    AUTOR: Brenda Sztryk
    COLABORADORES: 
    """
    limpiar_Pantalla()
    usuValidos = ["Brenda", "Leo", "Marina", "Ale"] # NOMBRES VALIDOS Y PASS PARA USO DEL SISTEMA...PUEDE SER CUALQUIER OTRO NOMBRE Y MENOS USUARIOS
    passValido = "pet"
    intentos = 3

    while intentos > 0:
        usuario = input ("ingrese su usuario para ingresar al sistema: ").lower()
        contraseña = input ("ingrese su contraseña de acceso: ").lower()
        for i in range (len(usuValidos)):
            usuValidos[i] = usuValidos[i].lower() #pase usuValidos a minusc. p/ comparar en el if con usuario del input
            if usuValidos[i] == usuario and passValido.lower() == contraseña:
                print ()
                print((Style.BRIGHT + "INGRESO EXITOSO!!").center(100))
                intentos = 0
                break
        else:
            intentos = intentos - 1
            print(f"error! le quedan {intentos} intentos ")
            if intentos == 0:
                print("acceso BLOQUEADO!! ",end="")
                print("comuniquese al: 1222-3334")
                return 

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
    '''
    Función que guarda datos recolectados en la funcion agregar, no recibe argumentos,
    no retorna valor
    AUTOR:
    COLABORADORES:
    '''
    with open("pacientes.json","w") as archivo:
        json.dump(pacientes,archivo,indent=4) #dump es volcar
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
       os.system("clear") #este clear aparecia al ejecutarse el menu como algo no valido, cuando lo pase a cls dejo de hacerlo. 

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
    limpiar_Pantalla()
    while True:
        try:
            bucaId = input("\t\tIngrese el DNI a buscar: ")
            if bucaId in lista.keys():
                for nombre, valor in lista.items():
                    print()
                    print("\t\tDatos del Paciente:".upper())
                    print(("=" * 70).center(100))
                    for itemPaci, valorPaci in valor.items():
                        if itemPaci == "mascotas":
                            continue
                        print(f'\t\t{itemPaci}: {valorPaci}'.capitalize())
                    print()
                    print("\t\tMascotas:".upper())
                    print(("=" * 70).center(100))
                    for itemPaci, valorPaci in valor.items():
                        if itemPaci == "mascotas":
                            num = len(valorPaci)
                            carti = 1
                            while num > 0:
                                num -= 1
                                print(f'{("-" * 35)}{carti}{"-" * 35}'.center(100))
                                print(f'\t\ta.Nombre de Mascota: {valorPaci[num]["nombre Mascota"]}')
                                print(f'\t\tb.Tipo de Mascota: {valorPaci[num]["tipo"]}')
                                print(f'\t\tc.Raza de Mascota: {valorPaci[num]["raza"]}')
                                print(f'\t\td.Sexo de la Masota: {valorPaci[num]["sexo"]}')
                                print(f'\t\te.Edad de la Mascota: {valorPaci[num]["edad"]} años')
                                print(f'\t\tf.Peso de la Mascota: {valorPaci[num]["peso"]}Kg')
                                carti += 1
                print(("=" * 70).center(100))
                input("\t\tPresione Enter para continuar")
                limpiar_Pantalla()
                break
        except:
            print("Dato Invalido!")



def modificarD(lista):
    '''
    Función que al ingrear el dni del paciente da como resultado el dato actual y por consiguiente
    da la opción de modificar datos como año de la mascota y peso de la mascota referida al paciente. 
    Parametros: 
    Una lista de datos.
    Retorna: 
    Una lista modificada. 
    Autor: Leonardo Rios
    Colaboradores: Marina Toledo, Ale Ante, Brenda Sztryk
    '''
    limpiar_Pantalla()
    while True:
        try:
            bucaId = input("\t\tIngrese el DNI a buscar: ")
            if bucaId in lista.keys():
                for nombre, valor in lista.items():
                    print()
                    print("\t\tDatos del Paciente:".upper())
                    print(("=" * 70).center(100))
                    for itemPaci, valorPaci in valor.items():
                        if itemPaci == "mascotas":
                            continue
                        print(f'\t\t{itemPaci}: {valorPaci}'.capitalize())
                    print()
                    print("\t\tMascotas:".upper())
                    print(("=" * 70).center(100))
                    for itemPaci, valorPaci in valor.items():
                        if itemPaci == "mascotas":
                            num = len(valorPaci)
                            carti = 1
                            while num > 0:
                                num -= 1
                                print(f'{("-" * 35)}{carti}{"-" * 35}'.center(100))
                                print(f'\t\ta.Nombre de Mascota: {valorPaci[num]["nombre Mascota"]}')
                                print(f'\t\tb.Tipo de Mascota: {valorPaci[num]["tipo"]}')
                                print(f'\t\tc.Raza de Mascota: {valorPaci[num]["raza"]}')
                                print(f'\t\td.Sexo de la Masota: {valorPaci[num]["sexo"]}')
                                print(f'\t\te.Edad de la Mascota: {valorPaci[num]["edad"]} años')
                                print(f'\t\tf.Peso de la Mascota: {valorPaci[num]["peso"]}Kg')
                                carti += 1
                print(("=" * 70).center(100))
        
    
                while True:
                    try:
                        respo = input("\t\tDesea cambiar una cartilla S/N\n\t\t>  ").upper()
                        if respo == "N":
                            break
                        elif respo == "S": 
                            catillaCambiar = int(input("\t\tIngrese la cartilla que desea cambiar\n\t\t> ")) - 1
                            limpiar_Pantalla()
                            num = len(valorPaci)
                            if catillaCambiar in range(0, len(valorPaci) + 1):
                                num -= 1
                                print(f'\t\tUsted decidió cambiar {valorPaci[num]["nombre Mascota"]}')
                                while True:
                                    try:
                                        datoACambiar = input("\t\tIngrese la letra referida al dato que desea cambiar\n\t\t>a.Edad\n\t\t>b.Peso?\n\t\t: ").lower()
                                        match datoACambiar:
                                            case "a":
                                                print("\t\tDecidió cambiar Edad:")
                                                nuevaEdad = int(input("\t\tIngrese la nueva edad de la mascota\n\t\t> "))
                                                valorPaci[num]["edad"] = nuevaEdad
                                                print("\t\tCambio realizado!")
                                                guardar_Pacientes()
                                                break
                                            case "b":
                                                print("\t\tDecidió cambiar Peso")
                                                nuevoPeso = float(input("\t\tIngrese el nuevo peso de la mascota\n\t\t> "))
                                                valorPaci[num]["peso"] = nuevoPeso
                                                print("\t\tCambio realizado!")
                                                guardar_Pacientes()
                                                break
                                            case _:
                                                print(colorama.Fore.RED + "\t\tValor no válido!" + colorama.Fore.RESET)
                                    except ValueError:
                                        print(colorama.Fore.RED + "\t\tDato Inválido!" + colorama.Fore.RESET)
                                break
                            else: 
                                print("Dato Invalido!")
                    except ValueError:
                        print(colorama.Fore.RED + "\t\tDato Inválido!" + colorama.Fore.RESET)
                break
            else: 
                print("\t\tDato Invalido")
        except ValueError:
            print(colorama.Fore.RED + "\t\tDato Invalido!" + colorama.Fore.RESET)
        return lista

def buscar_Pac (pacientes):
    """ 
    Función que filtra la busqueda de mascotas a través del dni del dueño.
    Recibe un argumento en formato diccionario compuesto con otros elementos
    y lista de mascotas x dueño. No retorna valor
    AUTOR: Brenda Sztryk
    COLABORADORES:
    """
    limpiar_Pantalla()
    
    dni = (input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)) # si convierto a entero no me funciona en la busqueda !!!
    if dni in pacientes: #si dni esta en pacientes imprime dato dueño y mascotas
        paci = pacientes[dni]
        print()
        print("="*30)
        print(f"DNI: {dni}\n{paci['nombre']} {paci['Apellido']}")
        print("="*30)
        
        # MASCOTAS
        cont = 1
        for elem in paci["mascotas"]: # elem son los diccionarios de la lista
            print (f"{"Mascota"} {cont}")
            cont = cont + 1
            for c,v in elem.items():
                print (f"\t{c}: {v}")
    else:
        print(f"DNI: {dni} no se encuentra registrado. \nDesea registrarlo ahora? " )
        resp= input("responda: S / N ").upper()
        if resp == "S":
            agregar_Pac(pacientes)
        else:    
            return
    
def agregar_Pac(pacientes):
    """ Función que recibe un argumento (dicc. pacientes), 
    la base de datos global de la aplicacion ,  no retorna valor.
    AUTOR: Brenda Sztryk
    COLABORADORES: Leo Rios
    """
    limpiar_Pantalla() 
    nomDueño = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre dueño mascota: " + Fore.RESET).upper()
    apellDueño = input(Fore.LIGHTMAGENTA_EX +"Ingrese el apellido: "+ Fore.RESET).upper()
    dni = int(input(Fore.LIGHTMAGENTA_EX +"Ingrese numero de DNI: "+ Fore.RESET))
    for numDni in pacientes:
        if numDni == dni:
            print(f"error!!, el dni {dni} ya se encuentra registrado")
            return 
    pacientes[dni] = {"nombre":nomDueño,
                      "Apellido":apellDueño,
                      "mascotas":[]  # me funcionó con lista pero no con diccionario
                      }
    op = input (Fore.LIGHTMAGENTA_EX +"Desea registrar mascota?: S /N: " + Fore.RESET).upper()
    while op == "S".upper():
        nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota 🐱: " + Fore.RESET).upper()
        tipo = input (Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
        raza = input (Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
        sexo = input (Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
        while sexo != "M".upper() and sexo != "H".upper(): #este while es por si tipea otra letra que no sea H o M
            print (Fore.LIGHTMAGENTA_EX + "error, debe ingresar M o H" + Fore.RESET)
            sexo = input (Fore.LIGHTMAGENTA_EX + "ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET)
            break
        edad = int (input (Fore.LIGHTMAGENTA_EX + "Ingrese edad de la mascota: " + Fore.RESET))
        peso = float (input(Fore.LIGHTMAGENTA_EX + "Ingrese peso de la mascota en Kg: " + Fore.RESET))
        mascota = {"nombre Mascota": nomMascota,
                   "tipo":tipo,
                   "raza": raza,
                   "sexo": sexo,
                   "edad": edad,
                   "peso":peso}
        pacientes[dni]["mascotas"].append(mascota)
        guardar_Pacientes()
        #print(f"{pacientes[dni]["mascotas"]}") #solo para corroborar
        print(Style.BRIGHT + "La mascota se registró exitosamente" + Style.RESET_ALL)
        resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
        if resp == "N":
            return


    
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
pacientes = cargar_Pacientes()
#validar() #llama a la funcion antes que el menu para que acceda solo el usuario permitido (nombre con inicial mayusc / pass: pet)
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
            buscar_Pac (pacientes)
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
