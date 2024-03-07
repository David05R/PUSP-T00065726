from errores import error_opcion
from errores import clear_console
from gestionar_compu import alquilar_computadora
from gestionar_bici import reservar_bicicleta
from gestionar_compra import menu_compra

def menu(id_usuario):
  id=id_usuario
  while True:
    print("\n")
    text = "============Por favor seleccione una opción============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "1. Alquiler de computadores"
    centered_text = text.center(64)
    print(centered_text)
    text = "2. Reservación de bicicletas"
    centered_text = text.center(64)
    print(centered_text)
    text = "3. Compra en linea"
    centered_text = text.center(64)
    print(centered_text)
    text = "4. Salir"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "======================================================"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "~~~~~~~~~~~~~~~~~~~~~~PUSP~~~~~~~~~~~~~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    op = int(input("Ingrese una opción: ".rjust(42)))
    print("\n")
    clear_console()

    if(op == 1):

      alquilar_computadora(id)
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()

    if (op == 2):

      reservar_bicicleta(id)
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()

    if(op == 3):
      menu_compra(id)
      print("compra")
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()

    if(op == 4):
      
      print("salir")
      break

    if(op !=1 and op !=2 and op !=3 and op !=4):
      error_opcion()