from errores import error_opcion
from errores import clear_console
from inicio_sesion import imprimir_inicio_sesion
from gestion_admin import imprimir_admin

TypeU = 0

while True:
  text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  text = "============Inicio de sesión============"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  print("Digite el tipo de usuario:".rjust(46))
  print("1. Administrador".rjust(40))
  print("2. Estudiante".rjust(38))
  print("\n")
  text = "========================================"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  text = "~~~~~~~~~~~~~~~~~~~~~~PUSP~~~~~~~~~~~~~~~~~~~~~~"
  centered_text = text.center(64)
  print(centered_text)
  print("\n")
  TypeU = input("Ingrese Tipo de Usuario: ".rjust(43))
  clear_console()

  if(TypeU == "1"):
    imprimir_admin()

  if(TypeU == "2"):
    imprimir_inicio_sesion()

  if(TypeU != "1" and TypeU != "2"):
    error_opcion() 