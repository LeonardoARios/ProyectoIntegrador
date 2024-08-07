""" 
APLICACION DE GESTION DE PACIENTES PARA VETERINARIOS
AUTORES: Marina Toledo, Alejandro Ante, Leonardo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 
"""
# Pensamos una aplicacion que gestiona mascotas/dueño mascota para una veterinaria, desde su 
# ingreso hasta su baja/eliminación, pasando x búsqueda filtrada x DNI del dueño, un listado 
# de la base de datos y opción de modificar los mismos. Cuenta también con un facturador/
# presupuestador de servicios. Adicional un README y LICENSE.
# Inicialmente fue pensada como aplicacion real de celular, y nos dimos cuenta que se abria 
# a muchas ramas de conexiones, asi que empezamos a acotar a lo que queriamos mostrar teniendo 
# en cuenta los items a cumplir (agregar, eliminar, listar, buscar, modificar, etc), asimismo es
# posible generar relación entre las funciones creadas y mostrar respuestas/acciones tanto x el SI 
# como por el NO en el código. Pasamos por diferentes dificultades, como no saber de donde tomar 
# los datos para nuestras funciones x no haber persistencia, fuimos inventando datos para 
# realizarlas hasta que apareció JSON el salvador! y así fuimos cerrando ideas, esto es prueba 
# y error para corregir, modificar y mejorar. Supimos estar en contacto y exponer nuestras ideas 
# para tomar las mas acordes y encaminar el TP. Como detalle de las funciones, los input para DNI los
# dejamos como string dado que no realizariamos a posteriori cálculos matemáticos, de inicio los trabajamos
# como INT y en alguna funcion nos trajo problemas comenzando a dar fallas al funcionamiento de la misma,
# decidimos quitarlo en todas. Tambien aclaramos que algunas de las funciones, cuando hay que realizar 
# una eleccion de respuesta a una pregunta, tienen la opcion de agregar mascotas sin la necesidad de ir 
# al menu principal, esto aparece en el eliminar, buscar y modificar. 
# Brenda: mis funciones no tienen tratamiento de errores, no llegue a aplicarlas si bien entiendo que hay
# que tratar la linea de codigo que pueda dar error y colocar la excepcion a ese error. Quiesiera practicarlo 
# y prefiero que no se rompar el código.

import json
import os
import colorama
from colorama import Fore,Style
#from funcionesEmergencia import presupuestar
import datetime

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
    AUTOR: Brenda Sztryk, Leo Rios
    COLABORADORES: Alejandro Ante, Marina Toledo
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
                limpiar_Pantalla()
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
    # Tanto la función cargar como guardar me costó entenderlas (Brenda), pero viendo las
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

    os.system("cls")

