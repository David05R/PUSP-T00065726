from gestionar_usuarios import registrar, eliminar
from errores import error_datos
from errores import error_opcion
from errores import clear_console
from gestionar_compu import devolver_computadora, mostrar_computadoras
from gestionar_compu import menuc
from gestionar_bici import menub

class Administrador:
  def __init__(self, ID_administrador, Contra):
    self.ID_administrador = ID_administrador
    self.Contra = Contra

admin = Administrador("admin", "admin")

def imprimir_admin():
  while True:
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: *********"
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
    username = input("Ingrese ID del Administrador: ".rjust(38))
    clear_console()
    print("~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~")
    print("\n")
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: "
    centered_text = text.rjust(38)
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
    text = "============Administrador============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "Administrador: "
    centered_text = text.rjust(37)
    print(centered_text + username)
    text = "Contraseña: "
    centered_text = text.rjust(36)
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

    if(admin.ID_administrador==username and admin.Contra==clave):

      while True:
        text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
        centered_text = text.center(64)
        print(centered_text)
        print("\n")
        text = "============Administrador============"
        centered_text = text.center(64)
        print(centered_text)
        print("\n")

        print("1. Agregar usuario".rjust(41))
        print("2. Eliminar usuario".rjust(41))
        print("3. Gestionar computadoras".rjust(41))
        print("4. Gestionar bicicletas".rjust(41))
        print("5. Cerrar sesión".rjust(40))

        print("\n")
        text = "========================================"
        centered_text = text.center(64)
        print(centered_text)

        op = int(input("Ingrese una opción: ".rjust(42)))
        print("\n")
        clear_console()

        if(op == 1):

          id_nuevo_usuario = input("Ingrese el ID del usuario a agregar: ")
          contrasena_nuevo_usuario=input("Ingrese la contraseña de usuario a agregar: ")
          clear_console()
          registrar(id_nuevo_usuario, contrasena_nuevo_usuario)

        if (op == 2):

          eliminar_id = input("Ingrese el ID del usuario a eliminar: ")
          eliminar(eliminar_id)
          clear_console()

        if(op == 3):
          menuc()
          clear_console()

        if(op == 4):
          menub()
          clear_console()

        if(op == 5):
          clear_console()
          break

        if(op !=1 and op !=2 and op !=3 and op != 4 and op !=5):
          error_opcion()

    else:
      error_datos()
      break
    break