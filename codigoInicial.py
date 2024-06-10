""" APLICACION DE GESTION INTEGRAL PARA VETERINARIOS
AUTORES: Marina Toledo, Ale Ante, Leo Rios, Brenda Sztryk
FECHA: 2024
VERSION: 1.0 """


import os
import colorama
from colorama import Back,Fore,Style #dejo agregado esto x si usamos los estilos




def limpiar_Pantalla():
   os.system("cls")
   """ La funcion limpia la pantalla para ver solamente
   lo que se quiere mostrar. No espera argumentos, no retorna valor
   AUTOR:
   COLABORADORES:"""




def menu():
   """ La funcion da opciones a seleccionar x el usuario
   no espera argumentos, y retorna la opcion elegida x usuario.
   AUTOR:
   COLABORADORES:"""




   print(colorama.Fore.CYAN)
   print("="*70)
   print("\t 1. Agregar Paciente")
   print("\t 2. Listar")
   print("\t 3. Salir")
   op = int(input("Ingresa la Opción:  "))
   return op


def listar(lista):
   print(colorama.Fore.CYAN)
   #como es una lista veo primero que tiene adentro
   for paciente in lista:
       print("-"*70)
       print(paciente) #Esto lo vamos a borrar
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
 
   masco = []
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
           print("Usted seleccionó Agregar")
           agregar(pacientes)
           print(nombre) #esto lo puse para ver el contenido si indexaba(despues borramos)
           print(len(nombre)) #esto lo puse para ver cuanto media la lista(despues borramos)
           input("Presione enter para continuar")
       case 2:
           print("Usted seleccionó Listar")
           listar(nombre)
           input("Presione enter para continuar")
       case 3:
           print("SALDRA DEL PROGRAMA")
           break
       case _:
           print("Valor invalido")
   op = menu()


print("Hasta Luego! ")