""" 
APLICACION DE GESTION DE PACIENTES PARA VETERINARIOS
AUTORES: Marina Toledo, Alejandro Ante, Leonardo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 
"""
import json
import os
import colorama
from colorama import Fore,Style

def guardarValidar(listaValidacion):
    '''
    Función que guarda, en formato .json la lista de usuarios para ser utilizados como forma de 
    validación
    Parametros:
    Un diccionarios
    Retorna: 
    Ninguno
    Autor: Leonardo Rios
    Colaboradores: Marina Toledo, Ale Ante, Brenda Sztryk
    '''

    with open("validacion.json", "w") as file:
        json.dump(listaValidacion,file,indent=4)
    return

def cargaValidar():
    '''
    Funcion que carga los datos de los usuarios que están registrados para utilizar la 
    aplicación.
    Parametro: 
    Ninguno
    Retorna: 
    Un diccionario vacio
    Autor: Leonardo Rios
    Colaboradores: Marina Toledo, Ale Ante, Brenda Sztryk

    '''

    try:
        with open("validacion.json", "r") as file: 
            return json.load(file)
    except:
        return {}

def validar(listaUsuario):
    '''
    Función que permite el ingreso a la aplicación. Requiere usuarios
    permitidos con pass de 3 intentos de acceso.
    Cree una lista de usuarios que a futuro puede cambiar ya sea quitando
    empleados, agregando, o modificando, dependiendo de la rotación de los
    mismos
    AUTOR: Brenda Sztryk
    COLABORADORES: Leonardo Rios, Alejandro Ante, Marina Toledo
    '''

    print((Style.BRIGHT + "*" * 20).center(100) )
    print ("Gestion Integral para Veterinarios".center(95))
    print((Style.BRIGHT + "*" * 40).center(100) )
    print ()
    
    while True:
        try:
            respo = input(colorama.Fore.LIGHTMAGENTA_EX + "Quiere registrar un nuevo Usuario? S/N\n>  " + colorama.Fore.RESET).upper()
            if respo == "S":
                inUsuario = input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese el nombre de usuario a registrar\n>  ")
                inPass = input("Ingrese la contraseña a registrar\n>  " + colorama.Fore.RESET)
                listaUsuario[inUsuario]=inPass
                guardarValidar(listaUsuario)
                return listaUsuario
            else:
                input(colorama.Fore.LIGHTMAGENTA_EX + "Presione Enter para continuar" + colorama.Fore.RESET)
                limpiar_Pantalla()
                break
        except:
            print(colorama.Fore.RED + "Validación Incorrecta" + colorama.Fore.RESET)

    while True:
        try:
            ingUsuario = input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese su Usuario:  " + colorama.Fore.RESET)
            limpiar_Pantalla()
            if ingUsuario in listaUsuario:
                ingPassword = input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese su contraseña:  " + colorama.Fore.RESET)
                if ingPassword in listaUsuario.values():
                    limpiar_Pantalla()
                    print(colorama.Fore.LIGHTGREEN_EX + "Ingreso Correcto\nBienvenido!" + colorama.Fore.RESET)
                    input(colorama.Fore.LIGHTMAGENTA_EX + "Presione Enter para Continuar" + colorama.Fore.RESET)
                    limpiar_Pantalla()
                    break
                else:
                    print(colorama.Fore.RED + "Password Incorrecto!" + colorama.Fore.RESET)
                    
        except:
            print("Dato no válido")

