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
    with open("pacientes.json","w") as archivo:
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
    while True:
        try:
            bucaId = int(input("\t\tIngrese el DNI a buscar: "))
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
                break
            else: 
                print("Dato Invalido!")
        except:
            print("Dato Invalido!")
    

def modificarD(lista):
    while True:
        try:
            bucaId = int(input("\t\tIngrese el DNI a buscar: "))
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
                                            break
                                        case "b":
                                            print("\t\tDecidió cambiar Peso")
                                            nuevoPeso = float(input("\t\tIngrese el nuevo peso de la mascota\n\t\t> "))
                                            valorPaci[num]["peso"] = nuevoPeso
                                            print("\t\tCambio realizado!")
                                            break
                                        case _:
                                            print(colorama.Fore.RED + "\t\tValor no válido!" + colorama.Fore.RESET)
                                except ValueError:
                                    print(colorama.Fore.RED + "\t\tDato Inválido!" + colorama.Fore.RESET)
                            break
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

    dni = (input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI a buscar, sin puntos ni comas: " + Fore.RESET)) # si convierto a entero no me funciona en la busqueda !!!
    if dni in pacientes: #si dni esta en pacientes imprime dato dueño y mascotas
        pacientes = pacientes[dni]
        print()
        print("="*30)
        print(f"DNI: {dni}\n{pacientes['nombre']} {pacientes['Apellido']}")
        print("="*30)
        
         # MASCOTAS
        cont=1
        while True: 
            for elem in pacientes["mascotas"]: # elem son los diccionarios de la lista
                print (f"{"Mascota"} {cont}")
                cont = cont + 1
                for c,v in elem.items():
                    print (f"\t{c}: {v}")
            return 
    else:
        print(f"DNI: {dni} no se encuentra registrado. \nDesea registrarlo ahora? " )
        resp= input("responda: S / N ").upper()
        if resp == "S":
            agregar_Pac(pacientes)
        else:    
            return
    
def agregar_Pac(pacientes):
       
    nomDueño = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre dueño mascota: " + Fore.RESET).upper()
    apellDueño = input(Fore.LIGHTMAGENTA_EX +"Ingrese el apellido: "+ Fore.RESET).upper()
    dni = int(input(Fore.LIGHTMAGENTA_EX +"Ingrese DNI: "+ Fore.RESET))
   
    pacientes[dni] = {"nombre":nomDueño, "Apellido":apellDueño, "mascotas":[]} #me lo tomó con lista pero no con diccionario
   
    op = input (Fore.LIGHTMAGENTA_EX +"Desea registrar mascota?: S /N: "+ Fore.RESET).upper()
    while op == "S".upper():
           
        nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota 🐱: " + Fore.RESET).upper()
        tipo = input (Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
        raza = input (Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
        sexo = input (Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
        while sexo != "M".upper() and sexo != "H".upper(): #este while es por si tipea otra letra que no sea H o M
            print (Fore.LIGHTMAGENTA_EX + "error, debe ingresar M o H" + Fore.RESET)
            sexo = input (Fore.LIGHTMAGENTA_EX + "ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET)
            break
        edad = int (input (Fore.LIGHTMAGENTA_EX +"Ingrese edad de la mascota: " + Fore.RESET))
        peso = float (input(Fore.LIGHTMAGENTA_EX +"Ingrese peso de la mascota: " + Fore.RESET))

        mascota = {"nombre Mascota": nomMascota, "tipo":tipo, "raza": raza,"sexo": sexo, "edad": edad,"peso":peso}
        pacientes[dni]["mascotas"].append(mascota)
        print(f"{pacientes[dni]["mascotas"]}")

        resp=input (Fore.LIGHTMAGENTA_EX +"Desea registrar otra mascota?: S /N: "+ Fore.RESET).upper()
        if resp == "N":
            return
        
        #Guardo el diccionario pero que aparezca la variable nomMascota como clave del dict macotas
        dueñoMascota[nomMascota] = mascota
        #Creo una pregunta para salir del bucle: 
        #pregunta = input("\t\tQuiere agregar otra mascota?S/N:  ").upper()
        #if pregunta != "S":
            #break
    pacientes[dniDueño] = {"Dueño":{"Nombre": nomDueño, "Apellido": apellDueño}, "Mascotas":dueñoMascota }
    #guardar_Pacientes()

    #return pacientes
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
