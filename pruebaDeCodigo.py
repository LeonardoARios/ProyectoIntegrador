def validar():
    """
    funcion que permite el ingreso con usuario y pass
    com posibilidad de cambiarla y agregarla a una lista
    de accesos validos
    AUTOR: Brenda Sztryk
    COLABORADORES:
    """
    #Registro de usuario
    '''
    usuarios = {}
    bande = True
    while bande:
        pregunt = input("Quiere registrar un nuevo usuario?:s/n:  ".upper())
        if pregunt == "s".lower():
            usuario = input("Ingrese su nombre de usuario\n ")
            password = input("Ingrese su contaseña\n ")
            usuarios[usuario]=password
        else:
            print("Ok, regresa a Ingreso".upper())
            bande = False
    print(usuarios)

    intentos = 3
    while intentos > 0:
        print(f'Quedan {intentos} intentos')
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario in usuarios.keys():
            password = input("Ingrese su contraseña: ") 
            if password in usuarios.values():
                print("login Exitoso!".upper())

            else:
                print("Contraseña Incorrecta")
                intentos = intentos - 1
        else: 
            print("El usuario no se encuentra registrado")
            intentos = intentos - 1'''
        

    '''usuValidos = ["Brenda", "Leo", "Marina", "Ale"] # NOMBRES VALIDOS Y PASS PARA USO DEL SISTEMA...PUEDE SER CUALQUIER OTRO NOMBRE Y MENOS USUARIOS
    passValido = "pet"
    intentos = 3


    while intentos > 0:
        usuario = input ("ingrese su usuario para ingresar al sistema: ").lower()
        contraseña = input ("ingrese su contraseña de acceso: ").lower()
        for i in range (len(usuValidos)):
            usuValidos[i] = usuValidos[i].lower() #pase users_validos a minusc. p/ comparar en el if con usuario del input
            if usuValidos[i] == usuario and passValido.lower() == contraseña:
                print("ingreso exitoso!!")
                intentos = 0
                break
        else:
            intentos = intentos - 1
            print(f"error! le quedan {intentos} intentos ")
            if intentos == 0:
                print("acceso BLOQUEADO!! ",end="")
                print("comuniquese al: 1222-3334")
                return False'''
    
'''pacientes=[]
mascota={
    "nombre":"pepe",
    "tipo":"loro",
    "raza":"paraguayo",
    "dni":"2424"
}
pacientes.append(mascota)
mascota={
    "nombre":"pepe",
    "tipo":"reptil",
    "raza":"cururu",
    "dni":"2420"
}
pacientes.append(mascota)
mascota={
    "nombre":"capitan",
    "tipo":"perro",
    "raza":"labrador",
    "dni":"2420"
}
pacientes.append(mascota)
dni=input("ingrese el dni del dueño: ")
for m in pacientes:
    if m["dni"]==dni:
        print(f"mascota: {m['nombre']} dni dueño {m['dni']}")'''
            
'''from colorama import Fore, init
init(autoreset=True)

def agregar_Pac(pacientes):
    print(pacientes)

    nomDueño = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre dueño mascota: " + Fore.RESET).upper()
    apellDueño = input(Fore.LIGHTMAGENTA_EX + "Ingrese el apellido: " + Fore.RESET)
    dni = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese DNI: " + Fore.RESET))
    dueño = {"nombre": nomDueño, "apellido": apellDueño}
    
    # Inicializar el registro del dueño si no existe
    if dni not in pacientes:
        pacientes[dni] = {"Dueño": dueño, "Mascotas": []}
    else:
        # Actualizar los datos del dueño si es necesario
        pacientes[dni]["Dueño"] = dueño
    
    while True:
        nomMascota = input(Fore.LIGHTMAGENTA_EX + "Ingrese nombre de la mascota: " + Fore.RESET).upper()
        tipo = input(Fore.LIGHTMAGENTA_EX + "Ingrese tipo de mascota: " + Fore.RESET).upper()
        raza = input(Fore.LIGHTMAGENTA_EX + "Ingrese raza de la mascota: " + Fore.RESET).upper()
        sexo = input(Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
        
        while sexo != "M" and sexo != "H":  # Verificación de entrada válida para sexo
            print(Fore.LIGHTMAGENTA_EX + "Error, debe ingresar M o H" + Fore.RESET)
            sexo = input(Fore.LIGHTMAGENTA_EX + "Ingrese sexo de la mascota: M > macho / H > hembra " + Fore.RESET).upper()
        
        edad = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese edad de la mascota: " + Fore.RESET))
        peso = float(input(Fore.LIGHTMAGENTA_EX + "Ingrese peso de la mascota: " + Fore.RESET))
        
        # Crear nueva entrada para la mascota
        nueva_mascota = {
            "nombre": nomMascota,
            "tipo": tipo,
            "raza": raza,
            "sexo": sexo,
            "edad": edad,
            "peso": peso
        }
        
        # Agregar la nueva mascota a la lista de mascotas del dueño
        pacientes[dni]["Mascotas"].append(nueva_mascota)
        
        print(Fore.LIGHTMAGENTA_EX + f"{nomMascota} se agregó con éxito a la base de datos" + Fore.RESET)
        print(pacientes)
        
        resp = input(Fore.LIGHTMAGENTA_EX + "Desea registrar otra mascota?: S / N: " + Fore.RESET).upper()
        if resp == "N":
            break
    
    return pacientes

# Ejemplo de uso
pacientes = {}
pacientes = agregar_Pac(pacientes)'''

def agregar_Pac(pacientes):
    # Se inicializa un diccionario vacío para almacenar las mascotas del dueño actual
    mascotas_dueño = {}

    # Se solicitan los datos del dueño
    nomDueño = input("Ingrese nombre dueño mascota: ").upper()
    apellDueño = input("Ingrese el apellido: ")
    dni = int(input("Ingrese DNI: "))

    # Bucle para agregar mascotas al dueño actual
    while True:
        nomMascota = input("Ingrese el nombre de la mascota: ")
        tipo = input("Ingrese que tipo de mascota es:  ")
        raza = input("Ingrese la raza de la mascota:  ")
        sexo = input("Ingrese el sexo de la mascota: ")
        edad = input("Ingrese la edad de la mascota:  ")
        peso = input("Ingrese el peso de la mascota:  ")

        # Se crea un diccionario para almacenar los datos de la mascota
        mascota = {
            "Nombre": nomMascota,
            "tipo": tipo,
            "raza": raza, 
            "sexo": sexo, 
            "edad": edad,
            "peso": peso, 
        }

        # Se agrega la mascota al diccionario de mascotas del dueño actual
        mascotas_dueño[nomMascota] = mascota

        # Se pregunta si se desea agregar otra mascota
        otra_mascota = input("¿Desea agregar otra mascota para el mismo dueño? (S/N): ").upper()
        if otra_mascota != "S":
            break

    # Se agrega el diccionario de mascotas del dueño actual al diccionario principal de pacientes
    pacientes[dni] = {"dueño": {"nombre": nomDueño, "apellido": apellDueño}, "mascotas": mascotas_dueño}

    print(pacientes)
    return pacientes
pacientes = {}
agregar_Pac(pacientes)

