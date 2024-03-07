from errores import clear_console
from errores import error_opcion

class Bicicleta:
  def __init__(self, codigo):
    self.codigo = codigo
    self.id_usuario = None

  def esta_disponible(self):
    return self.id_usuario is None

  def reservar(self, id_usuario):
    if self.esta_disponible():
      self.id_usuario = id_usuario
      return True
    else:
      return False

  def devolver(self):
    self.id_usuario = None

bicicletas = [Bicicleta(f"B{i:02d}") for i in range(1, 51)]

def reservar_bicicleta(id_usuario):
  for bicicleta in bicicletas:
    if bicicleta.esta_disponible():
      bicicleta.reservar(id_usuario)
      print(f"La bicicleta {bicicleta.codigo} ha sido reservada por el usuario {id_usuario}")
      return
  print("No hay bicicletas disponibles para reservar")

def devolver_bicicleta(codigo):
  for bicicleta in bicicletas:
      if bicicleta.codigo == codigo:
          bicicleta.devolver()
          print(f"La bicicleta {bicicleta.codigo} ha sido devuelta")
          return
  print(f"No se encontró ninguna bicicleta con el código {codigo}")

def mostrar_bicicletas():
  for bicicleta in bicicletas:
      estado = "Disponible" if bicicleta.esta_disponible() else f"reservada por el usuario {bicicleta.id_usuario}"
      print(f"Computadora {bicicleta.codigo}: {estado}")

def menub():
  while True:
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Gestion Bicicletas============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")

    print("1. Mostrar Bicicletas".rjust(41))
    print("2. Devolver Bicicleta".rjust(41))
    print("3. Regresar a la pagina anterior".rjust(40))

    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)

    op = int(input("Ingrese una opción: ".rjust(42)))
    print("\n")

    if(op == 1):

      mostrar_bicicletas()
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()
    if (op == 2):

      codigo = input("Ingrese el código de la bicicleta a devolver: ")
      devolver_bicicleta(codigo)
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()

    if(op == 3):
      clear_console()
      break

    if(op !=1 and op !=2 and op !=3):
      error_opcion()