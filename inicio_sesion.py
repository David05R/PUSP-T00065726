from gestionar_usuarios import buscar_usuario
from errores import error_datos
from menu_principal import menu
import os

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_inicio_sesion():
  while True: 
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Inicio de sesión============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Usuario: *********"
    centered_text = text.center(64)
    print(centered_text)
    text = "Contraseña: *********"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~PUSP~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    username = input("Ingrese ID de usuario: ".rjust(38))
    clear_console()
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Inicio de sesión============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Usuario: "
    centered_text = text.rjust(31)
    print(centered_text + username)
    text = "Contraseña: *********"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~PUSP~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    clave = input("Ingrese la contraseña: ".rjust(38))
    clear_console()
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Inicio de sesión============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Usuario: "
    centered_text = text.rjust(31)
    print(centered_text + username)
    text = "Contraseña: "
    centered_text = text.rjust(31)
    print(centered_text + clave)
    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~PUSP~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    print("Presione Enter para continuar...".center(64))
    input()
    clear_console()
    if(buscar_usuario(username, clave)):
      menu(username)
      break
    else:
      error_datos()