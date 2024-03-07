import pickle
  
class Usuario:

  def __init__(self, id_usuario, contra):
    self.id_usuario = id_usuario
    self.contra = contra
    

lista_usuarios = []

def registrar(id_usuario, contra):
  nuevo_usuario = Usuario(id_usuario, contra)
  lista_usuarios.append(nuevo_usuario)
  guardar_usuarios()

def guardar_usuarios():
  with open("Usuarios.pkl", "wb") as archivo_binario:
    pickle.dump(lista_usuarios, archivo_binario)

def eliminar(id_usuario):
  for usuario in lista_usuarios:
    if usuario.id_usuario == id_usuario:
      lista_usuarios.remove(usuario)
      guardar_usuarios()
      return
  print(f"No se encontro usuario con ID {id_usuario}")
  print("\n")
  print("Presione Enter para continuar...".center(64))
  input()

def buscar_usuario(id_usuario, contra):
  with open("Usuarios.pkl", "rb") as archivo_binario:
    lista_usuarios = pickle.load(archivo_binario)
    for usuario in lista_usuarios:
      if usuario.id_usuario == id_usuario and usuario.contra == contra:
        return True
  return False      