def cargar_Pacientes(): # lee el archivo y lo pone en el dicc.
    """
    Función que lee un archivo y lo coloca en el diccionario base,
    no recibe argumento, retorna un diccionario vacío en caso de haber
    un error, seria la solución a la continuidad del programa
    AUTOR: Brenda Sztryk
    COLABORADORES: Ale Ante
    """
    # Tanto la función cargar como guardar me costó entenderlas, pero viendo las
    # clases grabadas, otros videos, y recolectando informacion de apuntes
    # logre armarlas, ahi comprendí la importancia de la persistencia.
    # Inicialmente no sabía de donde tomar los datos para realizar las funciones
    # (inventé un dicc, una lista, datos ficticios para trabajarlas) y una vez 
    # vimos persistencia con json encontre de donde partir. En este punto
    # logramos conectar el trabajo porque supimos desde donde manejarnos.
    
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
    La función limpia la pantalla 
    Realiza un limpiado de caracteres en la terminal al invocar
    Parametros: 
    No espera
    Retorna: 
    No tiene
    AUTOR: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
    COLABORADORES:
    """

    os.system("clear") # tener en cuenta el CLS para windows

def eliminar_Pac(pacientes):
    """ 
    Función que trabaja sobre un diccionario (base de datos), permite eliminar
    un cliente y sus mascotas o alguna de sus mascotas. Si se llego al punto
    # que no hay mascotas asociadas, se pueden incorporar nuevas.
    Recibe 1 argumento. No retorna valor.
    AUTOR: Brenda Sztryk, Ale Ante
    COLABORADORES:
    """
    # La idea es eliminar una mascota de un dni asociado. Dado que las mascotas
    # son diccionarios dentro de una lista, se nos complicó poder acceder x índice
    # y luego de muchos intentos optamos solo x eliminar al dueño y sus mascotas.
    # Brenda: como desafío personal me propuse resolverlo.... (probé mil maneras):
    # con len, con rango, despues quise asociar una enumeración para ver si era mas
    # facil eliminar únicamente a la mascota ingresando ese identificador numérico, 
    # busque informacion al respecto, llegué al "enumerate", y aca surgió que si
    # enumeraba desde 1 luego deberia restar 1 para que los datos quedaran vinculados 
    # con los índices de la lista.Tambien probe la conversión de lista a diccionario
    # pero igualmente el "tipo" era lista... esto quedó finalmente.. la listaaa 🤯🤯🤯
    
    limpiar_Pantalla()

    print("Usted seleccionó" + Fore.LIGHTMAGENTA_EX  + " ELIMINAR " + Style.RESET_ALL)
    print()
    print (Fore.LIGHTMAGENTA_EX + "A" + Fore.RESET + "- Dar de baja Dueño")
    print (Fore.LIGHTMAGENTA_EX + "B" + Fore.RESET + "- Dar de baja Mascota" )
    print()
    op = input(Fore.LIGHTMAGENTA_EX + "Ingrese opción deseada: " + Fore.RESET).upper()
    if op == "A":
        dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)
        print()
        if dni in pacientes: #si dni esta en pacientes imprime dato dueño y mascotas
            #paci = pacientes[dni]
            print("="*30)
            print(f"DNI: {dni}\n{pacientes[dni]['nombre']} {pacientes[dni]['Apellido']}")
            print("="*30)
            print()
            confirmar = input(Fore.LIGHTMAGENTA_EX + "Confirma eliminación: S / N: " + Fore.RESET).upper()
            if confirmar == "S":
                del pacientes[dni]
                guardar_Pacientes()
                print()
                print (Fore.LIGHTGREEN_EX + "Cliente eliminado exitosamente" + Fore.RESET)
            else:
                return
        else:
            print ("El DNI no se encuentra registrado") 
    if op == "B":
        dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)
        print()
        paci = pacientes[dni]["mascotas"] # lista con diccionarios de mascotas
        if dni in pacientes:
            if len(paci) > 0: # si es > a 0: hay mascotas
                print (f"{pacientes[dni]['nombre']} {pacientes[dni]['Apellido']}")
                print("="*30)
                for num,mascota in enumerate(paci):
                    print (Fore.LIGHTMAGENTA_EX + f"Mascota {num + 1}: {Fore.RESET} {mascota['nombre Mascota']} - {mascota['tipo']}") #sumo 1 p/ numerar desde 1
                print()
                eliminar = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese NUMERO de mascota a dar de baja: "  + Fore.RESET))
                indice = eliminar - 1 # resto 1 xq los indices de la lista arrancan en cero. Restando coincidiria: el numero a eliminar con el indice
                if indice >= 0:
                    del paci[indice]
                    opcion = input ("Confirma la baja de la mascota? S / N: ").upper()
                    if opcion == "S":
                        guardar_Pacientes()
                        print()
                        print (Fore.LIGHTGREEN_EX + f"La Mascota {mascota['nombre Mascota']} se dio de baja EXITOSAMENTE" + Fore.RESET)
                else:
                    print(Fore.LIGHTMAGENTA_EX + "ERROR" + Fore.RESET + "ingrese un número correcto" )
                    return
            elif len(paci) == 0: # si es cero, no hay mascotas
                print (f"NO existen mascotas asociadas a {Fore.LIGHTMAGENTA_EX} {pacientes[dni]['nombre']}")
                darBaja = input("Desea dar de baja este DNI: S / N: ").upper()
                if darBaja == "S":
                    del pacientes[dni]
                    guardar_Pacientes()
                else:
                    print()
                    incorporar = input("Desea incorporar una mascota: S / N ").upper()
                    if incorporar == "S":
                        nomMascota=input("ingrese nombre mascota: ")
                        nuevaMascota = {"nueva Mascota": nomMascota}
                        paci.append(nuevaMascota)
                        guardar_Pacientes()
                        return
        else:
            print(f"El DNI {Fore.LIGHTMAGENTA_EX} NO {Fore.RESET} existe en la base de datos")
            return

    
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
    print(colorama.Fore.LIGHTMAGENTA_EX + "Usted seleccionó Listar" + colorama.Fore.RESET)
    print(("-"*70))
    limpiar_Pantalla()
    for nombre, valor in lista.items():
        print()
        print(colorama.Fore.LIGHTMAGENTA_EX + "Datos del Pacientes:".upper())
        print(("=" * 70) + colorama.Fore.RESET)
        for itemPaci, valorPaci in valor.items():
            if itemPaci == "mascotas":
                continue
            print(f'{itemPaci}: {valorPaci}'.upper())
        print()
        print(colorama.Fore.LIGHTMAGENTA_EX + "Mascotas:".upper())
        print(("=" * 70)+ colorama.Fore.RESET)
        for itemPaci, valorPaci in valor.items():
            if itemPaci == "mascotas":
                num = len(valorPaci)
                carti = 1
                while num > 0:
                    num -= 1
                    print(f'{("-" * 30)}Cartilla {carti}{"-" * 30}')
                    print(f'Nombre de Mascota: {valorPaci[num]["nombre Mascota"]}')
                    print(f'Tipo de Mascota: {valorPaci[num]["tipo"]}')
                    print(f'Raza de Mascota: {valorPaci[num]["raza"]}')
                    print(f'Sexo de la Masota: {valorPaci[num]["sexo"]}')
                    print(f'Edad de la Mascota: {valorPaci[num]["edad"]} años')
                    print(f'Peso de la Mascota: {valorPaci[num]["peso"]}Kg')
                    carti += 1
    print(colorama.Fore.LIGHTMAGENTA_EX + ("=" * 70)+ colorama.Fore.RESET)
    input("\t\tPresione Enter para continuar")
    limpiar_Pantalla()

def modificarD(lista):
    '''
    Función que al ingrear el dni del paciente da como resultado el dato actual y por consiguiente
    da la opción de modificar datos como edad de la mascota y peso de la mascota referida al paciente. 
    Parametros: 
    Una lista de datos.
    Retorna: 
    Una lista modificada. 
    Autor: Leonardo Rios
    Colaboradores: Marina Toledo, Ale Ante, Brenda Sztryk
    '''
    limpiar_Pantalla()
    print(colorama.Fore.LIGHTMAGENTA_EX + "Usted seleccionó Modificar" + colorama.Fore.RESET)
    print(("-"*70))
    while True:
        try:
            bucaId = input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese el DNI a buscar: " + colorama.Fore.RESET)
            if bucaId in lista.keys():
                print()
                print(colorama.Fore.LIGHTMAGENTA_EX + "Datos del Paciente".upper())
                print(("="*70 + colorama.Fore.RESET))
                for nombre, valor in lista[bucaId].items():
                    if nombre == 'mascotas':
                        mascota = nombre
                        continue
                    print(f'{nombre}: {valor}')
                print()
                print(colorama.Fore.LIGHTMAGENTA_EX + "Datos de Mascotas".upper())
                print(("="*70 + colorama.Fore.RESET))
                for masco, valor2 in lista[bucaId].items():
                    if masco == 'mascotas':
                        num = len(valor2)
                        carti = 1
                        while num >0:
                            num -= 1
                            print(f'{("-" * 25)}Cartilla {carti}{"-" *35}')
                            print(f'Nombre de Mascotas: {valor2[num]["nombre Mascota"]}')
                            print(f'Tipo de Mascota: {valor2[num]["tipo"]}')
                            print(f'Raza de la Mascota: {valor2[num]["raza"]}')
                            print(f'Sexo de la Mascota: {valor2[num]["sexo"]}')
                            print(f'Edad de la Mascota: {valor2[num]["edad"]} años')
                            print(f'Peso de la Mascota: {valor2[num]["peso"]} kg')
                            carti += 1
                print((colorama.Fore.LIGHTMAGENTA_EX + "="*70 + colorama.Fore.RESET))
                while True:
                    try:
                        respo2 = input(colorama.Fore.LIGHTMAGENTA_EX + "Desea cambiar datos de la cartilla S/N\n>  " + colorama.Fore.RESET).upper()
                        if respo2 == "S":
                            catillaCambiar = int(input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese el número de cartilla que desea cambiar\n>  "+ colorama.Fore.RESET)) -1
                            limpiar_Pantalla()
                            num = len(valor2)
                            if catillaCambiar in range(0, len(valor2) + 1):
                                num -= 1
                                print(colorama.Fore.LIGHTMAGENTA_EX + f'Decidió cambiar {valor2[num]["nombre Mascota"]}' + colorama.Fore.RESET)
                                while True:
                                    try:
                                        datoACambiar = input(colorama.Fore.LIGHTMAGENTA_EX + "Ingrese la letra referida al dato que desea cambiar\na.Edad\nb.Peso\n>  "+ colorama.Fore.RESET).lower()
                                        match datoACambiar:
                                            case "a":
                                                limpiar_Pantalla()
                                                print(colorama.Fore.LIGHTMAGENTA_EX + "Decidió cambiar Edad:")
                                                nuevaEdad = int(input("Ingrese la nueva edad de la mascota\n> " + colorama.Fore.RESET))
                                                valor2[num]['edad'] = nuevaEdad
                                                print(colorama.Fore.LIGHTGREEN_EX + "Cambio realizado!" + colorama.Fore.RESET)
                                                print(valor2[num]['edad'])
                                                guardar_Pacientes()
                                                break
                                            case "b":
                                                limpiar_Pantalla()
                                                print(colorama.Fore.LIGHTMAGENTA_EX + "Decidió cambiar Peso")
                                                nuevoPeso = float(input("Ingrese el nuevo peso de la mascota\n> " + colorama.Fore.RESET))
                                                valor2[num]['peso'] = nuevoPeso
                                                print(colorama.Fore.LIGHTGREEN_EX + "Cambio realizado!"+ colorama.Fore.RESET)
                                                guardar_Pacientes()
                                                break
                                            case _:
                                                limpiar_Pantalla()
                                                print(colorama.Fore.RED + "Valor no válido!" + colorama.Fore.RESET)
                                    except:
                                        print(colorama.Fore.RED + "Valor Inválido!" + colorama.Fore.RESET)
                        else:
                            limpiar_Pantalla()
                            break
                    except:
                        print(colorama.Fore.RED + "Valor Inválido!" + colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED + "No se ecuentra DNI" + colorama.Fore.RESET)
        except:
            print(colorama.Fore.RED + "Valor Inválido" + colorama.Fore.RESET)
        break
    return lista
    

def buscar_Pac (pacientes):
    """ 
    Función que filtra la búsqueda de mascotas a través del dni del dueño.
    Recibe un diccionario compuesto con otras estructuras de datos. 
    No retorna valor
    AUTOR: Brenda Sztryk
    COLABORADORES:
    """
    # No me resulto dificil, siempre viendo diferentes formas de escribir para acceder a 
    # elementos, printeando para ver como quedaba el desarrollo y posibles errores y
    # reacomodando todo para una mejor visual.
    # Me gustó poder incorporar la llamada a otra función (agregar) lo que dió continuidad a
    # la ejecucion del código 😀

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
                print (f"{c}: {v}")
            print()
    else:
        print()
        resp = input(Fore.LIGHTMAGENTA_EX +f"DNI: {dni}{Fore.RESET} NO se encuentra registrado. \nDesea registrarlo ahora? S / N: " ).upper()
        if resp == "S":
            print()
            agregar_Pac(pacientes)
        else:    
            return
    
def agregar_Pac(pacientes):
    """
    Función que recibe un argumento (dicc. de pacientes), 
    la base de datos global de la aplicación, no retorna valor.
    AUTOR: Brenda Sztryk
    COLABORADORES: Leo Rios
    """
    # Tuvimos problemas para poder hacer un diccionario de mascotas (diccionario dentro de otro)
    # porque las mascotas debian individualizarce con sus datos, hubo intentos pero quedaban 
    # repetidos ciertos elementos del diccionario en el exterior del mismo, la información no 
    # quedaba como se necesitaba, tras varias pruebas, los datos quedaron ordenados y a partir 
    # de ahí avanzamos más a profundidad en las funciones de cada uno.
    # Brenda: particularmente esta función la noto visualmente desordenada. Quizá porque hay
    # otra forma de escribirla o de plantearl o acomodarla.
    
    #limpiar_Pantalla() 
    nomDueño = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre dueño mascota: " + Fore.RESET).upper()
    apellDueño = input(Fore.LIGHTMAGENTA_EX +"Ingrese el apellido: "+ Fore.RESET).upper()
    dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese numero de DNI: "+ Fore.RESET)
    for numDni in pacientes:
        if numDni == dni:
            print(f"ERROR!!, el dni {dni} ya se encuentra registrado")
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
            print (Fore.LIGHTMAGENTA_EX + "ERROR, debe ingresar M o H" + Fore.RESET)
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
        print(Style.BRIGHT + "La mascota se registró EXITOSAMENTE" + Style.RESET_ALL)
        resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
        if resp == "N":
            return
    else:
        return


def facturar():
     
    """
    Función que muestra en la consola la lista de precios actualizada de los servicios
    que brinda la veterinaria. Los servicios y sus valores se encuentran en un diccionario
    que puede ser modificado por el programador.
    No recibe argumentos
    No retorna nada
    """
    serv = {'Consulta':6000,'Vacuna':3000,'Castración':7000,'Análisis':4000,'Radiografía':5000,'Ecografía':6000}
    fecha = '05/07/2024'    #la fecha se carga automaticamente
    print('='*100)
    print()
    print(Style.BRIGHT + ' SYS PETS '.center(100)) #Back. color de fondo
    print(Style.RESET_ALL)
    print('='*100)
    print()
    print(f'\tFecha: {fecha}'.rjust(90).center(100))
    print()
    print((" * " * 30).center(100))
    print()
    print (" Lista de precios ".center(40).center(100))
    print()
    print((" * " * 30).center(100) )
    print()
    print(f'\t Servicio \t  Precio ')
    print()
    cont = 1
    for s, v in serv.items():
       print(f'\t {s} \t  $ {v}')
       cont = cont + 1
    print('='*100)
    print()
    print('Precios válido por 3 días')
    print()
    print('='*100)
    print()

def menu():
    """
    La función propone opciones a seleccionar x el usuario
    no espera argumentos y retorna la opción elegida.
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
            print(colorama.Fore.LIGHTMAGENTA_EX +("-"*70).center(100) + colorama.Fore.RESET)
            print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tUsted seleccionó Salir" + colorama.Fore.RESET)
            break
        case _:
            print("\t\tValor invalido")
    op = menu()
print("\t\tHasta Luego! ")