def eliminar_Pac(pacientes):
    """ 
    Función que trabaja sobre un diccionario (base de datos), permite eliminar
    un cliente y sus mascotas o alguna de sus mascotas. Si se llego al punto
    # que no hay mascotas asociadas, se pueden incorporar nuevas.
    Recibe 1 argumento. No retorna valor.
    AUTOR: Brenda Sztryk, Ale Ante
    COLABORADORES:
    """
    # La idea inicial fue eliminar x mascota. Dado que las mascotas son diccionarios 
    # dentro de una lista, se nos complicó poder acceder x índice aún entendiendo el 
    # tema de índices, luego de muchos intentos optamos x la eliminación del dueño y 
    # sus mascotas asociadas, cumpliendo con la funcion de eliminar.
    # Brenda: como desafío personal me propuse resolverlo.... (probé,probé,probé):
    # con len, con rango, quise asociar una enumeración para facilitar eliminación
    # únicamente de la mascota ingresando ese identificador numérico, busque información
    # al respecto, llegué al "enumerate", y aca surgió que: si enumeraba desde 1, luego 
    # deberia restar 1 para que los elementos quedaran vinculados con los índices de la
    # lista.Tambien probé la conversión de lista a diccionario pero igualmente el "tipo" 
    # seguia siendo lista... esto quedó finalmente.. la LISTAAA 🤯🤯🤯
    # Para la entrega final incorporé al código: que si el DNI no registra mascotas
    # se ofrezca el registro de una o varias o ninguna, tambien preguntar si
    # el dueño de la mascota desea darse de baja o no.
    
    limpiar_Pantalla()

    print(Fore.LIGHTMAGENTA_EX + "Usted seleccionó"  + " ELIMINAR " + Style.RESET_ALL)
    print(("-"*70))
    print (Fore.LIGHTMAGENTA_EX + "A" + Fore.RESET + "- Dar de baja Dueño")
    print (Fore.LIGHTMAGENTA_EX + "B" + Fore.RESET + "- Dar de baja Mascota" )
    print()
    op = input(Fore.LIGHTMAGENTA_EX + "Ingrese opción deseada: " + Fore.RESET).upper()
    if op == "A":
        dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)
        print()
        if dni in pacientes: #si dni esta en pacientes imprime dato dueño y mascotas
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
            print (Fore.LIGHTMAGENTA_EX + "El DNI no se encuentra registrado" + Fore.RESET) 
    if op == "B":
        dni = input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)
        print()
        
        if dni in pacientes:
            paci = pacientes[dni]["mascotas"] # lista con diccionarios de mascotas
            if len(paci) > 0: # si es > a 0: hay mascotas
                print (f"{pacientes[dni]['nombre']} {pacientes[dni]['Apellido']}")
                print("="*30)

                for num,mascot in enumerate(paci):
                    print (Fore.LIGHTMAGENTA_EX + f"Mascota {num + 1}: {Fore.RESET}{mascot['nombre Mascota']} - {mascot['tipo']}") #sumo 1 p/ numerar desde 1
                print()
                while True:
                    eliminar = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese NUMERO de mascota a dar de baja: "  + Fore.RESET))
                    indice = eliminar - 1 # resto 1 xq los indices de la lista comienzan en cero. Así coincidiria: el numero a eliminar con el indice
                    if indice in range(len(paci)):
                        del paci[indice]
                        opcion = input (f"Confirma la baja de {mascot['nombre Mascota']} ? S / N: ").upper()
                        if opcion == "S":
                            guardar_Pacientes()
                            print()
                            print (Fore.LIGHTGREEN_EX + f"La Mascota {mascot['nombre Mascota']} se dio de baja EXITOSAMENTE" + Fore.RESET)
                            break
                        else:
                            return
                    else:
                        print(Fore.LIGHTMAGENTA_EX + f"ERROR " + Fore.RESET +  "intente nuevamente" )
                        print()
            else:
                len(paci) == 0 # si es cero, no hay mascotas
                print (Fore.LIGHTMAGENTA_EX + f"NO {Fore.RESET} existen mascotas asociadas a  {pacientes[dni]['nombre']}")
                darBaja = input("Desea dar de baja este DNI: S / N: ").upper()
                if darBaja == "S":
                    del pacientes[dni]
                    guardar_Pacientes()
                else: # a modo ejemplo desde aca se podria agregar una mascota (cuando se hace eliminacion de la  ultima mascota de este DNI): iria parte del codigo de la funcion agregar
                    print()
                    incorporar = input("Desea incorporar una mascota: S / N ").upper()
                    if incorporar == "S":
                        nomMascota=input("ingrese nombre mascota: ")
                        nuevaMascota = {"nueva Mascota": nomMascota}
                        paci.append(nuevaMascota)
                        guardar_Pacientes()
                        return
        else:
            print(Fore.LIGHTMAGENTA_EX +f"DNI: {dni}{Fore.RESET} NO se encuentra registrado en la base de datos")
            return

