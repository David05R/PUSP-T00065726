from errores import clear_console
from errores import error_opcion

class Computadora:
  def __init__(self, codigo):
    self.codigo = codigo
    self.id_usuario = None

  def esta_disponible(self):
    return self.id_usuario is None

  def alquilar(self, id_usuario):
    if self.esta_disponible():
      self.id_usuario = id_usuario
      return True
    else:
      return False

  def devolver(self):
    self.id_usuario = None

computadoras = [Computadora(f"C{i:02d}") for i in range(1, 51)]

def alquilar_computadora(id_usuario):
  for computadora in computadoras:
    if computadora.esta_disponible():
      computadora.alquilar(id_usuario)
      print(f"La computadora {computadora.codigo} ha sido alquilada por el usuario {id_usuario}")
      return
  print("No hay computadoras disponibles para alquilar")

def devolver_computadora(codigo):
  for computadora in computadoras:
      if computadora.codigo == codigo:
          computadora.devolver()
          print(f"La computadora {computadora.codigo} ha sido devuelta")
          return
  print(f"No se encontró ninguna computadora con el código {codigo}")

def mostrar_computadoras():
  for computadora in computadoras:
      estado = "Disponible" if computadora.esta_disponible() else f"Alquilada por el usuario {computadora.id_usuario}"
      print(f"Computadora {computadora.codigo}: {estado}")

def menuc():
  while True:
    text = "~~~~~~~~~~Bienvenido a PUSP~~~~~~~~~~"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")
    text = "============Gestion Computadoras============"
    centered_text = text.center(64)
    print(centered_text)
    print("\n")

    print("1. Mostrar computadoras".rjust(42))
    print("2. Devolver computadora".rjust(42))
    print("3. Regresar a la pagina anterior".rjust(46))

    print("\n")
    text = "========================================"
    centered_text = text.center(64)
    print(centered_text)

    op = int(input("Ingrese una opción: ".rjust(42)))
    print("\n")

    if(op == 1):

      mostrar_computadoras()
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()
    if (op == 2):

      codigo = input("Ingrese el código de la computadora a devolver: ")
      devolver_computadora(codigo)
      print("\n")
      print("Presione Enter para continuar...".center(64))
      input()
      clear_console()
  
    if(op == 3):
      clear_console()
      break

    if(op !=1 and op !=2 and op !=3):
      error_opcion()
