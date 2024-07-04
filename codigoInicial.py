""" 
APLICACION DE GESTION DE PACIENTES PARA VETERINARIOS
AUTORES: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 
"""
import json
import os
import colorama
from colorama import Fore,Style

def guardarValidar(listaValidacion):

    with open("validacion.json", "w") as file:
        json.dump(listaValidacion,file,indent=4)
    return

def cargaValidar():

    try:
        with open("validacion.json", "r") as file: 
            return json.load(file)
    except:
        return {}

def validar(listaUsuario):

    while True:
        try:
            respo = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tQuiere registrar un nuevo Usuario?S/N\n\t\t>  " + colorama.Fore.RESET).upper().center(100)
            if respo == "S":
                inUsuario = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese el nombre de usuario a registrar\n\t\t>  ")
                inPass = input("\t\tIngrese la contraseña a registrar\n\t\t>  " + colorama.Fore.RESET)
                listaUsuario[inUsuario]=inPass
                guardarValidar(listaUsuario)
                return listaUsuario
            else:
                input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tPresine Enter para continuar" + colorama.Fore.RESET)
                limpiar_Pantalla()
                break
        except:
            print(colorama.Fore.RED + "\t\tValidacion Incorrecta" + colorama.Fore.RESET)

    intentos = 3
    while intentos > 0:
        try:
            ingUsuario = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese su Usuario:  " + colorama.Fore.RESET)
            if ingUsuario in listaUsuario:
                ingPassword = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese su contraseña:  " + colorama.Fore.RESET)
                if ingPassword in listaUsuario.values():
                    limpiar_Pantalla()
                    print(colorama.Fore.LIGHTGREEN_EX + "\t\tIngreso Correcto\n\t\tBienvenido!" + colorama.Fore.RESET)
                    input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tPresione Enter para Continuar" + colorama.Fore.RESET)
                    limpiar_Pantalla()
                    break
                else:
                    print(colorama.Fore.RED + "\t\tPassword Incorrecto!" + colorama.Fore.RESET)
                    intentos = intentos - 1
                    if intentos == 1:
                        print(colorama.Fore.RED + "\t\tLe queda un intento mas"+ colorama.Fore.RESET.upper())
            else:
                while True:
                    try:
                        print(colorama.Fore.RED + "\t\tUsuario No registrado!" + colorama.Fore.RESET)
                        respo2 = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tQuiere registrar al Usuario? S/N\n\t\t>  " + colorama.Fore.RESET).upper()
                        if respo2 == "S":
                            inUsuario = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese el nombre de usuario a registrar\n\t\t>  " +colorama.Fore.RESET)
                            inPass = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese la contraseña a registrar\n\t\t>  " + colorama.Fore.RESET)
                            listaUsuario[inUsuario]=inPass
                            guardarValidar(listaUsuario)
                            return listaUsuario
                        else:
                            input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tPresione Enter para Continuar" + colorama.Fore.RESET)
                            break
                    except(ValueError):
                        print("\t\tCaracter No Valido!".upper())
        except:
            print("\t\tDato no valido")
'''
def validar():
    """ 
    Función que permite el ingreso a la aplicación. Requiere usuarios
    permitidos con pass de 3 intentos de acceso.
    AUTOR: Brenda Sztryk
    COLABORADORES: 
    """
    # Cree una lista de usuarios que a futuro puede cambiar ya sea quitando
    # empleados, agregando, o modificando, dependiendo de la rotación de los
    # mismos
    # LEO ESTE COMENTARIO SI TENES QUE MODIFICARLO EN BASE AL CAMBIO QUE PROPUSISTE, HACELO
    
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
                print("comuniquese al: 📱 1222-3334")
                return
''' 