def presupuestar(pacientes):
    """
    Función que genera un presupuesto/ticket a un DNI de la base de datos,
    global (pacientes) la cual recibe como argumento.
    No retorna valor
    AUTOR: Leo Rios, Brenda Sztryk
    COLABORAORES: Ale Ante, Marina Toledo
    """
    # Si bien al ticket le faltan detalles para hacerlo mas real, ejemplo datetime, concluimos 
    # que tiene un buen desarrollo y funciona 👏👏👏
    # Comenzamos con servicios ofrecidos formato diccionario y luego, como también sucedió a lo 
    # largo del trabajo, uno va escribiendo el código y se enfrenta a ciertas trabas, las cuales
    # se sortean con las pruebas de ejecución, debug y moviendo lineas de codigo.
    # No hicimos Json para esta función (la lista que almacena precios de servicios a traves de
    # un append, x mas que no los muestra, salvo al printearlos, quedan en memoria para
    # posterior cálculo, en este caso suma). Para la version futura se podría presupuestar en base 
    # a mascotas seleccionadas de la lista que arroja x DNI.
    
       
    print() 
    dni = input(f"Ingrese{Fore.LIGHTMAGENTA_EX} DNI{Fore.RESET} del cliente para presupuestar: ")
    print()
    if dni in pacientes: # DUEÑO
        paci = pacientes[dni]['mascotas']
        print()
        print("TICKET".center(50))
        print("NO VALIDO COMO FACTURA".center(50))
        print("="*50)

        fechaHoy= datetime.date.today()
        hora = datetime.time(10,20,35)
        print(Fore.LIGHTMAGENTA_EX + f"SYS PETS.SRL {Fore.RESET}  \t\t\t {fechaHoy}")
        print(f"Gaona 125,CABA. (1427) \t\t {hora}")
        print("Tel: 4200-5000")
        print("="*50)
        print()
        for nombre,dato in pacientes[dni].items():
            if nombre == 'mascotas':
                continue
            print(f'{nombre}: {dato}')
        print("="*50)

        for mascotas,datos in pacientes[dni].items(): # CANTIDAD MASCOTAS
            if mascotas == 'mascotas':
                print(f'Cant. Mascotas Registradas: {len(datos)}')
                print("-"*50)

        for num,mascot in enumerate(paci,1): # NUMERADO MASCOTAS
            print (Fore.LIGHTMAGENTA_EX + f"Mascota {num}: {Fore.RESET}{mascot['nombre Mascota']} - {mascot['tipo']}") #sumo 1 p/ numerar desde 1
        print()
        print(Style.BRIGHT + f"SERVICIOS OFRECIDOS:{Style.RESET_ALL} ")
        print("="*50)
        
        servicios = [("Vacuna",3000),("Consulta",6000),("Castración",7000),("Análisis",4000),("Radiografía",5000),("Ecografía",6000)]
        
        for enum, (item, precio) in enumerate(servicios,1): #enumero dsd 1 para elegir opcion
            print(Fore.LIGHTMAGENTA_EX + f"\t{enum} {Fore.RESET}- {item}")
        print()
        print(Style.BRIGHT+ f"SERVICIOS SELECCIONADOS PARA 1 MASCOTA {Style.RESET_ALL}")
        print("="*50)   
            
        suma = []
        while True:
            elegir = int(input("Elija NUMERO, o (cero) 0 para finalizar:"))
            print()
            indice = elegir - 1 #resto 1 para que coincida con los indices de lista 
            if indice < 0:
                print(Fore.LIGHTMAGENTA_EX + f"\t\t\tTOTAL: ${sum(suma) * 1.21}{Fore.RESET} ")
                break
            elif indice >= 0 and indice < len(servicios):
                print(f"Seleccionó {elegir} \t{Fore.LIGHTMAGENTA_EX} \t{servicios[indice][0]}: ${servicios[indice][1]} {Fore.RESET}") # accedo x indice a la tupla de la lista
                suma.append(servicios[indice][1]) # el indice 1 es el precio
            else:
                print (f"NUMERO {Fore.LIGHTMAGENTA_EX} INCORRECTO {Fore.RESET}")
        return
    else:   
       print (f" El DNI: {dni} {Fore.LIGHTMAGENTA_EX} NO se encuentra registrado {Fore.RESET} ") 
       return
       # ACA SE ABRE POSIBILIDAD DE REGISTRAR CON OPCION "A"
       # DEL MENU LLAMANDO A LA FUNCION "AGREGAR".


    
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
        print(f'DNI: {nombre}')
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
                print(f'DNI: {bucaId}')
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
                        respo2 = input(colorama.Fore.LIGHTMAGENTA_EX + "Desea cambiar datos de la cartilla S/N\nO 'A' si Quiere ingresar una nueva mascota\n>  " + colorama.Fore.RESET).upper()
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
                        elif respo2 == "A":
                            nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota: " + Fore.RESET).upper()
                            tipo = input (Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
                            raza = input (Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
                            sexo = input (Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
                            while sexo != "M".upper() and sexo != "H".upper(): #este while es por si tipea otra letra que no sea H o M
                                print (Fore.LIGHTMAGENTA_EX + "ERROR, debe ingresar M o H" + Fore.RESET)
                                sexo = input (Fore.LIGHTMAGENTA_EX + "ingrese sexo de la mascota: M > macho / H > hembra: " + Fore.RESET).upper()
                            edad = int (input (Fore.LIGHTMAGENTA_EX + "Ingrese edad de la mascota: " + Fore.RESET))
                            peso = float (input(Fore.LIGHTMAGENTA_EX + "Ingrese peso de la mascota en Kg: " + Fore.RESET))
                            mascota = {"nombre Mascota": nomMascota,
                                       "tipo":tipo,
                                       "raza": raza,
                                       "sexo": sexo,
                                       "edad": edad,
                                       "peso":peso}
                            lista[bucaId]["mascotas"].append(mascota)
                            print(lista[bucaId]["mascotas"])
                            guardar_Pacientes()
                            break
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
    # elementos, printeando para ver como quedaba el desarrollo, mejorando las salidas y
    # reordenando para una mejor visual. Me gustó poder incorporar la llamada a otra
    # función (agregar), lo que dió continuidad a la ejecución del código 😀
    # Para la entrega final icorporé la opcion "agregar mascotas" a un DNI, tenga o no
    # mascotas asociadas, lo que posibilita hacerlo sin recurrir al menu inicial.
    # Si bien el hecho de no recurrir almenu se puede presentar en varias oportunidades, 
    # y funciones, no lo apliqué para no ser repetitiva con las lineas de codigo y 
    # procesos de carga de datos.
    # x ejemplo, acá en el buscar se puede agregar mascota pero tambien podria añadir
    # opcion "eliminar" si es que en ese momento se quiere dar de baja una mascota. 
    # Voy notando que se presentan varias salidas en las respuestas x SI o x NO en el código

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
        incorporar = input("Desea incorporar mascotas? S / N: " ).upper()
        while incorporar == "S".upper():
                nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota: " + Fore.RESET).upper()
                tipo = input (Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
                raza = input (Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
                sexo = input (Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
                while sexo != "M".upper() and sexo != "H".upper(): #este while es por si tipea otra letra que no sea H o M
                    print (Fore.LIGHTMAGENTA_EX + "ERROR, debe ingresar M o H" + Fore.RESET)
                    sexo = input (Fore.LIGHTMAGENTA_EX + "ingrese sexo de la mascota: M > macho / H > hembra: " + Fore.RESET).upper()
                edad = int (input (Fore.LIGHTMAGENTA_EX + "Ingrese edad de la mascota: " + Fore.RESET))
                peso = float (input(Fore.LIGHTMAGENTA_EX + "Ingrese peso de la mascota en Kg: " + Fore.RESET))
                mascota = {"nombre Mascota": nomMascota,
                           "tipo":tipo,
                           "raza": raza,
                           "sexo": sexo,
                           "edad": edad,
                           "peso":peso}
                pacientes[dni]['mascotas'].append(mascota)
                guardar_Pacientes()
                print(Style.BRIGHT + f"La mascota {nomMascota} se registró EXITOSAMENTE" + Style.RESET_ALL)
                resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
                if resp == "N":
                     return
        else:
            return
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
    # Tuvimos problemas para poder hacer un diccionario dentro de otro para la cant. de mascotas x dueño, 
    # o sea que cada mascota individualizada en diccionarios no logramos colocarlas dentro de otro en
    # vez dentro de una lista. Como funcionó con esta última lo dejamos así... aunque realizamos intentos 
    # para trabajar con diccionarios. Finalmente con la lista pudimos avanzar en las funciones de cada uno.
    # Brenda: particularmente esta función la noto visualmente desordenada. Quizá porque hay
    # otra forma de escribirla, de plantear o acomodar las líneas de código.
    
    limpiar_Pantalla() 
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
        print(Style.BRIGHT + f"La mascota {nomMascota} se registró EXITOSAMENTE" + Style.RESET_ALL)
        resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
        if resp == "N":
            return
    else:
        return

def menu():
    """
    La función propone opciones a seleccionar x el usuario
    no espera argumentos y retorna la opción elegida.
    AUTOR: Brenda Sztryk
    COLABORADORES: Marina Toledo, Ale Ante, Leo Rios
    """
    print()
    print((Style.BRIGHT + "*" * 40).center(100) )
    print (" MENU ".center(0).center(95))
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
bande = True
op = menu()
while bande:
    match op:
        case "a": #Nuevo Paciente
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
            presupuestar()
            input("\t\tPresione enter para continuar")

        case "g": #Salir
            print(colorama.Fore.LIGHTMAGENTA_EX +("-"*70).center(100) + colorama.Fore.RESET)
            print(colorama.Fore.LIGHTMAGENTA_EX + "\t\tUsted seleccionó Salir" + colorama.Fore.RESET)
            break
        case _:
            print("\t\tValor invalido")
    op = menu()
print("\t\tHasta Luego! ")
