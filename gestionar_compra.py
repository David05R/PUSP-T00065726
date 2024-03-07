from errores import clear_console
productos = {
    'Manzanas': 2.5,
    'Plátanos': 1.8,
    'Leche': 1.2,
    'Pan': 0.8,
    'Libretas': 1.5,
    'Lápices': 0.5
}
class Compra:
    def __init__(self, id_estudiante):
        self.id_estudiante = id_estudiante
        self.productos_comprados = []

    def agregar_producto(self, producto, cantidad):
        if producto in productos:
            precio_unitario = productos[producto]
            self.productos_comprados.append({
                'producto': producto,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario
            })

    def generar_factura(self):
        total = sum(item['cantidad'] * item['precio_unitario'] for item in self.productos_comprados)
        print("~~~~~~~~~~ Factura ~~~~~~~~~~")
        print(f"ID del Estudiante: {self.id_estudiante}")
        print("Productos Comprados:")
        for item in self.productos_comprados:
            print(f"Producto: {item['producto']}, Cantidad: {item['cantidad']}, Precio Unitario: {item['precio_unitario']}")
        print(f"Total a Pagar: {total}")
def menu_compra(id):
    compra = Compra(id)  
    while True:
        clear_console()
        print("~~~~~ Menú de Compras ~~~~~")
        print("\n")
        print("1. Comprar Manzanas")
        print("2. Comprar Plátanos")
        print("3. Comprar Leche")
        print("4. Comprar Pan")
        print("5. Comprar Libretas")
        print("6. Comprar Lápices")
        print("7. Generar Factura y Salir")
        print("\n")
        opcion = int(input("Ingrese una opción: "))
        print("\n")
        if opcion == 7:
            compra.generar_factura()
            break
        else:
            producto = list(productos.keys())[opcion - 1]
            cantidad = int(input("Ingrese la cantidad de {}: ".format(producto)))
            compra.agregar_producto(producto, cantidad)

        input("Presione Enter para continuar...")