def cargar_Pacientes(): # lee el archivo y lo pone en el dicc.
    """
    Función que lee un archivo y lo coloca en el diccionario base,
    no recibe argumento, retorna un diccionario vacío en caso de haber
    un error, seria la solucion a la continuidad del programa
    AUTOR: Brenda Sztryk
    COLABORADORES: Ale Ante
    """
    # Tanto la función cargar como guardar me costó entenderlas, pero viendo las
    # clases grabadas, otros videos, y recolectando informacion de apuntes
    # logre armarlas, ahi comprendi la importancia de la persistencia.
    # Inicialmente no sabía de donde tomar los datos para realizar las funciones
    # (inventé un dicc, una lista, datos ficticios para trabajrlas) y una vez 
    # vimos persistencia con json encontre de donde partir. En este punto
    # logramos conectar el trabajo porque supimos desde donde manejarnos
    
    try:
        with open("pacientes.json","r") as archivo:
            return json.load(archivo)
    except:
        return {}

def guardar_Pacientes(): #esto deberia guardar lo que se incorporó al dicc
    '''
    Función que guarda datos recolectados de la función que la ha llamado,
    no recibe argumentos, no retorna valor
    AUTOR: Brenda Sztryk
    COLABORADORES: Ale Ante
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

    os.system("cls")

def eliminar_Pac(pacientes):
    """ 
    Función que trabaja sobre un diccionario (base de datos), permite eliminar
    un cliente o alguna de sus mascotas. Recibe 1 argumento. No retorna valor.
    AUTOR: Brenda Sztryk, Ale Ante
    COLABORADORES:
    """
    # La idea es eliminar una mascota de un dni asociado. dado que las mascotas
    # son diccionarios dentro de una lista, se nos complico poder acceder x indice
    # para eliminar.
    # Brenda: como desafio personal me propuse resolverlo.... (esta en proceso)..
    # mientras, la eliminacion es del dueño con sus mascotas 🤯🤯
    
    limpiar_Pantalla()

    print("Usted seleccionó" + Fore.LIGHTMAGENTA_EX  + " ELIMINAR " + Style.RESET_ALL)
    print()
    print (Fore.LIGHTMAGENTA_EX + "A" + Fore.RESET + "- Dar de baja Dueño")
    print (Fore.LIGHTMAGENTA_EX + "B" + Fore.RESET + "- Dar de baja Mascota" )
    print()
    op = input(Fore.LIGHTMAGENTA_EX + "Ingrese opción deseada: " + Fore.RESET).upper()
    if op == "A":
        dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET) # si convierto a entero no me funciona.
        print()
        if dni in pacientes: #si dni esta en pacientes imprime dato dueño y mascotas
            #paci = pacientes[dni]
            print(f"DNI: {dni}\n{pacientes[dni]['nombre']} {pacientes[dni]['Apellido']}")
            print()
            confirmar = input(Fore.LIGHTMAGENTA_EX + "Confirma eliminación: S / N: " + Fore.RESET).upper()
            if confirmar == "S":
                del pacientes[dni]
                guardar_Pacientes()
                print ("Cliente eliminado exitosamente")
            else:
                return
        else:
            print ("El DNI no se encuentra registrado") 

    
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
    print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tUsted seleccionó Listar" + colorama.Fore.RESET)
    print(("-"*70).center(100))
    limpiar_Pantalla()
    for nombre, valor in lista.items():
        print()
        print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDatos del Pacientes:".upper())
        print(("=" * 70).center(100) + colorama.Fore.RESET)
        for itemPaci, valorPaci in valor.items():
            if itemPaci == "mascotas":
                continue
            print(f'\t\t{itemPaci}: {valorPaci}'.upper())
        print()
        print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tMascotas:".upper())
        print(("=" * 70).center(100)+ colorama.Fore.RESET)
        for itemPaci, valorPaci in valor.items():
            if itemPaci == "mascotas":
                num = len(valorPaci)
                carti = 1
                while num > 0:
                    num -= 1
                    print(f'{("-" * 35)}{carti}{"-" * 35}'.center(100))
                    print(f'\t\tNombre de Mascota: {valorPaci[num]["nombre Mascota"]}')
                    print(f'\t\tTipo de Mascota: {valorPaci[num]["tipo"]}')
                    print(f'\t\tRaza de Mascota: {valorPaci[num]["raza"]}')
                    print(f'\t\tSexo de la Masota: {valorPaci[num]["sexo"]}')
                    print(f'\t\tEdad de la Mascota: {valorPaci[num]["edad"]} años')
                    print(f'\t\tPeso de la Mascota: {valorPaci[num]["peso"]}Kg')
                    carti += 1
    print(colorama.Fore.LIGHTMAGENTA_EX + ("=" * 70).center(100)+ colorama.Fore.RESET)
    input("\t\tPresione Enter para continuar")
    limpiar_Pantalla()

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
    lista = cargar_Pacientes()
    limpiar_Pantalla()
    print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tUsted seleccionó Modificar" + colorama.Fore.RESET)
    print(("-"*70).center(100))
    while True:
        try:
            bucaId = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese el DNI a buscar: " + colorama.Fore.RESET)
            if bucaId in lista.keys():
                print()
                print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDatos del Paciente".upper())
                print(("="*70 + colorama.Fore.RESET).center(100))
                for nombre, valor in lista[bucaId].items():
                    if nombre == 'mascotas':
                        mascota = nombre
                        continue
                    print(f'\t\t{nombre}: {valor}')
                print()
                print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDatos de Mascotas".upper())
                print(("="*70 + colorama.Fore.RESET).center(100))
                for masco, valor2 in lista[bucaId].items():
                    if masco == 'mascotas':
                        num = len(valor2)
                        carti = 1
                        while num >0:
                            num -= 1
                            print(f'{("-" * 25)}Cartilla {carti}{"-" *35}'.center(100))
                            print(f'\t\tNombre de Mascotas: {valor2[num]["nombre Mascota"]}')
                            print(f'\t\tTipo de Mascota: {valor2[num]["tipo"]}')
                            print(f'\t\tRaza de la Mascota: {valor2[num]["raza"]}')
                            print(f'\t\tSexo de la Mascota: {valor2[num]["sexo"]}')
                            print(f'\t\tEdad de la Mascota: {valor2[num]["edad"]} años')
                            print(f'\t\tPeso de la Mascota: {valor2[num]["peso"]} kg')
                            carti += 1
                print((colorama.Fore.LIGHTMAGENTA_EX + "="*70 + colorama.Fore.RESET).center(100))
                while True:
                    try:
                        respo2 = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDesea cambiar datos de la cartilla S/N\n\t\t>  " + colorama.Fore.RESET).upper()
                        if respo2 == "S":
                            catillaCambiar = int(input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese el numero de cartilla que desea cambiar\n\t\t>  "+ colorama.Fore.RESET)) -1
                            limpiar_Pantalla()
                            num = len(valor2)
                            if catillaCambiar in range(0, len(valor2) + 1):
                                num -= 1
                                print(colorama.Fore.LIGHTMAGENTA_EX + f'\t\tDecidió cambiar {valor2[num]["nombre Mascota"]}' + colorama.Fore.RESET)
                                while True:
                                    try:
                                        datoACambiar = input(colorama.Fore.LIGHTMAGENTA_EX + "\t\tIngrese la letra referida al dato que desea cambiar\n\t\ta.Edad\n\t\tb.Peso\n\t\t>  "+ colorama.Fore.RESET).lower()
                                        match datoACambiar:
                                            case "a":
                                                limpiar_Pantalla()
                                                print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDecidió cambiar Edad:")
                                                nuevaEdad = int(input("\t\tIngrese la nueva edad de la mascota\n\t\t> " + colorama.Fore.RESET))
                                                valor2[num]["edad"] = nuevaEdad
                                                print(colorama.Fore.LIGHTGREEN_EX + "\t\tCambio realizado!" + colorama.Fore.RESET)
                                                guardar_Pacientes()
                                                break
                                            case "b":
                                                limpiar_Pantalla()
                                                print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tDecidió cambiar Peso")
                                                nuevoPeso = float(input("\t\tIngrese el nuevo peso de la mascota\n\t\t> " + colorama.Fore.RESET))
                                                valor2[num]["peso"] = nuevoPeso
                                                print(colorama.Fore.LIGHTGREEN_EX + "\t\tCambio realizado!"+ colorama.Fore.RESET)
                                                guardar_Pacientes()
                                                break
                                            case _:
                                                limpiar_Pantalla()
                                                print(colorama.Fore.RED + "\t\tValor no válido!" + colorama.Fore.RESET)
                                    except:
                                        print(colorama.Fore.RED + "Valor Invalido!" + colorama.Fore.RESET)
                        else:
                            limpiar_Pantalla()
                            break
                    except:
                        print(colorama.Fore.RED + "Valor Invalido!" + colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED + "No se ecuentra DNI" + colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED + "Valor Invalido" + colorama.Fore.RESET)
        break
    

def buscar_Pac (pacientes):
    """ 
    Función que filtra la busqueda de mascotas a través del dni del dueño.
    Recibe un diccionario compuesto con otras estructuras de datos. 
    No retorna valor
    AUTOR: Brenda Sztryk
    COLABORADORES:
    """
    # No me resulto dificil, siempre viendo diferentes formas de escribir para acceder a 
    # elementos, printeando para ver como quedaba el desarrollo y posibles errores y
    # reacomodando todo para una mejor visual.
    # Me gusto poder incorporar la llamada a otra funcion (agregar) lo que dio continuidad a
    # la ejecucion del codigo 😀

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
            print (Fore.LIGHTMAGENTA_EX + Style.BRIGHT+ f"{"Mascota"} {cont}" + Style.RESET_ALL)
            cont = cont + 1
            for c,v in elem.items():
                print (f"\t{c}: {v}")
            print()
    else:
        print(f"DNI: {dni} no se encuentra registrado. \nDesea registrarlo ahora? " )
        resp= input("responda: S / N ").upper()
        if resp == "S":
            agregar_Pac(pacientes)
        else:    
            return
    
def agregar_Pac(pacientes):
    """
    Función que recibe un argumento (dicc. de pacientes), 
    la base de datos global de la aplicacion, no retorna valor.
    AUTOR: Brenda Sztryk
    COLABORADORES: Leo Rios
    """
    # Tuvimos problemas para poder hacer un diccionario de mascotas (diccionario dentro de otro)
    # porque las mascotas debian individualizarce con sus datos, hubo intentos pero quedaban 
    # repetidos ciertos elementos del diccionario en el exterior del mismo, la informacion no 
    # quedaba como se necesitaba,tras varias pruebas, los datos quedaron ordenados y a partir 
    # de ahi avanzamos mas a profundidad en las funciones de cada 1.
    # Brenda: particularmente esta funcion la noto visualmente desordenada. Quiza sea porque hay
    # otra forma de escribirla o de plantearla.
    
    #limpiar_Pantalla() 
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
        nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota: " + Fore.RESET).upper()
        tipo = input (Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
        raza = input (Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
        sexo = input (Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
        while sexo != "M".upper() and sexo != "H".upper(): #este while es por si tipea otra letra que no sea H o M
            print (Fore.LIGHTMAGENTA_EX + "error, debe ingresar M o H" + Fore.RESET)
            sexo = input (Fore.LIGHTMAGENTA_EX + "ingrese sexo de la mascota: M > macho / H > hembra: " + Fore.RESET).upper()
            #break
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
        print()
        print(Style.BRIGHT + "La mascota se registró exitosamente" + Style.RESET_ALL)
        resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
        if resp == "N":
            return
    else:
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
    op_elegida = input("\t\t\t\tIngrese letra seleccionada: ").lower()
    limpiar_Pantalla()
    return op_elegida

#Programa Principal
limpiar_Pantalla()
pacientes = cargar_Pacientes()
listaValidacion = cargaValidar()
validar(listaValidacion)
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
            eliminar_Pac(pacientes)
            input("\t\tPresione enter para continuar")
            
        case "d": #Modificar Dato
            modificarD(pacientes)
            print(("-"*70).center(100))
            print(colorama.Fore.RESET)
            input("\t\tPresione enter para continuar")
            limpiar_Pantalla()

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
